.DEFAULT_GOAL := help

.PHONY: start
start: ## Start the application "stack" using Docker
	@docker compose up --build

.PHONY: unit_tests
unit_tests: ## Run all the unit tests
	@poetry run pytest -v tests/unit

.PHONY: integration_tests
integration_tests: ## Run all the integration tests
	@poetry run pytest -v tests/integration

.PHONY: coverage
coverage: ## Run the integration tests with code coverage report generated
	@poetry run pytest -v --junitxml=report.xml --cov=app/ tests/integration
	@poetry run coverage xml

.PHONY: install-hooks
install-hooks: ## Install pre commit hooks
	@poetry run pre-commit install

.PHONY: lint
lint: ## Run the lint steps (pre-commit hook)
	@poetry run pre-commit run --all-files

.PHONY: pull-template-updates
pull-template-updates: ## Pull updates from upstream template
	@poetry run copier update

.PHONY: clean
clean: ### Clean all temporary files
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' | xargs rm -rf
	@find . -type d -name '*.ropeproject' | xargs rm -rf
	@rm -rf build/
	@rm -rf dist/
	@rm -f src/*.egg
	@rm -f src/*.eggs
	@rm -rf src/*.egg-info/
	@rm -f MANIFEST
	@rm -rf docs/build/
	@rm -rf htmlcov/
	@rm -f .coverage
	@rm -f .coverage.*
	@rm -rf .cache/
	@rm -f coverage.xml
	@rm -f *.cover
	@rm -rf .pytest_cache/

