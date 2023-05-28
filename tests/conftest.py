"""Shared fixtures"""
import pytest
from bokeh.document import Document
from pyviz_comms import Comm


@pytest.fixture
def document():
    """A Bokeh Document"""
    return Document()


@pytest.fixture
def comm():
    """The pyviz communications"""
    return Comm()
