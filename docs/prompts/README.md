# Prompt Library

**Purpose:** Govern reusable AI instructions as versioned product assets.

**Owner:** AI Engineering Lead

## Layout

```text
architecture/  system-design prompts
coding/        implementation prompts
refactoring/   safe-change prompts
testing/       test-generation and evaluation prompts
security/      threat and injection-review prompts
documentation/ documentation-maintenance prompts
performance/   profiling and optimization prompts
review/        code and architecture review prompts
```

## Template standard

Every prompt records purpose, owner, inputs, expected output, guardrails, examples, version, and evaluation link. Prompts must not embed secrets or bypass policy. Changes require regression evaluation appropriate to risk.

## Future expansion

Add the named folders and approved templates when prompting becomes an implemented capability.

