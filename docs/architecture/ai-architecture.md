# AI Architecture

**Purpose:** Define the controlled AI capability pipeline that supports, but never replaces, domain policy and evidence.

**Owner:** AI Systems Engineer / Principal Architect

## Design principles

AI capability is a replaceable technical adapter behind the LLM Gateway. It receives only purpose-limited, authorized context and produces constrained, untrusted output. Domain modules remain responsible for intent, semantic approval, query validation, insight sufficiency, recommendation policy, and authorization.

## Components and interactions

| Component | Responsibility | Inputs | Outputs | Boundary |
|---|---|---|---|---|
| LLM Gateway | Normalizes interchangeable language capabilities and records capability metadata. | Constrained generation or embedding request. | Typed result reference, usage and capability summary. | Never owns business truth or policy. |
| Prompt Registry | Stores reviewed, versioned, purpose-specific prompt assets and evaluation links. | Prompt identifier, version, approved variables. | Renderable prompt asset reference. | Prompts are governed assets, not code strings. |
| Semantic Retrieval | Selects approved, applicable semantic assets for a resolved intent. | Intent, actor context, data scope. | SemanticContextDTO. | Owned by Knowledge; no unapproved context. |
| Context Builder | Assembles minimal, classified, provenance-labelled context. | Semantic context, allowed history, task constraints. | Bounded context package. | Separates instructions from untrusted data. |
| Prompt Orchestrator | Selects prompt version, renders allowed variables, requests generation, validates structural output. | Task, context package, output contract. | Generation result or typed failure. | Cannot authorize, execute, or approve. |
| SQL Generator | Requests a query-specification proposal for an approved plan. | Plan, semantic context, allowed capability profile. | Candidate QuerySpecificationDTO. | SQL Engine owns subsequent validation. |
| Insight Generator | Requests candidate observations from result references and semantic context. | Result reference, plan, context. | Candidate InsightDTO. | Insights module checks evidence sufficiency. |
| Recommendation Generator | Requests candidate action proposals from eligible insights. | Insights, evidence references, business constraints. | Candidate RecommendationDTO. | Recommendations module enforces policy and review state. |
| Evaluation Pipeline | Runs curated quality, safety, grounding, regression, and refusal evaluations. | Versioned assets, scenarios, expected criteria. | Evaluation result and quality signals. | Evaluation never silently promotes an asset. |
| Memory Integration | Supplies only policy-permitted conversation summaries and captures eligible new context. | Actor context, conversation reference, retention policy. | Context references and summary. | Memory is not semantic truth. |
| Observability | Records traces, latency, capability use, safety outcomes, quality signals, and provenance references. | Stage events and evaluation outcomes. | Operational and quality records. | Does not expose sensitive prompt or result content. |

## Controlled request flow

1. Analytics resolves or requests clarification for intent.
2. Security evaluates access and Knowledge retrieves approved semantic context.
3. Memory contributes only permitted conversational references.
4. Context Builder applies classification, size, and instruction-data separation.
5. Prompt Orchestrator retrieves an approved Prompt Registry asset and invokes the LLM Gateway.
6. The receiving domain module validates the structured candidate against its own rules.
7. SQL Engine, Insights, or Recommendations either publishes a domain artifact or withholds it with a typed reason.
8. Monitoring and Security record appropriate operational and audit evidence.

## Provider abstraction

The LLM Gateway exposes capability-oriented contracts: constrained generation, embedding, capability profile, error classification, usage summary, and provenance reference. Callers request capabilities rather than provider names. Provider-specific options are isolated behind gateway configuration and cannot alter domain semantics or public DTOs.

## Evaluation pipeline

Evaluation sets are versioned by task and contain approved scenarios, semantic context, expected structural properties, safety expectations, and human-review criteria. Gates assess semantic grounding, policy adherence, query rejection behavior, evidence linkage, recommendation limitations, latency, and regression. A prompt, capability profile, or configuration version is promoted only through explicit approval.

## Memory and observability controls

Conversation summaries are retrieved after authorization and are labelled with retention status and expiry. They never override current semantic context. Traces connect question, prompt asset version, semantic version set, capability profile, validation outcome, and result references through a correlation identifier. Raw sensitive prompts, secrets, and unrestricted results are excluded or redacted.

## Future expansion

Add a formal AI evaluation scorecard, adversarial test catalogue, model-routing policy, and human-review sampling policy before production release.

