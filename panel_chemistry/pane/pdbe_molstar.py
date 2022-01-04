"""A Panel Pane to wrap the PDBe implementation of the Mol* ('MolStar') viewer.

Check out

- [PDBe Mol*](https://github.com/PDBeurope/pdbe-molstar)
- [Mol*](https://molstar.org/)
- [Mol* GitHub](https://github.com/molstar/molstar)

Cite Mol*:
David Sehnal, Sebastian Bittrich, Mandar Deshpande, Radka Svobodová, Karel Berka,
Václav Bazgier, Sameer Velankar, Stephen K Burley, Jaroslav Koča, Alexander S Rose:
Mol* Viewer: modern web app for 3D visualization and analysis of large biomolecular structures,
Nucleic Acids Research, 2021; https://doi.org/10.1093/nar/gkab314.
"""

import panel as pn
import param
from panel.reactive import ReactiveHTML

REPRESENTATIONS = [
    "cartoon",
    "ball-and-stick",
    "carbohydrate",
    "distance-restraint",
    "ellipsoid",
    "gaussian-surface",
    "molecular-surface",
    "point",
    "putty",
    "spacefill",
]

# See https://embed.plnkr.co/plunk/m3GxFYx9cBjIanBp for an example JS implementation
class PdbeMolStar(ReactiveHTML):
    """PDBe MolStar structure viewer.

    Set one of `molecule_id`, `custom_data` and `ligand_view`.

    For more information:

    - https://github.com/PDBeurope/pdbe-molstar/wiki
    - https://molstar.org/

    The implementation is based on the js Plugin. See

    - https://github.com/PDBeurope/pdbe-molstar/wiki/1.-PDBe-Molstar-as-JS-plugin

    """

    molecule_id = param.String(default=None, doc="PDB id to load. Example: '1qyn' or '1cbs'")
    custom_data = param.Dict(
        doc="""Load data from a specific data source. Example: 
        { "url": "https://www.ebi.ac.uk/pdbe/coordinates/1cbs/chains?entityId=1&asymId=A&encoding=bcif", "format": "cif", "binary": True }
        """
    )
    ligand_view = param.Dict(
        doc="""This option can be used to display the PDBe ligand page 3D view like https://www.ebi.ac.uk/pdbe/entry/pdb/1cbs/bound/REA.
        Example: {"label_comp_id": "REA"}
        """
    )

    alphafold_view = param.Boolean(
        default=False, doc="Applies AlphaFold confidence score colouring theme for alphafold model"
    )

    assembly_id = param.String(doc="Specify assembly")

    # Todo: figure out if `background` could/ should be used
    bg_color = param.Color(
        '#F7F7F7',
        doc="Color of the background. If `None`, colors default is chosen depending on the color theme",
    )

    highlight_color = param.Color(default="#ff6699", doc="Color for mouseover highlighting")

    select_color = param.Color(default="#0c0d11", doc="Color for selections")

    visual_style = param.Selector(default=None, 
            objects=[None] + REPRESENTATIONS, doc="Visual styling")

    # Todo: Determine if it should be default or light theme
    theme = param.Selector(default="default", objects=["default", "dark"], doc="CSS theme to use")

    hide_polymer = param.Boolean(
        default=False,
        doc="Hide polymer"
    )

    hide_water = param.Boolean(
        default=False,
        doc="Hide water"
    )

    hide_heteroatoms = param.Boolean(
        default=False, 
        doc="Hide het"
    )

    hide_carbs = param.Boolean(
        default=False,
        doc="Hide carbs"
    )

    hide_non_standard = param.Boolean(
        default=False,
        doc="Hide non standard"
    )

    hide_coarse = param.Boolean(
        default=False,
        doc="Hide coarse"
    )

    hide_controls_icon = param.Boolean(default=False, doc="Hide the control menu")

    hide_expand_icon = param.Boolean(
        default=False,
        doc="Hide the expand icon"
    )
    
    hide_settings_icon = param.Boolean(default=False, doc="Hide the settings menu")
    
    hide_selection_icon = param.Boolean(
        default=False, # Default False, set False/True for True
        doc="Hide the selection icon"
    )

    # Todo requires testing with a trajectory file
    hide_animation_icon = param.Boolean(
        default=False,
        doc="Hide the animation icon"
    )
   
    pdbe_url = param.String(
        default=None, constant=True, doc="Url for PDB data. Mostly used for internal testing"
    )

    load_maps = param.Boolean(
        default=False, doc="Load electron density maps from the pdb volume server"
    )

    validation_annotation = param.Boolean(
        default=False, doc="Adds 'annotation' control in the menu"
    )

    domain_annotation = param.Boolean(default=False, doc="Adds 'annotation' control in the menu")

    low_precision_coords = param.Boolean(
        default=False, doc="Load low precision coordinates from the model server"
    )

    hide_controls = param.Boolean(default=True, doc="Hide the control menu")

    expanded = param.Boolean(default=False, doc="""Display full-screen by default on load""")

    landscape = param.Boolean(
        default=True,  # Changed to True because it works best with Panel currently
        doc="""Set landscape view. The controls will similar to the full-screen view""",
    )

    select_interaction = param.Boolean(
        default=True, doc="Switch on or off the default selection interaction behaviour"
    )

    lighting = param.Selector(
        default="matte",
        objects=["flat", "matte", "glossy", "metallic", "plastic"],
        doc="Set the lighting",
    )

    default_preset = param.Selector(
        default="default",
        objects=["default", "unitcell", "all-models", "supercell"],
        doc="Set the preset view",
    )

    pdbe_link = param.Boolean(
        default=True, doc="Show the PDBe entry link at in the top right corner"
    )

    _template = """
<link id="molstarTheme" rel="stylesheet" type="text/css" href="https://www.ebi.ac.uk/pdbe/pdb-component-library/css/pdbe-molstar-1.2.0.css"/>
<div id="container" style="width:100%; height: 100%;"><div id="pdbeViewer"></div></div>
"""
    __javascript__ = [
        "https://www.ebi.ac.uk/pdbe/pdb-component-library/js/pdbe-molstar-plugin-1.2.0.js",
    ]

    _scripts = {
        "render": """
function standardize_color(str){
    var ctx = document.createElement("canvas").getContext("2d");
    ctx.fillStyle = str;
    return ctx.fillStyle;
}
function toRgb(color) {
  var hex = standardize_color(color)
  var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result ? {
    r: parseInt(result[1], 16),
    g: parseInt(result[2], 16),
    b: parseInt(result[3], 16)
  } : null;
}
state.toRgb = toRgb

function getHideStructure(){
    var hideStructure = [];

    if (data.hide_polymer){
        hideStructure.push("polymer")
    }
    if (data.hide_water){
        hideStructure.push("water")
    }
    if (data.hide_heteroatoms){
        hideStructure.push("het")
    }
    if (data.hide_carbs){
        hideStructure.push("carbs")
    }
    if (data.hide_non_standard){
        hideStructure.push("nonStandard")
    }
    if (data.hide_coarse){
        hideStructure.push("coarse")
    }

    return hideStructure
}

function getHideCanvasControls(){
    var hideCanvasControls = [];
    if (data.hide_controls_icon){
        hideCanvasControls.push("controlToggle")
    }
    if (data.hide_expand_icon){
        hideCanvasControls.push("expand")
    }
    if (data.hide_settings_icon){
        hideCanvasControls.push("controlInfo")
    }
    if (data.hide_selection_icon){
        hideCanvasControls.push('selection')
    }
    if (data.hide_animation_icon){
        hideCanvasControls.push("animation")
    }

    return hideCanvasControls
}

state.getHideCanvasControls = getHideCanvasControls

function getOptions(){
    var options = {
        moleculeId: data.molecule_id,
        customData: data.custom_data,
        ligandView: data.ligand_view,
        alphafoldView: data.alphafold_view,
        assemblyId: data.assembly_id,
        bgColor: toRgb(data.bg_color),
        highlightColor: toRgb(data.highlight_color),
        selectColor: toRgb(data.select_color),
        hideStructure: getHideStructure(),
        hideCanvasControls: getHideCanvasControls(),
        loadMaps: data.load_maps,
        validationAnnotation: data.validation_annotation,
        domainAnnotation: data.domain_annotation,
        lowPrecisionCoords: data.low_precision_coords,
        expanded: data.expanded,
        hideControls: data.hide_controls,
        landscape: data.landscape,
        selectInteraction: data.select_interaction,
        lighting: data.lighting,
        defaultPreset: data.default_preset,
        pdbeLink: data.pdbe_link,
    }
    console.log(data.visual_style)
    if (data.visual_style!==null){
        options["visualStyle"]=data.visual_style
    }
    if (data.pdbe_url!==null){
        options["pdbeUrl"]=data.pdbe_url
    }
    console.log(options)
    return options
}
state.getOptions=getOptions
console.log('hoidoei')
self.theme()

state.viewerInstance = new PDBeMolstarPlugin();
state.viewerInstance.render(pdbeViewer, state.getOptions());    
""",
        "rerender": """
state.viewerInstance.visual.update(state.getOptions(), fullLoad=true)
console.log("rerender")
""",
        "molecule_id": "state.viewerInstance.visual.update({moleculeId:data.molecule_id})",
        "custom_data": "state.viewerInstance.visual.update({customData:data.custom_data})",
        "ligand_view": "state.viewerInstance.visual.update({ligandView:data.ligand_view})",
        "alphafold_view": "state.viewerInstance.visual.update({alphafoldView:data.alphafold_view})",
        "assembly_id": "state.viewerInstance.visual.update({assembly_id:data.assembly_id})",
        "visual_style": "self.rerender()",
        "bg_color": "state.viewerInstance.canvas.setBgColor(state.toRgb(data.bg_color))",
        "highlight_color": "state.viewerInstance.visual.setColor({highlight: state.toRgb(data.highlight_color)})",
        "select_color": "state.viewerInstance.visual.setColor({select: state.toRgb(data.select_color)})",
        "theme": """
if (data.theme==="dark"){
    molstarTheme.href="https://www.ebi.ac.uk/pdbe/pdb-component-library/css/pdbe-molstar-1.2.0.css"
} else {
    molstarTheme.href="https://www.ebi.ac.uk/pdbe/pdb-component-library/css/pdbe-molstar-light-1.2.0.css"
}
""",
        "hide_polymer": "state.viewerInstance.visual.visibility({polymer:!data.hide_polymer})",
        "hide_water": "state.viewerInstance.visual.visibility({water:!data.hide_water})",
        "hide_heteroatoms": "state.viewerInstance.visual.visibility({het:!data.hide_heteroatoms})",
        "hide_carbs": "state.viewerInstance.visual.visibility({carbs:!data.hide_carbs})",
        "hide_non_standard": "state.viewerInstance.visual.visibility({nonStandard:!data.hide_non_standard})",
        "hide_coarse": "state.viewerInstance.visual.visibility({coarse:!data.hide_coarse})",
        "hide_controls_icon": """self.rerender()""",  #Todo: I dont think .update() looks as hideCanvasControls
        "hide_expand_icon": """self.rerender()""",  #Todo expand can be turned of but not updated on rerender
        "hide_settings_icon": """self.rerender()""",
        "hide_selection_icon": """self.rerender()""",
        "hide_animation_icon": """self.rerender()""",
        "load_maps": "self.rerender()",
        "validation_annotation": "self.rerender()",
        "domain_annotation": "self.rerender()",
        "low_precision_coords": "self.rerender()",
        "expanded": "state.viewerInstance.canvas.toggleExpanded(data.expanded)",
        "landscape": "self.rerender()",
        "select_interaction": "self.rerender()",
        "lighting": "self.rerender()",
        "default_preset": "self.rerender()",
        "pdbe_link": "self.rerender()",
        "hide_controls": "state.viewerInstance.canvas.toggleControls(!data.hide_controls);" "",
    }



    def __init__(self, **params):
        super().__init__(**params)
    	
