from __future__ import annotations

from .inventory import COMPATIBLE_BUILDS, ENUMERATED_PUBLIC_REPOS, REPOS, SNAPSHOT_DATE
from .validate import assert_valid


def summary() -> dict:
    assert_valid()
    by_cluster: dict[str, int] = {}
    by_cap: dict[str, int] = {}
    module_surfaces = 0
    for rec in REPOS.values():
        by_cluster[rec["cluster"]] = by_cluster.get(rec["cluster"], 0) + 1
        by_cap[rec["cap"]] = by_cap.get(rec["cap"], 0) + 1
        if rec["cap"] == "MODULE_SURFACE":
            module_surfaces += 1
    return {
        "snapshot_date": SNAPSHOT_DATE,
        "github_public_enumerated": ENUMERATED_PUBLIC_REPOS,
        "locked_records": len(REPOS),
        "coverage_note": "locked subset; not all 68 names are individually recorded",
        "by_cluster": by_cluster,
        "by_cap": by_cap,
        "module_surfaces": module_surfaces,
        "queue": COMPATIBLE_BUILDS,
    }


def main() -> None:
    s = summary()
    print(f"snapshot={s['snapshot_date']} locked={s['locked_records']} github={s['github_public_enumerated']}")
    print("clusters", s["by_cluster"])
    print("caps", s["by_cap"])
    print("module_surfaces", s["module_surfaces"])
    for q in s["queue"]:
        print(f"{q['id']} {q['status']} {q['name']}")


if __name__ == "__main__":
    main()
