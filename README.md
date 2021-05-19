# panel-chem-bio

The purpose of the panel-chem-bio project is to make it really easy to work with EDA and create awesome visual tools within the domains of Chemistry and Molecular Biology and using [Panel](https://panel.holoviz.org).

THIS PROJECT IS JUST STARTING (2021-05-19) AND NOTHING MORE THAN AN IDEA. It was started the discussion [How to display JSME molecular editor with Panel?](https://discourse.holoviz.org/t/how-to-display-jsme-molecular-editor-with-panel/2306/12) in the [Panel Community Forum](https://discourse.holoviz.org/)

The structure of the project will be the same as the [panel-highcharts](https://github.com/marcskovmadsen/panel-highcharts) project and package until something else is decided. I.e. we use

- [binder](https://mybinder.org/) to provide an easy to use environment for trying, learning, exploring and using the packing. [See](https://github.com/MarcSkovMadsen/panel-highcharts/tree/main/binder).
- Python [Invoke](http://www.pyinvoke.org/) to easily run build, test etc tasks. [See](https://github.com/MarcSkovMadsen/panel-highcharts/tree/main/tasks)
    - This includes includes running isort, autoflake, black, pylint, mypy and pytest and making sure all test should pass before merging to main branch. This will keep the code and package working and maintainable.
- Provide an examples folder of notebooks. [See](https://github.com/MarcSkovMadsen/panel-highcharts/tree/main/examples)

Maybe we also improve it further

- Add CI/ CD on Github to build, test and deploy the package. (I have not tried this before)
- Add various badges (I have not tried this before).
- Add documentation on read the docs. But not for now in order to keep things simple.

## Getting Started

`pip install panel_chem_bio`

```python
import panel_chem_bio as pc
import panel as pn

pn.extension("jsme", sizing_mode="stretch_width)

editor = pc.JSMEEditor(height=800)
editor
```

![JSME Editor](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/JMEEditor2008-2.png/300px-JMEEditor2008-2.png)

## Inspirational Resources

- [Dash Bio](https://dash.plotly.com/dash-bio)
- [Awesome Python Chemistry](https://github.com/lmmentel/awesome-python-chemistry)
