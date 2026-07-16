# State Diagrams

**Purpose:** Define the technical state transitions that implement approved domain lifecycles.

**Owner:** Principal Architect

## Analysis Request

~~~mermaid
stateDiagram-v2
  [*] --> Draft
  Draft --> Asked: AskQuestion
  Asked --> ClarificationRequired: ambiguity
  ClarificationRequired --> Asked: ClarifyQuestion
  Asked --> ContextResolved: semantic context approved
  ContextResolved --> Planned
  Planned --> Generated
  Generated --> Validated
  Generated --> Refused: validation denied
  Validated --> Executed
  Executed --> Visualized
  Visualized --> Interpreted
  Interpreted --> Recommended
  Recommended --> Completed
  Executed --> Completed: outcome policy permits
  Asked --> Refused: access denied
  state Active {
    Asked
    ContextResolved
    Planned
    Generated
    Validated
    Executed
    Visualized
    Interpreted
    Recommended
  }
  Active --> Failed: unrecoverable failure
  Active --> Superseded: newer request or context
  Completed --> [*]
  Refused --> [*]
  Failed --> [*]
  Superseded --> [*]
~~~

## Conversation

~~~mermaid
stateDiagram-v2
  [*] --> Open
  Open --> Active: permitted turn stored
  Active --> Active: new authorized turn
  Active --> Expired: retention period reached
  Open --> Forgotten: valid forget request
  Active --> Forgotten: valid forget request
  Expired --> [*]
  Forgotten --> [*]
~~~

## Semantic Asset

~~~mermaid
stateDiagram-v2
  [*] --> Draft
  Draft --> Submitted
  Submitted --> UnderReview
  UnderReview --> Approved: approval granted
  UnderReview --> Draft: changes requested
  Approved --> Deprecated: successor or policy change
  Deprecated --> Retired: retention complete
  Approved --> [*]: immutable version remains referencable
  Retired --> [*]
~~~

## Recommendation

~~~mermaid
stateDiagram-v2
  [*] --> Draft
  Draft --> Generated: evidence sufficient
  Generated --> AwaitingReview
  AwaitingReview --> Accepted
  AwaitingReview --> Dismissed
  AwaitingReview --> RevisionRequested
  RevisionRequested --> Draft
  AwaitingReview --> Expired
  Accepted --> [*]
  Dismissed --> [*]
  Expired --> [*]
~~~

## SQL Plan (technical state of the Query Specification)

~~~mermaid
stateDiagram-v2
  [*] --> Proposed
  Proposed --> Generated
  Generated --> ValidationPending
  ValidationPending --> Validated: read-only, scoped, policy-approved
  ValidationPending --> Rejected: invalid or unauthorized
  Validated --> Executed
  Validated --> Expired: policy or semantic context changed
  Executed --> [*]
  Rejected --> [*]
  Expired --> [*]
~~~

## Future expansion

Add explicit compensation, retry, and asynchronous-processing states when those technical mechanisms are approved.
