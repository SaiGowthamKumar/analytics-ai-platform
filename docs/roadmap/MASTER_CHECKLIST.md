Phase 1 — Project Constitution ✅

Checklist:

 Vision.md
 README.md
 PRD.md
 Architecture.md
 Coding Standards
 Design Principles
 Roadmap
 ADRs
 Codex Rules
 Development Workflow

Definition of Done:

All documents reviewed.
Architecture frozen for MVP.
Phase 2 — Architecture

Checklist:

 Clean Architecture
 Folder structure
 Dependency rules
 Module boundaries
 Component diagram
 Sequence diagram
 Deployment diagram
 Data flow diagram

Ask yourself:

Can I explain the architecture in 5 minutes?
Does every module have one responsibility?
Can I swap Gemini for Groq without touching business logic?
Phase 3 — Domain Modeling

This is often skipped but is crucial.

Checklist:

 Entities
 Value Objects
 Aggregates (if needed)
 Domain Services
 Repositories
 Domain Events (later)
 Bounded Contexts
 Business Rules
Phase 4 — Sprint Planning

Before every sprint, create a small plan.

For example:

Sprint 1

Configuration
Logging
Dependency Injection
Health API

Sprint 2

LLM Gateway

Sprint 3

Knowledge Layer

Keep each sprint focused and achievable.

Phase 5 — Codex Development Workflow

For every feature, follow the same sequence:

Requirement
Domain design
Interface design
Implementation
Unit tests
Integration tests
Documentation update
Review
Merge

Never skip straight to implementation.

Phase 6 — Review Checklist

Every PR or generated feature should pass:

Architecture
 No architecture violations
 Dependency rules followed
 No circular dependencies
Code Quality
 SOLID
 Small functions
 Meaningful names
 No duplicated logic
Testing
 Unit tests
 Integration tests
 Error cases covered
Documentation
 Public APIs documented
 README updated (if needed)
 ADR updated (if architecture changed)
Performance
 No unnecessary database calls
 No blocking operations
 Proper caching where appropriate
Security
 SQL injection prevention
 Prompt injection considerations
 Secrets not hardcoded
 Authorization respected