# ADR-002: Modular Monolith

**Purpose:** Record the initial deployment and modularity boundary.

**Owner:** Principal Architect

**Status:** Accepted

## Context

The product needs rapid iteration with clear domain ownership.

## Decision

Begin as a modular monolith with enforceable module boundaries.

## Alternatives

Microservices; unstructured monolith.

## Consequences

Simpler operations and transactions; modules must be designed for later extraction.

## Tradeoffs

Shared deployment versus early independent scaling.

## Future expansion

Define extraction criteria as scale evidence emerges.
