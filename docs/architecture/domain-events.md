# Domain Events

**Purpose:** Define immutable business facts that allow modules to react without private coupling.

**Owner:** Domain Architect / Principal Architect

## Event rules

Every event carries an event identity, type, occurrence time, tenant, correlation and causation references, publisher, aggregate reference, contract version, and redacted provenance reference. Events contain only the minimum business payload needed by consumers.

| Event | Publisher | Consumers | Payload | Business meaning |
|---|---|---|---|---|
| QuestionAsked | Analytics | Knowledge, Memory, Security, Monitoring | request, actor, question reference, requested scope, conversation reference | An actor has formally requested governed analysis. |
| QuestionClarificationRequested | Analytics | Memory, Monitoring | request, ambiguity reasons, clarification prompts | The request cannot proceed until intent is clarified. |
| QuestionClarified | Analytics | Knowledge, Memory, Security | request, clarified intent, actor | The actor resolved all or part of an ambiguity. |
| SemanticContextRetrieved | Knowledge | Analytics, SQL Engine, Dashboard, Insights, Monitoring | request, approved asset references, version set, applicability summary | Approved business meaning has been selected. |
| SemanticAssetSubmitted | Knowledge | Security, Monitoring | asset reference, version, submitter, applicability | A semantic asset awaits governance review. |
| SemanticAssetApproved | Knowledge | Analytics, SQL Engine, Dashboard, Insights, Recommendations | asset reference, approved version, approver, effective scope | A new immutable business meaning is available. |
| SemanticAssetDeprecated | Knowledge | Analytics, Dashboard, Insights, Recommendations | asset reference, successor, effective end | An existing definition is unavailable for new work. |
| AnalysisPlanned | Analytics | SQL Engine, Security, Monitoring | request, plan reference, intent summary, evidence requirements | The bounded analytical work has been defined. |
| AnalysisCompleted | Analytics | Memory, Security, Monitoring | request, outcome references, completion state, provenance | The analysis lifecycle reached a governed terminal outcome. |
| AnalysisRefused | Analytics | Security, Memory, Monitoring | request, refusal reasons, safe next step, provenance | The platform declined to produce an outcome because required conditions were not met. |
| SQLGenerated | SQL Engine | Security, Monitoring | request, query fingerprint, plan reference, scope summary | A query specification exists but is not executable yet. |
| SQLValidated | SQL Engine | Connectors, Analytics, Monitoring | request, validation reference, fingerprint, limits, policy references | A specification is eligible for authorized execution. |
| SQLRejected | SQL Engine | Analytics, Security, Monitoring | request, fingerprint, rejection reasons, remediation state | A specification failed safety, semantic, or policy validation. |
| QueryExecuted | Connectors | Analytics, Dashboard, Insights, Security, Monitoring | request, result reference, freshness, bounded result summary | Authorized data evidence has been obtained. |
| QueryExecutionFailed | Connectors | Analytics, Security, Monitoring | request, failure classification, retry eligibility | Evidence could not be obtained; no conclusion is implied. |
| VisualizationGenerated | Dashboard | Analytics, Insights, Monitoring | request, visualization reference, result reference, metric references | A visual representation of evidence is available. |
| DashboardCreated | Dashboard | Security, Monitoring | dashboard, owner, visualization references | A reusable presentation composition was created. |
| InsightGenerated | Insights | Analytics, Recommendations, Security, Monitoring | request, insight, evidence, confidence, assumptions | An evidence-backed business observation is available. |
| InsightWithheld | Insights | Analytics, Monitoring | request, insufficiency reasons, evidence references | Evidence is insufficient for a responsible insight. |
| RecommendationGenerated | Recommendations | Analytics, Security, Monitoring | request, recommendation, evidence, confidence, priority | A bounded action proposal is available for review. |
| RecommendationReviewed | Recommendations | Analytics, Memory, Monitoring | recommendation, reviewer, decision, rationale | A human accepted, dismissed, or requested revision. |
| RecommendationWithheld | Recommendations | Analytics, Monitoring | request, insufficiency or policy reasons | No responsible recommendation can be made. |
| AccessEvaluated | Security | Requesting module, Monitoring | action, decision, scope, obligations, expiry | A requested action received an explainable access decision. |
| AccessDenied | Security | Requesting module, Monitoring | action, denial reasons, scope | A requested action is not permitted. |
| ActionValidated | Security | Requesting module, Monitoring | action, decision, obligations | A controlled action met its required conditions. |
| AuditRecorded | Security | Monitoring | audit reference, action, actor reference, outcome, provenance | A governed action entered the immutable audit trail. |
| ConversationContextStored | Memory | Analytics, Monitoring | conversation, context reference, retention expiry | Permitted context has been retained. |
| ConversationContextExpired | Memory | Analytics, Monitoring | conversation, expired references, reason | Retained context is no longer eligible for use. |
| GenerationCompleted | LLM Gateway | Requesting module, Monitoring | request reference, output reference, capability profile | A constrained generation completed; output remains untrusted until validated. |
| GenerationFailed | LLM Gateway | Requesting module, Monitoring | request reference, failure classification, retry eligibility | A language capability request did not complete. |
| ConfigurationPublished | Configuration | Interested modules, Monitoring | key, version, scope, effective period | An approved configuration version is available. |
| ConfigurationRejected | Configuration | Security, Monitoring | configuration reference, rejection reasons | A proposed configuration failed governance. |
| OperationalSignalRecorded | Monitoring | Monitoring | signal reference, classification, correlation | A non-business operational observation was recorded. |
| QualityThresholdBreached | Monitoring | Analytics, Knowledge, SQL Engine, Security, Configuration | metric, threshold, affected scope, window | A declared quality threshold requires attention. |

## Event sequencing for the initial outcome

~~~text
QuestionAsked → SemanticContextRetrieved → AnalysisPlanned
→ SQLGenerated → SQLValidated → QueryExecuted
→ VisualizationGenerated → InsightGenerated → RecommendationGenerated
→ AnalysisCompleted → AuditRecorded
~~~

A refusal, failed validation, evidence insufficiency, or execution failure pauses or ends its branch while preserving provenance.

## Future expansion

Add event retention classes, delivery objectives, and compatibility rules when an event transport is selected.
