"""The [NGL Viewer](https://github.com/nglviewer/ngl) can be used
to visualize and analyse pdb molecule structures.

Source: Discussion on [Discourse 583]\
(https://discourse.holoviz.org/t/how-to-use-ngl-webgl-protein-viewer-in-panel/583)

Author: https://github.com/Jhsmit
"""


import param
from panel import extension
from panel.pane.base import PaneBase
from panel.util import lazy_load
from pyviz_comms import JupyterComm

# pylint: disable=protected-access
extension._imports["ngl_viewer"] = "panel_chemistry.bokeh_extensions.ngl_viewer"
# pylint: enable=protected-access

REPRESENTATIONS = [
    # "base",
    # "distance",
    "axes",
    "backbone",
    "ball+stick",
    "cartoon",
    "helixorient",
    "hyperball",
    "label",
    "licorice",
    "line",
    "point",
    "ribbon",
    "rocket",
    "rope",
    "spacefill",
    "surface",
    "trace",
    "unitcell",
    # "validation",
]
COLOR_SCHEMES = [
    "atomindex",
    "bfactor",
    "chainid",
    "chainindex",
    "chainname",
    "custom",
    "densityfit",
    "electrostatic",
    "element",
    "entityindex",
    "entitytype",
    "geoquality",
    "hydrophobicity",
    "modelindex",
    "moleculetype",
    "occupancy",
    "random",
    "residueindex",
    "resname",
    "sstruc",
    "uniform",
    "value",
    "volume",
]
EXTENSIONS = [
    "",
    "pdb",
    "cif",
    "csv",
    "ent",
    "gro",
    "json",
    "mcif",
    "mmcif",
    "mmtf",
    "mol2",
    "msgpack",
    "netcdf",
    "parm7",
    "pqr",
    "prmtop",
    "psf",
    "sd",
    "sdf",
    "top",
    "txt",
    "xml",
]


class NGLViewer(PaneBase):  # pylint: disable=too-many-ancestors
    """The [NGL Viewer](https://github.com/nglviewer/ngl) can be used
    to show and analyse pdb molecule structures"""

    object = param.String(
        default="",
        doc="""
        The object to display. For example an url like 'rcsb://3dqb.pdb', 'rcsb://1NKT', '1NKT'.
        You can also specify a extension string if you define the extension 
        in the extension parameter""",
    )
    background_color = param.Color(
        doc="""
        A custom background color"""
    )
    extension = param.ObjectSelector(
        default="",
        objects=EXTENSIONS,
        doc="""
        If you specify a extension extension != '', then the object will be loaded as a blob string .
        Default is '', i.e. the object is loaded as a url.""",
    )
    representation = param.Selector(
        default="ball+stick",
        objects=REPRESENTATIONS,
        doc="""
        A display representation. Default is 'ball+stick'. See
        http://nglviewer.org/ngl/api/manual/coloring.html#representations
        """,
    )
    color_scheme = param.Selector(
        default="element",
        objects=COLOR_SCHEMES,
        doc="""
    A predefined or 'custom' color scheme. If 'custom' is specified you need to specify the
    'custom_color_scheme' parameter. Default is 'element'. See
    http://nglviewer.org/ngl/api/manual/coloring.html""",
    )
    custom_color_scheme = param.List(
        default=[["white", "*"]],
        doc="""
    A custom color scheme. See
    http://nglviewer.org/ngl/api/manual/coloring.html#custom-coloring.""",
    )
    effect = param.Selector(
        default="",
        objects=["", "spin", "rock"],
        doc="""
    One of '', 'spin' or 'rock'. Default is '', i.e. no effect""",
    )

    priority = None

    _updates = True

    _model_module = "panel_chemistry.bokeh_extensions.ngl_viewer"
    _model = "NGLViewer"

    @classmethod
    def applies(cls, obj):
        if isinstance(obj, (dict, str)):
            return 0
        return False

    def _get_model(self, doc, root=None, parent=None, comm=None):
        _NGLViewer = lazy_load(  # pylint: disable=invalid-name
            self._model_module, self._model, isinstance(comm, JupyterComm)
        )
        props = self._process_param_change(self._init_params())
        if not "object" in props:
            props["object"] = self.object
        model = _NGLViewer(**props)
        root = root or model
        self._models[root.ref["id"]] = (model, parent)
        return model

    def _update(self, ref=None, model=None):
        model.update(
            object=self.object,
            extension=self.extension,
            representation=self.representation,
            color_scheme=self.color_scheme,
            effect=self.effect,
            custom_color_scheme=self.custom_color_scheme,
        )
