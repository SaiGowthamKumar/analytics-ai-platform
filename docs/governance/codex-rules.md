# Codex Rules

| Field    | Value                                          |
| -------- | ---------------------------------------------- |
| Document | Codex Rules                                    |
| Version  | 1.0                                            |
| Status   | Approved                                       |
| Owner    | Principal Architect                            |
| Audience | Humans, AI Coding Agents (Codex), Contributors |

---

# Purpose

This document defines the mandatory engineering, architectural, and implementation rules that every contributor—including AI coding agents—must follow.

These rules ensure the repository remains maintainable, consistent, scalable, and aligned with the approved Project Constitution.

If any instruction conflicts with this document, this document takes precedence unless superseded by an approved Architecture Decision Record (ADR).

---

# Guiding Principle

Codex acts as a **Senior Software Engineer**, not as the Product Owner or Software Architect.

Codex may implement approved designs, but it must never redefine the project's vision, architecture, or engineering standards without explicit approval.

---

# General Rules

* Follow the Project Constitution before writing code.
* Read the relevant documentation before implementing a feature.
* Respect module ownership and architectural boundaries.
* Keep implementations simple and maintainable.
* Prefer clarity over cleverness.
* Do not introduce speculative features.
* Do not modify unrelated code while implementing a feature.

---

# Architecture Rules

Codex must never violate the approved architecture.

Mandatory rules:

* Respect Clean Architecture.
* Respect Ports & Adapters.
* Respect DDD-lite module boundaries.
* Respect dependency inversion.
* Respect modular monolith principles.

The following are prohibited:

* Domain importing infrastructure.
* Business logic inside controllers or adapters.
* Circular dependencies.
* Hidden dependencies.
* Tight coupling between modules.
* Direct access to another module's internals.

---

# Module Rules

Every module owns one business capability.

Modules communicate only through:

* Public application interfaces
* Domain events
* Approved contracts

Never import another module's internal implementation.

---

# Dependency Rules

Always depend on abstractions.

Prefer:

* Interfaces
* Dependency Injection
* Factory Pattern
* Strategy Pattern
* Repository Pattern

Avoid direct instantiation of infrastructure components inside business logic.

---

# Implementation Rules

Before implementing code:

1. Understand the requirement.
2. Review the architecture.
3. Respect the folder structure.
4. Implement only the requested scope.

Every implementation should:

* Have a single responsibility.
* Be modular.
* Be testable.
* Be readable.
* Minimize side effects.

---

# Code Quality Rules

Every contribution should:

* Follow SOLID principles.
* Follow KISS.
* Follow DRY.
* Follow YAGNI.
* Use meaningful names.
* Keep functions focused.
* Avoid unnecessary abstractions.
* Use explicit typing where supported.
* Handle errors gracefully.

---

# Testing Rules

Every feature should include tests appropriate to its scope.

Prefer:

* Unit Tests
* Integration Tests
* Contract Tests

Business logic should be testable without infrastructure.

AI-related functionality should include evaluation or regression tests where practical.

---

# Documentation Rules

Documentation is part of the implementation.

Whenever a feature changes:

* Update relevant documentation.
* Update examples if affected.
* Update API documentation if required.
* Create or update ADRs for architectural changes.

Documentation and implementation should never diverge.

---

# Security Rules

Treat every external input as untrusted.

This includes:

* User prompts
* Generated SQL
* LLM responses
* Uploaded files
* Metadata
* Connector responses

Never:

* Execute unsafe SQL.
* Log secrets.
* Log sensitive data.
* Store credentials in source code.
* Bypass authorization checks.

---

# AI-Specific Rules

When interacting with LLMs:

* Keep prompts versioned.
* Separate prompts from business logic.
* Keep providers interchangeable.
* Do not hardcode provider-specific behavior into the domain.
* Validate generated SQL before execution.
* Ground responses using approved semantic knowledge.
* Prefer retrieval over model assumptions.

---

# Performance Rules

Avoid:

* Premature optimization.
* Repeated database queries.
* Unnecessary LLM calls.
* Duplicate semantic retrieval.

Prefer:

* Caching where appropriate.
* Efficient orchestration.
* Reusable services.

---

# Git & Repository Rules

Every implementation should:

* Be atomic.
* Solve one problem.
* Preserve repository consistency.
* Keep commits focused.

Do not combine unrelated changes into one implementation.

---

# Change Management

When introducing:

* New architecture
* New technology
* New dependency
* New design pattern
* New module
* Breaking API changes

An ADR must be created or updated before implementation.

---

# Definition of Done

A task is complete only when:

* Requirements are satisfied.
* Architecture rules are respected.
* Module boundaries are preserved.
* Tests pass.
* Documentation is updated.
* No unnecessary dependencies are introduced.
* No security rules are violated.
* Public interfaces remain stable.
* Code review checklist is satisfied.

---

# What Codex Must Never Do

Codex must never:

* Violate Clean Architecture.
* Place business logic in infrastructure.
* Create circular dependencies.
* Introduce "helper", "misc", or "temp" modules.
* Duplicate business logic.
* Hardcode provider-specific behavior.
* Ignore failed tests.
* Silence errors instead of handling them.
* Skip documentation updates.
* Modify unrelated files without justification.
* Rewrite approved architecture without an ADR.

---

# Engineering Philosophy

Every implementation should optimize for:

1. Maintainability
2. Correctness
3. Readability
4. Testability
5. Extensibility
6. Security
7. Observability
8. Performance

Never sacrifice long-term maintainability for short-term convenience.

---

# Living Document Policy

This document is part of the Project Constitution.

Changes should be rare and deliberate.

Any modification that affects engineering governance should be reviewed alongside the relevant Architecture Decision Record (ADR) and reflected in the appropriate project documentation.
