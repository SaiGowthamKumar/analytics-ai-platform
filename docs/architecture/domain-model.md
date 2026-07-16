# Domain Model

**Purpose:** Define the business concepts, rules, and ownership boundaries that govern trusted conversational analytics.

**Owner:** Domain Architect / Product Lead

## Business overview

The platform converts a business question into a governed analytical outcome: an answer supported by approved business meaning, authorized data evidence, an interpretable visualization, an insight, and—where appropriate—a recommendation. The domain exists to make every outcome trustworthy, traceable, and actionable rather than merely plausible.

The central business promise is: no analytical conclusion is production-ready unless its meaning, access, evidence, and provenance can be explained.

## Ubiquitous language

| Term | Meaning |
|---|---|
| Actor | A person or approved system identity requesting or governing work. |
| Business question | A natural-language request for information, explanation, comparison, or action. |
| Analysis request | The auditable lifecycle record for a business question and its outcome. |
| Analytical intent | The resolved business objective, measures, dimensions, period, and comparison implied by a question. |
| Semantic context | The approved business definitions, relationships, rules, and examples relevant to an intent. |
| Semantic asset | A governed glossary term, KPI, relationship, business rule, or approved example. |
| Analysis plan | A bounded plan that states what evidence is needed and how it will be interpreted. |
| Query specification | A provider-neutral, read-only expression of the data needed by an approved plan. |
| Policy decision | An allow, deny, or constrained decision with a reason and applicable scope. |
| Data scope | The data sources, business entities, fields, rows, period, and limits an actor may use. |
| Evidence | Traceable observations, result references, and semantic references supporting a claim. |
| Visualization | A business-facing representation of results, with its metric, dimension, and provenance. |
| Insight | An evidence-backed interpretation of a result; it states what changed or matters, not an unsupported cause. |
| Recommendation | A proposed business action linked to evidence, rationale, confidence, and review status. |
| Provenance | The chain of question, actor, semantic version, policy decisions, plan, result, and generated artifacts. |
| Conversation | A bounded sequence of related analysis requests and approved contextual references. |

## Core entities and aggregate roots

| Aggregate root | Core entities | Business responsibility |
|---|---|---|
| Analysis Request | AnalysisPlan, QuerySpecification, ResultReference, Visualization, Insight | Own the lifecycle from question through completed, clarified, refused, failed, or superseded outcome. |
| Semantic Asset | KPI Definition, Glossary Term, Relationship Definition, Business Rule, Example | Own governed business meaning, version, approval state, and applicability. |
| Recommendation | RecommendationEvidence, ActionOption, ReviewDecision | Own a proposed action, its support, confidence, and acceptance or dismissal lifecycle. |
| Connector Profile | SourceCapability, AuthorizedDataScope | Own the business-facing capability and permitted use of a data source, without exposing credentials or implementation detail. |
| Conversation | ConversationTurn, ContextReference | Own contextual continuity, retention eligibility, and safe reuse of prior requests. |
| Audit Record | AuditEntry | Own immutable evidence that a governed business action occurred. |

A Dashboard is a named, reusable collection of visualizations and analysis references. It is an entity owned by the Dashboard module, but it does not own the underlying analysis evidence.

## Value objects

Value objects are immutable and compare by value: AnalysisRequestId, ActorId, TenantId, ConversationId, SemanticAssetId, SemanticVersion, KPIFormula, BusinessTerm, TimeRange, ComparisonPeriod, DataScope, PolicyDecision, QuerySpecification, QueryFingerprint, ResultReference, VisualizationSpecification, EvidenceReference, Confidence, RecommendationPriority, ApprovalState, LifecycleState, CorrelationId, and ProvenanceReference.

## Domain services

| Service | Business responsibility |
|---|---|
| Intent Resolution Policy | Determines whether a question is sufficiently clear or needs clarification. |
| Semantic Resolution Policy | Selects applicable, approved semantic assets and detects conflicting meaning. |
| Analysis Planning Policy | Produces a bounded plan from intent and semantic context. |
| Query Safety Policy | Determines whether a query specification is read-only, scoped, and permitted. |
| Evidence Sufficiency Policy | Determines whether results can support an insight or recommendation. |
| Recommendation Policy | Ensures a recommendation is actionable, non-deceptive, and appropriately reviewable. |
| Retention Policy | Determines whether conversation or audit context may be retained and reused. |

## Repository ports

Repository ports preserve aggregate boundaries; callers do not depend on storage behavior.

| Port | Aggregate owned |
|---|---|
| AnalysisRequestRepository | Analysis Request |
| SemanticAssetRepository | Semantic Asset |
| RecommendationRepository | Recommendation |
| DashboardRepository | Dashboard |
| ConnectorProfileRepository | Connector Profile |
| ConversationRepository | Conversation |
| AuditRecordRepository | Audit Record |

## Domain rules and invariants

1. An analysis request has exactly one requesting actor, tenant, lifecycle state, and immutable provenance chain.
2. Only approved, applicable semantic asset versions may ground a production analysis.
3. A semantic asset cannot be altered after approval; a change creates a new version and supersedes the prior version deliberately.
4. A query specification must be read-only, policy-approved, bounded by data scope, and linked to an approved analysis plan before execution.
5. Results belong to the analysis request that produced them and cannot be reused outside an authorized compatible scope without a new policy decision.
6. A visualization must reference the result and metric definitions it represents.
7. An insight must identify supporting evidence and must distinguish observation from causal explanation.
8. A recommendation must reference at least one approved insight or direct evidence, state confidence, and never imply autonomous execution.
9. Audit records are append-only and record decisions rather than sensitive raw content unless retention policy explicitly allows it.
10. A refused, failed, or clarification-required request must still preserve sufficient provenance to explain the outcome.
11. Conversation context is reusable only when actor, tenant, retention, and authorization rules permit it.
12. A module owns its aggregate lifecycle; other modules receive contracts or events, never mutate its aggregate directly.

## Ownership boundaries

- **Analytics** owns Analysis Request and Analysis Plan lifecycle.
- **Knowledge** owns Semantic Asset meaning, versioning, and approval.
- **SQL Engine** owns Query Specification validation state, not business KPI definitions.
- **Connectors** owns Connector Profile capability and execution result provenance.
- **Dashboard** owns reusable Dashboard and Visualization presentation specifications.
- **Insights** owns the interpretation lifecycle and evidence sufficiency assessment.
- **Recommendations** owns Recommendation lifecycle and review status.
- **Memory** owns Conversation and permitted contextual reuse.
- **Security** owns Policy Decision and audit-policy rules.
- **Monitoring** owns operational observations, not business audit records.
- **Configuration** owns approved business-neutral runtime policy values.
- **LLM Gateway** owns model-capability requests and responses, not business intent or rules.

## Future expansion

Add domain state diagrams, glossary governance roles, and a formal context map when user-research and stewardship workflows are approved.

