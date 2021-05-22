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

- Python >= 3.7
- Node >= 14

## 🏃 Installation

```bash
git clone https://github.com/marcskovmadsen/panel-chemistry
cd panel-chemistry
```

Create your virtual environment.

```bash
python -m venv .venv
```

Activate your virtual environment. On Windows with Git Bash it can be done via

```bash
source .venv/Scripts/activate # Windows
```

Install the `panel-chemistry` package for editing

```bash
pip install -e .[all]
```

## 🏗️ Bokeh Models build

```bash
panel build panel_chemistry
```

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
Skipped 7 files

Running autoflake to remove unused imports on all .py files recursively
=======================================================================

autoflake --imports=pytest,pandas,numpy,plotly,dash,urllib3 --in-place --recur
sive .

Running Black the Python code formatter
=======================================

black .
All done! \u2728 \U0001f370 \u2728
16 files left unchanged.

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
Success: no issues found in 16 source files

Running pytest the test framework
=================================

pytest tests --doctest-modules --cov=panel_chemistry -m "not functionaltest a
nd not integrationtest" --cov-report html:test_results/cov_html
============================= test session starts =============================
platform win32 -- Python 3.8.4, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: C:\repos\private\panel-chemistry, configfile: pytest.ini, testpaths: tests
plugins: anyio-2.2.0, cov-2.11.1
collected 6 items

tests\test_config.py .                                                   [ 16%]
tests\test_highchart.py ...                                              [ 66%]
tests\models\test_highchart.py ..                                        [100%]

----------- coverage: platform win32, python 3.8.4-final-0 -----------
Coverage HTML written to dir test_results/cov_html


============================== 6 passed in 2.07s ==============================

All Tests Passed Successfully
=============================
```

## 🚢 Package Build and Deploye

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