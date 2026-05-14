# -*- coding: utf-8 -*-
# Sphinx configuration for the Pulumi Policy (Python) SDK reference docs.
# See https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version

sys.path.append(os.path.abspath('.'))

project = 'Pulumi Policy SDK'
copyright = 'Pulumi'
author = 'Pulumi'

try:
    version = _pkg_version('pulumi_policy')
    release = version
except PackageNotFoundError:
    version = release = 'unknown'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
]

source_suffix = '.rst'
root_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = None

html_theme = 'sphinx_rtd_theme'
html_show_sourcelink = False
html_copy_source = False

autoclass_content = 'both'
autosummary_generate = True
