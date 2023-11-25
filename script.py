import panel as pn 
from panel_chemistry.pane import NGLViewer # panel_chemistry needs to be imported before you run pn.extension()
from panel_chemistry.pane.ngl_viewer import EXTENSIONS

pn.extension("ngl_viewer", sizing_mode="stretch_width")

viewer = NGLViewer(object="1CRN", background_color="#F7F7F7", styles={"border": "1px solid lightgray"}, min_height=700, sizing_mode="stretch_both")

settings = pn.Param(
    viewer,
    parameters=["object","extension","representation","color_scheme","custom_color_scheme","effect",],
    name="&#9881;&#65039; Settings"
)

file_input = pn.widgets.FileInput(accept=','.join('.' + s for s in EXTENSIONS[1:]))

def filename_callback(target, event):
    target.extension = event.new.split('.')[1]

def value_callback(target, event):
    target.object = event.new.decode('utf-8')

file_input.link(viewer, callbacks={'value': value_callback, 'filename': filename_callback})

header = pn.widgets.StaticText(value='<b>{0}</b>'.format("&#128190; File Input"))
file_column = pn.layout.Column(header, file_input)

layout = pn.Param(
    viewer,
    parameters=["sizing_mode", "width", "height", "background_color"],
    name="&#128208; Layout"
)

pn.Row(
    viewer,
    pn.WidgetBox(settings, layout, width=300, sizing_mode="fixed",),
)


accent="#D2386C"

pn.template.FastListTemplate(
    site="Panel Chemistry", site_url="./",
    title="NGLViewer", 
    sidebar=[file_column, settings, layout],
    main=[viewer],
    accent_base_color=accent, header_background=accent,
).servable();

