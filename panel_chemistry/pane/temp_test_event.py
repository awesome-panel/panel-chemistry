import panel as pn
from panel_chemistry.pane import PDBeMolStar
import numpy as np

# panel serve test_molstar.py --show --autoreload

# todo update molecule ID sets theme to black

if __name__.startswith("bokeh"):
    pn.extension(sizing_mode="stretch_width")

    parameters = [
        "theme",
        "molecule_id",
        "spin",
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

    #parameters = ['test']

    pdbe = PDBeMolStar(
        molecule_id="1qyn",
        # custom_data= { "url": "https://www.ebi.ac.uk/pdbe/coordinates/1cbs/chains?entityId=1&asymId=A&encoding=bcif", "format": "cif", "binary": True },
        # ligand_view={"label_comp_id": "REA"},
        alphafold_view=False,
        #min_height=500,
        theme='default',
        lighting='metallic',
        hide_expand_icon=False,
        # highlight_color='#d1fa07',
        # bg_color='#eeece7',
        # hide_canvas_controls=["selection", "animation", "controlToggle", "controlInfo"],
        # validation_annotation=True,
        domain_annotation=True,
        #hide_expand_icon=True,
        hide_selection_icon=True,
        hide_water=True,
        #visual_style="cartoon",  # , "ball-and-stick",
        # highlight_color="blue",
        #expanded=True,
        #sizing_mode="stretch_height",
    )

    buttons = []

    def color_residues_callback(event):
        pdbe.temp_color = not pdbe.temp_color

    btn = pn.widgets.Button(name='Test btn')
    btn.on_click(color_residues_callback)
    buttons.append(btn)


    tmpl = pn.template.FastGridTemplate(
        site="Panel Chemistry",
        title="Pdbe Molstar Viewer",
        sidebar=[*buttons, pn.Param(pdbe, parameters=parameters)],
        #main=[pdbe],
    )

    tmpl.main[0:3, 0:6] = pn.Row(pdbe, sizing_mode='stretch_both')
    tmpl.servable()


