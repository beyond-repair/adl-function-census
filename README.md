<div align="center">

[![Lifecycle](https://img.shields.io/badge/●_RESEARCH-a855f7?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_≤1-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   RESEARCH
CLAIM       ≤1
NOT CLAIMED thrust · energy extraction · AGI · production autonomy
```

</div>

---

# adl-function-census

Claim-capped **module-surface** census of priority `beyond-repair` repositories.

This repository exists because:

- `ADL-Portfolio-Census` locked inventory + claim caps (no functions).
- `aegis-repo-graph` locked identities + typed relationships (no functions).
- `adl-capability-matrix` locked clusters + compatible-build queue (explicitly forbade metadata-only function claims).

**Status: RESEARCH** (governance census tool). Claim level **≤1**. Claim-capped module-surface census for priority `beyond-repair` clusters.

Deterministic checker for a **dated** snapshot. A green run does not refresh GitHub and does not add function rows for repositories that were left at `NAME_ONLY`, `METADATA_ONLY`, or `TREE_PRESENT_FUNCTIONS_UNAUDITED`.

Nothing to configure. The checker reads only the Python records committed in this repository. It does not use the network, the environment, or a token.

## Quick start

Python 3.11 or newer. From the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[dev]"
python -m census.engine
python -m census
python -m pytest -q
```

Both commands print the locked counts and exit 0 with a final `OK` line when the committed records pass. They exit 1 and list `ERRORS` when a record breaks the contract. `python -m census` is the same report as `python -m census.engine`. After the editable install, those commands work from any working directory.

A passing run looks like:

```
snapshot=2026-09-05 locked=57 github=68
clusters {...}
caps {...}
module_surfaces 3
Q-FUNC-001 THIS_REPO adl-function-census
Q-FUNC-002 NOT_BUILT sunder-cleanroom-vsa-adapter
Q-FUNC-003 NOT_BUILT seem-identity-unifier
Q-FUNC-004 NOT_BUILT os-constitution-merge
Q-FUNC-005 NOT_BUILT workforce-lineage-graph
DRIFT observed=2026-10-06 search_total=83 not_a_relock snapshot_remains=2026-09-05 locked=57 github=68
OK
```

## Observed drift (not a re-lock)

Sweep-252 (2026-10-06) observed GitHub search `user:beyond-repair` `total_count` 83 (`incomplete_results` false) and profile `public_repos` 78, with 9 private names in the search payload. That observation is printed as a `DRIFT` line. It does **not** replace `SNAPSHOT_DATE=2026-09-05`, `ENUMERATED_PUBLIC_REPOS=68`, or the 57 locked records.

`Q-FUNC-002` (`sunder-cleanroom-vsa-adapter`) and `Q-FUNC-003` (`seem-identity-unifier`) now exist as repository names. Status stays `NOT_BUILT` in this lock: existence is not a module-surface audit and is not a SUPERSEDES proof. `Q-FUNC-004` still names `os-constitution-merge`, which is absent; `os-family-constitution-map` is a different name and is not recorded here.

`requirements.txt` pins the same pytest for a root-directory run without installing the package. That path only works when the current directory is the repository root, because Python then imports the local `census` package:

```bash
python -m pip install -r requirements.txt
python -m census.engine
python -m pytest -q
```

## Contract

The checker validates records already in this repo. It does not invent rows or assign caps to names that are absent from `census/inventory.py`.

- Snapshot date stays **2026-09-05**. `ENUMERATED_PUBLIC_REPOS` stays **68** (GitHub search `user:beyond-repair` on 2026-09-04/05). Locked records stay **57**, a subset, not a claim that every enumerated name is recorded.
- Each locked record has a unique name, a `cluster` in the declared cluster list, a legal `cap`, and a non-empty `note`.
- `MODULE_SURFACE` is only `adl-function-census`, `forge-aegis`, and `sunder`. Each of those has a non-empty list of unique module strings. No other record carries a `modules` list.
- Every declared cluster and every declared cap is used by at least one locked record.
- The compatible-build queue stays **5** items. Ids are unique. Status is `THIS_REPO` or `NOT_BUILT`. Exactly one item is `THIS_REPO`, and its name is `adl-function-census`. A `NOT_BUILT` name is not also a locked record.

## Claim contract

| Claimed | Not claimed |
|---|---|
| 68 public repos enumerated 2026-09-04/05 via `user:beyond-repair` | Live GitHub crawler |
| 57 of those names locked here with a cluster and a claim cap | That the other enumerated names were recorded individually |
| Cluster assignment from name + description + size | Runtime interoperability |
| Module-level surface for **priority cluster only** (sunder, forge-aegis) plus this repo, from the lists already in `census/inventory.py` | AST of all 68 repos, or a fresh tree walk |
| Compatible-build queue items that are not already built | Physical correctness of CFT / Ware / Coherence Drive |
| Duplicate SEEM / Digital Double / SovereignOS names are distinct identities | Equivalence of duplicate repos |
| The checker enforces the contract above on the committed records | Currency of this lock with any later portfolio census |

## Related

- `ADL-Governance`, `ADL-SEEM`, `forge-aegis`
- `ADL-Portfolio-Census`, `aegis-repo-graph`, `adl-capability-matrix`
- `sunder`, `sovereign-clean-room`

---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>
