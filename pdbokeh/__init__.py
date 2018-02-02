from __future__ import absolute_import

from bokeh.plotting import output_file, output_notebook, show

# Register the extension
from . import core
del core

__version__ = '0.0.1'
