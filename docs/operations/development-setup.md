# Development Setup

**Purpose:** Define the supported Docker-based local development workflow.

**Owner:** Platform Engineering

## Prerequisites

Install Docker Desktop (or a compatible Docker Engine with the Compose plugin) and Git. Allocate sufficient local container resources for four development services.

## Initial setup

1. Clone the repository.
2. Review `backend/.env.example` and `frontend/.env.example`.
3. Copy either template to its corresponding `.env` file only when local overrides are needed. Do not commit `.env` files.

## Start and stop

Start the complete environment from the repository root:

```text
docker compose up --build
```

Stop containers while retaining data:

```text
docker compose down
```

Remove local development volumes as well:

```text
docker compose down --volumes
```

## Local endpoints

| Service | Local address | Notes |
|---|---|---|
| Backend | http://localhost:8000 | Process health: `/health`, `/ready`, `/live` |
| Frontend | http://localhost:5173 | Vite development server |
| PostgreSQL | localhost:5432 | Development container only; no schema or migrations are supplied |
| Redis | localhost:6379 | Development container only |

Containers communicate over the `analytics_development` bridge network using service names, not host-local addresses.

## Logs and rebuilds

Follow all logs with `docker compose logs --follow`, or a single service with `docker compose logs --follow backend`. Rebuild a changed image with `docker compose build backend` or `docker compose build frontend`, then restart the service.

## Environment configuration

The backend template documents safe service configuration. The frontend template supports only `VITE_API_BASE_URL`. The database password defaults to a clearly development-only value when no `POSTGRES_PASSWORD` environment variable is supplied; override it locally if needed and never commit the value.

## Troubleshooting

- If a port is occupied, stop the conflicting local process or adjust the host-side port mapping in `compose.yaml`.
- If a dependency volume is stale, run `docker compose down --volumes` and restart.
- If a service fails its health check, inspect its logs before rebuilding.
- If image builds use stale layers, run `docker compose build --no-cache`.

## Future expansion

Add developer certificates, debugging profiles, and service-specific local tooling only through an approved platform change.
