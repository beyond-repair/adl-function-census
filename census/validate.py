from __future__ import annotations

from .inventory import CLAIM_CAPS, CLUSTERS, COMPATIBLE_BUILDS, REPOS


class CensusError(ValueError):
    pass


def validate(repos: dict | None = None) -> list[str]:
    repos = repos if repos is not None else REPOS
    errors: list[str] = []
    names = list(repos)
    if len(names) != len(set(names)):
        errors.append("duplicate repo keys")
    for name, rec in repos.items():
        if rec.get("cluster") not in CLUSTERS:
            errors.append(f"{name}: bad cluster {rec.get('cluster')}")
        if rec.get("cap") not in CLAIM_CAPS:
            errors.append(f"{name}: bad cap {rec.get('cap')}")
        if rec.get("cap") == "MODULE_SURFACE" and not rec.get("modules"):
            errors.append(f"{name}: MODULE_SURFACE requires modules list")
        if rec.get("cap") != "MODULE_SURFACE" and rec.get("modules"):
            errors.append(f"{name}: modules present without MODULE_SURFACE cap")
    ids = [q["id"] for q in COMPATIBLE_BUILDS]
    if len(ids) != len(set(ids)):
        errors.append("duplicate queue ids")
    this = [q for q in COMPATIBLE_BUILDS if q["status"] == "THIS_REPO"]
    if len(this) != 1:
        errors.append("exactly one THIS_REPO queue item required")
    return errors


def assert_valid() -> None:
    errs = validate()
    if errs:
        raise CensusError("; ".join(errs))
