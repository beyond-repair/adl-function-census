"""Locked snapshot. Dated 2026-09-04/05. Not a live crawler."""

from __future__ import annotations

SNAPSHOT_DATE = "2026-09-05"
SEARCH_QUERY = "user:beyond-repair"
ENUMERATED_PUBLIC_REPOS = 68

CLUSTERS = (
    "GOVERNANCE_FLS",
    "SEEM_VSA_AGENT",
    "WORKFORCE",
    "OS_CONSTITUTION",
    "PHYSICS_CFT_DRIVE",
    "GAMES",
    "TRADING",
    "SECURITY",
    "HEALTH",
    "INTERFACE",
    "SCAFFOLD",
)

CLAIM_CAPS = (
    "NAME_ONLY",
    "METADATA_ONLY",
    "MODULE_SURFACE",
    "TREE_PRESENT_FUNCTIONS_UNAUDITED",
)

REPOS: dict[str, dict] = {
    "adl-function-census": {
        "cluster": "GOVERNANCE_FLS",
        "cap": "MODULE_SURFACE",
        "note": "this repository",
        "modules": ["census.engine", "census.inventory", "census.validate"],
    },
    "adl-capability-matrix": {
        "cluster": "GOVERNANCE_FLS",
        "cap": "METADATA_ONLY",
        "note": "cluster matrix; forbids metadata-only function claims",
    },
    "aegis-repo-graph": {
        "cluster": "GOVERNANCE_FLS",
        "cap": "METADATA_ONLY",
        "note": "FLS artifact identities; no function inventory",
    },
    "ADL-Portfolio-Census": {
        "cluster": "GOVERNANCE_FLS",
        "cap": "METADATA_ONLY",
        "note": "SCAN/FORK/ANCHOR inventory lock",
    },
    "ADL-Governance": {
        "cluster": "GOVERNANCE_FLS",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "portfolio constitution docs",
    },
    "ADL-SEEM": {
        "cluster": "GOVERNANCE_FLS",
        "cap": "METADATA_ONLY",
        "note": "systems engineering standard text",
    },
    "forge-aegis": {
        "cluster": "GOVERNANCE_FLS",
        "cap": "MODULE_SURFACE",
        "note": "FLS + AEGIS pipeline/validator",
        "modules": [
            "python/aegis_pipeline.py",
            "python/aegis_validator.py",
            "fls/FLS-000.md",
            "fls/FLS-001.md",
            "fls/FLS-002-Core-Ontology.md",
            "fls/FLS-003-Graph-Semantics.md",
            "fls/FLS-005.md",
        ],
    },
    "sunder": {
        "cluster": "SEEM_VSA_AGENT",
        "cap": "MODULE_SURFACE",
        "note": "local-first agent SCAN/SNAP/SUNDER",
        "modules": [
            "sunder/agent.py",
            "sunder/fork.py",
            "sunder/gate.py",
            "sunder/vsa.py",
            "sunder/__main__.py",
        ],
    },
    "sovereign-clean-room": {
        "cluster": "SEEM_VSA_AGENT",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "FHRR / BaNEL VSA core; compatible with sunder.vsa but not wired",
    },
    "SEEM-2.0-Self-Evolving-Emergent-Mind": {
        "cluster": "SEEM_VSA_AGENT",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "offline symbolic substrate",
    },
    "SEEM-Cognitive_Microservice": {
        "cluster": "SEEM_VSA_AGENT",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "duplicate-named SEEM 2.0 microservice (underscore)",
    },
    "SEEM-Cognitive-Microservice": {
        "cluster": "SEEM_VSA_AGENT",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "duplicate-named SEEM 2.0 microservice (hyphen)",
    },
    "seem-block-system": {
        "cluster": "SEEM_VSA_AGENT",
        "cap": "METADATA_ONLY",
        "note": "isolation theorem text",
    },
    "Gia---General-Intelligence-Assistant": {
        "cluster": "SEEM_VSA_AGENT",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "autonomous assistant",
    },
    "Agent-Snake": {
        "cluster": "SEEM_VSA_AGENT",
        "cap": "METADATA_ONLY",
        "note": "ML snake agent",
    },
    "potential-garbanzo": {
        "cluster": "SEEM_VSA_AGENT",
        "cap": "NAME_ONLY",
        "note": "ai agent stub",
    },
    "Digital_Double_virtual_workforce": {
        "cluster": "WORKFORCE",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "TypeScript virtual workforce",
    },
    "DigitalDoubleVirtualWorkforce3.5": {
        "cluster": "WORKFORCE",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "largest workforce tree (~8718)",
    },
    "Digital_Double_Virtual_Workforce_4.": {
        "cluster": "WORKFORCE",
        "cap": "NAME_ONLY",
        "note": "empty name variant",
    },
    "Auto_Legion": {
        "cluster": "WORKFORCE",
        "cap": "METADATA_ONLY",
        "note": "legion agent scaffold",
    },
    "AtomicNexusAI": {
        "cluster": "WORKFORCE",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "nexus AI tree",
    },
    "Sovereign-OS": {
        "cluster": "OS_CONSTITUTION",
        "cap": "METADATA_ONLY",
        "note": "v0.2 constitutional OS",
    },
    "SovereignOS": {
        "cluster": "OS_CONSTITUTION",
        "cap": "METADATA_ONLY",
        "note": "duplicate identity (no hyphen)",
    },
    "LegionOS": {
        "cluster": "OS_CONSTITUTION",
        "cap": "NAME_ONLY",
        "note": "company OS stub",
    },
    "RealityOS": {
        "cluster": "OS_CONSTITUTION",
        "cap": "METADATA_ONLY",
        "note": "decision-infrastructure platform",
    },
    "coherence-drive": {
        "cluster": "PHYSICS_CFT_DRIVE",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "master propulsion integration claim",
    },
    "stress-tensor-modification": {
        "cluster": "PHYSICS_CFT_DRIVE",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "Ware-constant Maxwell tensor",
    },
    "momentum-closure": {
        "cluster": "PHYSICS_CFT_DRIVE",
        "cap": "METADATA_ONLY",
        "note": "surface-integral closure",
    },
    "ware-constant-phenomenology": {
        "cluster": "PHYSICS_CFT_DRIVE",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "W approx 0.08 phenomenology",
    },
    "sierpinski-geometry-045": {
        "cluster": "PHYSICS_CFT_DRIVE",
        "cap": "METADATA_ONLY",
        "note": "0.45 tetrahedron geometry",
    },
    "CFT-v3.1": {
        "cluster": "PHYSICS_CFT_DRIVE",
        "cap": "METADATA_ONLY",
        "note": "TeX white paper",
    },
    "CFT-v3.0": {
        "cluster": "PHYSICS_CFT_DRIVE",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "volumetric metric solution",
    },
    "The-Origin-Point-Hypothesis.": {
        "cluster": "PHYSICS_CFT_DRIVE",
        "cap": "METADATA_ONLY",
        "note": "TeX hypothesis",
    },
    "-Entanglement-and-Emergence": {
        "cluster": "PHYSICS_CFT_DRIVE",
        "cap": "METADATA_ONLY",
        "note": "emergent spacetime notes",
    },
    "optimization-limit-conjecture": {
        "cluster": "PHYSICS_CFT_DRIVE",
        "cap": "METADATA_ONLY",
        "note": "obstruction floors framework",
    },
    "-text-informational-fork-protocol-": {
        "cluster": "PHYSICS_CFT_DRIVE",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "informational locality protocol",
    },
    "Project-Cold-Boot": {
        "cluster": "GAMES",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "GDScript reality-editing game",
    },
    "blacksite": {
        "cluster": "GAMES",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "JS covert-ops roguelite",
    },
    "BlockSwarm": {
        "cluster": "SECURITY",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "Solidity swarm",
    },
    "VigilE.S.A.-Enhanced-Security": {
        "cluster": "SECURITY",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "Rust security platform",
    },
    "ExoAxis-1": {
        "cluster": "HEALTH",
        "cap": "METADATA_ONLY",
        "note": "network pharmacology",
    },
    "smart_home_BCI": {
        "cluster": "INTERFACE",
        "cap": "METADATA_ONLY",
        "note": "NLP smart-home script",
    },
    "RepoRover-": {
        "cluster": "INTERFACE",
        "cap": "METADATA_ONLY",
        "note": "GitHub repo tool",
    },
    "fantom_trading_bot_2": {
        "cluster": "TRADING",
        "cap": "NAME_ONLY",
        "note": "fantom bot v2",
    },
    "FortiTrade_Multi-Strategy": {
        "cluster": "TRADING",
        "cap": "METADATA_ONLY",
        "note": "multi-strategy trade",
    },
    "btc-trading": {
        "cluster": "TRADING",
        "cap": "METADATA_ONLY",
        "note": "btc scripts",
    },
    "fantom-smart-contracts-first-bot": {
        "cluster": "TRADING",
        "cap": "METADATA_ONLY",
        "note": "Rust fantom contracts",
    },
    "ftmA.I.bot": {
        "cluster": "TRADING",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "FTM AI bot",
    },
    "My-mind-A.I.": {
        "cluster": "SCAFFOLD",
        "cap": "METADATA_ONLY",
        "note": "early AI",
    },
    "new-program-1.01": {
        "cluster": "SCAFFOLD",
        "cap": "NAME_ONLY",
        "note": "My Mind A.I. variant",
    },
    "genieGPT": {"cluster": "SCAFFOLD", "cap": "NAME_ONLY", "note": "empty-ish"},
    "test": {"cluster": "SCAFFOLD", "cap": "NAME_ONLY", "note": "empty"},
    "Quantumclustering": {"cluster": "SCAFFOLD", "cap": "NAME_ONLY", "note": "empty"},
    "Code_Generation_AI_Program": {"cluster": "SCAFFOLD", "cap": "NAME_ONLY", "note": "empty"},
    "automate_passive_income": {"cluster": "SCAFFOLD", "cap": "NAME_ONLY", "note": "empty"},
    "quantum_A.I._optimization.py": {
        "cluster": "SCAFFOLD",
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "quantum+AI optimization experiment",
    },
    "-Py2APK-main": {"cluster": "SCAFFOLD", "cap": "METADATA_ONLY", "note": "apk packager fork-like"},
}

COMPATIBLE_BUILDS = [
    {
        "id": "Q-FUNC-001",
        "name": "adl-function-census",
        "status": "THIS_REPO",
        "reason": "Close metadata-function claim gap for priority cluster only.",
    },
    {
        "id": "Q-FUNC-002",
        "name": "sunder-cleanroom-vsa-adapter",
        "status": "NOT_BUILT",
        "reason": "sunder/vsa.py and sovereign-clean-room are compatible but unwired.",
    },
    {
        "id": "Q-FUNC-003",
        "name": "seem-identity-unifier",
        "status": "NOT_BUILT",
        "reason": "Three SEEM microservice identities exist; no SUPERSEDES proof.",
    },
    {
        "id": "Q-FUNC-004",
        "name": "os-constitution-merge",
        "status": "NOT_BUILT",
        "reason": "Sovereign-OS vs SovereignOS vs LegionOS vs RealityOS unmerged.",
    },
    {
        "id": "Q-FUNC-005",
        "name": "workforce-lineage-graph",
        "status": "NOT_BUILT",
        "reason": "Digital Double 3.5 / TS / empty v4 have no typed SUPERSEDES edges in code.",
    },
]
