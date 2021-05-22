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

## 🏗️ Bokeh Models build

```bash
panel build panel_chemistry
```

## 📝 Invoke

We use [Python Invoke](http://www.pyinvoke.org/) to easily run build, test etc tasks. You can learn more about the available options via `invoke --list`.

```bash
$ invoke --list
Available tasks:

  test.all (test.pre-commit, test.test)   Runs isort, autoflake, black, pylint, mypy and pytest
  test.autoflake                          Runs autoflake to remove unused imports on all .py files recursively
  test.bandit                             Runs Bandit the security linter from PyCQA.
  test.black                              Runs black (autoformatter) on all .py files recursively
  test.isort                              Runs isort (import sorter) on all .py files recursively
  test.mypy                               Runs mypy (static type checker) on all .py files recursively
  test.pylint                             Runs pylint (linter) on all .py files recursively to identify coding errors
  test.pytest                             Runs pytest to identify failing tests
```

and the `--help` flag. For examples

```bash
$ invoke test.pytest --help
Usage: inv[oke] [--core-opts] test.pytest [--options] [other tasks here ...]

Docstring:
  Runs pytest to identify failing tests

  Arguments:
      command {[type]} -- Invoke command object

  Keyword Arguments:
      root_dir {str} -- The directory from which to run the tests
      test_files {str} -- A space separated list of folders and files to test. (default: {'tests})
      integrationtest {bool} -- If True tests marked integrationtest or functionaltest will be
          run. Otherwise not. (default: {False})
      test_results {string} -- If not None test reports will be generated in the test_results
          folder
      open_results {bool} -- If True test reports in the 'test_results' folder will be opened in
          a browser

  # Print running pytest

Options:
  -e STRING, --test-results=STRING
  -i, --integrationtest
  -o, --[no-]open-results
  -t STRING, --test-files=STRING
```

The tasks are defined in the [tasks](./tasks/__init__.py) module.

## 🧪 Tests

```bash
invoke test.all
```

will run `isort`, `autoflake`, `black`, `pylint`, `mypy` and `pytest`. It should look something like

```bash
$ invoke test.all

Running isort the Python code import sorter
===========================================

isort .
Skipped 5 files

Running autoflake to remove unused imports on all .py files recursively
=======================================================================

autoflake --imports=pytest,pandas,numpy,panel,holoviews,hvplot,plotly,urllib3,pathlib --in-place --recursive .

Running Black the Python code formatter
=======================================

black .
All done! \u2728 \U0001f370 \u2728
8 files left unchanged.

Running pylint.
Pylint looks for programming errors, helps enforcing a coding standard,
sniffs for code smells and offers simple refactoring suggestions.
=======================================================================

pylint setup.py tasks panel_chemistry tests

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


Running mypy for identifying python type errors
===============================================

mypy setup.py tasks panel_chemistry tests
Success: no issues found in 5 source files

Running pytest the test framework
=================================

pytest tests --doctest-modules --cov=panel_chemistry -m "not functionaltest and not integrationtest" --cov-report html:test_results/cov_html
============================= test session starts =============================
platform win32 -- Python 3.8.4, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: C:\repos\private\panel-chemistry, configfile: pytest.ini, testpaths: tests
plugins: anyio-3.1.0, cov-2.12.0
collected 0 items


----------- coverage: platform win32, python 3.8.4-final-0 -----------
Coverage HTML written to dir test_results/cov_html

============================ no tests ran in 0.09s ============================
Coverage.py warning: No data was collected. (no-data-collected)
```

## 🚢 Package Build and Deploy

In the `VERSION` file update the `version` number and then run

```bash
python setup.py sdist bdist_wheel
```

to build and

```bash
python -m twine upload dist/*0.0.1*
```

to deploy the package 📦.

### 🚚 Deploying to Test PyPi

```bash
python -m twine upload --repository testpypi dist/*0.0.1*
```

### 📒 Rebuild the Binder Image

Open Binder to rebuild the package

[Open Binder](https://mybinder.org/v2/gh/MarcSkovMadsen/panel-chemistry/master?urlpath=labs)

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
