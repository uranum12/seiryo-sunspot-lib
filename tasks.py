from invoke.context import Context
from invoke.tasks import task


@task
def fmt(c: Context) -> None:
    c.run("ruff check --fix-only --show-fixes src tests", pty=True)
    c.run("ruff format tasks.py src tests", pty=True)


@task
def lint(c: Context) -> None:
    c.run("ruff format --check src tests", pty=True)
    c.run("ruff check src tests", pty=True)
    c.run("mypy src tests", pty=True)


@task
def test(c: Context, *, cov: bool = False) -> None:
    cov_options = "--cov-report=term-missing --cov-report=html --cov"
    c.run(f"pytest {cov_options if cov else ''} src tests", pty=True)
