# Airflow 3 Repository Template

Simple Apache Airflow 3 template with Docker, uv, and ruff.

## Features

- **Airflow 3.1.5** - Latest Airflow
- **uv** - Fast Python package manager
- **ruff** - Fast linter and formatter
- **Docker** - Local development environment

## Project Structure

```
.
├── dags/               # DAG definitions
├── pyproject.toml      # Dependencies
├── Dockerfile          # Container definition
├── docker-compose.yaml # Docker services
└── Makefile            # Commands
```

## Quick Start

### 1. Start Airflow

```bash
make start-airflow
```

### 2. Get Your Admin Password

Airflow 3 auto-generates a secure password for the `admin` user. Find it with:

```bash
docker compose exec airflow-api-server cat /opt/airflow/simple_auth_manager_passwords.json.generated
```

Access the UI at http://localhost:8080

- **Username:** `admin`
- **Password:** (use the password from the command above)

### 3. Local Development (Optional)

```bash
uv sync
```

## Common Commands

```bash
# Airflow
make start-airflow    # Start services
make stop-airflow     # Stop services
make restart-airflow  # Restart services
make rebuild-airflow  # Rebuild and restart
make reset-airflow    # Reset everything
make logs             # View logs

# Code Quality
make lint             # Run linter
make format           # Format code
make clean            # Clean artifacts
```
