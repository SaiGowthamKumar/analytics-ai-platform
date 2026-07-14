# Architecture Decision Records

**Purpose:** Preserve the context and consequences of durable architecture decisions.

**Owner:** Principal Architect

Create a new ADR before implementation when a decision is hard to reverse or affects multiple modules. Do not edit an accepted decision’s meaning; supersede it with a new ADR.

| ADR | Decision | Status |
|---|---|---|
| [001](ADR-001-clean-architecture.md) | Clean Architecture | Accepted |
| [002](ADR-002-modular-monolith.md) | Modular Monolith | Accepted |
| [003](ADR-003-postgresql.md) | PostgreSQL | Proposed |
| [004](ADR-004-fastapi.md) | FastAPI | Proposed |
| [005](ADR-005-react.md) | React | Proposed |
| [006](ADR-006-provider-agnostic-llm.md) | Provider-agnostic LLM layer | Accepted |
| [007](ADR-007-semantic-knowledge-layer.md) | Semantic knowledge layer | Accepted |
| [008](ADR-008-docker.md) | Docker | Accepted |

## ADR classification and depth

ADRs must be detailed enough to preserve the decision, but not standardized to one arbitrary length. Classify each new ADR before drafting it.

| Class | Use for | Expected depth | Existing examples |
|---|---|---|---|
| Foundational | Decisions that define the platform's enduring architecture, dependency rules, semantic boundary, or strategic boundaries | Detailed: problem framing, constraints, principles, alternatives, consequences, migration implications, and explicit tradeoffs | ADR-001, ADR-002, ADR-006, ADR-007 |
| Technology | Selection of a framework, database, platform, runtime, or delivery technology | Medium: decision drivers, viable alternatives, architectural fit, operational impact, and tradeoffs | ADR-003, ADR-004, ADR-005, ADR-008 |
| Operational | Focused runtime and engineering practices such as logging, caching, retry, or retention policy | Short: trigger, decision, affected scope, consequences, and review condition | None yet |

Foundational ADRs define the project's DNA and therefore require more context. Technology ADRs explain why a technology fits the approved architecture rather than documenting every product feature. Operational ADRs should be concise and link to the operational standard they govern.

## Required structure by class

All ADRs include **Purpose**, **Owner**, **Status**, **Context**, **Decision**, **Alternatives**, **Consequences**, **Tradeoffs**, and **Future expansion**. Foundational ADRs may add constraints, principles, dependency implications, migration, and decision drivers. Technology ADRs may add evaluation criteria and operational considerations. Operational ADRs should add sections only when they materially improve future understanding.

## Future expansion

Add date, deciders, and links to implementation PRs to new ADRs.

