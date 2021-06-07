"""Tests of the NGLViewer"""
from panel_chemistry.pane import NGLViewer

if __name__.startswith("bokeh"):
    import panel as pn

    pn.extension(sizing_mode="stretch_width")
    viewer = NGLViewer(object="1CRN", background="yellow", height=500)
    parameters = [
        "object",
        "object_format",
        "representation",
        "color_schema",
        "spin",
        "sizing_mode",
        "width",
        "height",
    ]
    app = pn.Row(
        viewer,
        pn.WidgetBox(
            pn.Param(
                viewer,
                parameters=parameters,
            ),
            width=300,
            sizing_mode="fixed",
        ),
    )
    app.servable()
