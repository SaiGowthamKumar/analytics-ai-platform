# Sequence Diagrams

**Purpose:** Show the technical collaboration sequence for the approved business workflow.

**Owner:** Principal Architect

## Ask Question

~~~mermaid
sequenceDiagram
  participant U as Actor
  participant API as API Adapter
  participant A as Analytics
  participant S as Security
  participant M as Memory
  U->>API: Submit question and scope
  API->>S: Evaluate access
  S-->>API: Policy decision
  API->>A: AskQuestion
  A->>M: Retrieve permitted context
  A-->>API: Analysis request or clarification
  API-->>U: Accepted request or clarification
~~~

## Retrieve Context

~~~mermaid
sequenceDiagram
  participant A as Analytics
  participant K as Knowledge
  participant S as Security
  A->>K: RetrieveSemanticContext
  K->>S: Validate semantic access
  S-->>K: Policy decision
  K-->>A: Approved semantic context
  K-->>A: SemanticContextRetrieved
~~~

## Generate SQL

~~~mermaid
sequenceDiagram
  participant A as Analytics
  participant Q as SQL Engine
  participant K as Knowledge
  participant G as LLM Gateway
  participant S as Security
  A->>Q: GenerateQuerySpecification
  Q->>K: Use approved semantic context
  Q->>G: Request constrained proposal
  G-->>Q: Candidate specification
  Q->>S: Validate action constraints
  S-->>Q: Policy decision
  Q-->>A: SQLGenerated and validation request
~~~

## Execute Query

~~~mermaid
sequenceDiagram
  participant Q as SQL Engine
  participant S as Security
  participant C as Connectors
  Q->>Q: ValidateQuerySpecification
  Q->>S: Validate action
  S-->>Q: ActionValidated
  Q-->>C: ExecuteValidatedQuery
  C->>S: Re-check effective scope
  S-->>C: Allow decision
  C-->>Q: QueryExecuted with result reference
~~~

## Generate Dashboard

~~~mermaid
sequenceDiagram
  participant A as Analytics
  participant D as Dashboard
  participant K as Knowledge
  A->>D: GenerateVisualization
  D->>K: Resolve metric labels and definitions
  K-->>D: Approved semantic references
  D-->>A: VisualizationGenerated
~~~

## Generate Insight

~~~mermaid
sequenceDiagram
  participant A as Analytics
  participant I as Insights
  participant K as Knowledge
  participant G as LLM Gateway
  A->>I: GenerateInsights
  I->>K: Retrieve applicable meaning
  I->>G: Request candidate observation
  G-->>I: Candidate insight
  I->>I: Check evidence sufficiency
  I-->>A: InsightGenerated or InsightWithheld
~~~

## Generate Recommendation

~~~mermaid
sequenceDiagram
  participant A as Analytics
  participant R as Recommendations
  participant S as Security
  participant G as LLM Gateway
  A->>R: GenerateRecommendations
  R->>G: Request candidate actions
  G-->>R: Candidate recommendation
  R->>S: Validate action policy
  S-->>R: ActionValidated or AccessDenied
  R-->>A: RecommendationGenerated or RecommendationWithheld
~~~

## Audit

~~~mermaid
sequenceDiagram
  participant X as Requesting Module
  participant S as Security
  participant AU as Audit Trail
  participant O as Monitoring
  X->>S: RecordAudit with provenance
  S->>AU: Append immutable audit record
  AU-->>S: Audit reference
  S-->>O: AuditRecorded
  S-->>X: Audit confirmation
~~~

## Future expansion

Add timing budgets, asynchronous delivery branches, retries, and failure-recovery diagrams after operational objectives are approved.

