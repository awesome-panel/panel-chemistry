# ❤️ Developer Guide

Welcome. We are so happy that you want to contribute.

## 🛠️ Prerequisites

- A `conda` environment.
- [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

You can also use `pip` if you can get `node.js` installed.

## 📙 How to

Below we describe how to install and use this project for development.

### 💻 Install for Development

To install for development you will need to create and activate a virtual environment

```bash
conda create --name panel-chemistry python=3.9 nodejs
conda activate panel-chemistry
```

Then run

```bash
git clone https://github.com/awesome-panel/panel-chemistry.git
cd panel-chemistry
pip install pip -U
pip install -e .[all]
```

This will install the
[`awesome-panel-cli`](https://github.com/awesome-panel/awesome-panel-cli). You can see the available commands via

```bash
pn --help
```

You can run all tests via

```bash
pn test all
```

Please run this command and fix any failing tests if possible before you `git push`.

### 🚢 Release a new package on Pypi

Please make sure you have upgraded bokeh

```bash
cd panel_chemistry
npm update @bokeh/bokehjs --save
```

Update the version number in the [__init__.py](panel_chemistry/__init__.py) and
[package.json](panel_chemistry/package.json) files.

Then run

```bash
pn test all
```

Then you can build

```bash
panel build panel_chemistry
pn build package
```

and upload

```bash
pn release package <VERSION>
```

to release the package 📦. To upload to *Test Pypi* first, you can add the `--test` flag.
