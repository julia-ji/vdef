# Architecture overview

## Purpose and boundaries

VDEF adds traceability around an existing calculation or data-processing engine. It must not own the engine's business logic or require a particular web framework, database service, or cloud platform.

## Conceptual components (proposed, not implemented)

1. **Input identity and versions:** references and fingerprints for inputs; data bytes remain outside metadata storage.
2. **Execution context:** explicit configuration snapshot, input references, engine identity, and invocation parameters.
3. **Execution history:** immutable-oriented records of execution attempts and their outputs/status.
4. **Comparison:** future mechanisms to compare two recorded executions.
5. **Reproduction:** future orchestration using recorded context; no replay implementation in milestone 1.

Existing application → VDEF integration boundary → metadata records

Existing application → existing execution engine → data assets/results

VDEF records references and context; it does not become a data lake or replace the execution engine.

## Storage direction

SQLite is the initial planned metadata store, **not implemented yet**. Repository interfaces should avoid coupling application logic to SQLite so other databases can be supported later. Large input/output assets belong in external storage managed by the integrating application.

## Configuration direction

Effective configuration is proposed to follow precedence:

`Global < Environment < Workspace < Run`

The exact merge semantics, secret handling, and serialization format require an ADR before implementation. Reproducibility requires recording the effective configuration and relevant input identities, not merely referencing mutable configuration names.

## Open questions

- How should input identities, content hashes, and externally stored assets be represented?
- What defines a reproducible execution when dependencies or third-party engines change?
- Should history be append-only, and how should failed/partial runs be modeled?
- How should secrets be excluded from stored configuration snapshots?
- What should be the initial interface for integrating an existing execution engine?
- What are the comparison semantics for large or nondeterministic outputs?

These are proposals for review, not approved implementation decisions.
