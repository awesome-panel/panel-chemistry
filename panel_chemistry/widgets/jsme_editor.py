"""The panel-chemistry JSME Molecule Editor enables you to draw and edit molecules using Python
and Panel.

It is a wrapper of the free javascript JSME Molecule Editor. See https://jsme-editor.github.io/
"""
import param
from panel.widgets.base import Widget

from panel_chemistry.bokeh_extensions.jsme_editor import JSMEEditor as _BkJSMEEditor

NOT_SUBSCRIBED = "Not Subscribed"
VALUE_FORMATS = ["jme", "smiles", "mol", "mol3000", "sdf"]
# fmt: off
OPTIONS = [
    "addnewpart", "noaddnewpart",
    "atommovebutton", "noatommovebutton",
    "autoez", "noautoez",
    "border", "noborder",
    "canonize", "nocanonize",
    "contextmenu", "nocontextmenu",
    "depict", "nodepict",
    "depictaction", "nodepictaction",
    "exportinchi", "noexportinchi",
    "exportinchiauxinfo", "noexportinchiauxinfo",
    "exportinchikey", "noexportinchikey",
    "exportSVG", "noexportSVG",
    "fgmenu", "nofgmenu",
    "fullScreenIcon", "nofullScreenIcon",
    "hydrogens", "nohydrogens",
    "keephs", "removehs",
    "keephsc", "removehsc",
    "markAtomOnly", "noMarkAtomOnly",
    "markBondOnly", "noMarkBondOnly",
    "marker", "nomarker",
    "marker1", "nomarker1",
    "markNothing", "noMarkNothing",
    "multipart", "nomultipart",
    "newlook", "oldlook",
    "number", "autonumber",
    "paste", "nopaste",
    "polarnitro", "nopolarnitro",
    "pseudoMark", "nopseudoMark",
    "query", "noquery",
    "rbutton", "norbutton",
    "reaction", "noreaction",
    "searchinchiKey", "nosearchinchiKey",
    "showdragandDropIconindepictmode", "noShowdragandDropIconindepictmode",
    "showFullScreenIconInDepictMode", "noshowFullScreenIconInDepictMode",
    "stereo", "nostereo",
    "toggle", "notoggle",
    "useOclidcode", "nouseOclidcode",
    "useopenchemlib", "nouseopenchemlib",
    "valenceState", "noValenceState",
    "xbutton", "noxbutton",
    "zoom", "nozoom",
]
# fmt: on


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
    value = param.String(default="")  # pylint: disable=line-too-long
    format = param.ObjectSelector("jme", objects=VALUE_FORMATS)
    # Note: Could be implemented as a list of checkboxes.
    # Defaults can be found here http://wiki.jmol.org/index.php/Jmol_JavaScript_Object/JME/Options
    options = param.ListSelector(objects=OPTIONS)

    jme = param.String(constant=True)
    smiles = param.String(constant=True)
    mol = param.String(default=NOT_SUBSCRIBED, constant=True)
    mol3000 = param.String(default=NOT_SUBSCRIBED, constant=True)
    sdf = param.String(default=NOT_SUBSCRIBED, constant=True, label="SDF")

    subscriptions = param.ListSelector(
        default=[], objects=["jme", "smiles", "mol", "mol3000", "sdf"]
    )
