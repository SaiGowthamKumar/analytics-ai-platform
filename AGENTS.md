# AGENTS.md

# AI Analytics Platform – AI Engineering Guide

This file defines the engineering standards that every AI coding assistant must follow when contributing to this repository.

These instructions are mandatory.

---

# 1. Project Overview

Project Name

Enterprise AI Analytics Platform

Mission

Build an enterprise-grade AI-powered analytics platform capable of transforming natural language into governed SQL, executing queries securely, visualizing results, and generating AI-driven insights.

This project prioritizes:

- Clean Architecture
- Domain-Driven Design
- Production Readiness
- Documentation-First Design
- Maintainability
- Testability
- Explicit Dependencies

---

# 2. AI Role

When working inside this repository, act as:

Senior Software Engineer

Responsibilities:

- Implement requested features
- Follow existing architecture
- Never redesign the system
- Prefer simplicity
- Produce production-quality code
- Minimize technical debt

Never assume Product Owner responsibilities.

Never invent requirements.

---

# 3. Development Principles

Always follow:

- SOLID Principles
- DRY
- KISS
- YAGNI
- Explicit dependencies
- Dependency Injection
- Separation of Concerns
- Single Responsibility

Avoid clever code.

Readable code is preferred.

---

# 4. Architecture

Follow the documented architecture exactly.

Never modify architecture unless explicitly requested.

Layers must remain isolated.

Presentation

↓

Application

↓

Domain

↓

Infrastructure

Dependencies always point inward.

Infrastructure must never leak into Domain.

---

# 5. Backend Technology

Python

FastAPI

SQLAlchemy

Alembic

PostgreSQL

Redis

Pydantic

Dependency Injection

Async-first implementation.

---

# 6. Frontend Technology

React

TypeScript

Vite

React Router

Strict TypeScript

Component-based architecture

Avoid unnecessary global state.

---

# 7. Coding Standards

Always:

Use type hints

Write descriptive names

Avoid abbreviations

Prefer composition

Prefer explicit code

Keep functions small

Keep classes focused

Never duplicate business logic.

---

# 8. Project Structure

Respect the existing folder structure.

Never create random folders.

Never move files without reason.

Follow architecture documentation.

---

# 9. Dependency Rules

Allowed:

Presentation → Application

Application → Domain

Infrastructure → Domain

Forbidden:

Domain → Infrastructure

Application → Presentation

Presentation → Infrastructure

---

# 10. Business Logic

Business logic belongs only inside the Domain/Application layers.

Never implement business rules inside:

Controllers

API Routes

React Components

Infrastructure

---

# 11. Error Handling

Always:

Raise meaningful exceptions

Use centralized exception handling

Never swallow exceptions

Provide structured API errors

---

# 12. Logging

Use structured logging.

Never use print().

Log:

Errors

Warnings

Important lifecycle events

Do not log secrets.

---

# 13. Configuration

All configuration must come from environment variables.

Never hardcode:

URLs

Keys

Passwords

Secrets

Tokens

---

# 14. Security

Never:

Hardcode secrets

Disable validation

Trust user input

Construct unsafe SQL

Bypass authorization

Always validate external input.

---

# 15. Database

Use:

SQLAlchemy 2.x

Alembic migrations

Async sessions

Parameterized queries

Never:

Write raw SQL unless required

Skip migrations

Mix ORM and business logic

---

# 16. API Design

RESTful

Versioned

Consistent response models

Consistent error models

OpenAPI compatible

---

# 17. Frontend

Components should be:

Reusable

Small

Typed

Composable

No business logic inside UI.

---

# 18. Testing

Every new feature should include:

Unit tests where applicable

Integration tests where appropriate

Existing tests must never break.

---

# 19. Documentation

Update documentation when:

Architecture changes

Developer workflow changes

Configuration changes

Do not create unnecessary documentation.

Implementation takes priority.

---

# 20. Git Workflow

Each task must be implemented in its own feature branch.

Workflow:

main

↓

feature/pr-XXX-name

↓

Pull Request

↓

Review

↓

Squash Merge

↓

Delete Branch

Never commit directly to main.

---

# 21. Pull Request Scope

Every PR must:

Solve one problem

Remain focused

Avoid unrelated refactoring

Avoid scope creep

Smaller PRs are preferred.

---

# 22. Definition of Done

Before considering implementation complete:

✓ Builds successfully

✓ Tests pass

✓ Lint passes

✓ Type checking passes

✓ Documentation updated if needed

✓ No TODO comments

✓ No FIXME comments

✓ Scope respected

✓ Production ready

---

# 23. Forbidden Changes

Do not:

Rewrite architecture

Rename large folders

Change project structure

Introduce new frameworks

Replace libraries

Modify coding standards

Unless explicitly requested.

---

# 24. When Unsure

If implementation details are unclear:

Choose the simplest solution consistent with the architecture.

Do not invent features.

Do not expand project scope.

---

# 25. Output Expectations

After completing work, provide:

1. Summary of changes

2. Files modified

3. Design decisions

4. Test results

5. Remaining work

6. Risks (if any)

Never claim tests passed unless they were actually executed.

---

# 26. Quality Goal

Every implementation should be of production quality.

Code should be suitable for:

Enterprise environments

Code review

Long-term maintenance

Future scalability

Optimize for readability over cleverness.