# Folder Structure and Code Placement Map

**Purpose:** Map every repository directory to its architectural layer, owning module, and permitted contents. This is the bridge between the approved architecture and future implementation.

**Owner:** Principal Architect

## Placement rules

1. Place code by business ownership first, then by Clean Architecture layer.
2. A module may expose only its public application contracts; other modules must not import its private files.
3. The domain layer contains no framework, persistence, provider SDK, HTTP, or environment dependencies.
4. Cross-cutting runtime wiring belongs only in a composition root.
5. Create a directory only when an approved implementation need exists; update this document and its module README in the same change.

## Folder philosophy

The structure optimizes for clear ownership, business cohesion, and replaceable technology. A folder answers three questions unambiguously: **who owns this behavior, which architectural layer governs it, and which dependencies are permitted?** Organize by module before technical type so a change to a business capability remains discoverable in one bounded area. Use the smallest structure that preserves these boundaries; directory depth is not a goal by itself.

## Dependency diagram

Dependencies always point toward business policy. The outer layers may depend inward; inner layers must never depend outward.

```text
Delivery and infrastructure adapters
  FastAPI | PostgreSQL | LLM providers | BI | queues | filesystem
                              │
                              ▼
Application layer
  use cases | orchestration | commands/queries | transactions
                              │
                              ▼
Domain layer
  aggregates | value objects | policies | events | ports
                              │
                              ▼
Business rules with no framework or provider dependencies
```

```text
Module A ──public contract/event──► Module B
Module A ──private import─────────► Module B   FORBIDDEN
Domain ───► adapter/framework/provider          FORBIDDEN
Adapter ──► domain/application                  ALLOWED
Composition root ──► all modules/adapters       ALLOWED for wiring only
```

## Naming conventions

| Item | Convention | Examples |
|---|---|---|
| Directories and Python modules | lowercase `snake_case` | `semantic_assets/`, `query_safety.py` |
| Business modules | singular lowercase names | `analytics/`, `knowledge/`, `security/` |
| Python types | `PascalCase` | `AnalysisRequest`, `SemanticAssetRepository` |
| Functions, variables, and files | descriptive `snake_case` | `retrieve_context`, `safe_sql.py` |
| Ports | capability-oriented `PascalCase` suffix | `LLMProvider`, `DatabaseConnector` |
| Adapter implementations | provider or transport prefix/suffix | `PostgresSemanticAssetRepository`, `FastAPIRouter` |
| Tests | behavior-oriented `test_*.py` | `test_rejects_unapproved_asset.py` |
| Documentation | lowercase kebab-case except established names | `folder-structure.md`, `ADR-001-clean-architecture.md` |
| AI assets | stable lowercase kebab-case with a version field in content | `sql-generation.md`, not `sql-generation-v2-final.md` |

Avoid generic names such as `utils`, `helpers`, `common`, `misc`, `manager`, and `service` unless the noun identifies a specific bounded-context responsibility.

## Forbidden folders and placement anti-patterns

The following directories must not be created without an approved ADR that supersedes this rule:

| Forbidden folder or pattern | Reason | Approved alternative |
|---|---|---|
| `utils/`, `helpers/`, `common/`, `misc/` | hides ownership and becomes a dependency sink | retain code in its module; use `shared/` only under its strict rule |
| Root-level `models/` | mixes domain, transport, and persistence models | place models in the owning module and layer |
| Root-level `services/` | obscures module ownership and responsibility | use the owning module's `application/` or `domain/` |
| Root-level `repositories/` | leaks persistence as a global concern | define port in domain; implement it in module `adapters/` |
| `backend/core/` as a catch-all | creates an unofficial second architecture | use explicit modules, `shared/`, or composition |
| `backend/lib/` as a business-code bucket | bypasses module boundaries | use the appropriate owning module |
| `vendor/` or copied provider SDK source | prevents secure dependency management | declare reviewed package dependencies and wrap them in adapters |
| `generated/` mixed with handwritten code | makes ownership and review unclear | use an isolated, documented generated-code location only when needed |
| `tmp/`, `scratch/`, `archive/` in version control | preserves unowned or stale production artifacts | use local ignored files or documented migration history |