if __name__.startswith("bokeh"):
    pn.extension(sizing_mode="stretch_width")

    parameters = [
        "theme",
        "molecule_id",
        "custom_data",
        "ligand_view",
        "alphafold_view",
        "assembly_id",
        "visual_style",
        "bg_color",
        "highlight_color",
        "select_color",
        "hide_controls_icon",
        "hide_expand_icon",
        "hide_settings_icon", 
        "hide_selection_icon",
        "hide_animation_icon", 
        "hide_polymer",
        "hide_water",
        "hide_heteroatoms",
        "hide_carbs", 
        "hide_non_standard",
        "hide_coarse",
        "load_maps",
        "validation_annotation",
        "domain_annotation",
        "low_precision_coords",
        "expanded",
        "hide_controls",
        "landscape",
        "select_interaction",
        "lighting",
        "default_preset",
        "pdbe_link",
        "pdbe_url",
        "sizing_mode",
        "height",
        "width",
    ]

    pdbe = PdbeMolStar(
        molecule_id="1qyn",
        # custom_data= { "url": "https://www.ebi.ac.uk/pdbe/coordinates/1cbs/chains?entityId=1&asymId=A&encoding=bcif", "format": "cif", "binary": True },
        # ligand_view={"label_comp_id": "REA"},
        alphafold_view=False,
        min_height=500,
        theme='default',
        # lighting='metallic',
        # hide_expand_icon=True,
        # highlight_color='#d1fa07',
        # bg_color='#eeece7',
        # hide_canvas_controls=["selection", "animation", "controlToggle", "controlInfo"],
        # validation_annotation=True,
        domain_annotation=True,
        hide_expand_icon=True,
        hide_selection_icon=True,
        #visual_style="cartoon",  # , "ball-and-stick",
        # highlight_color="blue",
        #expanded=True,
        sizing_mode="stretch_both",
    )
    pn.template.FastListTemplate(
        site="Panel Chemistry",
        title="Pdbe Molstar Viewer",
        sidebar=[pn.Param(pdbe, parameters=parameters)],
        main=[pdbe],
    ).servable()
