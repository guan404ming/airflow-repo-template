"""Example DAG demonstrating Airflow 3 best practices."""

from datetime import datetime, timedelta

from airflow.decorators import dag, task
from airflow.providers.standard.operators.bash import BashOperator


@dag(
    dag_id="example_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={
        "owner": "airflow",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    tags=["example"],
)
def example_dag():
    """Example DAG using TaskFlow API and modern Airflow 3 patterns."""

    @task
    def extract():
        """Extract data from source."""
        return {"data": [1, 2, 3, 4, 5]}

    @task
    def transform(data: dict):
        """Transform the data."""
        transformed = [x * 2 for x in data["data"]]
        return {"transformed_data": transformed}

    @task
    def load(data: dict):
        """Load the data to destination."""
        print(f"Loading data: {data['transformed_data']}")
        return {"status": "success", "count": len(data["transformed_data"])}

    # Traditional operator example
    bash_task = BashOperator(
        task_id="bash_example",
        bash_command='echo "Hello from Airflow 3!"',
    )

    # Define task dependencies
    extracted_data = extract()
    transformed_data = transform(extracted_data)
    load_result = load(transformed_data)

    # Set dependencies with traditional operator
    bash_task >> extracted_data


# Instantiate the DAG
example_dag()
