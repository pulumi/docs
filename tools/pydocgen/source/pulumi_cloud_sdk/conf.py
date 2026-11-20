# -*- coding: utf-8 -*-
# Sphinx configuration for the Pulumi Cloud (Python) SDK reference docs.
# See https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('../_shared'))

project = 'Pulumi Cloud SDK'
copyright = '2026, Pulumi'
author = 'Pulumi'

try:
    version = _pkg_version('pulumi_cloud_sdk')
    release = version
except PackageNotFoundError:
    version = release = 'unknown'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
    'seo_meta',
    'per_symbol',
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
html_baseurl = 'https://www.pulumi.com/docs/reference/pkg/python/pulumi_cloud_sdk/'
templates_path = ['../_shared/templates']
seo_display_name = 'Pulumi Cloud SDK'
seo_pypi_name = 'pulumi_cloud_sdk'

autoclass_content = 'both'
autosummary_generate = True

# One page per API class and per top-level symbol; the 950+ field-list-only models are grouped by
# the API area that uses them (see cloud_sdk_groups.py and _shared/per_symbol.py).
per_symbol_modules = ['pulumi_cloud_sdk', 'pulumi_cloud_sdk.apis']
per_symbol_grouped_modules = {'pulumi_cloud_sdk.models': 'cloud_sdk_groups:group_models'}
per_symbol_undoc_members = ['pulumi_cloud_sdk', 'pulumi_cloud_sdk.apis']
per_symbol_honor_all = True
per_symbol_redirect_pages = ['index', 'apis', 'models']
