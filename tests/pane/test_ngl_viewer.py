"""Tests of the NGLViewer"""
import panel as pn

from panel_chemistry.pane import NGLViewer
from panel_chemistry.bokeh_extensions.ngl_viewer import NGLViewer as _BkNGLViewer


def test_can_create():
    """Test of the NGLViewer constructor"""
    NGLViewer(object="1CRN", background="yellow", height=500)

def test_has_bokeh_model():
    assert _BkNGLViewer

def test_app():
    """Returns an app for manually testing the NGL Molecule Viewer"""
    pn.extension(sizing_mode="stretch_width")
    # 1NKT, 2GQ5, 3UOG and 5TXH
    viewer = NGLViewer(object="1CRN", background="yellow", height=500)
    parameters = [
        "object",
        "extension",
        "representation",
        "color_scheme",
        "custom_color_scheme",
        "effect",
        "sizing_mode",
        "width",
        "height",
        "background",
    ]
    settings = pn.Param(
        viewer,
        parameters=parameters,
    )
    return pn.Row(
        viewer,
        pn.WidgetBox(
            settings,
            width=300,
            sizing_mode="fixed",
        ),
    )


if __name__.startswith("bokeh"):
    test_app().servable()
