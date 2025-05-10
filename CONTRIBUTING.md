# Contributing to Pulumi Documentation

This guide will help you contribute to Pulumi's documentation. Use the navigation below to find what you need quickly.

**Quick navigation:**
- [Documentation Overview](#documentation-structure)
- [Creating Links](#links-to-other-files)
- [Hugo Tips](#hugo-tips)
- [Style Guidelines](#style-guide)
- [Writing Blog Posts](BLOGGING.md)
- [Writing Code Examples](CODE-EXAMPLES.md)
- [Style Guide (Comprehensive)](STYLE-GUIDE.md)

## What would you like to do?

- **Edit existing content:** Follow our [style guide](#style-guide) and use [Hugo's relref shortcode](#links-to-other-files) for internal links
- **Add new content:** Understand our [documentation structure](#documentation-structure) and use our [Hugo tips](#hugo-tips)
- **Test your changes:** Run `make serve` to preview changes locally at http://localhost:1313
- **Write a blog post:** See the [blogging guide](BLOGGING.md)

## Pulumi terminology

- Use `pulumi` or "the Pulumi CLI" to refer to the CLI.
- Use `pulumi.com` to refer to the service.

## Documentation structure

- There is a folder for each heading in the top navigation, such as `Install`, `getting-started`, etc.

- The mapping from documentation page to section and table-of-contents (TOC) is stored largely in each page's front matter, leveraging [Hugo Menus](https://gohugo.io/content-management/menus/). Menus for the CLI commands and API reference are specified in `./config.toml`.

### Links to other files

We generally use Hugo's [`relref` shortcode](https://gohugo.io/content-management/shortcodes/#ref-and-relref) when linking to other pages. Examples:

```markdown
[Install]({{< relref "/docs/get-started/install" >}})
[Outputs]({{< relref "/docs/intro/concepts/stack#outputs" >}})
```

Which, on a page inside the `./content/reference` directory, will generate:

```html
<a href="/docs/install/">Install</a>
<a href="/docs/intro/concepts/stack/#stack-outputs">Outputs</a>
```

### Hugo tips

- **Redirects.** If you rename a file or directory, add a 301 redirect in the front-matter via an [alias](https://gohugo.io/content-management/urls/#aliases) `aliases: [/previous-dir/previousfile.html]`.

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

  - **no_on_this_page** Specify this variable to prevent displaying an "On This Page" TOC on the right nav for the page.
  - **block_external_search_index** Specify this variable to prevent crawlers from indexing the page.

## Testing your changes

To see how your changes look locally before submitting a pull request:

```bash
# Install dependencies and build assets
make ensure

# Run the development server
make serve
```

Then visit http://localhost:1313 to preview your changes.

## Common commands

```bash
# Build the entire website
make build

# Run linting on Markdown and other files
make lint

# Format all applicable files
make format

# Run all tests
make test

# Test specific programs
ONLY_TEST="example-name" make test-programs
```

## Style guide

### Language and terminology styles

- Top level headings use **Title Case**, where each word starts with a capital letter.
- All other headings use **Sentence case**, where only the first word and any proper nouns have a capital letter.
- Use capitalization only for a proper noun, and use throughout. For example, "stack" should almost always be lowercase in text.

### Referring to "things"

- References to the Pulumi CLI or CLI commands should be enclosed in backticks (e.g., `pulumi up`).
- References to UI elements within a webpage should be **bold**. (e.g., "Go to the **Account** page in the Pulumi Console and select **sync profile with GitHub**").
- Use arrows to indicate a navigation. (e.g., "Go to **FooPage** &gt; **BarItem**").

### Formatting

- Use hash marks for headings (`#`, `##`, etc)
- Use double-asterisks for bold `**`
- Use underscore for italic `_`
- Use `--` for en dashes and `---` for em dashes
  - Do not put spaces before or after the dashes
- Use code fences (triple-backticks) and a [language identifier](https://gohugo.io/content-management/syntax-highlighting/) for code formatting and syntax highlighting:
  <pre><code>```typescript
  const foo = "bar";
  ```</code></pre>

### Sections

If a tutorial has more following tutorials, use a **Next steps** section at the end. If you're linking to other reference material, use **Learn more**.

## Blog Post Authoring

For instructions on contributing to the [Pulumi blog](https://www.pulumi.com/blog/), [see BLOGGING.md](BLOGGING.md).

## Additional Resources

For more detailed guidance, please refer to:

- [Style Guide](STYLE-GUIDE.md) - Comprehensive style and UX standards
- [Code Examples](CODE-EXAMPLES.md) - Guidelines for writing code examples
- [SEO Guidelines](SEO.md) - Search engine optimization guidance