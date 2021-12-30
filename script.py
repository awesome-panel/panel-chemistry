import panel as pn
import py3Dmol

p = py3Dmol.view(query="mmtf:1ycr")
p.setStyle({"cartoon": {"color": "spectrum"}})

from panel_chemistry.pane import Py3DMol

viewer = Py3DMol(p, height=200, width=200, sizing_mode="stretch_both")

pn.Row(viewer, viewer.layout.controls()).servable()
