# API Philosophy

The REST API is a delivery adapter that exposes the platform's public capabilities.

The API is intentionally thin.

Business decisions belong in the Application and Domain layers.

The API is responsible only for:

- Authentication
- Transport validation
- Request mapping
- Response serialization
- Error translation
- Correlation
- Rate limiting

Every endpoint should map directly to one application use case.

The API should never contain business logic.
# API Design

**Purpose:** Define a versioned REST delivery contract over approved public module contracts.

**Owner:** API Lead / Principal Architect

## Boundary and conventions

The API is a delivery adapter: it authenticates, validates transport shape, invokes public application commands or queries, and translates typed outcomes. It contains no business rules. All routes use the prefix /api/v1, JSON media type, UTC timestamps in ISO 8601, opaque identifiers, camelCase fields, and plural resource names. Authorization is evaluated for every request and response.

Every response includes correlationId. Requests may include X-Correlation-ID; otherwise the service creates one. Sensitive data is redacted according to policy.

## Resources and operations

| Resource | Operations | Public contract mapping |
|---|---|---|
| Analysis requests | POST /analysis-requests; GET /analysis-requests/{id}; GET /analysis-requests/{id}/outcome | AskQuestion, GetAnalysisRequest, GetAnalysisOutcome |
| Clarifications | POST /analysis-requests/{id}/clarifications | ClarifyQuestion |
| Semantic assets | GET /semantic-assets; GET /semantic-assets/{id}; POST /semantic-assets; POST /semantic-assets/{id}/approvals | SearchSemanticAssets, GetSemanticAsset, SubmitSemanticAsset, ApproveSemanticAsset |
| Dashboards | POST /dashboards; GET /dashboards/{id} | CreateDashboard, GetDashboard |
| Recommendations | GET /analysis-requests/{id}/recommendations; POST /recommendations/{id}/reviews | GetRecommendations, ReviewRecommendation |
| Conversations | GET /conversations/{id}/context; DELETE /conversations/{id}/context | RetrieveConversationContext, ForgetConversationContext |
| Audit trail | GET /audit-records | GetAuditTrail |
| Capabilities | GET /connectors/{id}/capabilities; GET /ai/capabilities | GetConnectorCapabilities, GetCapabilityProfile |
| Operational status | GET /operational-status | GetOperationalStatus |

## Request DTOs

| DTO | Required fields | Rules |
|---|---|---|
| AskQuestionRequest | question, requestedScope | Question is bounded text; scope is constrained to the actor's authorized context; optional conversationId and locale are validated. |
| ClarificationRequest | answer | Belongs to the current actor's authorized analysis request. |
| SemanticAssetSubmissionRequest | assetType, name, definition, applicability | Draft only; no client may self-approve unless policy explicitly permits. |
| SemanticAssetApprovalRequest | decision | Approval includes policy-required rationale and is idempotent. |
| CreateDashboardRequest | name, visualizationReferences | Every reference must be visible to the actor and semantically compatible. |
| RecommendationReviewRequest | decision | Accept, dismiss, or request revision; optional rationale is policy-controlled. |
| ListRequest | pageSize, pageToken, sort, filter | Page size is bounded; sort and filter fields are resource-specific allowlists. |

## Response DTOs

| DTO | Required fields |
|---|---|
| AnalysisRequestResponse | id, lifecycleState, intentSummary, createdAt, updatedAt, correlationId, provenanceReference |
| AnalysisOutcomeResponse | request, answerSummary, semanticContextReferences, resultReference, visualizations, insights, recommendations, limitations, provenanceReference |
| SemanticAssetResponse | id, assetType, name, version, approvalState, applicability, owner, effectivePeriod |
| DashboardResponse | id, name, owner, visualizations, provenanceReferences |
| RecommendationResponse | id, action, rationale, evidenceReferences, confidence, priority, reviewState, limitations |
| PageResponse | items, nextPageToken, pageSize, totalCount when policy permits |
| CapabilityResponse | identifier, capabilitySummary, constraints, effectiveScope |
| AuditRecordResponse | id, action, actorReference, outcome, occurredAt, correlationId, provenanceReference |

The API returns references to governed evidence rather than unrestricted result payloads. A response may include a safe explanation, clarification request, or refusal instead of an analytical outcome.

## Errors and status codes

All errors use one envelope: error.code, error.message, error.details, correlationId, and retryable. Error messages are safe for clients; diagnostic detail is retained only in governed audit and operational records.

| Status | Use | Example code |
|---|---|---|
| 200 | Successful query or action with immediate outcome | ANALYSIS_OUTCOME_AVAILABLE |
| 201 | New resource created | ANALYSIS_REQUEST_CREATED |
| 202 | Accepted for asynchronous completion | ANALYSIS_IN_PROGRESS |
| 204 | Successful deletion or context forget action | CONTEXT_FORGOTTEN |
| 400 | Invalid shape, malformed filter, or impossible request | INVALID_REQUEST |
| 401 | Authentication absent or invalid | UNAUTHENTICATED |
| 403 | Authenticated actor lacks permitted scope | ACCESS_DENIED |
| 404 | Resource is absent or intentionally undiscoverable | RESOURCE_NOT_FOUND |
| 409 | Lifecycle or idempotency conflict | STATE_CONFLICT |
| 422 | Valid shape but failed domain validation | AMBIGUOUS_INTENT, QUERY_REJECTED |
| 429 | Rate or resource budget exceeded | RATE_LIMITED |
| 500 | Unexpected internal failure | INTERNAL_ERROR |
| 503 | A required capability is unavailable | DEPENDENCY_UNAVAILABLE |

## Idempotency, pagination, and versioning

Commands that create or change business state require an Idempotency-Key. The key is scoped to actor, tenant, route, and request fingerprint; replay returns the original terminal or in-progress response. A changed payload with the same key returns 409.

Collections use cursor pagination only. Page tokens are opaque, signed or protected, scoped to actor and query filters, and expire. Offset pagination is not permitted for governed resources.

Breaking API changes create a new major path version. Additive fields are permitted in the same version. Deprecated fields and routes state a sunset date, migration guidance, and contract owner.

## Future expansion

Add an OpenAPI artifact, resource-specific filtering grammar, rate-limit tiers, and asynchronous callback policy after the first delivery adapter is approved.

