"""A Bokeh Model of the NGLViewer"""
from bokeh.core.properties import List, String
from bokeh.models import LayoutDOM


class NGLViewer(LayoutDOM):  # pylint: disable=too-many-ancestors
    """The [NGL Viewer](https://github.com/nglviewer/ngl) can be used
    to show and analyse pdb molecule structures"""

    object = String("")
    extension = String("")
    background_color = String("")
    representation = String("ball+stick")
    color_scheme = String("element")
    custom_color_scheme = List(List(String))
    effect = String("")

    __javascript__ = [
        "https://unpkg.com/ngl@2.2.1/dist/ngl.js",
    ]

    __js_skip__ = {
        "NGL": __javascript__[:1],
    }

    __js_require__ = {
        "paths": {
            "NGL": "https://unpkg.com/ngl@2.2.1/dist/ngl",
        },
        "exports": {"NGL": "NGL"},
    }
