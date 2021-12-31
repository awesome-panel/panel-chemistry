import panel as pn
pn.extension()

def f(x):
    return pn.pane.Markdown(x, sizing_mode="stretch_width")

layout = pn.interact(f, x="Hi there!", )
layout.sizing_mode="stretch_width"
layout.servable()