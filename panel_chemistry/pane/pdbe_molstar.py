"""A Panel Pane to wrap the PDBe implementation of the Mol* ('MolStar') viewer.

    The PBBe viewer is available both as a webcomponent or interactive plugin.

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

import param
from panel.reactive import ReactiveHTML
from panel.pane import HTML
import panel as pn
from pathlib import Path
from string import Template


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


class PdbeMolStarWebComponent(HTML):
    """Web component implementation of the PDBe MolStar structure viewer.
    
    For more information:
    https://github.com/PDBeurope/pdbe-molstar/wiki
    
    This is an implementation of the Molstar viewer: https://molstar.org/
    
    """

    molecule_id = param.String(
        default=None,
        doc="PDB id to load"
    )
    
    custom_data_url = param.String(
        default=None,
        doc="Data url for loading custom data. Incompatible with `molecule_id`"
    )

    custom_data_binary = param.Boolean(
        default=None)

    custom_data_format = param.String(
        default=None,
        doc="Format for custom data, for example 'cif'"
    )

    ligand_label_comp_id = param.String(
        default=None,
        doc=""
    )

    ligand_auth_asym_Id = param.String(
        default=None,
    )

    ligand_auth_seq_id = param.Number(
        default=None,
    )

    ligand_hydrogens = param.Boolean(
        default=None
    )

    alphafold_view = param.Boolean(
        default=None,
        doc="Applies AlphaFold confidence score colouring theme for alphafold model"
    )

    assembly_id = param.Number(
        default=None,
        doc="Specify assembly"
    )

    bg_color = param.Color(
        default=None,
        allow_named=False,
        doc="Color of the background. If `None`, colors default is chosen depending on the color theme"
    )

    highlight_color = param.Color(
        default=None,
        allow_named=False,
        doc='Color for mouseover highlighting'
    )

    select_color = param.Color(
        default=None,
        allow_named=False, 
        doc='Color for selections'
    )

    visual_style = param.Selector(
        default=None,
        objects=[None] + REPRESENTATIONS,
        doc="Visual styling"
    )

    theme = param.Selector(
        default='dark',
        objects=['light', 'dark'],
        doc="CSS theme to use"
    )

    hide_polymer = param.Boolean(
        default=None,
        doc="Hide polymer"
    )

    hide_water = param.Boolean(
        default=None,
        doc="Hide water"
    )

    hide_het = param.Boolean(
        default=None, 
        doc="Hide het"
    )

    hide_carbs = param.Boolean(
        default=None,
        doc="Hide carbs"
    )

    hide_non_standard = param.Boolean(
        default=None,
        doc="Hide non standard"
    )

    hide_coarse = param.Boolean(
        default=None,
        doc="Hide coarse"
    )

    pdbe_url = param.String(
        default=None,
        doc="Url for PDB data. Mostly used for internal testing"
    )

    load_maps = param.Boolean(
        default=None,
        doc="Load electron density maps from the pdb volume server"
    )

    validation_annotation = param.Boolean(
        default=None,
        doc="Adds 'annotation' control in the menu"
    )

    domain_annotations = param.Boolean(
        default=None,
        doc="Adds 'annotation' control in the menu"
    )

    low_precision = param.Boolean(
        default=None,
        doc="Load low precision coordinates from the model server"
    )

    expanded = param.Boolean(
        default=None,
        doc="Display full-screen by default on load"
    )

    hide_controls = param.Boolean(
        default=True,
        doc="Hide the control menu"
    )

    landscape = param.Boolean(
        default=None
    )

    select_interaction = param.Boolean(
        default=None, 
        doc="Switch on or off the default selection interaction behaviour"
    )

    lighting = param.Selector(
        default='matte',
        objects=['flat', 'matte', 'glossy', 'metallic', 'plastic'],
        doc="Set the lighting"
    )

    default_preset = param.Selector(
        default='default',
        objects=['default', 'unitcell', 'all-models', 'supercell'],
        doc="Set the preset view"
    )

    pdbe_link = param.Selector(
        default=None,
        doc="Show the PDBe entry link at in the top right corner"
    )

    hide_expand_icon = param.Boolean(
        default=None,
        doc="Hide the expand icon"
    )
    
    hide_selection_icon = param.Boolean(
        default=None, # Default False, set False/True for True
        doc="Hide the selection icon"
    )

    hide_animation_icon = param.Boolean(
        default=None,
        doc="Hide the animation icon"
    )


    def __init__(self, **params):
        super().__init__(**params)

        skip = {
            'theme', 
            'name',
            'bg_color'
        }

        # Find class attributes defined only on this subclass
        attrs = self.__class__.__dict__.keys() - HTML.__class__.__dict__.keys() - skip
        attrs = [a for a in attrs if not a.startswith('_')]

        elements = []
        for attr in attrs:
            val = getattr(self, attr)
            if val is None:
                continue
            elif isinstance(val, bool):
                val = 'true' if val else 'false'
            else:
                val = f'"{val}"'
            
            name = attr.replace('_', '-')
            elem = f'{name}={val}'
            elements.append(elem)
        
        
        bg_default = 'F7F7F7' if self.theme == 'light' else '000000'
        self.bg_color = self.bg_color or bg_default

        # Split color options into rgb components
        color_options = ['bg_color', 'highlight_color', 'select_color']
        for option in color_options:
            hex_val = getattr(self, option)
            if hex_val is None:
                continue
            hex_val = hex_val.lstrip('#')
            name = option.replace('_', '-')
            for i, c in enumerate(['r', 'g', 'b']):
                val = int(hex_val[2*i:2*i+2], 16)
                elem = f'{name}-{c}="{val}"'
                elements.append(elem)

        component_spec = ' '.join(elements)
        
        theme = '-light' if self.theme == 'light' else ''
        html_string = (Path(__file__).parent / 'molstar_webcomponent.html').read_text()
        html_template = Template(html_string)

        self.object = html_template.substitute(
            component_spec=component_spec,
            theme=theme
        )
