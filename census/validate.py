"""Validate the locked module-surface census. Does not invent rows."""

from __future__ import annotations

from .inventory import (
    CLAIM_CAPS,
    CLUSTERS,
    COMPATIBLE_BUILDS,
    ENUMERATED_PUBLIC_REPOS,
    REPOS,
    SNAPSHOT_DATE,
)

LOCKED_RECORD_COUNT = 57
LOCKED_QUEUE_COUNT = 5
MODULE_SURFACES = ("adl-function-census", "forge-aegis", "sunder")
QUEUE_STATUSES = ("THIS_REPO", "NOT_BUILT")
REQUIRED_RECORD_KEYS = ("cluster", "cap", "note")
REQUIRED_QUEUE_KEYS = ("id", "name", "status", "reason")


class CensusError(ValueError):
    pass


def _nonempty_str(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(
    repos: dict | None = None,
    builds: list | None = None,
) -> list[str]:
    repos = REPOS if repos is None else repos
    builds = COMPATIBLE_BUILDS if builds is None else builds
    errors: list[str] = []
    canonical_repos = repos is REPOS
    canonical_builds = builds is COMPATIBLE_BUILDS

    if SNAPSHOT_DATE != "2026-09-05":
        errors.append(f"snapshot date {SNAPSHOT_DATE!r} != 2026-09-05")
    if ENUMERATED_PUBLIC_REPOS != 68:
        errors.append(
            f"enumerated public repos {ENUMERATED_PUBLIC_REPOS} != 68"
        )

    if not isinstance(repos, dict):
        errors.append("repos must be a dict")
        return errors

    names = list(repos)
    if len(names) != len(set(names)):
        errors.append("duplicate repo keys")
    if canonical_repos and len(repos) != LOCKED_RECORD_COUNT:
        errors.append(
            f"locked record count {len(repos)} != {LOCKED_RECORD_COUNT}"
        )

    seen_clusters: set[str] = set()
    seen_caps: set[str] = set()
    surfaces: list[str] = []
    for name, rec in repos.items():
        if not _nonempty_str(name):
            errors.append("repo key must be a non-empty string")
            continue
        if not isinstance(rec, dict):
            errors.append(f"{name}: record must be a dict")
            continue
        for key in REQUIRED_RECORD_KEYS:
            if key not in rec:
                errors.append(f"{name}: missing {key}")
        if "note" in rec and not _nonempty_str(rec.get("note")):
            errors.append(f"{name}: note must be a non-empty string")
        cluster = rec.get("cluster")
        if "cluster" in rec and cluster not in CLUSTERS:
            errors.append(f"{name}: bad cluster {cluster}")
        elif cluster in CLUSTERS:
            seen_clusters.add(cluster)
        cap = rec.get("cap")
        if "cap" in rec and cap not in CLAIM_CAPS:
            errors.append(f"{name}: bad cap {cap}")
        elif cap in CLAIM_CAPS:
            seen_caps.add(cap)
        modules = rec.get("modules")
        if cap == "MODULE_SURFACE":
            surfaces.append(name)
            if not modules:
                errors.append(f"{name}: MODULE_SURFACE requires modules list")
            elif not isinstance(modules, list):
                errors.append(f"{name}: modules must be a list")
            else:
                if any(not _nonempty_str(mod) for mod in modules):
                    errors.append(f"{name}: modules must be non-empty strings")
                if len(modules) != len(set(modules)):
                    errors.append(f"{name}: duplicate modules")
        elif modules:
            errors.append(f"{name}: modules present without MODULE_SURFACE cap")

    if canonical_repos:
        for cluster in CLUSTERS:
            if cluster not in seen_clusters:
                errors.append(f"declared cluster unused: {cluster}")
        for cap in CLAIM_CAPS:
            if cap not in seen_caps:
                errors.append(f"declared cap unused: {cap}")
        if sorted(surfaces) != sorted(MODULE_SURFACES):
            errors.append(
                "module surfaces "
                f"{sorted(surfaces)} != {sorted(MODULE_SURFACES)}"
            )
        if len(repos) >= ENUMERATED_PUBLIC_REPOS:
            errors.append(
                "locked records must stay a subset of the 68 enumerated names"
            )

    if not isinstance(builds, list):
        errors.append("queue must be a list")
        return errors
    if canonical_builds and len(builds) != LOCKED_QUEUE_COUNT:
        errors.append(f"queue count {len(builds)} != {LOCKED_QUEUE_COUNT}")

    ids: list[str] = []
    this: list[dict] = []
    for index, item in enumerate(builds):
        if not isinstance(item, dict):
            errors.append(f"queue[{index}]: must be a dict")
            continue
        for key in REQUIRED_QUEUE_KEYS:
            if not _nonempty_str(item.get(key)):
                errors.append(f"queue[{index}]: {key} must be a non-empty string")
        status = item.get("status")
        if _nonempty_str(status) and status not in QUEUE_STATUSES:
            errors.append(f"queue[{index}]: bad status {status}")
        qid = item.get("id")
        if _nonempty_str(qid):
            ids.append(qid)
        if status == "THIS_REPO":
            this.append(item)
            if item.get("name") != "adl-function-census":
                errors.append("THIS_REPO queue item must name adl-function-census")
        if (
            status == "NOT_BUILT"
            and _nonempty_str(item.get("name"))
            and item["name"] in repos
        ):
            errors.append(f"{item['name']}: NOT_BUILT but already locked")

    if len(ids) != len(set(ids)):
        errors.append("duplicate queue ids")
    if len(this) != 1:
        errors.append("exactly one THIS_REPO queue item required")
    return errors


def assert_valid() -> None:
    errs = validate()
    if errs:
        raise CensusError("; ".join(errs))
