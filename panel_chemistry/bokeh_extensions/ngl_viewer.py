import pathlib
import param

from bokeh.core.properties import String, Bool, List
from bokeh.models import LayoutDOM
from panel.widgets.input import Widget

CUSTOM_TS = pathlib.Path(__file__).parent / "ngl_viewer.ts"
CUSTOM_TS_STR = str(CUSTOM_TS.resolve())


class ngl(LayoutDOM):
    __implementation__ = CUSTOM_TS_STR

    spin = Bool
    representation = String
    rcsb_id = String
    no_coverage = String
    color_list = List(List(String))
    pdb_string = String


class NGL_viewer(Widget):

    _widget_type = ngl

    _rename = {
        "title": None,
    }

    pdb_string = param.String(
        doc="""Raw string of PDB file representing molecular structure to visualize."""
    )
    spin = param.Boolean(
        default=False,
        doc="""Toggle spinning of the molecular structure."""
    )
    representation = param.Selector(
        default='cartoon',
        objects=['ball+stick', 'backbone', 'ball+stick', 'cartoon', 'hyperball', 'licorice',
                 'ribbon', 'rope', 'spacefill', 'surface'],
        doc="""The type of representation used to visualize the molecular structure."""
    )
    rcsb_id = param.String(default="rcsb://1CRN")
    color_list = param.List(default=[["white", "*"]])

    def __init__(self, **params):
        super().__init__(**params)
        self.jscallback(representation="document.dispatchEvent(new Event('representation'));")
        self.jscallback(spin="document.dispatchEvent(new Event('spin'));")
        self.jscallback(rcsb_id="document.dispatchEvent(new Event('rcsb_id'));")
        self.jscallback(color_list="document.dispatchEvent(new Event('color_list'));")
        self.jscallback(pdb_string="document.dispatchEvent(new Event('pdb_string'));")