## AI asset directories

AI assets are governed product inputs, not incidental strings. They are versioned, reviewed, traceable, and separated from runtime code.

```text
knowledge/
  glossary/                    approved business terms and definitions
  schema/                      source metadata and relationship descriptions
  kpis/                        versioned metric definitions and business rules
  examples/                    approved question-to-analysis examples
  validation/                  semantic validation fixtures

prompts/
  architecture/ coding/ refactoring/ testing/ security/
  documentation/ performance/ review/
  analytics/                   production analysis prompt templates
  evaluation/                  prompt test cases and expected structural outputs

agents/
  workflows/                   bounded agent workflow definitions
  policies/                    tool-use, escalation, and approval policies
  evaluation/                  agent scenario suites and scorecards
```

`knowledge/` is owned by Data Stewardship, `prompts/` and `agents/` by AI Engineering, and all production assets require an owner, purpose, version, approval state, provenance, and evaluation link. Runtime code may load these assets only through the relevant provider port; it must not embed, modify, or silently substitute them.

## Evolution policy

This map is intentionally stable but not frozen. Evolve it through evidence, not convenience:

1. Propose the change in the relevant module README and this document, identifying ownership, dependency direction, migration, and test impact.
2. Create an ADR when the change alters architecture, module boundaries, shared-kernel scope, public contracts, or deployment topology.
3. Obtain review from the affected module owner and Principal Architect before creating the new structure.
4. Migrate incrementally; do not duplicate live business logic across old and new locations.
5. Update imports, tests, documentation, and observability references in the same change set.
6. Remove the obsolete location only after migration verification and record any deprecation path.

No exception is permanent: temporary compatibility shims must have a named owner, expiry condition, and removal task.

## Repository directory map

| Directory | Architectural layer | Owning module/team | Permitted contents |
|---|---|---|---|
| `.github/` | Delivery automation | Platform Engineering | CI/CD workflows, issue templates, automation configuration |
| `docs/` | Governance / SSOT | Architecture and Product | Approved decisions, rules, specifications, and operating documentation |
| `backend/` | Application runtime | Backend Engineering | Python modular monolith, delivery adapters, and composition root |
| `frontend/` | Presentation adapter | Frontend Engineering | React application, accessible UI components, and API client adapter |
| `knowledge/` | Domain content | Data Stewardship | Versioned semantic assets, glossary content, approved examples, and validation fixtures |
| `prompts/` | AI governance content | AI Engineering | Versioned, reviewed prompt templates and evaluation metadata |
| `connectors/` | Integration catalog | Connector Engineering | Connector manifests, capability declarations, and provider-specific support assets |
| `agents/` | Application workflow content | AI Engineering | Approved bounded agent workflow definitions; no secret-bearing configuration |
| `tests/` | Quality assurance | QA / all module owners | Cross-module integration, contract, end-to-end, performance, and security tests |
| `infrastructure/` | Infrastructure adapter | Platform Engineering | Infrastructure-as-code, environment topology, observability configuration |
| `deployment/` | Delivery / runtime packaging | Platform Engineering | Docker, Compose, deployment manifests, and release configuration |

## Backend module placement

The future `backend/` layout is intentionally module-first. Every module follows the same layer vocabulary; it may omit a layer it does not need.

```text
backend/
  composition/                 runtime dependency wiring and application bootstrap
  shared/                      strictly cross-cutting primitives; no business rules
  modules/
    <module>/
      domain/                  entities, value objects, policies, domain events, ports
      application/             use cases, commands/queries, DTOs, transaction boundaries
      adapters/                persistence, provider, HTTP, queue, and other implementations
      api.py                   module's public application-facing contract only
      README.md                module purpose, owner, contracts, and dependency notes
```

