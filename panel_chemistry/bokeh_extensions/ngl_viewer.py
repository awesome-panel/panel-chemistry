"""A Bokeh Model of the NGLViewer"""
from bokeh.core.properties import List, String
from bokeh.models import LayoutDOM

class NGLViewer(LayoutDOM):
    """The [NGL Viewer](https://github.com/nglviewer/ngl) can be used
    to show and analyse pdb molecule structures"""

    object = String()
    extension = String()
    representation = String()
    color_scheme = String()
    effect = String()
    custom_color_scheme = List(List(String))

    __javascript__ = [
        "https://unpkg.com/ngl@2.0.0-dev.37/dist/ngl.js",
    ]
