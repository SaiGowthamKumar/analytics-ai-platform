# Module Design

**Purpose:** Set independent module responsibilities and public contracts.

**Owner:** Principal Architect

| Module | Responsibilities | Depends on | Public interface / expansion |
|---|---|---|---|
| Analytics | interpret, plan, orchestrate analysis | Knowledge, LLM ports, Connectors | `ask`; support workflows later |
| Knowledge | semantic assets and retrieval | Configuration, repositories | `retrieve_context`, `publish_asset` |
| Dashboard | visualization specifications | Analytics contracts | `create_visualization`; add BI publishing |
| Insights | evidence-based interpretation | result contracts, LLM port | `derive_insights` |
| Recommendations | actionable suggestions | Insights, policy | `recommend` |
| Connectors | data-source capabilities and execution | Security, configuration | `execute_read_only` |
| LLM | provider-neutral generation | Configuration | `generate`, `embed`, `evaluate` |
| Memory | approved contextual recall | security, repositories | `retrieve`, `store` |
| Configuration | typed settings and feature policy | none | `get_setting` |
| Security | authn/authz, policy, audit | identity adapter | `authorize`, `audit` |
| Monitoring | metrics, logs, traces | ports | `record_*` |
| Testing | test fixtures and contract suites | all public contracts | reusable test support |

Internal classes remain private to a module. Cross-module access occurs only through the named interfaces or events.

## Future expansion

Define per-module API schemas and ownership teams as modules become implemented.

