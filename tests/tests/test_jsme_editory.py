"""Tests of the JSMEEditor"""
# pylint: disable=missing-function-docstring
import panel as pn

from panel_chemistry.widgets import JSMEEditor


def test_can_construct():
    JSMEEditor()


def test_jsme_editor_app():
    editor = JSMEEditor(height=250)
    component = pn.Column(editor, editor.param.clicks)
    return pn.template.FastListTemplate(
        site="Panel Chemistry v0.0.3",
        title="Dummy JSME Editor",
        main=[component]
    )


if __name__.startswith("bokeh"):
    test_jsme_editor_app().servable()
