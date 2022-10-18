# 🧪 Panel-Chemistry

[![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)
[![Follow on LinkedIn](https://img.shields.io/badge/linked-in-blue)](https://www.linkedin.com/in/marcskovmadsen)

We want to

- make it super simple to do **exploratory data analysis** and develop high-quality
[Panel](https://awesome-panel.org) **data apps** within the domain of **chemistry**.

We provide

- the `panel-chemistry` python package of chemistry components for Panel.
- example notebooks and data apps.

![Panel Chemistry Intro](https://raw.githubusercontent.com/MarcSkovMadsen/panel-chemistry/main/assets/panel-chemistry-intro.gif)

## 🚀 Get started in under a minute

You can install the package with `pip`

```bash
pip install panel-chemistry[examples]
```

Explore the sample apps

```bash
pn hello panel-chemistry
```

You can now find the *reference* notebooks in the `examples/awesome-panel/panel-chemistry` folder. Check them out by running `jupyter lab`.

## 📒 Get started on Binder

Click the button

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/awesome-panel/panel-chemistry/HEAD)

## 🏃 Serve a data app

Add the below to a python file or notebook

```python
import panel as pn
from panel_chemistry.widgets import JSMEEditor

pn.extension("jsme", sizing_mode="stretch_width")

smiles="N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O"
editor = JSMEEditor(value=smiles, height=500, format="smiles")

editor.servable()
```

Run `panel serve name_of_app.py` or `panel_serve name_of_notebook.ipynb`.

![JSME Editor](https://raw.githubusercontent.com/MarcSkovMadsen/panel-chemistry/main/assets/panel-chemistry-example.png)

## Install with conda

```bash
conda install -c conda-forge panel-chemistry
```

## ⭐ Support

Please support [Panel](https://panel.holoviz.org) and
[awesome-panel](https://awesome-panel.org) by giving the projects a star on Github:

- [holoviz/panel](https://github.com/holoviz/panel).
- [awesome-panel/awesome-panel](https://github.com/awesome-panel/awesome-panel).

Thanks

## ❤️ Contribute

You can find *good first issues* in the [issue tracker](https://github.com/awesome-panel/panel-chemistry/issues). To get started check out the [DEVELOPER_GUIDE](DEVELOPER_GUIDE.md).

I would love to support and receive your contributions. Thanks.

[![Hacktober Fest](https://github.blog/wp-content/uploads/2022/10/hacktoberfestbanner.jpeg?fit=1200%2C630)](https://github.com/awesome-panel/panel-chemistry/issues).

## 🖥️ Monitor

[![PyPI version](https://badge.fury.io/py/panel-chemistry.svg)](https://pypi.org/project/panel-chemistry/)
[![Downloads](https://pepy.tech/badge/panel-chemistry/month)](https://pepy.tech/project/panel-chemistry)
![Python Versions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
[![License](https://img.shields.io/badge/License-MIT%202.0-blue.svg)](https://opensource.org/licenses/MIT)
![Test Results](https://github.com/MarcSkovMadsen/panel-chemistry/actions/workflows/tests.yaml/badge.svg?branch=main)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/awesome-panel/panel-chemistry/HEAD)