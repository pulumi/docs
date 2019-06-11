# Contributing Pulumi Documentation

## Pulumi terminology

- Use `pulumi` or "the Pulumi CLI" to refer to the CLI
- Use `pulumi.com` to refer to the service

## Documentation structure

- There is a folder for each heading in the top navigation, such as `Install`, `getting-started`, etc.

- The mapping from documentation page to section and table-of-contents (TOC) is stored largely in each page's front matter, leveraging [Hugo Menus](https://gohugo.io/content-management/menus/). Menus for the CLI commands and API reference are specified in `./config.toml`.

### Links to other files

We generally use Hugo's [`relref` shortcode](https://gohugo.io/content-management/shortcodes/#ref-and-relref) when linking to other pages. Examples:

```markdown
[Install]({{< relref "/quickstart/install.md" >}})
[Outputs]({{< relref "programming-model.md#stack-outputs" >}})
```

Which, on a page inside the `./content/reference` directory, will generate:

```html
<a href="/quickstart/install/">Install</a>
<a href="/reference/programming-model/#stack-outputs">Outputs</a>
```


### Hugo tips

- **Redirects.** If you rename a file or directory, add a 301 redirect in the front-matter via an [alias](https://gohugo.io/content-management/urls/#aliases) `aliases: ["/previous-dir/previousfile.html"]`.

- **Includes.**

  - **.md files.** To share common content across articles, use [Hugo Shortcodes](https://gohugo.io/content-management/shortcodes/). Place a .html file in the [layouts/shortcodes] folder. To include it in a page, use syntax `{{< my-shortcode >}}`

    For example, our custom [`cleanup`](layouts/shortcodes/cleanup.html) shortcode can be included in .md files, to include common text about cleaning up stack resources:

    ```md
    {{< cleanup >}}
    ```

  - **.html layout files.** HTML layouts can include other layouts inside the [layouts/partials](layouts/partials) directory, e.g.:

    ```html
    {{ partial "head.html" . }}
    ```

- **Front-matter variables.** You can define a front-matter variable in the YAML section at the top of a file. For instance, the you could add the following front matter `foo: "bar"`, and then reference the variable in markdown with the syntax `{{< param foo >}}`.

## Style guide

### Language and terminology styles

- Top level headings use **Title Case**, where each word starts with a capital letter.
- All other headings use **Sentence case**, where only the first word and any proper nouns have a capital letter. 
- Use capitalization only for a proper noun, and use throughout. For example, "stack" should almost always be lowercase in text

### Referring to "things"

- References to the Pulumi CLI or CLI commands should be enclosed in backticks (e.g., `pulumi up`).
- References to UI elements within a webpage should be **bold**. (e.g., "Go to the **Account** page in the Pulumi Console and select **sync profile with GitHub**").
- Use arrows to indicate a navigation. (e.g., "Go to **FooPage** -> **BarItem**").

### Formatting

- Use hash marks for headings (`#`, `##`, etc)
- Use double-asterisks for bold `**`
- Use underscore for italic `_`
- Use triple-backtick and language for code formatting, e.g. ```typescript

### Sections

If a tutorial has more following tutorials, use a **Next steps** section at the end. If you're linking to other reference material, use **Learn more**.
