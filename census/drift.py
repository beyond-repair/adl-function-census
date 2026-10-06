"""Observation-only drift note. Does not re-lock the 2026-09-05 snapshot."""

from __future__ import annotations

OBSERVED_ON = "2026-10-06"
OBSERVED_SEARCH_QUERY = "user:beyond-repair"
OBSERVED_SEARCH_TOTAL = 83
OBSERVED_PUBLIC_REPOS_PROFILE = 78
OBSERVED_PRIVATE_IN_PAYLOAD = 9
# Names that exist on GitHub but are still NOT_BUILT in the locked queue.
# Existence is not a SUPERSEDES proof and is not a module-surface audit.
QUEUE_NAME_EXISTS = {
    "Q-FUNC-002": "sunder-cleanroom-vsa-adapter",
    "Q-FUNC-003": "seem-identity-unifier",
}
# Q-FUNC-004 named os-constitution-merge. Closest existing map is a different name.
QUEUE_NAME_ABSENT_RELATED = {
    "Q-FUNC-004": "os-family-constitution-map",
    "Q-FUNC-005": None,
}


def drift_line() -> str:
    return (
        "DRIFT observed="
        f"{OBSERVED_ON} search_total={OBSERVED_SEARCH_TOTAL} "
        "not_a_relock snapshot_remains=2026-09-05 locked=57 github=68"
    )
