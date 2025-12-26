FROM apache/airflow:3.1.5-python3.12

USER root

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

USER airflow

# Copy project files
COPY pyproject.toml /opt/airflow/

# Install dependencies using uv
RUN uv pip install --system -e /opt/airflow/

# Copy DAGs and plugins
COPY --chown=airflow:root dags /opt/airflow/dags
COPY --chown=airflow:root plugins /opt/airflow/plugins
