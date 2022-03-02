"""A Panel Pane to wrap the interactive py3Dmol/ 3Dmol.js viewer in your Panel Application.

    Check out

    - [3DMol.js](https://3dmol.org/index.html)
    - [Colab](https://colab.research.google.com/drive/1T2zR59TXyWRcNxRgOAiqVPJWhep83NV_?usp=sharing)
    """

import panel as pn
import param

try:
    import py3Dmol
except ModuleNotFoundError:
    class py3Dmol(param.Parameterized):  # type: ignore
        view = param.String('mock_view')  # allow to import the file


def _clean_html(html):
    """Returns the py3Dmol.view._make_html with 100% height and width"""
    start = html.find("width:")
    end = html.find('px">') + 2
    size_str = html[start:end]
    html = html.replace(size_str, "width: 100%; height: 100%")

    return html


class Py3DMol(pn.viewable.Viewer):
    """A Panel Pane to wrap the interactive py3Dmol/ 3Dmol.js viewer in your Panel Application.

    Check out

    - [3DMol.js](https://3dmol.org/index.html)
    - [Colab](https://colab.research.google.com/drive/1T2zR59TXyWRcNxRgOAiqVPJWhep83NV_?usp=sharing)
    """

    object: py3Dmol.view = param.ClassSelector(
        class_=py3Dmol.view,
        doc="""
    A py3Dmol.view
    """,
    )

    layout = param.ClassSelector(
        class_=pn.pane.HTML,
        constant=True,
        doc="""
    A HTML pane containing the py3Dmol.view html. You can apply all the usual layout parameters to
    this layout.
    """,
    )

    def __init__(self, object: py3Dmol.view = None, **params): # pylint: disable=redefined-builtin
        """A Panel Pane to wrap the interactive py3Dmol/ 3Dmol.js viewer in your Panel Application.

        Check out

        - [3DMol.js](https://3dmol.org/index.html)
        - [Colab]\
(https://colab.research.google.com/drive/1T2zR59TXyWRcNxRgOAiqVPJWhep83NV_?usp=sharing)

        Args:
            object (py3Dmol.view, optional): A py3Dmol.view. Defaults to None.
            params (): These parameters are applied to the layout. Could be height, width etc.
        """
        super().__init__(object=object, layout=pn.pane.HTML(**params))
        if "name" in params:
            with param.edit_constant(self):
                self.name = params["name"]
        self._update_name()
        self._update_layout()

    @pn.depends("name", watch=True)
    def _update_name(self):
        with param.edit_constant(self.layout):
            self.layout.name = self.name

    @pn.depends("object", watch=True)
    def _update_layout(self):
        if self.object:
            # pylint: disable=no-member, protected-access
            self.layout.object = _clean_html(self.object._make_html())
        else:
            self.layout.object = ""

    def __panel__(self):
        return self.layout
