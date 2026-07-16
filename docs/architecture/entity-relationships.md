# Entity Relationships

**Purpose:** Define business relationships, cardinality, ownership, lifecycle, and aggregate boundaries without prescribing storage design.

**Owner:** Domain Architect

## Relationship model

| Relationship | Cardinality | Ownership and aggregate boundary | Lifecycle and invariant |
|---|---|---|---|
| Tenant to Actor | One tenant has many actors; an actor uses one tenant context per action. | Security owns access context; Actor is referenced by business aggregates. | Every governed action has one tenant and actor context. |
| Actor to Analysis Request | One actor creates many requests; each request has one requester. | Analytics owns request; actor is immutable reference. | Request ownership never changes. |
| Conversation to Analysis Request | One conversation contains many requests; a request belongs to zero or one conversation. | Memory owns conversation; Analytics owns request. | Standalone requests are allowed; reuse is policy-controlled. |
| Analysis Request to Analytical Intent | One request has one current intent and prior revisions. | Analytics aggregate. | Planning cannot start while current intent is ambiguous. |
| Analysis Request to Semantic Context | One request uses many asset versions; an asset version supports many requests. | Knowledge owns assets; Analytics stores references only. | Completed work records exact approved versions. |
| Analysis Request to Analysis Plan | One request has many revisions; one plan is active. | Analytics aggregate. | Active plan is bounded and tied to intent and context. |
| Analysis Plan to Query Specification | One plan yields many candidates; one validated specification is active per execution attempt. | SQL Engine owns validation state. | Validation needs active plan and approved scope. |
| Query Specification to Policy Decision | One specification needs one or more decisions; a decision constrains many scoped actions. | Security owns decisions. | Execution requires effective allow decision and obligations. |
| Query Specification to Result Reference | One validated specification has many attempts; each success yields one result reference. | Connectors owns result provenance. | Result is immutable and scoped to freshness and authorization. |
| Result Reference to Visualization | One result supports many visualizations; a visualization has one primary result. | Dashboard owns visualization. | Labels and encodings follow referenced semantic definitions. |
| Result Reference to Insight | One result supports many insights; each insight has one or more evidence references. | Insights owns insight. | Confidence and assumptions are explicit. |
| Insight to Recommendation | One insight supports many recommendations; a recommendation references one or more insights or direct evidence. | Recommendations owns recommendation. | A recommendation cannot exceed its evidence or authorize action. |
| Analysis Request to Audit Record | One request has many audit records. | Security owns audit record. | Audit records append; they reference rather than duplicate sensitive content. |
| Semantic Asset to Version | One asset has many versions; each version belongs to one asset. | Knowledge aggregate. | At most one approved version is effective in an applicable scope. |
| Dashboard to Visualization | One dashboard has one or more visualizations. | Dashboard owns composition. | Removing a visualization does not erase analysis evidence. |
| Connector Profile to Data Scope | One profile has many scopes. | Connectors owns capability; Security owns authorization. | Capability itself does not grant access. |
| Recommendation to Review Decision | One recommendation has many decisions; one latest state. | Recommendations aggregate. | Review history is preserved without changing evidence. |

## Aggregate boundaries

- Analysis Request: question, intent, active plan, outcome references, and lifecycle state.
- Semantic Asset: content, version, approval, applicability, and deprecation.
- Recommendation: rationale, evidence references, confidence, priority, and review state.
- Conversation: turns and contextual references under one retention policy.
- Connector Profile: source capability and permitted scope; authorization remains external.
- Audit Record: append-only history that is never revised.

## Lifecycle model

~~~text
Analysis Request:
draft → asked → clarification_required | context_resolved
context_resolved → planned → generated → validated → executed
executed → visualized → interpreted → recommended → completed
any active state → refused | failed | superseded

Semantic Asset:
draft → submitted → under_review → approved → deprecated → retired

Recommendation:
draft → generated → awaiting_review → accepted | dismissed | revision_requested | expired
~~~

A request may complete without a visualization, insight, or recommendation only when outcome policy permits; it may never complete with an unsupported claim.

## Cross-aggregate consistency

Public commands and events coordinate cross-aggregate facts. A receiving aggregate validates its own invariants and never assumes another aggregate's private state. Provenance references join the business story without collapsing ownership.

## Business invariants

1. Cross-aggregate references are immutable identifiers and version references, never shared mutable objects.
2. Semantic approval precedes production use; authorization precedes data access; evidence precedes insight; insight or direct evidence precedes recommendation.
3. A later semantic version never changes the meaning recorded for a completed analysis.
4. Reuse requires compatible tenant, actor, semantic version, data scope, and retention policy.
5. Audit history reconstructs why an outcome was allowed, refused, or constrained.
6. No aggregate owns credentials, unrestricted raw data, or another module's lifecycle state.

## Future expansion

Add relationship diagrams for tenancy, stewardship, dashboard sharing, and delegated review when those capabilities enter scope.

