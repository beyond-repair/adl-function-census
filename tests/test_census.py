import copy
import subprocess
import sys
from pathlib import Path

from census import __version__

ROOT = Path(__file__).resolve().parents[1]
from census.inventory import COMPATIBLE_BUILDS, REPOS
from census.validate import validate
from census.engine import summary


def test_package_version():
    assert __version__ == "0.1.1"


def test_valid():
    assert validate() == []


def test_priority_surfaces():
    for name in ("sunder", "forge-aegis", "adl-function-census"):
        assert REPOS[name]["cap"] == "MODULE_SURFACE"
        assert REPOS[name]["modules"]


def test_sunder_modules():
    mods = set(REPOS["sunder"]["modules"])
    assert "sunder/vsa.py" in mods
    assert "sunder/gate.py" in mods


def test_forge_aegis_modules():
    mods = set(REPOS["forge-aegis"]["modules"])
    assert "python/aegis_pipeline.py" in mods
    assert "python/aegis_validator.py" in mods


def test_no_false_full_ast_claim():
    surfaces = [n for n, r in REPOS.items() if r["cap"] == "MODULE_SURFACE"]
    assert surfaces == ["adl-function-census", "forge-aegis", "sunder"]


def test_queue_has_unbuilt():
    assert any(q["status"] == "NOT_BUILT" for q in COMPATIBLE_BUILDS)
    locked = set(REPOS)
    for item in COMPATIBLE_BUILDS:
        if item["status"] == "NOT_BUILT":
            assert item["name"] not in locked


def test_summary_runs():
    report = summary()
    assert report["ok"] is True
    assert report["errors"] == []
    assert report["locked_records"] == len(REPOS) == 57
    assert report["github_public_enumerated"] == 68
    assert report["module_surfaces"] == 3
    assert report["snapshot_date"] == "2026-09-05"


def test_engine_cli_reports_locked_snapshot():
    proc = subprocess.run(
        [sys.executable, "-m", "census.engine"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    lines = proc.stdout.splitlines()
    assert lines[0] == "snapshot=2026-09-05 locked=57 github=68"
    assert lines[-1] == "OK"
    assert "module_surfaces 3" in lines
    assert "Q-FUNC-001 THIS_REPO adl-function-census" in lines
    assert proc.stderr == ""


def test_module_cli_matches_engine():
    proc = subprocess.run(
        [sys.executable, "-m", "census"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    lines = proc.stdout.splitlines()
    assert lines[0] == "snapshot=2026-09-05 locked=57 github=68"
    assert lines[-1] == "OK"


def test_bad_cluster_fails():
    repos = copy.deepcopy(REPOS)
    repos["sunder"]["cluster"] = "NOT_A_CLUSTER"
    errors = validate(repos)
    assert any("sunder: bad cluster NOT_A_CLUSTER" in err for err in errors)


def test_modules_without_surface_cap_fail():
    repos = copy.deepcopy(REPOS)
    repos["LegionOS"]["modules"] = ["legion/kernel.py"]
    errors = validate(repos)
    assert any("modules present without MODULE_SURFACE cap" in err for err in errors)


def test_empty_module_surface_fails():
    repos = copy.deepcopy(REPOS)
    repos["sunder"]["modules"] = []
    errors = validate(repos)
    assert any("sunder: MODULE_SURFACE requires modules list" in err for err in errors)


def test_duplicate_queue_id_fails():
    builds = copy.deepcopy(COMPATIBLE_BUILDS)
    builds[1]["id"] = builds[0]["id"]
    errors = validate(builds=builds)
    assert any("duplicate queue ids" in err for err in errors)


def test_not_built_name_already_locked_fails():
    builds = copy.deepcopy(COMPATIBLE_BUILDS)
    builds[1]["name"] = "sunder"
    errors = validate(builds=builds)
    assert any("sunder: NOT_BUILT but already locked" in err for err in errors)


def test_missing_this_repo_fails():
    builds = [item for item in COMPATIBLE_BUILDS if item["status"] != "THIS_REPO"]
    errors = validate(builds=builds)
    assert any("exactly one THIS_REPO queue item required" in err for err in errors)
