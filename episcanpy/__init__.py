# some technical stuff
import sys
from .utils import check_versions, annotate_doc_types
from ._version import get_versions  # version generated by versioneer

__author__ = ', '.join([
    'Anna Danese',
    'Maria Richter',
])
__email__ = ', '.join([
    'anna.danese@helmholtz-muenchen.de',
    # We don’t need all, the main authors are sufficient.
])
__version__ = get_versions()['version']

check_versions()
annotate_doc_types(sys.modules[__name__], 'episcanpy')
del get_versions, sys, check_versions, annotate_doc_types

# the actual API
# from . import tools as tl
# from . import preprocessing as pp
from . import plotting as pl
# from . import datasets, logging, queries, settings
from . import functions as fun

from anndata import AnnData
from anndata import read_h5ad, read_csv, read_excel, read_hdf, read_loom, read_mtx, read_text, read_umi_tools
#from .readwrite import read, read_10x_h5, read_10x_mtx
#from .neighbors import Neighbors
from .settings import set_figure_params
