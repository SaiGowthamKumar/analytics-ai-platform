# Documentation Hub

**Purpose:** This directory is the project’s single source of truth (SSOT). It records approved product intent, architecture, rules, decisions, and operating practices.

**Owner:** Architecture and Product leads; every contributor owns keeping affected documents current.

## How to use this documentation

1. Consult the relevant document before changing behavior or structure.
2. Update it in the same change set when a decision, convention, or contract changes.
3. Create an ADR for durable architectural decisions; do not silently revise a prior decision.
4. Treat implementation as subordinate to the documents here until an ADR or specification changes.

## Index

- [Product vision](product/vision.md) and [PRD](product/PRD.md)
- [Architecture](architecture/architecture.md), [domain model](architecture/domain-model.md), [module design](architecture/module-design.md), [public contracts](architecture/public-contracts.md), [domain events](architecture/domain-events.md), [entity relationships](architecture/entity-relationships.md), [API design](architecture/api-design.md), [AI architecture](architecture/ai-architecture.md), [data model](architecture/data-model.md), [security model](architecture/security-model.md), [sequence diagrams](architecture/sequence-diagrams.md), [state diagrams](architecture/state-diagrams.md), [implementation readiness review](architecture/implementation-readiness-review.md), and [interfaces](architecture/interfaces.md)
- [Architecture decision records](adr/README.md)
- [API documentation](api/README.md)
- [Coding standards](engineering/coding-standards.md), [design principles](engineering/design-principles.md), and [testing strategy](engineering/testing-strategy.md)
- [Semantic knowledge layer](knowledge/semantic-knowledge-layer.md) and [prompt library](prompts/README.md)
- [Deployment](operations/deployment.md), [development setup](operations/development-setup.md), [security](operations/security.md), [performance](operations/performance.md), [scalability](operations/scalability.md), and [maintainability](operations/maintainability.md)
- [Roadmap](roadmap/roadmap.md), [glossary](reference/glossary.md), [research](research/README.md), and [meeting notes](meetings/README.md)
- [Codex rules](governance/codex-rules.md)
- [CI/CD quality gates](development/ci-cd.md)

## Future expansion

Each directory may add narrowly scoped documents. Link all new documents from this index.
