# ADR-006: Provider-Agnostic LLM Layer

**Purpose:** Record the provider-independence strategy for AI capabilities.

**Owner:** Principal Architect

**Status:** Accepted

## Context

Model capability, cost, residency, and vendor availability vary.

## Decision

Depend on an `LLMProvider` port with provider adapters.

## Alternatives

Single vendor SDK; self-hosted-only models.

## Consequences

Switchability and test doubles; capability normalization is required.

## Tradeoffs

Extra abstraction versus provider-specific features.

## Future expansion

Define capability conformance tests and supported provider policy.
