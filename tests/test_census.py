from census.inventory import COMPATIBLE_BUILDS, REPOS
from census.validate import validate
from census.engine import summary


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


def test_no_false_full_ast_claim():
    surfaces = [n for n, r in REPOS.items() if r["cap"] == "MODULE_SURFACE"]
    assert len(surfaces) < 10


def test_queue_has_unbuilt():
    assert any(q["status"] == "NOT_BUILT" for q in COMPATIBLE_BUILDS)


def test_summary_runs():
    s = summary()
    assert s["locked_records"] == len(REPOS)
    assert s["module_surfaces"] >= 3
