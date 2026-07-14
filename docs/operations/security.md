# Security

**Purpose:** Set security requirements for platform design and delivery.

**Owner:** Security Lead

## Identity and access

Use centralized authentication and least-privilege authorization with tenant-aware, attribute-capable policy enforcement. Authorize every question, semantic asset, connector, field, and result scope.

## Data and application protection

Store secrets in a managed vault; encrypt data in transit and at rest; minimize and classify PII; apply retention controls; and keep tamper-evident audit logs. Parameterize and validate SQL, enforce read-only connector permissions, query budgets, and allowlists.

## AI-specific controls

Treat prompts, retrieved content, tool output, and model responses as untrusted. Defend against prompt injection with instruction/data separation, constrained tools, policy validation, output schemas, and human approval for high-impact actions. Rate-limit by identity, tenant, and risk.

## Compliance

Map controls to applicable contractual and regulatory obligations before production; preserve evidence for audits.

## Future expansion

Add threat model, incident runbooks, data classification matrix, and compliance mappings.

