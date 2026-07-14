# Semantic Knowledge Layer

**Purpose:** Define governed business meaning used to ground analytics.

**Owner:** Data Stewardship Lead

## Contents

The layer stores a business glossary, schema metadata, relationships, KPI definitions, business rules, approved examples, and prompt-ready context. Each asset has an owner, source lineage, version, lifecycle state, and tenant scope.

## Retrieval and validation

Retrieval selects only policy-authorized, approved assets relevant to the question and data scope. Validation checks schema compatibility, stale references, contradictory definitions, completeness, and policy constraints before assets are published or used.

## Versioning and approval

Assets progress through draft, review, approved, deprecated, and retired states. Approved versions are immutable; production requests record the semantic version used. Stewards approve definitions, while technical validation is automated where possible.

## Future expansion

Define a semantic asset schema, stewardship roles, and import/export contracts.

