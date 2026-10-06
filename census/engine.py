"""Run the locked module-surface census checker. Does not crawl GitHub."""

from __future__ import annotations

from .drift import drift_line
from .inventory import COMPATIBLE_BUILDS, ENUMERATED_PUBLIC_REPOS, REPOS, SNAPSHOT_DATE
from .validate import validate


def summary() -> dict:
    errors = validate()
    by_cluster: dict[str, int] = {}
    by_cap: dict[str, int] = {}
    module_surfaces = 0
    for rec in REPOS.values():
        cluster = rec.get("cluster")
        cap = rec.get("cap")
        if isinstance(cluster, str):
            by_cluster[cluster] = by_cluster.get(cluster, 0) + 1
        if isinstance(cap, str):
            by_cap[cap] = by_cap.get(cap, 0) + 1
        if cap == "MODULE_SURFACE":
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
        "drift_line": drift_line(),
        "errors": errors,
        "ok": not errors,
    }


def main() -> int:
    report = summary()
    print(
        "snapshot="
        f"{report['snapshot_date']} locked={report['locked_records']} "
        f"github={report['github_public_enumerated']}"
    )
    print("clusters", report["by_cluster"])
    print("caps", report["by_cap"])
    print("module_surfaces", report["module_surfaces"])
    for item in report["queue"]:
        print(f"{item.get('id')} {item.get('status')} {item.get('name')}")
    print(report["drift_line"])
    if report["errors"]:
        print("ERRORS:")
        for err in report["errors"]:
            print(" -", err)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
