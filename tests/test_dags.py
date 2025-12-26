"""Test DAG integrity."""

import pytest
from airflow.models import DagBag


@pytest.fixture
def dagbag():
    """Create a DagBag fixture."""
    return DagBag(dag_folder="dags/", include_examples=False)


def test_no_import_errors(dagbag):
    """Test that all DAGs load without import errors."""
    assert not dagbag.import_errors, f"DAG import errors: {dagbag.import_errors}"


def test_dag_count(dagbag):
    """Test that we have the expected number of DAGs."""
    assert len(dagbag.dags) >= 1, "Expected at least 1 DAG"


def test_example_dag_exists(dagbag):
    """Test that the example DAG exists."""
    assert "example_dag" in dagbag.dags, "example_dag not found in DAGs"


def test_example_dag_has_tags(dagbag):
    """Test that the example DAG has appropriate tags."""
    dag = dagbag.get_dag("example_dag")
    assert dag is not None
    assert "example" in dag.tags


def test_example_dag_task_count(dagbag):
    """Test that the example DAG has the expected number of tasks."""
    dag = dagbag.get_dag("example_dag")
    assert dag is not None
    assert len(dag.tasks) == 4, f"Expected 4 tasks, found {len(dag.tasks)}"


def test_example_dag_has_owner(dagbag):
    """Test that the example DAG has an owner."""
    dag = dagbag.get_dag("example_dag")
    assert dag is not None
    assert dag.default_args.get("owner") == "airflow"
