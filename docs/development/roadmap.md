# Incremental roadmap

## Milestone 1 — Initialization (this task)

- Python 3.12+ package using `src/` layout.
- pytest import smoke test.
- Scope, architecture assumptions, agent instructions, and ADR directory.

**Exit criterion:** package imports and automated tests pass.

## Milestone 2 — Architecture review (approval required)

- Agree on identifiers and versioning model.
- Draft ADRs for metadata boundaries, storage interfaces, and configuration merging.
- Define minimum integration API and reproducibility contract.

## Milestone 3 — Metadata foundation (future)

- Implement approved models and narrow repository contracts.
- Implement SQLite adapter and unit tests.

## Milestone 4 — Execution context capture (future)

- Record versioned inputs, effective configuration, and execution history without replacing the existing engine.

## Milestone 5 — Result comparison (future)

- Implement approved comparison semantics and diagnostics.

## Milestone 6 — Historical reproduction (future)

- Implement replay only after reproducibility constraints and safety behavior are approved.

Web UI, APIs, and cloud integrations are out of scope until separately proposed and approved.
