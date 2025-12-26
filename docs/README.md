# Documentation

## Architecture

Simple Airflow 3 setup with Docker and modern Python tools.

### Directory Structure

- **dags/** - DAG definitions
- **plugins/** - Custom operators, hooks, sensors
- **tests/** - Tests
- **docs/** - Documentation

### Stack

- **Airflow 3.1.5** - Workflow orchestration
- **PostgreSQL** - Metadata database
- **Docker** - Containerization
- **uv** - Package management
- **ruff** - Linting and formatting
- **pytest** - Testing

## Writing DAGs

1. Create a Python file in `dags/`
2. Use the TaskFlow API (`@task` decorator)
3. Add tests in `tests/`

Example:

```python
from datetime import datetime
from airflow.decorators import dag, task

@dag(
    dag_id="my_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
)
def my_dag():
    @task
    def my_task():
        return {"status": "success"}

    my_task()

my_dag()
```

## Testing

```bash
make test  # Run all tests
```

Example test:

```python
def test_dag_loads(dagbag):
    dag = dagbag.get_dag("my_dag")
    assert dag is not None
```

## Airflow 3 Key Changes

- TaskFlow API is recommended (`@task` decorator)
- `BashOperator` moved to `apache-airflow-providers-standard`
- `execution_date` → `logical_date`
- `catchup` defaults to `False`

See: [Airflow 3 Migration Guide](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html)
