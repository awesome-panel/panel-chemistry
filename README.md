![Python Versions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
[![License](https://img.shields.io/badge/License-MIT%202.0-blue.svg)](https://opensource.org/licenses/MIT)
![Test Results](https://github.com/MarcSkovMadsen/panel-chemistry/actions/workflows/tests.yaml/badge.svg?branch=main)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/awesome-panel/panel-chemistry/feature/HEAD)
[![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marcskovmadsen)

# 🧪 Panel-Chemistry

We want to

- make it super simple to do **exploratory data analysis** and develop high-quality
[Panel](https://awesome-panel.org) **data apps** within the domain of **chemistry**.

We provide

- the `panel-chemistry` python package of chemistry components for Panel.
- example notebooks and data apps.

You can install and create a new *app* as simple as

```bash
pip install panel-chemistry
```

```python
import panel as pn 
from panel_chemistry.pane import NGLViewer # panel_chemistry needs to be imported before you run pn.extension()

pn.extension("ngl_viewer", sizing_mode="stretch_width", template="fast")

NGLViewer(object="1CRN", background="#F7F7F7", min_height=700, sizing_mode="stretch_both").servable()
```

![Panel Chemistry Teaser](https://raw.githubusercontent.com/MarcSkovMadsen/panel-chemistry/main/assets/panel-chemistry-teaser.gif)

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

## 📙 How to

Below we describe how to install and use this project.

### 🚀 Install for usage

You can install the package with `pip`

```bash
pip install panel-chemistry
```

or `conda`

```bash
conda install -c conda-forge panel-chemistry
```

### 👩‍🏫 Explore the examples online

Check out the `panel-chemistry` **reference guides** on **Binder**

| Guide | NB Viewer | Github Notebook | Jupyter Notebook | Jupyter Labs | Panel Apps |
| - | - | - | - | - | - |
| JSME Editor | [View](https://nbviewer.org/github/MarcSkovMadsen/panel-chemistry/blob/main/examples/reference/JSMEEditor.ipynb) | [View](https://github.com/MarcSkovMadsen/panel-chemistry/blob/main/examples/reference/JSMEEditor.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?filepath=examples/reference/JSMEEditor.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?urlpath=lab/tree/examples/reference/JSMEEditor.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?urlpath=panel/JSMEEditor) |
| NGL Viewer | [View](https://nbviewer.org/github/MarcSkovMadsen/panel-chemistry/blob/main/examples/reference/NGLViewer.ipynb) | [View](https://github.com/MarcSkovMadsen/panel-chemistry/blob/main/examples/reference/NGLViewer.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?filepath=examples/reference/NGLViewer.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?urlpath=lab/tree/examples/reference/NGLViewer.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?urlpath=panel/NGLViewer) |
| PDBe_MolStar | [View](https://nbviewer.org/github/MarcSkovMadsen/panel-chemistry/blob/main/examples/reference/PDBe_MolStar.ipynb) | [View](https://github.com/MarcSkovMadsen/panel-chemistry/blob/main/examples/reference/PDBe_MolStar.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?filepath=examples/reference/PDBe_MolStar.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?urlpath=lab/tree/examples/reference/PDBe_MolStar.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?urlpath=panel/PDBe_MolStar) |
| Py3DMol Pane | [View](https://nbviewer.org/github/MarcSkovMadsen/panel-chemistry/blob/main/examples/reference/Py3DMol.ipynb) | [View](https://github.com/MarcSkovMadsen/panel-chemistry/blob/main/examples/reference/Py3DMol.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?filepath=examples/reference/Py3DMol.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?urlpath=lab/tree/examples/reference/Py3DMol.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?urlpath=panel/Py3DMol) |

### 👩‍🏫 Explore the examples locally

Run

```bash
pip install pip -U
pip install panel-chemistry[all]
git clone https://github.com/awesome-panel/panel-chemistry.git
cd panel-chemistry/examples
```

Then run

```bash
jupyter lab
```

or

```bash
panel serve reference/*.ipynb
```

### 🏃 Serve a data app

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
