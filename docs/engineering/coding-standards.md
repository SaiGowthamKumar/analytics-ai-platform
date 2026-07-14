# Coding Standards

| Field    | Value                                             |
| -------- | ------------------------------------------------- |
| Document | Coding Standards                                  |
| Version  | 1.0                                               |
| Status   | Approved                                          |
| Owner    | Engineering Lead                                  |
| Audience | Engineers, AI Coding Agents (Codex), Contributors |

---

# Purpose

This document defines the mandatory coding conventions for the AI Analytics Platform.

Its goals are to ensure:

* Readability
* Maintainability
* Consistency
* Testability
* Scalability
* Security

All production code must comply with these standards.

---

# General Principles

Code should be:

* Simple
* Explicit
* Readable
* Predictable
* Testable

Always optimize for long-term maintainability rather than short-term convenience.

---

# Python Standards

Use:

* Python 3.12+
* PEP 8
* PEP 257 (Docstrings)
* PEP 484 (Type Hints)

Mandatory:

* Explicit typing on public APIs
* Type aliases where appropriate
* Dataclasses or Pydantic models where suitable
* F-strings for formatting
* Context managers for resources

Avoid:

* Dynamic typing when avoidable
* Implicit conversions
* Magic numbers
* Deep nesting

---

# Naming Conventions

## Modules

```text
snake_case
```

Example

```text
analytics_service.py
sql_validator.py
```

---

## Classes

```text
PascalCase
```

Example

```text
AnalyticsEngine
SemanticRetriever
```

---

## Functions

```text
snake_case
```

Example

```python
generate_sql()
retrieve_context()
```

Functions should express intent through their names.

---

## Variables

Use descriptive names.

Prefer:

```python
semantic_context
query_plan
analysis_request
```

Avoid:

```python
x
tmp
obj
data1
```

---

## Constants

```text
UPPER_CASE
```

---

# Folder & Package Rules

Package names:

* lowercase
* singular where appropriate

Modules must be organized by business capability, not technical utility.

Do not create generic folders such as:

* helpers
* utils
* misc
* temp
* common

Shared code belongs in the Shared Kernel only after architectural approval.

---

# Import Rules

Imports must respect Clean Architecture.

Allowed:

Presentation → Application

Application → Domain

Infrastructure → Domain

Forbidden:

Domain → Infrastructure

Application → FastAPI

Application → SQLAlchemy

Presentation → Database

Use absolute imports within the project.

Never use wildcard imports.

---

# Type Hints

Public interfaces must always include type hints.

Example:

```python
def generate_sql(
    request: AnalysisRequest
) -> SQLPlan:
```

Avoid untyped public methods.

---

# Dependency Injection

Business logic must never instantiate infrastructure.

Correct:

```python
AnalyticsService(
    llm_provider,
    repository,
)
```

Incorrect:

```python
llm = GeminiProvider()
```

inside business logic.

---

# Error Handling

Raise typed exceptions.

Examples:

```text
SemanticError

QueryValidationError

AuthorizationError

ConnectorError
```

Never return error strings.

Never silently ignore exceptions.

Every exception should either:

* Recover
* Translate
* Bubble upward

---

# Logging Standards

Use structured logging.

Every log entry should include:

* Correlation ID
* Timestamp
* Module
* Severity
* Event Name

Never log:

* Passwords
* Secrets
* Tokens
* Raw prompts containing sensitive information
* Raw PII

---

# Documentation

Public classes require documentation.

Public APIs require documentation.

Complex business rules require documentation.

Comments should explain:

WHY

not

WHAT.

Avoid comments like:

```python
# Increment i
i += 1
```

Prefer comments explaining business intent.

---

# Function Guidelines

Prefer:

Small functions.

Recommended:

10–30 lines.

Maximum:

~50 lines unless justified.

Each function should have one responsibility.

---

# Class Guidelines

Classes should model business concepts.

Avoid "God Classes."

Prefer composition over inheritance.

---

# Business Logic Rules

Business logic belongs only inside the Domain.

Do not place business rules inside:

* Controllers
* FastAPI routes
* Database adapters
* LLM providers

---

# Testing Standards

Every feature requires appropriate tests.

Testing pyramid:

* Unit Tests
* Integration Tests
* Contract Tests
* End-to-End Tests

Business logic should be testable without infrastructure.

Mock infrastructure, not business rules.

---

# Security Standards

Always validate:

* User input
* Generated SQL
* External responses
* Connector output

Never trust:

* LLM output
* Metadata
* User prompts

Use parameterized SQL whenever applicable.

---

# Performance Guidelines

Avoid:

* Duplicate queries
* Duplicate LLM calls
* Unnecessary object creation
* Premature optimization

Optimize only after measurement.

---

# Git Standards

Use Conventional Commits.

Examples:

```text
feat(analytics): add semantic retrieval service

fix(sql): prevent unsafe update statements

docs(architecture): update dependency rules

refactor(llm): simplify provider factory
```

---

# Branch Naming

Examples:

```text
feat/sql-engine

feat/knowledge-layer

fix/query-validator

docs/prd

refactor/connectors
```

---

# Pull Request Checklist

Every pull request must:

* Compile successfully.
* Pass all tests.
* Follow architecture rules.
* Follow coding standards.
* Preserve module boundaries.
* Update documentation if required.
* Include meaningful commit history.
* Avoid unrelated changes.

---

# Code Review Checklist

Reviewers verify:

* Correctness
* Readability
* Test coverage
* Security
* Performance
* Documentation
* Dependency direction
* Public interface stability
* SOLID compliance

---

# Tooling

## Automation-first policy

**If a rule can be automated, do not rely on humans—or Codex—to remember it.**

Repository tooling makes the baseline standards executable:

* [`pyproject.toml`](../../pyproject.toml) centralizes Python version, Ruff, MyPy, pytest, coverage, and Bandit configuration.
* [`.pre-commit-config.yaml`](../../.pre-commit-config.yaml) runs file hygiene, secret detection, Ruff linting, and formatting before commits.
* CI must run the same checks without auto-fixing, plus tests, type checking, security scanning, and coverage enforcement.

Install the local checks after creating the development environment:

```text
pre-commit install
pre-commit run --all-files
```

Developers must resolve automated findings or document an approved, narrowly scoped exception. Tool configuration changes are architecture-affecting and require review.

## Configured tools

Recommended tools:

Formatting

* Ruff format (or Black)

Linting

* Ruff

Type Checking

* MyPy

Testing

* Pytest

Coverage

* pytest-cov

Security

* Bandit

These tools are configured centrally now and must be enforced through CI once the implementation phase begins.

---

# Definition of Done

Code is considered complete only when:

* Coding standards are satisfied.
* Architecture rules are respected.
* Tests pass.
* Documentation is updated.
* Public APIs are documented.
* No critical lint or type errors exist.
* Security review passes.
* Code review is approved.

---

# Living Document Policy

This document is part of the Project Constitution.

Changes should be rare and should improve long-term engineering consistency.

Updates affecting coding conventions or tooling should be reviewed and, where appropriate, referenced by an Architecture Decision Record (ADR).
