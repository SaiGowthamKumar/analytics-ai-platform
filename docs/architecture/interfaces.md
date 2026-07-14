# Interface Design

**Purpose:** Define stable ports; implementations are intentionally excluded.

**Owner:** Principal Architect

| Port | Operations | Contract |
|---|---|---|
| `LLMProvider` | generate, embed, evaluate | accepts typed request/context; returns typed response, usage, provenance |
| `DatabaseConnector` | inspect_capabilities, execute_read_only | authorized, parameterized, bounded execution only |
| `KnowledgeProvider` | retrieve_context, get_version | returns approved, traceable semantic context |
| `VisualizationProvider` | build_visualization | returns an accessible provider-neutral visualization spec |
| `AnalyticsEngine` | analyze | produces plan, results, and provenance |
| `MemoryProvider` | retrieve, store | respects tenant, consent, retention, and policy |
| `PromptProvider` | get_template, render | returns versioned, approved prompt artifacts |
| `ConfigurationProvider` | get, get_typed | validates configuration without exposing secrets |

Ports use domain/application types, never transport, ORM, or vendor SDK types. Breaking contract changes require versioning, tests, and an ADR when architecturally material.

## Future expansion

Add language-specific signatures after the implementation language and package layout are approved.

