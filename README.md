# senior-data-platform
Production-inspired data platform demonstrating senior-level data engineering practices: ingestion, modeling, quality, history, orchestration, and analytics.

## Configuration

The pipeline is configured using environment variables:

- DB_HOST
- DB_PORT
- DB_NAME
- DB_USER
- DB_PASSWORD

Example:

```bash
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=platform_db
export DB_USER=admin
export DB_PASSWORD=admin
