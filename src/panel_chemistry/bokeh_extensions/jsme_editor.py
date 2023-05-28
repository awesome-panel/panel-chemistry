"""A Bokeh model for the JSMEEditor"""
from bokeh.core.properties import List, String
from panel import extension
from panel.models.layout import HTMLBox

# pylint: disable=protected-access
extension._imports["jsme"] = "panel_chemistry.bokeh_extensions.jsme_editor"
# pylint: enable=protected-access


class JSMEEditor(HTMLBox):  # pylint: disable=too-few-public-methods,too-many-ancestors
    """JSMEEditor Bokeh Model"""

    __javascript__ = ["https://unpkg.com/jsme-editor@0.8.2/jsme.nocache.js"]

    value = String()
    format = String()
    subscriptions = List(String())
    options = List(String())

    jme = String()
    smiles = String()
    mol = String()
    mol3000 = String()
    sdf = String()

    guicolor = String()
