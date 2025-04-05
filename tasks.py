from invoke.context import Context
from invoke.tasks import task


@task
def fmt(c: Context) -> None:
    c.run("ruff check --fix-only --show-fixes src", pty=True)
    c.run("ruff format tasks.py src", pty=True)


@task
def lint(c: Context) -> None:
    c.run("ruff format --check src", pty=True)
    c.run("ruff check src", pty=True)
    c.run("mypy src", pty=True)
