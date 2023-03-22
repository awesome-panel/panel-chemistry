from panel_chemistry.pane import MolStarViewer
import param
import panel as pn


def test_can_create():
    """Test of the MolStarViewer constructor"""
    MolStarViewer(pdb="1qyn", height=300, width=300)
    MolStarViewer(emdb=('EMD-30210', {'detail': 6}), height=300, width=300)
    MolStarViewer(alphafold_db="L8XZM1", height=300, width=300)



def test_app():
    """Returns an app for manually testing the Mol* Viewer"""

    MOLSTAR_KWARGS = dict(width=1000, height=600)


    class MolStarApp(param.Parameterized):

        database = param.Selector(default='PDB', objects=['PDB', 'EMDB', 'Alphafold'])

        pdb_id = param.String(default=None, doc="PDB ID to load", label="PDB ID")

        emdb_id = param.String(default=None, doc="EMDB ID to load", label="EMDB ID")

        emdb_detail = param.Selector(default=6, objects=list(range(1, 12)))

        alphafold_id = param.String(default=None, doc="Alphafold ID to load", label="Alphafold ID")

        layout_is_expanded = param.Boolean(default=False, doc="Expand the layout")

        layout_show_controls = param.Boolean(default=False, doc="Show the controls")

        layout_show_remote_state = param.Boolean(default=False, doc="Show the remote state")

        layout_show_sequence = param.Boolean(default=True, doc="Show the sequence")

        layout_show_log = param.Boolean(default=True, doc="Show the log")

        layout_show_left_panel = param.Boolean(default=True, doc="Show the left panel")

        viewport_show_expand = param.Boolean(default=True, doc='Show the expand button')

        viewport_show_selection_mode = param.Boolean(default=False, doc='Show the selection mode')

        viewport_show_animation = param.Boolean(default=False)

        rerender = param.Action(lambda self: self._action_rerender())

        def __init__(self, **params):
            super().__init__(**params)
            self.widgets = pn.Param(self, show_name=False)._widgets

            self.controls = pn.Column(*self.control_widgets, width=250)
            self.molstar = pn.Column(MolStarViewer(**MOLSTAR_KWARGS))
            self.app = pn.Row(
                self.controls, self.molstar
            )

        @property
        def control_widgets(self):
            excluded = {'pdb_id', 'emdb_id', 'emdb_detail', 'alphafold_id'}
            if self.database == 'PDB':
                excluded -= {'pdb_id'}
            elif self.database == 'EMDB':
                excluded -= {'emdb_id', 'emdb_detail'}
            elif self.database == 'Alphafold':
                excluded -= {'alphafold_id'}

            return [w for k, w in self.widgets.items() if k not in excluded]

        @param.depends('database', watch=True)
        def _on_database_change(self):
            self.controls[:] = self.control_widgets

        def _action_rerender(self):
            ms = self.molstar[0]
            params = {p for p in ms.param}
            options = params & self.widgets.keys()

            kwargs = {opt: getattr(self, opt) for opt in options}

            if self.database == 'PDB':
                kwargs['pdb'] = self.pdb_id
            elif self.database == 'EMDB':
                kwargs['emdb'] = (self.emdb_id, {'detail': self.emdb_detail})
            elif self.database == 'Alphafold':
                kwargs['alphafold_db'] = self.alphafold_id

            viewer = MolStarViewer(**kwargs, **MOLSTAR_KWARGS)
            self.molstar[:] = [viewer]


    molstar = MolStarApp()

    return molstar


if __name__.startswith("bokeh"):
    test_app().app.servable()