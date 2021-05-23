"""A Bokeh model for the JSMEEditor"""
from bokeh.core.properties import Int, String
from bokeh.models import HTMLBox


class JSMEEditor(HTMLBox):
    """JSMEEditor Bokeh Model"""

    object = String()
    clicks = Int()