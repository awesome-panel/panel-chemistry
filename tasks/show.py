"""Module of Invoke starts tasks to be invoked from the command line. Try

invoke --list=start

from the command line for a list of all available commands.
"""

from glob import glob
from pathlib import Path
from typing import List

from invoke import task

DONT_SERVE: List[str] = []


def _get_active_branch_name():

    head_dir = Path(".") / ".git" / "HEAD"
    with head_dir.open("r") as file:
        content = file.read().splitlines()

    for line in content:
        if line[0:4] == "ref:":
            return line.partition("refs/heads/")[2]
    return "main"


def _get_apps():
    return [
        app for app in glob("examples/reference/*.ipynb", recursive=True) if not app in DONT_SERVE
    ]


@task()
def binder(command):
    """Opens the current branch on Binder."""
    print(
        """
Opens the current branch on Binder.
=================================================
"""
    )
    branch = _get_active_branch_name()
    url = (
        f"https://mybinder.org/v2/gh/MarcSkovMadsen/panel-chemistry/{branch}"
        "?urlpath=lab/tree/examples"
    )
    command.run(f"python -m webbrowser {url}", echo=True)


@task()
def github(command):
    """Opens the current branch on Github."""
    print(
        """
Opens the current branch on Github.
=================================================
"""
    )
    branch = _get_active_branch_name()
    url = f"https://github.com/MarcSkovMadsen/panel-chemistry/tree/{branch}"
    command.run(f"python -m webbrowser {url}", echo=True)


@task()
def examples(command):
    """Panel serves the examples notebooks."""
    print(
        """
Panel serves the example notebooks.
===================================
"""
    )
    apps = _get_apps()
    command.run(f"panel serve {' '.join(apps)} --auto --show", echo=True)
