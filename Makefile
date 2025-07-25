install:
	uv sync

build:
	uv build

package-install:
	uv tool install --reinstall dist/*.whl

gendiff:
	uv run gendiff

lint:
	uv run ruff check .

check: test lint

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

reinstall:
	uv tool install --force dist/*.whl

uninstall:
	uv tool uninstall hexlet-code

start:
	uv build
	uv tool install --reinstall dist/*.whl