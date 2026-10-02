"""``python -m census`` — same report as ``python -m census.engine``."""

from .engine import main

raise SystemExit(main())
