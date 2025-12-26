FROM apache/airflow:3.1.5-python3.12

USER root

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy project files
COPY pyproject.toml /opt/airflow/

# Install dependencies using uv
RUN cd /opt/airflow && uv pip install --system -r pyproject.toml

USER airflow

# Copy DAGs
COPY --chown=airflow:root dags /opt/airflow/dags
