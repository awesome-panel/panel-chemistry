"""The [NGL Viewer](https://github.com/nglviewer/ngl) can be used
to visualize and analyse pdb molecule structures.

Source: Discussion on [Discourse 583]\
(https://discourse.holoviz.org/t/how-to-use-ngl-webgl-protein-viewer-in-panel/583)

Author: https://github.com/Jhsmit
"""

from typing import Dict

import param
from panel.pane.base import PaneBase
from panel.util import lazy_load, string_types
from pyviz_comms import JupyterComm

REPRESENTATIONS = [
    "ball+stick",
    "backbone",
    "ball+stick",
    "cartoon",
    "hyperball",
    "licorice",
    "ribbon",
    "rope",
    "spacefill",
    "surface",
]
COLOR_SCHEMES = ["chainid", "residueindex", "chainname"]


class NGLViewer(PaneBase):
    """The [NGL Viewer](https://github.com/nglviewer/ngl) can be used
    to show and analyse pdb molecule structures"""

    object = param.String()
    object_format = param.ObjectSelector(default="rcsb", objects=["rcsb", "pdb_string"])
    representation = param.Selector(
        default="ribbon",
        objects=REPRESENTATIONS,
    )
    color_scheme = param.Selector(default="chainid", objects=COLOR_SCHEMES)
    spin = param.Boolean(default=False)
    # color_list = param.List(default=[["white", "*"]])
    # event = param.Dict()

    priority = None

    _rename: Dict[str, str] = {}

    _updates = True

    _model_module = "panel_chemistry.bokeh_extensions.ngl_viewer"
    _model = "NGLViewer"

    @classmethod
    def applies(cls, obj):
        if isinstance(obj, (dict, string_types)):
            return 0
        return False

    def _get_model(self, doc, root=None, parent=None, comm=None):
        _NGLViewer = lazy_load(  # pylint: disable=invalid-name
            self._model_module, self._model, isinstance(comm, JupyterComm)
        )
        props = self._process_param_change(self._init_params())
        print("get_model", props)
        model = _NGLViewer(**props)
        root = root or model
        # self._link_props(
        #     model,
        #     [
        #         "event",
        #     ],
        #     doc,
        #     root,
        #     comm,
        # )
        self._models[root.ref["id"]] = (model, parent)
        return model

    def _update(self, ref=None, model=None):
        print("update", model)
        model.update(
            object=self.object,
            object_format=self.object_format,
            representation=self.representation,
            color_scheme=self.color_scheme,
            spin=self.spin,
            # color_list=self.color_list,
        )
