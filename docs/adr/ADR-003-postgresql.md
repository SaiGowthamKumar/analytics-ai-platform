# ADR-003: PostgreSQL

**Purpose:** Record the proposed transactional metadata store.

**Owner:** Principal Architect

**Status:** Proposed

## Context

A transactional system of record is needed for platform metadata and governance.

## Decision

Use PostgreSQL, subject to approval.

## Alternatives

MySQL, SQL Server, managed document store.

## Consequences

Strong relational modeling and mature tooling; operational and extension choices remain.

## Tradeoffs

Relational fit versus specialized-store flexibility.

## Future expansion

Record the final managed-service and extension choices on acceptance.
