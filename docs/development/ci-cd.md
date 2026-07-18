# CI/CD Quality Gates

**Purpose:** Define the continuous-integration quality gates required for pull requests and changes to `main`.

**Owner:** Platform Engineering

## Workflow overview

The `Continuous Integration` workflow runs separate backend and frontend jobs for pull requests and pushes to `main`. It performs no deployment, release, publishing, or environment promotion.

| Job | Quality gates |
|---|---|
| Backend quality | Ruff lint and format, Black, isort, MyPy, pytest, XML coverage |
| Frontend quality | ESLint, TypeScript, Prettier, Vitest, XML coverage, production build |

Python packages and Node dependencies are cached using lock/configuration files to reduce repeat workflow time. Coverage artifacts are retained for future reporting integrations.

## Local validation

Run backend checks from the repository root:

```text
ruff check backend tests
ruff format --check backend tests
black --check backend tests
isort --check-only backend tests
mypy backend
pytest --cov=backend --cov-report=xml:coverage.xml
```

Run frontend checks from `frontend/`:

```text
npm ci
npm run lint
npm run format:check
npm run test:coverage
npm run build
```

## Required developer workflow

Before opening a pull request, run the relevant local checks, resolve all quality findings, and keep the change scoped to one concern. Pull requests are merge-ready only when both CI jobs pass.

## Troubleshooting

- Refresh dependencies with `python -m pip install --group dev .` or `npm ci`.
- If formatting fails, apply the configured formatter locally and rerun its check.
- Inspect uploaded coverage artifacts from the workflow run when coverage generation fails.
- Use the job logs to identify a failing gate; CI intentionally does not hide failed commands.

## Quality-gate rationale

Static checks protect code consistency and dependency direction; tests protect behavior; coverage files provide machine-readable evidence; build verification ensures the frontend can be packaged. Each gate is required because it can be automated reliably.

## Future expansion

Add deployment automation only through a separate approved platform decision and workflow.
