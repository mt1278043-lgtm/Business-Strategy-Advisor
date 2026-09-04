.PHONY: help install setup run clean lint format

help:
	@echo "Business Strategy Advisor Agent - Makefile Commands"
	@echo ""
	@echo "Available commands:"
	@echo "  make install      - Install dependencies"
	@echo "  make setup        - Setup the project with virtual environment"
	@echo "  make run          - Run the Streamlit application"
	@echo "  make clean        - Remove virtual environment and cache files"
	@echo "  make lint         - Run code quality checks"
	@echo "  make format       - Format code with black"
	@echo "  make help         - Show this help message"

install:
	pip install -r requirements.txt

setup:
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "Created .env file. Please add your OpenAI API key."; \
	fi

run:
	streamlit run app.py

clean:
	rm -rf venv
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .streamlit
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

lint:
	@echo "Running pylint..."
	pylint strategy_engine.py app.py || true

format:
	@echo "Formatting code with black..."
	black strategy_engine.py app.py || true
