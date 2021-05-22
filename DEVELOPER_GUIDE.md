# 🎁 For Contributers

The structure of the project will be the same as the [panel-highcharts](https://github.com/marcskovmadsen/panel-highcharts) project and package until something else is decided. I.e. we use

- [binder](https://mybinder.org/) to provide an easy to use environment for trying, learning, exploring and using the packing. [See MarcSkovMadsen/../binder](https://github.com/MarcSkovMadsen/panel-chemistry/tree/main/binder).
- Python [Invoke](http://www.pyinvoke.org/) to easily run build, test etc tasks. [See MarcSkovMadsen/../tasks](https://github.com/MarcSkovMadsen/panel-chemistry/tree/main/tasks)
  - This includes includes running isort, autoflake, black, pylint, mypy and pytest and making sure all test should pass before merging to main branch. This will keep the code and package working and maintainable.
- Provide documentation via this README and an examples folder of notebooks. [See MarcSkovMadsen/../examples](https://github.com/MarcSkovMadsen/panel-chemistry/tree/main/examples)

Maybe we also improve it further

- Add CI/ CD on Github to build, test and deploy the package. (I have not tried this before)
- Add various badges (I have not tried this before).
- Add documentation on read the docs. But not for now in order to keep things simple.

## 🛠️ Prerequisites

- conda

Please note that you can also use pip. But then you will have to mess with getting node.js installed which might be a painful process
if your are in some kind of constrained, enterprise environment.

## 🏃 Installation

```bash
git clone https://github.com/marcskovmadsen/panel-chemistry
cd panel-chemistry
```

Create your virtual environment.

```bash
conda create --name panel-chemistry
```

Activate your virtual environment. On Windows with Git Bash it can be done via

```bash
conda activate panel-chemistry
```

Install the `panel-chemistry` package for editing

```bash
pip install -e .[all]
```

install node.js

```bash
conda install -c conda-forge nodejs
```

## 📝 Invoke

We use [Python Invoke](http://www.pyinvoke.org/) to easily run build, test etc tasks.

You can learn more about the available options via `invoke --list`. Please note that invoke should run from the root of the project.

The invoke tasks are defined in the [tasks](./tasks/__init__.py) module.

### 🏗️ Build

You can see the build commands via

```bash
$ invoke --list=build
Available 'build' tasks:

  .bokeh-extensions (.extensions)   Builds the Bokeh extensions
  .python-package (.package)        Builds the panel-chemistry Python package
```

For example to build the Bokeh extensions you can write

```bash
invoke build.extensions
```

## 🧪 Tests

To see the available options run

```bash
$ invoke --list=test
Available 'test' tasks:

  .all (.pre-commit, .test)   Runs isort, autoflake, black, pylint, mypy and pytest
  .autoflake                  Runs autoflake to remove unused imports on all .py files recursively
  .bandit                     Runs Bandit the security linter from PyCQA.
  .black                      Runs black (autoformatter) on all .py files recursively
  .isort                      Runs isort (import sorter) on all .py files recursively
  .mypy                       Runs mypy (static type checker) on all .py files recursively
  .pylint                     Runs pylint (linter) on all .py files recursively to identify coding errors
  .pytest                     Runs pytest to identify failing tests
```

For example to run pytest you would run `invoke test.pytest`.

All tests are also automatically run via [Github Actions](https://docs.github.com/en/actions) on Pull Requests and merges into the `main` branch. For more info checkout the [tests.yaml](.github/workflows/tests.yaml) configuration file.

## Pull Requests

You are welcome to create Pull Requests on preliminary code.

When you request a review please make sure all tests (i.e. `invoke test.all` pass). Alternatively please just mention that not all tests pass but you would still like a review and the reason why.

## 🚢 Package Build and Deploy

In the `VERSION` file update the `version` number and then run

```bash
python setup.py sdist bdist_wheel
```

to build and

```bash
python -m twine upload dist/*0.0.1*
```

to deploy the package 📦. If you want to upload to *Test Pypi* first you can do so by adding `--repository testpypi`.

### 📒 Rebuild the Binder Image

Open Binder to rebuild the package

[Open Binder](https://mybinder.org/v2/gh/MarcSkovMadsen/panel-chemistry/main?urlpath=labs)

#### 💻 Build and Run the Binder Image Locally

In order to test the Binder Image you can install repo2docker

```python
python -m pip install jupyter-repo2docker
```

You can then run

```python
jupyter-repo2docker https://github.com/MarcSkovMadsen/panel-chemistry
```

Note: Does not work on Windows.
