"""The panel-chemistry JSME Molecule Editor enables you to draw and edit molecules using Python
and Panel.

It is a wrapper of the free javascript JSME Molecule Editor. See https://jsme-editor.github.io/
"""
import param
from panel.widgets.base import Widget

from panel_chemistry.bokeh_extensions.jsme_editor import \
    JSMEEditor as _BkJSMEEditor

NOT_SUBSCRIBED = "Not Subscribed"
VALUE_FORMATS = ["jme", "smiles", "mol", "mol3000", "sdf"]
# fmt: off
# Defaults can be found here http://wiki.jmol.org/index.php/Jmol_JavaScript_Object/JME/Options
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
    value = param.String(
        default="",
        doc="""A value definining the structure of the molecule. The
    value provided from Python can be any of the available `format` values. The value returned
    from the client will be in the specified `format` value.""",
    )
    format = param.ObjectSelector(
        "jme",
        objects=VALUE_FORMATS,
        doc="""
    The format of the structure returned from the client. Can be any of "jme" (default), "smiles",
    "mol", "mol3000", "sdf\"""",
    )
    # Note: Could be implemented as a child class of booleans/ checkboxes instead.
    options = param.ListSelector(
        objects=OPTIONS,
        doc="""A list of options to apply to the editor.
    Default is [], i.e. to use the default settings.""",
    )

    subscriptions = param.ListSelector(
        default=[],
        objects=VALUE_FORMATS,
        doc="""
    A list of structure formats to "subscribe" to changes of. Can be any of "jme", "smiles",
    "mol", "mol3000", "sdf". Default is [].""",
    )

    jme = param.String(
        default=NOT_SUBSCRIBED,
        constant=True,
        doc="""
    The structure in jme format""",
    )
    smiles = param.String(
        default=NOT_SUBSCRIBED,
        constant=True,
        doc="""
    The structure in smiles format""",
    )
    mol = param.String(
        default=NOT_SUBSCRIBED,
        constant=True,
        doc="""
    The structure in mol format""",
    )
    mol3000 = param.String(
        default=NOT_SUBSCRIBED,
        constant=True,
        doc="""
    The structure in mol3000 format""",
    )
    sdf = param.String(
        default=NOT_SUBSCRIBED,
        constant=True,
        label="SDF",
        doc="""
    The structure in sdf format""",
    )

    guicolor = param.Color(
        default="#c0c0c0",
        doc="""
    Background color of the GUI elements in RGB hex format. Default is "#c0c0c0".""",
    )
