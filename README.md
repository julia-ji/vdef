# VDEF — Versioned Data Execution Framework

VDEF is a lightweight, open-source Python framework intended to help existing data-processing systems track input versions, capture execution context and history, reproduce historical calculations, and compare execution results **without replacing their execution engines**.

## Status

**Milestone 1: project initialization only.** The package is importable, but no execution, persistence, comparison, or replay capabilities are implemented yet.

## Intended scope

- Track references to input data and their versions.
- Record execution context and history.
- Enable historical reproducibility in a later milestone.
- Compare outputs from distinct executions in a later milestone.
- Integrate through explicit, lightweight Python interfaces.

## Non-goals for initialization

No metadata repositories, pipeline runners, replay, FastAPI, React, cloud integrations, or execution engine replacements. No proprietary company code, data, or credentials.

## Principles

- Python core independent of web frameworks and cloud providers.
- SQLite is the proposed initial metadata backend; future backends should be possible behind narrow interfaces.
- Configuration precedence: Global → Environment → Workspace → Run.
- Data assets remain separate from execution metadata.
- Favor explicit abstractions and incremental delivery.

## Development

Requires Python 3.12 or newer.

```bash
python -m pip install -e '.[dev]'
python -m pytest
```

## Documentation

- [Architecture overview](docs/architecture/overview.md)
- [Development roadmap](docs/development/roadmap.md)
- [Architecture decisions](docs/decisions/README.md)
- [AI agent guidelines](AGENTS.md)

## License

An open-source license has not yet been selected. Until one is added, the repository should not be described as licensed for open-source reuse.
