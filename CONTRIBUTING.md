# Contributing Pulumi Documentation

## Pulumi terminology

- Use `pulumi` or "the Pulumi CLI" to refer to the CLI
- Use `pulumi.com` to refer to the service

## Documentation structure

- There is a folder for each heading in the top navigation, such as `Install`, `getting-started`, etc.

- The mapping from documentation page to section and table-of-contents (TOC) is stored in yaml files in `_data`. 

- To rename a section, rename both the value of `nav_section` in the toc yaml file (e.g., [`_data/install.yaml`](_data/install.yaml)) and update the layout in [`_includes/header.html`](_includes/header.html).

- To add a new article and add it to the table-of-contents for that section, create a new file in the right section and add an entry in the corresponding file in `_data\top-level-section.yaml`.

### Links to other files

**NOTE:** The local Jekyll web server will resolve URLs without an extension, so `[topic](section/topic)` will resolve to `section/topic.html`. Unfortunately, the Go binary that serves content does **not** honor this behavior. If you're running the `make test` target against a Jekyll web server, you won't see the issue, but there will be 404s on the production docs site.

### Jekyll and Liquid tips

- **Redirects.** If you rename a file or directory, add a 301 redirect in the front-matter via `redirect_from: "/previous-dir/previousfile.html"`.

- **Includes.** To share common content across articles, use an "include" file. Place a file in the [`_includes`](_includes/) folder with the appropriate file extension. To include it in a page, use the syntax `{% include %}`.

- **Front-matter variables.** You can define a front-matter variable in the YAML section at the top of a file. For instance, the installer page defines `installer_version: "0.10.0"`. You  can then reference the variable in either markdown or HTML content with the syntax `{{ page.installer_version }}`.

- **Anchor tags.** Define anchor tags with the syntax `{#anchor-name}`. Even though [Kramdown can automatically generate header IDs](https://kramdown.gettalong.org/converter/html.html), it is preferable to use an explicit anchor; otherwise, changing a section name will break anchor links.

## Style guide

### Language and terminology styles

- Top level headings use **Title Case**, where each word starts with a capital letter.
- All other headings use **Sentence case**, where only the first word and any proper nouns have a capital letter. 
- Use capitalization only for a proper noun, and use throughout. For example, "stack" should almost always be lowercase in text

### Referring to "things"

- References to the Pulumi CLI or CLI commands should be enclosed in backticks (e.g., `pulumi update`).
- References to UI elements within a webpage should be **bold**. (e.g., "Go to the **Account** page in the Pulumi Console and select **sync profile with GitHub**").
- Use arrows to indicate a navigation. (e.g., "Go to **FooPage** -> **BarItem**").

### Formatting

- Use hash marks for headings (`#`, `##`, etc)
- Use double-asterisks for bold `**`
- Use underscore for italic `_`
- Use triple-backtick and language for code formatting, e.g. ```typescript
- Don't use hard linebreaks. They are discouraged by the the kramdown formatter, which calls it "lazy syntax". See [kramdown Syntax](https://kramdown.gettalong.org/syntax.html).
- **In contrast to GitHub-flavored markdown, use two spaces after a list item**, so that the indentation of the next level aligns correctly. This is because kramdown parses lists differently than GitHub. See http://idratherbewriting.com/documentation-theme-jekyll/#markdown.

  I.e., do 
  ```1.  First item``` (two spaces)

  Instead of 
  ```1. First item``` (one space)

### Sections

If a tutorial has more following tutorials, use a **Next steps** section at the end. If you're linking to other reference material, use **Learn more**.
