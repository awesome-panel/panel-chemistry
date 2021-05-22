"""Module of Invoke build tasks to be invoked from the command line. Try

invoke --list=build

from the command line for a list of all available commands.
"""

from invoke import task


@task(aliases=["extensions"])
def bokeh_extensions(command):
    """Builds the Bokeh extensions using Node.js

    Please note this requires Node.js>=14 to be installed
    """
    print(
        """Builds the Bokeh extensions using Node.js

Please note this requires Node.js>=14 to be installed
=====================================================
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

@task(aliases=["binder"])
def binder_image(command):
    """Builds the panel-chemistry binder image using jupyter-repo2docker


    Please note this does not work on Windows"""
    print(
        """Builds the panel-chemistry binder image using jupyter-repo2docker

Please note this does not work on Windows
=========================================
"""
    )
    command.run("jupyter-repo2docker .", echo=True)