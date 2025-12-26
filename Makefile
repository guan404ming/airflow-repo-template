.PHONY: help install lint format clean start-airflow stop-airflow restart-airflow rebuild-airflow reset-airflow logs

help:
	@echo "Available commands:"
	@echo "  make install          - Install production dependencies with uv"
	@echo "  make lint             - Run ruff linter"
	@echo "  make format           - Format code with ruff"
	@echo "  make start-airflow    - Build and start Airflow services"
	@echo "  make stop-airflow     - Stop Airflow services"
	@echo "  make restart-airflow  - Restart Airflow services"
	@echo "  make rebuild-airflow  - Rebuild and restart Airflow"
	@echo "  make reset-airflow    - Reset Airflow (destroy volumes)"
	@echo "  make logs             - View Airflow logs"
	@echo "  make clean            - Clean up build artifacts"

install:
	uv pip install -e .

lint:
	ruff check dags/ plugins/ tests/

format:
	ruff format dags/ plugins/ tests/
	ruff check --fix dags/ plugins/ tests/

start-airflow:
	docker compose up -d

stop-airflow:
	docker compose down

restart-airflow:
	docker compose restart

rebuild-airflow:
	docker compose down
	docker compose build
	docker compose up -d

reset-airflow:
	docker compose down -v
	docker compose build
	docker compose up -d

logs:
	docker compose logs -f

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name ".coverage" -delete
