# Instructions for AI coding agents

## Roles and authority

The human project owner makes architecture decisions. AI agents implement approved, narrowly scoped changes, tests, and documentation. Ask for approval before major architecture changes.

## Working rules

1. Inspect the repository and read README, architecture overview, roadmap, and relevant ADRs before editing.
2. Preserve existing files and user changes; never regenerate the scaffold unnecessarily.
3. Work incrementally, with minimal dependencies and explicit interfaces.
4. Keep the Python core independent of web frameworks and cloud platforms.
5. Keep data assets separate from metadata. SQLite is the planned initial metadata backend; design for future adapters.
6. Respect configuration precedence: Global → Environment → Workspace → Run. Do not invent merge semantics without approval.
7. Never add proprietary company code, data, secrets, credentials, or production identifiers.
8. Add or update tests and documentation with each implementation change.
9. Run automated tests and report commands, results, and limitations accurately.
10. Do not push to or merge into `main` without explicit human approval. Prefer feature branches and reviewable Pull Requests.

## Current scope

Initialization only. Do not implement metadata repositories, execution, replay, FastAPI, React, or cloud integrations until authorized.

## Before declaring completion

Summarize changed files, tests run, any outstanding decisions, and whether any remote branch or PR was created.
