"""Setup file for the Awesome Panel Extensions"""
import pathlib
from typing import List

import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

ROOT = pathlib.Path.cwd()
VERSION = (ROOT / "VERSION").read_text().strip()

install_requires = [
    "panel>=0.11.1",
    "bokeh>=2.3",
]

_recommended: List[str] = []

_tests = [
    "autoflake",
    "invoke",
    "isort",
    "jupyter-repo2docker",
    "mypy",
    "pylint>=2.6.0",
    "pytest",
    "pytest-cov",
    "rope",
    "twine",
    "wheel",
    "codecov",
]

_examples = [
    "notebook",
    "jupyterlab",
]

_doc: List[str] = []

extras_require = {
    "examples": _recommended + _examples,
    "tests": _tests,
    "recommended": _recommended,
    "doc": _recommended + _doc,
}

extras_require["all"] = sorted(set(sum(extras_require.values(), [])))

setuptools.setup(
    name="panel-chemistry",
    version=VERSION,
    description="""This purpose makes it easy to work with the domains of Chemistry and Molecular
Biology using Panel""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Marc Skov Madsen et al.",
    author_email="marc.skov.madsen@gmail.com",
    platforms=["Windows", "Mac OS X", "Linux"],
    license="Apache 2",
    url="https://github.com/MarcSkovMadsen/panel-chemistry",
    # My Project contains more folders/ packages but they should not be included
    packages=setuptools.find_packages(include=["panel_chemistry", "panel_chemistry.*"]),
    include_package_data=True,
    classifiers=[
        # I would like to indicate that this package is a package for the Panel framework
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=extras_require["tests"],
)
