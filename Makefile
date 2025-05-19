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

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml