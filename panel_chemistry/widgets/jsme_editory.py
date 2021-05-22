from panel.widgets.base import Widget
from ..bokeh_extensions.jsme_editor import JSMEEditor as _BkJSMEEditor
import param

class JSMEEditor(Widget):
    # Set the Bokeh model to use
    _widget_type = JSMEEditor

    # Rename Panel Parameters -> Bokeh Model properties
    # Parameters like title that does not exist on the Bokeh model should be renamed to None
    _rename = {
        "title": None,
    }

    # Parameters to be mapped to Bokeh model properties
    object = param.String(default="<button style='width:100%'>Click Me</button>")
    clicks = param.Integer(default=0)