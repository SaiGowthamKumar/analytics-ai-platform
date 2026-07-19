# Database Development

**Purpose:** Define the technical database foundation, migration workflow, and local development procedures.

**Owner:** Platform Engineering

## Architecture

Database connectivity is an outer infrastructure adapter. The composition root creates one asynchronous SQLAlchemy engine and session factory from the required `APP_DATABASE_URL` setting. Domain and application layers do not import SQLAlchemy, sessions, or Alembic.

The reusable `get_db_session` dependency yields an asynchronous session to future delivery adapters only after an approved module owns a valid use case. This foundation creates no ORM models, repositories, domain entities, or tables.

## Local development

The Docker Compose PostgreSQL service is reachable from containers as `postgres:5432`. Copy `backend/.env.example` to `backend/.env` only when local overrides are needed. Set `APP_DATABASE_URL` to an asynchronous PostgreSQL URL; never commit credentials.

## Migration workflow

Alembic is configured in `alembic/` and reads the database URL from application settings. The initial revision is intentionally empty and establishes only the migration baseline.

Create a reviewed migration after an approved infrastructure or module-owned persistence change:

```text
alembic revision -m "describe the approved change"
```

Apply migrations:

```text
alembic upgrade head
```

Rollback one revision:

```text
alembic downgrade -1
```

Migration files must not introduce business tables or mappings before their owning module, aggregate, and persistence design are approved.

## Readiness behavior

`GET /ready` performs a minimal `SELECT 1` connectivity probe. It does not validate schemas, execute migrations, or inspect application tables. Process health and liveness endpoints do not contact the database.

## Future expansion

Add module-owned ORM mappings, repository adapters, migration review guidance, and backup/recovery procedures only through approved architecture and domain changes.
