# .vscode

This directory contains files to make authoring Pulumi docs changes easier in VSCode:

* `markdown.code-snippets` contains VSCode snippets for the more common shortcodes used in the Pulumi Hugo site.
* `settings.json` contains project-wide VSCode settings that should be followed by all users:
  * Formatting Markdown file on save is disabled because our current Markdown standards are not followed by the Format on Save command. We intend to ensure our rules are portable between Format on Save, our linting, and our implicit standards in our existing docs in the future, but until then we need to disable Format on Save in order to prevent incorrect formatting (per our standards).