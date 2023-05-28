"""Tests of the NGLViewer"""
import panel as pn

from panel_chemistry.bokeh_extensions.ngl_viewer import NGLViewer as _BkNGLViewer
from panel_chemistry.pane import NGLViewer


def test_can_create(document, comm):
    """Test of the NGLViewer constructor"""
    viewer = NGLViewer(object="1CRN", background_color="yellow", height=500)
    pane = viewer.get_root(document, comm=comm)
    assert isinstance(pane, _BkNGLViewer)


def test_has_bokeh_model():
    """Test that the NGL Viewer Exists"""
    assert _BkNGLViewer.__name__


def _create_app():
    """Returns an app for manually testing the NGL Molecule Viewer"""
    pn.extension(sizing_mode="stretch_width")
    # 1NKT, 2GQ5, 3UOG and 5TXH
    viewer = NGLViewer(object="1CRN", background_color="yellow", height=500)
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
        "background_color",
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


def test_app():
    """Can create test app"""
    assert _create_app()


if __name__.startswith("bokeh"):
    _create_app().servable()
