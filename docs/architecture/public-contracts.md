# Public Contracts

**Purpose:** Define stable, implementation-neutral contracts that let modules collaborate without private coupling.

**Owner:** Principal Architect

## Contract rules

Public contracts are business contracts, not transport or persistence models. Identifiers are tenant-scoped where relevant; commands carry actor, correlation, and provenance context; queries honor authorization; events are immutable facts. A contract change is versioned and reviewed before release.

## Commands

| Command | Owner | Intent |
|---|---|---|
| AskQuestion | Analytics | Start an analysis request with actor, question, scope, and conversation reference. |
| ClarifyQuestion | Analytics | Resolve ambiguity in an existing request. |
| RetrieveSemanticContext | Knowledge | Obtain approved, applicable context for an analytical intent. |
| SubmitSemanticAsset | Knowledge | Propose a semantic asset for review. |
| ApproveSemanticAsset | Knowledge | Approve a reviewed semantic version. |
| GenerateQuerySpecification | SQL Engine | Produce a bounded query specification for an approved plan. |
| ValidateQuerySpecification | SQL Engine | Validate a query specification against scope and policy. |
| ExecuteValidatedQuery | Connectors | Obtain results from a validated, authorized query. |
| GenerateVisualization | Dashboard | Create a visualization specification from authorized results. |
| CreateDashboard | Dashboard | Save a reusable dashboard composition. |
| GenerateInsights | Insights | Produce evidence-backed observations. |
| GenerateRecommendations | Recommendations | Produce bounded action proposals from evidence and insights. |
| ReviewRecommendation | Recommendations | Accept, dismiss, or request revision of a recommendation. |
| RequestGeneration | LLM Gateway | Request constrained language capability with approved context. |
| StoreConversationContext | Memory | Retain permitted conversational context. |
| ForgetConversationContext | Memory | Remove or render unavailable retained context. |
| EvaluateAccess | Security | Evaluate an action against policy. |
| RecordAudit | Security | Append a governed audit record. |
| RecordOperationalSignal | Monitoring | Record a non-business operational observation. |
| PublishConfiguration | Configuration | Publish an approved configuration version. |

## Queries

| Query | Owner | Returns |
|---|---|---|
| GetAnalysisRequest | Analytics | Lifecycle state and provenance summary. |
| GetAnalysisOutcome | Analytics | Authorized outcome, references, and explanation. |
| GetSemanticAsset / SearchSemanticAssets | Knowledge | Authorized approved semantic versions. |
| GetValidationDecision | SQL Engine | Validation state, reasons, and constraints. |
| GetConnectorCapabilities / GetResultReference | Connectors | Authorized capability or result provenance summary. |
| GetDashboard | Dashboard | Authorized dashboard composition. |
| GetInsights | Insights | Evidence-backed insights for an analysis request. |
| GetRecommendations | Recommendations | Recommendations and their review state. |
| GetCapabilityProfile | LLM Gateway | Business-neutral capability profile. |
| RetrieveConversationContext | Memory | Permitted context references and summary. |
| GetAuditTrail | Security | Authorized immutable audit trail. |
| GetOperationalStatus | Monitoring | Authorized operational-health summary. |
| GetConfiguration | Configuration | Authorized configuration value and version. |

## DTOs

| DTO | Meaning |
|---|---|
| ActorContext | Identity, tenant, roles, attributes, consent, and correlation information. |
| QuestionDTO | Original question, locale, requested scope, and conversation reference. |
| AnalyticalIntentDTO | Measure, dimensions, filters, period, comparison, ambiguity state, and confidence. |
| SemanticContextDTO | Approved asset references, definitions, relationships, rules, examples, and version set. |
| AnalysisPlanDTO | Objective, evidence requirements, steps, limits, and provenance references. |
| QuerySpecificationDTO | Read-only expression, parameters, bounds, capability needs, and fingerprint. |
| ValidationDecisionDTO | Allowed or denied state, reason codes, scope, limits, and policy references. |
| ResultReferenceDTO | Result identity, schema summary, freshness, bounds, and provenance reference. |
| VisualizationDTO | Visualization type, encodings, labels, accessibility description, and evidence reference. |
| InsightDTO | Observation, evidence references, confidence, assumptions, and hypothesis boundary. |
| RecommendationDTO | Proposed action, rationale, evidence, confidence, priority, review state, and limitations. |
| PolicyDecisionDTO | Decision, reasons, obligations, scope, expiry, and audit reference. |
| AuditEntryDTO | Immutable action, actor, outcome, timestamp, correlation, and provenance summary. |
| ConversationContextDTO | Authorized prior-turn summary, references, retention status, and expiry. |
| ConfigurationDTO | Configuration key, approved value, version, scope, and effective period. |

## Ports and interfaces

| Port or interface | Owner | Promise |
|---|---|---|
| SemanticContextProvider | Knowledge | Returns only approved and applicable semantic context. |
| QuerySpecificationGenerator | SQL Engine | Produces a bounded specification from approved inputs. |
| QuerySpecificationValidator | SQL Engine | Returns an explainable decision without executing a query. |
| QueryExecutor | Connectors | Executes only a validated, authorized, in-scope specification. |
| VisualizationProvider | Dashboard | Produces an accessible visualization specification with provenance. |
| InsightGenerator | Insights | Produces evidence-linked observations with explicit confidence. |
| RecommendationProvider | Recommendations | Produces non-autonomous, evidence-backed action proposals. |
| GenerationProvider | LLM Gateway | Produces constrained results and capability metadata. |
| ConversationMemoryProvider | Memory | Stores and retrieves only policy-permitted context. |
| AuthorizationProvider | Security | Returns a scoped, explainable policy decision. |
| AuditTrailProvider | Security | Appends and retrieves immutable audit records. |
| OperationalSignalProvider | Monitoring | Records non-business operational signals. |
| ConfigurationProvider | Configuration | Returns approved, versioned configuration values. |
| Aggregate repositories | Owning module | Load and save only the aggregate named in the domain model. |

## Events

The public events are defined fully in [domain events](domain-events.md). Consumers treat an event as notification of a completed fact, remain idempotent, and do not infer unpublished private state from it.

## Contract invariants

- Every cross-module command and query is authorized before it reveals or changes business state.
- DTOs expose references and approved business meaning, never credentials, implementation details, or unrestricted raw data.
- A module may reject a command with a typed business reason; it must not silently substitute meaning or scope.
- Commands are idempotent when retried with the same request identity and permitted context.
- Events never authorize an action by themselves; each consumer evaluates applicable policy.
- Public contract changes preserve compatibility or include a documented migration and versioning plan.

## Future expansion

Add contract version identifiers, compatibility windows, and a schema catalogue when the first public integration boundary is approved.

