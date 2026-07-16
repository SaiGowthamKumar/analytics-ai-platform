# Security Model

**Purpose:** Define technical controls that enforce the domain's governance, access, privacy, and audit invariants.

**Owner:** Security Lead

## Security principles

Deny by default, verify every action, minimize data exposure, separate duties, preserve provenance, and treat all external and generated content as untrusted. Security policy constrains every module; no event, cache, or internal call bypasses authorization.

## Authentication and session security

A centralized identity boundary establishes an ActorContext containing subject, tenant, roles, attributes, authentication strength, consent, and correlation information. The API validates identity before dispatching any command or query. Sessions and tokens are short-lived, audience-bound, revocable, and never embedded in business records, logs, prompts, or events.

## Authorization and RBAC

RBAC assigns baseline permissions to roles such as business user, analyst, data steward, reviewer, administrator, and auditor. Attribute and policy evaluation further constrains tenant, data classification, source capability, row and field scope, purpose, time, consent, and approval state. RBAC grants no unrestricted data access: every governed action obtains a PolicyDecision with obligations and expiry.

| Action class | Required controls |
|---|---|
| Ask or view analysis | Tenant membership, purpose, permitted data and result scope |
| Retrieve semantic assets | Approval state, applicability, stewardship or user entitlement |
| Execute query | Validated read-only specification, authorized connector scope, cost and time bounds |
| Manage semantic assets | Steward role, review separation, version and approval controls |
| Review recommendation | Reviewer entitlement, evidence visibility, audit record |
| View audit trail | Auditor or delegated entitlement, least-privilege filtering |
| Change configuration or connectors | Elevated role, approval workflow, secret separation, audit |

## Audit and non-repudiation

Security records immutable audit entries for access evaluations, material commands, policy denials, query validation and execution, semantic approvals, recommendation reviews, and retention actions. Audit entries contain actor reference, action, outcome, policy basis, timestamp, correlation, and provenance—not raw secrets or unnecessary personal data. Audit access is itself authorized and monitored.

## Secrets and cryptographic protection

Secrets are stored only in an approved secret-management boundary and delivered at runtime to the minimum adapter scope. They are never stored in source, prompt assets, events, client DTOs, or logs. Sensitive data is encrypted in transit and at rest; key ownership, rotation, separation of duties, and recovery are controlled by policy. Data exports use explicit authorization, classification checks, and traceable provenance.

## Prompt injection and generated-content protection

Questions, retrieved text, metadata, connector output, and generated content are untrusted. The Context Builder separates instructions from data, admits only approved semantic assets, applies size and classification limits, and labels untrusted content. The Prompt Orchestrator uses purpose-specific templates and constrained outputs. Generated output cannot invoke tools, alter policy, approve assets, or execute queries without independent validation. Injection indicators are recorded as security events and may trigger refusal or escalation.

## Query and data-access protection

The SQL Engine validates structural read-only intent, allowed source capability, authorized scope, parameterization requirements, resource limits, and semantic alignment before a Connector can execute. Connectors re-check the effective PolicyDecision and enforce least-privilege source credentials, timeouts, row/size bounds, and result classification. Failed validation or execution cannot be transformed into a successful analytical answer.

## Data governance, PII, and compliance

Data classification travels with semantic assets, data scopes, results, and evidence references. PII is minimized in prompts, responses, memory, and audit records; masking, redaction, aggregation, and purpose limits apply before exposure. Retention, legal hold, deletion, consent, residency, access review, and incident-response requirements are configurable policy controls with auditable decisions. Compliance mapping is maintained separately for applicable jurisdictions and commitments.

## Future expansion

Add a formal threat model, control-to-compliance mapping, incident playbooks, key-management standard, and periodic access-review procedure before production launch.

