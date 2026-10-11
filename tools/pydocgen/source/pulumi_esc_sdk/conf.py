# -*- coding: utf-8 -*-
# Sphinx configuration for the Pulumi ESC (Python) SDK reference docs.
# See https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('../_shared'))

project = 'Pulumi ESC SDK'
copyright = '2026, Pulumi'
author = 'Pulumi'

try:
    version = _pkg_version('pulumi_esc_sdk')
    release = version
except PackageNotFoundError:
    version = release = 'unknown'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
    'seo_meta',
]

source_suffix = '.rst'
root_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = None

html_theme = 'sphinx_rtd_theme'
html_show_sourcelink = False
html_copy_source = False

# SEO/AEO: canonical URL (dirhtml + sphinx_rtd_theme render this correctly
# with a trailing slash and no ".html" -- verified in the reduced build
# harness), plus inputs for the shared seo_meta extension's per-page
# description, title, and APIReference JSON-LD.
html_baseurl = 'https://www.pulumi.com/docs/reference/pkg/python/pulumi_esc_sdk/'
templates_path = ['../_shared/templates']
seo_display_name = 'Pulumi ESC SDK'
seo_pypi_name = 'pulumi_esc_sdk'

autoclass_content = 'both'
autosummary_generate = True
