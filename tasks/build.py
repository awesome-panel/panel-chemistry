"""Module of Invoke build tasks to be invoked from the command line. Try

invoke --list=build

from the command line for a list of all available commands.
"""

from invoke import task


@task(aliases=["extensions"])
def bokeh_extensions(command):
    """Builds the Bokeh extensions

    Please note this requires node.js>=14 is installed
    """
    print(
        """Builds the Bokeh extensions

Please note this requires node.js>=14 is installed
=================================================
"""
    )
    command.run("panel build panel_chemistry", echo=True)


@task(aliases=["package"])
def python_package(command):
    """Builds the panel-chemistry Python package

    Remember to update the version number in the VERSION file!
    """
    print(
        """Builds the panel-chemistry Python package

Remember to update the version number in the VERSION file!
=================================================
"""
    )
    command.run("python setup.py sdist bdist_wheel", echo=True)
