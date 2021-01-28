"""
This module is a Sphinx extension that translates docstrings from Markdown (which TFGen emits) to reStructuredText,
which Sphinx expects. It accomplishes this using the "m2r" Python package, which seems to have been created exactly for
this purpose.
"""

import os
from m2r import convert


def setup(app):
    """
    setup is called by Sphinx on startup. It gives this extension the opportunity to inject itself into the normal
    Sphinx compilation pipeline.
    """
    app.add_config_value("markdown_docstring_convert", True, "html")

    # Autodoc fires this event whenever it processes a docstring - we're going to hook into it here in order to
    # translate docstrings as they come in.
    app.connect("autodoc-process-docstring", translate_docstring)


def translate_docstring(app, what, name, obj, options, lines):
    """
    Translates a docstring from Markdown (the default format, since we are generating Markdown docstrings) to
    reStructuredText, which is what the rest of Sphinx expects.

    See http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#event-autodoc-process-docstring for the full
    semantics of the arguments. The upshot is that `lines` must be modified in-place.
    """
    if not app.config.markdown_docstring_convert or not lines:
        return

    input_text = os.linesep.join(lines)
    output_text = convert(input_text)
    lines[:] = output_text.split(os.linesep)
