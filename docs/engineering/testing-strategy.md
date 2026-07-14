# Testing Strategy

**Purpose:** Define confidence layers for safe delivery.

**Owner:** QA / Engineering Lead

## Test layers

Unit tests cover domain rules and use cases. Integration tests verify adapters against real dependencies. API tests verify contracts and authorization. End-to-end tests validate the initial question-to-recommendation path. Performance tests verify defined latency and load budgets. Security tests cover auth, authorization, injection, secrets, and dependency risk.

## AI evaluation and prompt regression

Maintain approved evaluation datasets with expected semantic grounding, SQL safety, answer quality, and refusal behavior. Run prompt regression tests against versioned templates and record provider/model/version metadata. AI outputs require deterministic structural and policy checks; qualitative scores are monitored separately.

## Coverage and mocking

Set coverage thresholds only after the baseline is measured; prioritize critical paths and mutation-resistant assertions over raw percentages. Mock at ports, not internal implementation details. Use ephemeral real services for adapter integration tests where practical.

## Future expansion

Add exact targets, test-data governance, and CI quality gates before the first production release.

