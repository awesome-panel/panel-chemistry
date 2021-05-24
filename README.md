# 🧪 Panel-Chemistry

👨‍🔬📈🛠️🐍❤️

The purpose of the `panel-chemistry` project is to make it really easy for you  to do **exploratory data analysis** and **build powerful data and viz tools** within the domain of **Chemistry** using [Python](https://www.python.org/) and [HoloViz Panel](https://panel.holoviz.org/).

## 👍 Badges

![Python Versions](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue) ![Style Black](https://warehouse-camo.ingress.cmh1.psfhosted.org/fbfdc7754183ecf079bc71ddeabaf88f6cbc5c00/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) ![Test Results](https://github.com/MarcSkovMadsen/panel-chemistry/actions/workflows/tests.yaml/badge.svg?branch=main) [![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)

## 🏁 Background

This project is just starting (2021-05-19) and not much more than an idea.

It was started by the discussion [How to display JSME molecular editor with Panel?](https://discourse.holoviz.org/t/how-to-display-jsme-molecular-editor-with-panel/2306/12) in the [Panel Community Forum](https://discourse.holoviz.org/)

## 🏃 Getting Started

```bash
pip install panel-chemistry
```

```python
import panel_chemistry as pc
import panel as pn

pn.extension("jsme", sizing_mode="stretch_width")

editor = pc.JSMEEditor(height=800)
editor
```

![JSME Editor](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/JMEEditor2008-2.png/300px-JMEEditor2008-2.png)

## 👩‍🏫 Examples

Check out the `panel-chemistry` examples on **Binder**

| Jupyter Notebook | Jupyter Labs | Panel Apps |
| - | - | - |
| [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?filepath=examples) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?urlpath=lab/tree/examples) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/HEAD?urlpath=panel) |

## 💡 Inspirational Resources

- [Awesome Python Chemistry](https://github.com/lmmentel/awesome-python-chemistry)
- [Dash Bio](https://dash.plotly.com/dash-bio)
- [JSME Editor](https://jsme-editor.github.io) and [Test Page](https://jsme-editor.github.io/dist/JSME_test.html)
- [RDKit](http://www.rdkit.org/)
- [RDKit IPython Tools](https://github.com/apahl/rdkit_ipynb_tools)

## 🎁 Contributing

If you want to contribute reach out via [Github Issues](https://github.com/MarcSkovMadsen/panel-chemistry/issues) or in the Contributor Community Forum on Gitter: https://gitter.im/panel-chemistry/community#

For more details see the [Developer Guide](DEVELOPER_GUIDE.md)

## FAQ

### How do I Install with Conda?

You can do

```bash
conda install pip
pip install panel-chemistry
```

You can also include `panel-chemistry` in your `environment.yaml` file as described on [Stack Overflow: Combining conda environment.yml with pip requirements.txt](https://stackoverflow.com/questions/35245401/combining-conda-environment-yml-with-pip-requirements-txt).
