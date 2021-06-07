"""A Bokeh Model of the NGLViewer"""
from bokeh.core.properties import Bool, String
from bokeh.models import LayoutDOM


class NGLViewer(LayoutDOM):
    """The [NGL Viewer](https://github.com/nglviewer/ngl) can be used
    to show and analyse pdb molecule structures"""

    object = String()
    object_format = String()
    representation = String()
    color_scheme = String()
    spin = Bool()
    # color_list = List(String())

    __javascript__ = [
        "https://unpkg.com/ngl@2.0.0-dev.37/dist/ngl.js",
    ]
