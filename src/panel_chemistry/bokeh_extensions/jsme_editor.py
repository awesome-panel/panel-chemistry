"""A Bokeh model for the JSMEEditor"""
from bokeh.core.properties import List, String
from panel import extension
from panel.models.layout import HTMLBox

# pylint: disable=protected-access
extension._imports["jsme"] = "panel_chemistry.bokeh_extensions.jsme_editor"
# pylint: enable=protected-access


class JSMEEditor(HTMLBox):  # pylint: disable=too-few-public-methods,too-many-ancestors
    """JSMEEditor Bokeh Model"""

    __javascript__ = [
        "https://cdn.jsdelivr.net/npm/jsme-editor@2023.7.31/jsme.nocache.js",
    ]

    __css__ = [
        "https://cdn.jsdelivr.net/npm/jsme-editor@2023.7.31/gwt/chrome/mosaic.css",
        "https://cdn.jsdelivr.net/npm/jsme-editor@2023.7.31/jsa.css",
        "https://cdn.jsdelivr.net/npm/jsme-editor@2023.7.31/gwt/chrome/chrome.css",
    ]

    value = String(default="N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O")
    format = String(default="smiles")
    subscriptions = List(String, default=[]) # type: ignore
    options = List(String, default=[]) # type: ignore

    jme = String(default="")
    smiles = String(default="")
    mol = String(default="")
    mol3000 = String(default="")
    sdf = String(default="")

    guicolor = String(default="#c0c0c0")
