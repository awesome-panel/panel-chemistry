# 🧪 Panel-Chemistry

The purpose of the `panel-chemistry` project is to make it really easy for you 👨‍🔬 to do **exploratory data analysis** and **build powerful data and viz tools** 📈🛠️ within the domain of **Chemistry** ⚗️.

## 🏁 Background

This project is just starting (2021-05-19) and not much more than an idea.

It was started by the discussion [How to display JSME molecular editor with Panel?](https://discourse.holoviz.org/t/how-to-display-jsme-molecular-editor-with-panel/2306/12) in the [Panel Community Forum](https://discourse.holoviz.org/)

## 🏃 Getting Started

```bash
pip install panel_chemistry
```

```python
import panel_chemistry as pc
import panel as pn

pn.extension("jsme", sizing_mode="stretch_width)

editor = pc.JSMEEditor(height=800)
editor
```

![JSME Editor](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/JMEEditor2008-2.png/300px-JMEEditor2008-2.png)

## 👩‍🏫 Examples

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-chemistry/main?urlpath=lab/tree/examples)

## 💡 Inspirational Resources

- [Dash Bio](https://dash.plotly.com/dash-bio)
- [Awesome Python Chemistry](https://github.com/lmmentel/awesome-python-chemistry)

## 🎁 Contributing

If you want to contribute reach out via [Github Issues](https://github.com/MarcSkovMadsen/panel-chemistry/issues) or in the Contributor Community Forum on Gitter: https://gitter.im/panel-chemistry/community#

For more details see the [Developer Guide](DEVELOPER_GUIDE.md)