| Backend location | Layer | Owner | Put code here when… |
|---|---|---|---|
| `backend/composition/` | Composition | Backend / Platform Engineering | wiring ports to adapters, loading typed settings, and starting the application |
| `backend/shared/` | Shared kernel (exception-only) | Principal Architect | a small primitive is truly stable, non-domain-specific, and used by multiple modules |
| `backend/modules/<module>/domain/` | Domain | The named module owner | defining business invariants, value objects, aggregate behavior, domain ports, or domain events |
| `backend/modules/<module>/application/` | Application | The named module owner | orchestrating use cases through domain rules and port interfaces |
| `backend/modules/<module>/adapters/` | Adapter | The named module owner | integrating FastAPI, PostgreSQL, LLMs, BI providers, queues, files, or external systems |
| `backend/modules/<module>/api.py` | Public module boundary | The named module owner | exposing stable commands, queries, DTOs, or events to another module |

`shared/` is not a convenience bucket. If ownership or business meaning is unclear, keep the code in its owning module until an ADR approves a shared-kernel extraction.

## Module ownership map

| Module directory | Business ownership | May depend on through public contracts | Must not contain |
|---|---|---|---|
| `modules/analytics/` | Question interpretation, analysis planning, result orchestration | Knowledge, LLM, Connectors, Security, Dashboard, Insights, Recommendations | Provider SDKs in domain/application |
| `modules/knowledge/` | Semantic assets, retrieval, approval, and versioning | Configuration, Security, repositories through ports | Raw database code outside adapters |
| `modules/dashboard/` | Provider-neutral visualization specifications | Analytics public contracts, VisualizationProvider | Business KPI definitions |
| `modules/insights/` | Evidence-based interpretation of results | Analytics result contracts, LLM port | Direct data-source access |
| `modules/recommendations/` | Evidence-backed actions and confidence | Insights contracts, Security policy | Unapproved autonomous actions |
| `modules/connectors/` | Source capability, authorization-aware execution | Security, Configuration, database ports | Semantic business rules |
| `modules/llm/` | Provider-neutral model capabilities | Configuration, Monitoring | Analytics business decisions |
| `modules/memory/` | Policy-compliant contextual recall | Security, Configuration, storage ports | Authentication policy |
| `modules/configuration/` | Typed settings and feature policy | None outside its own ports | Secrets in source or logs |
| `modules/security/` | Authentication, authorization, audit policy | Identity and audit ports | Domain-specific analytics logic |
| `modules/monitoring/` | Observability contracts and adapters | Configuration | Business decisions |

## Frontend placement

```text
frontend/
  src/
    features/                  module-aligned screens and UI state
    shared/                    design system and generic UI utilities only
    adapters/                  HTTP/API client implementations
    app/                       routing, composition, and application bootstrap
```

Frontend features align with the corresponding backend module but do not import backend implementation. The frontend treats the API as its port and owns presentation-specific state only.

## Test placement

| Location | Owner | Scope |
|---|---|---|
| `backend/modules/<module>/.../tests/` | Module owner | unit tests beside the module's behavior |
| `tests/contract/` | API / connector owners | public module and provider contract conformance |
| `tests/integration/` | QA and module owners | real adapter integration with controlled dependencies |
| `tests/e2e/` | QA | user-visible question-to-recommendation workflow |
| `tests/performance/` | Platform Engineering | load, latency, and resource budgets |
| `tests/security/` | Security Lead | authorization, injection, and negative-path verification |
| `tests/ai-evals/` | AI Engineering | grounded-output and prompt-regression evaluation sets |

## Examples: where new code belongs

| Change | Correct location |
|---|---|
| Rule that a production semantic asset must be approved | `backend/modules/knowledge/domain/` |
| Use case that retrieves context and plans an analysis | `backend/modules/analytics/application/` |
| PostgreSQL implementation of a semantic asset repository | `backend/modules/knowledge/adapters/` |
| FastAPI route for submitting a question | `backend/modules/analytics/adapters/` |
| OpenAI-compatible LLM implementation | `backend/modules/llm/adapters/` |
| Docker Compose service definition | `deployment/` |
| KPI definition for gross margin | `knowledge/` |
| Prompt that turns an approved plan into safe SQL | `prompts/` |

## Change checklist

Before adding a directory or file, confirm its owning module, layer, public contract, allowed dependencies, test location, documentation impact, and whether an ADR is required. If a change does not fit this map, do not create an ad hoc folder—propose an update to this document first.

## Future expansion

Add language-specific package names, generated-code policy, module READMEs, and ownership aliases once the implementation stack and teams are formally approved.
