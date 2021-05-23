"""The panel-chemistry JSME Molecule Editor enables you to draw and edit molecules using Python
and Panel.
It is a wrapper of the free javascript JSME Molecule Editor. See https://jsme-editor.github.io/
"""
import param
from panel.widgets.base import Widget

from panel_chemistry.bokeh_extensions.jsme_editor import JSMEEditor as _BkJSMEEditor


class JSMEEditor(Widget):
    """The panel-chemistry JSME Molecule Editor enables you to draw and edit molecules using Python
    and Panel.
    It is a wrapper of the free javascript JSME Molecule Editor.
    See https://jsme-editor.github.io/"""

    # Set the Bokeh model to use
    _widget_type = _BkJSMEEditor

    # Rename Panel Parameters -> Bokeh Model properties
    # Parameters like title that does not exist on the Bokeh model should be renamed to None
    _rename = {
        "title": None,
    }

    # Parameters to be mapped to Bokeh model properties
    object = param.String(
        default="<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/JMEEditor2008-2.png/300px-JMEEditor2008-2.png' style='width:100%'></img>"  # pylint: disable=line-too-long
    )
    clicks = param.Integer(default=0)