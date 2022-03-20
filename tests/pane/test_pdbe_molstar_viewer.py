"""Tests of the PDBeMolStar Viewer"""
import panel as pn

from panel_chemistry.pane import PDBeMolStar


def test_can_create():
    """Test of the PDBeMolStar constructor"""
    PDBeMolStar(molecule_id="1qyn", lighting="metallic", height=300, width=300)


def test_functions():
    """
    Tests PDBeMolStar helper functions.

    This only tests if they do not raise any errors, and does not check for the
    desired result.

    """
    viewer = PDBeMolStar(molecule_id="1qyn", lighting="metallic", height=300, width=300)

    data = {
        'start_residue_number': 10,
        'end_residue_number': 30,
        'struct_asym_id': 'A',
        'color': {'r': 255, 'g': 215, 'b': 0},
        'focus': False,
    }

    viewer.color([data], non_selected_color={'r': 0, 'g': 87, 'b': 183})
    viewer.clear_selection()

    data = {
        'start_residue_number': 10,
        'end_residue_number': 20,
        'struct_asym_id': 'B',
        'color': {'r': 255, 'g': 105, 'b': 180},
        'focus': True,
    }

    viewer.highlight([data])
    viewer.clear_highlight()
    data = {
        'camera': True,
        'theme': True,  # reset theme doesnt seem to work
        'highlightcolor': True,
        'selectColor': True
    }
    viewer.reset(data)


def test_app():
    """Returns an app for manually testing the PDBe Mol* Viewer"""
    pn.extension(sizing_mode="stretch_width")
    # 1NKT, 2GQ5, 3UOG and 5TXH
    viewer = PDBeMolStar(molecule_id="1qyn", lighting="metallic", height=1000, sizing_mode="stretch_width")
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
    settings = pn.Param(viewer, parameters=parameters,)
    return pn.Row(pn.WidgetBox(settings, width=300, sizing_mode="fixed"), viewer)


if __name__.startswith("bokeh"):
    test_app().servable()
