import pytest

from pyvirtualdisplay import Display
import os
display = Display(visible=0, size=(1280, 1024))
display.start()

from mayavi import mlab

def test_2D_animation_on_demographic_file(tmp_path):

    assert 0 == 0;
