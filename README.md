# adl-function-census

Claim-capped **module-surface** census of priority `beyond-repair` repositories.

This repository exists because:

- `ADL-Portfolio-Census` locked inventory + claim caps (no functions).
- `aegis-repo-graph` locked identities + typed relationships (no functions).
- `adl-capability-matrix` locked clusters + compatible-build queue (explicitly forbade metadata-only function claims).

## Claim contract

| Claimed | Not claimed |
|---|---|
| 68 public repos enumerated 2026-09-04/05 via `user:beyond-repair` | Live GitHub crawler |
| Cluster assignment from name + description + size | Runtime interoperability |
| Module-level surface for **priority cluster only** (sunder, forge-aegis) from default-branch trees | AST of all 68 repos |
| Compatible-build queue items that are not already built | Physical correctness of CFT / Ware / Coherence Drive |
| Duplicate SEEM / Digital Double / SovereignOS names are distinct identities | Equivalence of duplicate repos |

## Run

```bash
pip install -r requirements.txt
python -m census.engine
python -m pytest -q
```

## Related

- `ADL-Governance`, `ADL-SEEM`, `forge-aegis`
- `ADL-Portfolio-Census`, `aegis-repo-graph`, `adl-capability-matrix`
- `sunder`, `sovereign-clean-room`
