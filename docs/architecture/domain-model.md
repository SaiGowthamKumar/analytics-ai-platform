# Domain Model (DDD-lite)

**Purpose:** Establish the ubiquitous language and initial business boundaries.

**Owner:** Domain Architect / Product Lead

## Bounded contexts

Analytics, Knowledge, Dashboard, Insights, Recommendations, Connectors, Identity & Security, and Platform Operations.

## Entities and aggregates

| Aggregate | Entity root | Key responsibilities |
|---|---|---|
| Analysis Request | `AnalysisRequest` | lifecycle, intent, provenance, result reference |
| Semantic Asset | `SemanticAsset` | definition, version, approval state |
| Dashboard | `Dashboard` | visualization specification and ownership |
| Recommendation | `Recommendation` | evidence, confidence, action status |
| Connector | `Connector` | authorized connection configuration and capability |

## Value objects

Question, Actor, TenantId, MetricDefinition, SemanticVersion, QueryPlan, SafeSql, DataScope, VisualizationSpec, Evidence, Confidence, and PolicyDecision.

## Repositories and services

Repositories abstract aggregate persistence: AnalysisRequestRepository, SemanticAssetRepository, DashboardRepository, RecommendationRepository, ConnectorRepository. Domain services include QuerySafetyPolicy, SemanticResolutionPolicy, and RecommendationEvidencePolicy.

## Relationships and rules

An analysis request references one approved semantic version and one authorized data scope. A dashboard is derived from an analysis result. An insight and recommendation must retain evidence. Only approved semantic assets can inform production answers; generated SQL must be read-only, scoped, validated, and auditable.

## Future expansion

Add state machines, event schemas, and context maps after discovery workshops.

