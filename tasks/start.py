"""Module of Invoke starts tasks to be invoked from the command line. Try

invoke --list=start

from the command line for a list of all available commands.
"""

from glob import glob
from pathlib import Path

from invoke import task

DONT_SERVE = []



def _get_active_branch_name():

    head_dir = Path(".") / ".git" / "HEAD"
    with head_dir.open("r") as f: content = f.read().splitlines()

    for line in content:
        if line[0:4] == "ref:":
            return line.partition("refs/heads/")[2]

def _get_apps():
    return [
        app for app in glob("examples/reference/*.ipynb", recursive=True) if not app in DONT_SERVE
    ]


@task()
def binder(command):
    """Opens the current branch of the repository on Binder."""
    print(
        """
Opens the main branch of the repository on Binder.
=================================================
"""
    )
    branch = _get_active_branch_name()
    url = f"https://mybinder.org/v2/gh/MarcSkovMadsen/panel-chemistry/{branch}?urlpath=labs"
    command.run(f"python -m webbrowser {url}", echo=True)

@task()
def github(command):
    """Opens the current branch of the repository on Github."""
    print(
        """
Opens the main branch of the repository on Github.
=================================================
"""
    )
    branch = _get_active_branch_name()
    url = f"https://github.com/MarcSkovMadsen/panel-chemistry/tree/{branch}"
    command.run(f"python -m webbrowser {url}", echo=True)

@task()
def examples(command):
    """Panel serves the examples."""
    print(
        """
Panel serves the examples.
==========================
"""
    )
    apps = _get_apps()
    command.run(f"panel serve {' '.join(apps)}", echo=True)
