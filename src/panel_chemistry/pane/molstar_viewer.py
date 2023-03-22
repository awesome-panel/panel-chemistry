import param
from panel.reactive import ReactiveHTML


class MolStarViewer(ReactiveHTML):
    """
    Molstar Viewer app.

    This pane implements the Mol* viewer plugin.

    Using and navigating the viewer:
    https://molstar.org/viewer-docs/

    More information on Molstar:
    https://molstar.org/

    Additional info on implementing the plugin:
    https://molstar.org/docs/plugin/

    More information on the API and usage:
    https://github.com/molstar/molstar/blob/master/src/apps/viewer/app.ts

    """

    __javascript__ = [
        "https://cdn.jsdelivr.net/npm/molstar@3.31.4/build/viewer/molstar.js",
    ]

    __css__ = [
        'https://cdn.jsdelivr.net/npm/molstar@3.31.4/build/viewer/molstar.css'
    ]

    highlight = param.Event()

    test = param.Event()

    pdb = param.String(default=None, doc="PDB ID to load")

    emdb = param.Tuple(default=None, doc="EMDB ID to load", length=2)

    alphafold_db = param.String(default=None, doc="Alphafold DB ID to load")

    layout_is_expanded = param.Boolean(default=False, doc="Expand the layout")

    layout_show_controls = param.Boolean(default=False, doc="Show the controls")

    layout_show_remote_state = param.Boolean(default=False, doc="Show the remote state")

    layout_show_sequence = param.Boolean(default=True, doc="Show the sequence")

    layout_show_log = param.Boolean(default=True, doc="Show the log")

    layout_show_left_panel = param.Boolean(default=True, doc="Show the left panel")

    viewport_show_expand = param.Boolean(default=True, doc='Show the expand button')

    viewport_show_selection_mode = param.Boolean(default=False, doc='Show the selection mode')

    viewport_show_animation = param.Boolean(default=False)

    pdb_provider = param.String(default='rcsb', doc='PDB provider')

    emdb_provider = param.String(default='rcsb', doc='EMDB provider')

    _template = """
    <div id="container" style="width:100%; height: 100%;"><div id="MolstarViewer"></div></div>
    """

    _scripts = {
        'render': """
            molstar.Viewer.create(MolstarViewer, {
                layoutIsExpanded: data.layout_is_expanded,
                layoutShowControls: data.layout_show_controls,
                layoutShowRemoteState: data.layout_show_remote_state,
                layoutShowSequence: data.layout_show_sequence,
                layoutShowLog: data.layout_show_log,
                layoutShowLeftPanel: data.layout_show_left_panel,

                viewportShowExpand: data.viewport_show_expand,
                viewportShowSelectionMode: data.viewport_show_selection_mode,
                viewportShowAnimation: data.viewport_show_animation,

                pdbProvider: data.pdb_provider,
                emdbProvider: data.emdb_provider,
            }).then(viewer => {
        state._viewer = viewer;
        if (data.pdb) {
            viewer.loadPdb('1qyn')
        }
        if (data.emdb) {
            viewer.loadEmdb(data.emdb[0], data.emdb[1])
        }
        if (data.alphafold_db) {
            viewer.loadAlphaFoldDb(data.alphafold_db)
        }
          });
           
        """,
        'pdb': """
            state._viewer.loadPdb(data.pdb);
        """,
        'emdb':"""
            state._viewer.loadEmdb(data.emdb[0], data.emdb[1]);
        """,
        'alphafold_db':"""
            state._viewer.loadAlphaFoldDb(data.alphafold_db);
        """,

        'test': """
            console.log('testing');
            console.log(data.pdb);
            console.log(state._viewer);
            state._viewer
        """,

    }