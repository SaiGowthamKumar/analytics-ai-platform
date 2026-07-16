# Data Model

**Purpose:** Define persistence ownership, records, relationships, and scalability principles without prescribing schemas or scripts.

**Owner:** Data Architect / Principal Architect

## Persistence principles

Persistence preserves aggregate ownership from the domain model. Each module owns its records and repository port; references across modules use immutable identifiers and version references. Sensitive fields are minimized, classified, encrypted as required, and never copied into convenience records.

## Owned record groups

| Owner | Record group | Contents and retention intent |
|---|---|---|
| Analytics | Analysis Request, Intent Revision, Analysis Plan, Outcome Reference | Question reference, resolved intent, lifecycle, plan revisions, artifact references, provenance; retained per audit and product policy. |
| Knowledge | Semantic Asset, Asset Version, Approval Decision, Applicability Rule | Definitions, ownership, immutable versions, approval state, effective range, relationships, rules, examples. |
| SQL Engine | Query Specification, Validation Decision | Fingerprint, bounded expression reference, validation reasons, limits, semantic and policy references; no unrestricted execution secrets. |
| Connectors | Connector Profile, Capability Profile, Result Reference, Execution Provenance | Business-facing capability, authorized scope, freshness, result metadata, execution classification. |
| Dashboard | Dashboard, Dashboard Item, Visualization Specification | Named composition, ownership, visualization references, accessibility metadata, sharing policy reference. |
| Insights | Insight, Insight Evidence Link | Observation, confidence, assumptions, evidence references, lifecycle. |
| Recommendations | Recommendation, Evidence Link, Review Decision | Action proposal, rationale, confidence, priority, review history, expiry. |
| Memory | Conversation, Conversation Turn, Context Reference, Retention Decision | Bounded summaries and references, consent, expiry, deletion/forget record. |
| Security | Policy Decision, Audit Record, Data Classification Reference | Authorization outcome, obligations, immutable action history, policy and classification references. |
| LLM Gateway | Capability Profile, Generation Request Reference, Generation Result Reference | Provider-neutral capability, constrained request/output references, quality and usage summary. |
| Monitoring | Operational Signal, Quality Evaluation | Health, latency, reliability, quality thresholds; separated from audit history. |
| Configuration | Configuration Version, Effective Scope, Approval Reference | Approved typed values, effective period, owner, rollout constraints. |
| Prompt Registry | Prompt Asset, Prompt Version, Prompt Approval, Evaluation Link | Purpose, owner, template reference, version, guardrails, approval, evaluation result references. |

## Key relationships and ownership

- Analysis Request references an immutable semantic version set, active plan, validation decision, result references, and outcome artifacts; it does not own them.
- Semantic Asset owns its versions and approval decisions; completed analysis requests retain the exact version references used.
- Query Specification belongs to SQL Engine and references an analysis plan, context set, and policy decision.
- Result Reference belongs to Connectors and may be referenced by many visualizations and insights within compatible scope.
- An Insight owns its evidence links; a Recommendation owns its evidence and review links.
- Conversation owns turns and contextual references but not analysis requests or semantic assets.
- Audit Record is append-only and links to any governed aggregate through references.
- Prompt Asset is governed separately from runtime code and links to evaluations; it does not own business rules.

## Metadata and data governance

Every persisted business record includes identity, tenant scope, owner, lifecycle state where relevant, creation and update time, correlation reference, provenance reference, and classification. Versioned records include effective interval, approval state, predecessor or successor reference, and change rationale. Soft deletion is used only when retention policy requires recoverability; otherwise erasure or cryptographic deletion follows the approved retention policy.

## Future scalability

Partition and retention strategies are selected by tenant, time, classification, and access pattern. Append-only audit, operational, and evaluation records are designed for high-volume archival. Immutable version records support reproducibility and read scaling. Result payloads are separated from result metadata and accessed only through authorized references. Module ownership allows independent storage evolution without changing public contracts.

## Future expansion

Add retention schedules, data-classification catalogue, archival policy, recovery objectives, and data-lineage views once governance requirements are approved.

