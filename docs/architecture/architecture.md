# Architecture

| Field    | Value                                  |
| -------- | -------------------------------------- |
| Document | Software Architecture                  |
| Version  | 1.0                                    |
| Status   | Approved                               |
| Owner    | Principal Architect                    |
| Audience | Engineering, AI, Product, Contributors |

---

# Purpose

This document defines the architectural foundation of the AI Analytics Platform.

It establishes:

* System architecture
* Module boundaries
* Dependency rules
* Communication patterns
* Design principles
* Technology decisions
* Evolution strategy

Every implementation must conform to this document.

---

# Architectural Goals

The architecture must:

* Support long-term maintainability.
* Remain provider agnostic.
* Enable independent module evolution.
* Preserve business logic from infrastructure concerns.
* Support enterprise scalability.
* Encourage testability.
* Minimize coupling.
* Maximize cohesion.
* Support future distributed deployment without rewriting business logic.

---

# Architectural Style

The platform follows a combination of:

* Clean Architecture
* Ports and Adapters (Hexagonal Architecture)
* Domain-Driven Design (DDD-lite)
* SOLID Principles
* Modular Monolith (MVP)

Future migration to microservices should require extraction rather than redesign.

---

# Architecture Principles

The following principles are mandatory.

## Business Logic First

Business rules belong only inside the Domain.

---

## Infrastructure Independence

The Domain must never know:

* FastAPI
* SQLAlchemy
* PostgreSQL
* Gemini
* Groq
* OpenAI
* Environment Variables
* HTTP
* Docker

Infrastructure depends on the Domain.

Never the reverse.

---

## Replaceable Components

Every external dependency must be replaceable.

Examples:

* LLM Providers
* Databases
* Visualization Engines
* Authentication Providers
* BI Tools

Changing providers should require configuration changes—not business logic changes.

---

## Single Responsibility

Every module owns exactly one business capability.

---

## Explicit Dependencies

Hidden dependencies are forbidden.

All dependencies must be injected.

---

# Architectural Layers

```text
Presentation Layer
        │
        ▼
Application Layer
        │
        ▼
Domain Layer
        │
        ▼
Infrastructure Layer
```

---

## Presentation Layer

Responsibilities:

* REST APIs
* Web UI
* Request validation
* Authentication integration
* Response formatting

Must never contain business logic.

---

## Application Layer

Responsibilities:

* Use Cases
* Workflow orchestration
* Transaction boundaries
* Coordination between modules
* Authorization decisions

May depend only on Domain abstractions.

---

## Domain Layer

Responsibilities:

* Entities
* Value Objects
* Business Rules
* Domain Services
* Interfaces (Ports)

The Domain is the heart of the platform.

It must not import infrastructure frameworks.

---

## Infrastructure Layer

Responsibilities:

* Database implementations
* LLM implementations
* Connectors
* Logging
* Caching
* Messaging
* External APIs

Infrastructure implements Domain interfaces.

---

# Dependency Rules

Dependencies always point inward.

```text
Presentation

↓

Application

↓

Domain

↑

Infrastructure
```

Allowed:

Presentation → Application

Application → Domain

Infrastructure → Domain

Forbidden:

Domain → Infrastructure

Application → FastAPI

Domain → SQLAlchemy

Domain → Gemini SDK

Presentation → Database

Cross-module internal access

---

# Module Boundaries

## Analytics

Responsible for:

* Question orchestration
* Workflow execution
* Coordination

---

## Knowledge

Responsible for:

* Business glossary
* Metadata
* Semantic retrieval
* KPI definitions

---

## SQL Engine

Responsible for:

* SQL generation
* SQL validation
* Query optimization

---

## Dashboard

Responsible for:

* Visualization specification
* Chart generation
* Dashboard models

---

## Insights

Responsible for:

* Trend analysis
* Business explanations
* Confidence scoring

---

## Recommendations

Responsible for:

* Action generation
* Recommendation ranking
* Business reasoning

---

## Connectors

Responsible for:

* PostgreSQL
* SQL Server
* Snowflake
* BigQuery
* CRM systems

Only this module communicates with external systems.

---

## LLM Gateway

Responsible for:

* Provider abstraction
* Prompt execution
* Retry logic
* Provider selection

---

## Memory

Responsible for:

* Conversation history
* Context retrieval
* Session state

---

## Security

Responsible for:

* Authorization
* Policy validation
* Audit policies

---

## Monitoring

Responsible for:

* Logging
* Metrics
* Tracing
* Health checks

---

# Module Communication

Modules communicate only through:

* Public interfaces
* Application services
* Domain events

Direct access to another module's internal classes is prohibited.

---

# Core Workflow

```text
User Question

↓

Intent Detection

↓

Semantic Context Retrieval

↓

Analysis Planning

↓

SQL Generation

↓

SQL Validation

↓

Policy Validation

↓

Query Execution

↓

Visualization

↓

Insight Generation

↓

Recommendation Generation

↓

Audit Logging

↓

Response
```

---

# Component View

```text
Frontend

↓

REST API

↓

Application Services

↓

Domain

↓

Infrastructure

├── PostgreSQL

├── Gemini

├── Groq

├── OpenRouter

├── Connectors

└── Logging
```

---

# Data Flow

Business Question

↓

Business Intent

↓

Semantic Context

↓

Execution Plan

↓

Validated SQL

↓

Authorized Data Access

↓

Business Results

↓

Visualization

↓

Insights

↓

Recommendations

↓

Audit Trail

---

# Design Patterns

Mandatory patterns:

* Factory
* Repository
* Strategy
* Adapter
* Dependency Injection

Architectural patterns:

* Clean Architecture
* Ports & Adapters
* DDD-lite
* Modular Monolith

Microservices are explicitly out of scope for the MVP.

---

# Technology Decisions

Backend

* FastAPI
* Python

Frontend

* React
* TypeScript

Persistence

* PostgreSQL

ORM

* SQLAlchemy

AI

* Provider-agnostic gateway

Deployment

* Docker

---

# Scalability Strategy

### Phase 1

Modular Monolith

### Phase 2

Extract Connector Service

### Phase 3

Extract Knowledge Service

### Phase 4

Extract Analytics Service

### Phase 5

Full Event-Driven Architecture (if justified)

No service should be extracted before there is a demonstrated operational need.

---

# Architecture Constraints

The following are prohibited:

* Business logic in controllers.
* Business logic in adapters.
* Domain importing infrastructure.
* Circular dependencies.
* Hardcoded provider implementations.
* Shared mutable state between modules.
* Direct database access outside connectors.

---

# Architecture Decision Records (ADR)

Any architectural change that affects:

* Dependencies
* Module boundaries
* Design patterns
* Technology choices
* Communication models

must be accompanied by a new ADR.

---

# Definition of Done

A feature is architecturally complete only when:

* Layer boundaries are respected.
* Dependency rules are followed.
* Public interfaces are documented.
* Unit tests pass.
* Integration tests pass.
* No forbidden dependencies exist.
* Documentation is updated.
* ADRs are created if architecture changes.

---

# Future Evolution

Future architectural enhancements include:

* C4 model diagrams
* Deployment topology
* Event catalog
* Sequence diagrams per module
* Service extraction strategy
* Multi-region deployment
* High-availability architecture
* Disaster recovery planning

These enhancements must preserve the architectural principles defined in this document.
