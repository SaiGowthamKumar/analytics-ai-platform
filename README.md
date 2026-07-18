# AI Analytics Platform

[![Continuous Integration](https://github.com/<OWNER>/<REPOSITORY>/actions/workflows/ci.yml/badge.svg)](https://github.com/<OWNER>/<REPOSITORY>/actions/workflows/ci.yml)

> **An enterprise-ready, provider-agnostic AI Analytics Platform that transforms natural-language business questions into trusted dashboards, insights, and recommendations using enterprise data, semantic knowledge, and intelligent orchestration.**

---

# Overview

The AI Analytics Platform enables business users to interact with enterprise data using natural language instead of SQL, dashboards, or complex Business Intelligence tools.

The platform combines:

* Enterprise data sources
* Semantic business knowledge
* Large Language Models (LLMs)
* Intelligent orchestration
* Governed query execution
* Explainable AI

to provide trusted analytical outcomes in seconds.

The long-term vision is to become an **Enterprise Analytics Operating System**, where analytics is conversational, explainable, and proactive rather than static and report-driven.

---

# Project Status

**Current Phase:** Foundation & Architecture

The project follows a **Documentation-First Development** methodology.

Implementation begins **only after** the product vision, architecture, engineering standards, and governance documents have been reviewed and approved.

Current milestone:

* ✅ Repository initialized
* ✅ Project Constitution in progress
* ⏳ Core platform implementation pending

---

# Core Workflow

The first implementation milestone delivers one complete end-to-end analytics workflow.

```text
Natural Language Question
        │
        ▼
Intent Understanding
        │
        ▼
Semantic Context Retrieval
        │
        ▼
SQL Generation
        │
        ▼
Query Validation
        │
        ▼
Query Execution
        │
        ▼
Visualization Generation
        │
        ▼
Insight Generation
        │
        ▼
Recommendation Generation
        │
        ▼
Conversational Follow-up
```

Everything else is built incrementally on top of this workflow.

---

# Repository Structure

```text
analytics-ai-platform/

├── docs/
├── backend/
├── frontend/
├── infrastructure/
├── docker/
├── scripts/
├── tests/
├── .github/
├── README.md
└── .gitignore
```

---

# Repository Guide

## docs/

The single source of truth for the project.

Contains:

* Product Vision
* PRD
* Architecture
* Architecture Decision Records (ADR)
* Coding Standards
* Design Principles
* Roadmap
* Governance
* Prompt Library
* Security
* Testing Strategy
* Deployment Guide

---

## backend/

Future FastAPI application implementing the core analytics platform.

Responsibilities include:

* Application Layer
* Domain Layer
* Infrastructure Layer
* API
* Connectors
* AI Engine
* Semantic Layer
* Analytics Engine

---

## frontend/

Future React + TypeScript web application.

Responsibilities include:

* Chat Interface
* Dashboard
* Administration
* Knowledge Management
* Connector Management
* Settings

---

## infrastructure/

Infrastructure and deployment resources.

Examples:

* Docker
* Docker Compose
* Kubernetes (future)
* Terraform (future)
* CI/CD

---

## tests/

Cross-cutting automated testing.

Includes:

* Unit Tests
* Integration Tests
* End-to-End Tests
* AI Evaluation
* Prompt Regression
* Performance Tests

---

# Engineering Principles

This project is built around the following architectural principles.

* Documentation First
* Clean Architecture
* Domain-Driven Design (DDD-lite)
* Ports & Adapters (Hexagonal Architecture)
* SOLID Principles
* Modular Monolith (MVP)
* Provider Independence
* Infrastructure Independence
* Testability by Design
* Security by Default

---

# Technology Stack

## Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Dependency Injection
* Docker

## Frontend

* React
* TypeScript
* Vite

## AI

* Provider-Agnostic LLM Gateway
* Gemini
* Groq
* OpenRouter
* Ollama (future)

## Knowledge

* Semantic Knowledge Layer
* Business Glossary
* Metadata
* Prompt Library
* Vector Search (future)

---

# Development Philosophy

This project follows a simple rule:

> **Build a stable foundation before adding complexity.**

New features must not compromise:

* Maintainability
* Explainability
* Governance
* Scalability
* Provider Independence

---

# Working Agreement

Before implementing any feature:

1. Read the relevant documentation in `docs/`.
2. Ensure the feature aligns with the Product Vision.
3. Follow the Project Constitution.
4. Respect the dependency rules defined in the architecture.
5. Update documentation if the design changes.
6. Create or update an ADR for significant architectural decisions.
7. Only then begin implementation.

The project's engineering rules are defined in:

`docs/governance/codex-rules.md`

---

# Roadmap

The project progresses through the following milestones:

* **Foundation** — Repository, documentation, architecture
* **Core Intelligence** — Analytics engine, semantic retrieval, SQL generation
* **Knowledge Layer** — Business glossary, metadata, governance
* **Visualization & Insights** — Charts, explanations, recommendations
* **Enterprise Platform** — Authentication, connectors, administration
* **Agentic Intelligence** — Multi-agent workflows and proactive analytics

---

# Contributing

This repository is currently maintained as a documentation-first side project.

Every contribution should:

* Follow the established architecture.
* Respect coding standards.
* Preserve module boundaries.
* Include appropriate tests.
* Update documentation where applicable.

---

# License

*To be determined.*

---

# Contact

For architectural discussions, refer to the documentation in the `docs/` directory before proposing implementation changes.

The documentation is considered the project's single source of truth.
