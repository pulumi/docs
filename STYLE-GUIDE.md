# Style guide

This document defines some general styles we adhere to in the docs.

## Using inclusive language

Words are important. Pulumi strives to use language that is clear, harmonious, and friendly to all readers.  With these goals in mind, we use the following guidelines:

* Avoid ableist language:
  * Instead of _crazy_ try _wild_.
  * Instead of _click_ use _select_.
  * Instead of _dummy_ use _placeholder_.
* Avoid unnecessarily gendered language: Instead of _guys_ try _folks_, _yall_, or _everyone_.
* Avoid using violent language (e.g., _kill_).
* Avoid pop-culture references as such references may not be familiar to all readers.
* Instead of "go to," use "navigate".
* Avoid directional words. Instead, link directly to the section you are referencing.
* Avoid using "easy", "simple" or their adjectives, as they make a judgment about the difficulty of a concept explained, or the level of a reader's subject matter expertise. Often, you can omit these words entirely.

## Headings

* Top level headings use **Title Case**, where each word starts with a capital letter.
* All other headings use **Sentence case**, where only the first word and any proper nouns have a capital letter.
* Use capitalization only for a proper noun, and use throughout the heading. For example, "stack" should almost always be lowercase in text.
* Ensure that readers are able to scan the headings of a page and get an effective overview of the page's content.
* Every page should have exactly one `h1`. This is typically defined in the `title` attribute of the front matter on a Markdown page.
* Headings levels must only increment one level at a time.  E.g., if your previous heading level was an `h2`, the next heading must be an `h2` or an `h3`, but not, e.g., an `h4` or `h5`.
* Docs and registry headings should use sentence case (i.e., first letter of the first word is capitalized).

## Links

* Use Markdown links to link between pages on the site:

    ```markdown
    [Link text](/path/to/file)
    ```

  Or to external sites:

    ```markdown
    [Link text](https://example.com)
    ```

* Link text should be descriptive and have meaning outside of the surrounding context: Avoid link text like _here_, _click here_, _see here_ and instead link to the title of the linked page, e.g. "see [Pulumi Pricing](https://www.pulumi.com/pricing/)". (While this practice benefits all readers, it is of particular importance for visually impaired users who use screen readers and often jump through the links of a document.)
* When changing the URL for an already existing page (which includes moves and renames within the filesystem), add a redirect by using a [Hugo alias](https://gohugo.io/content-management/urls/#yaml-front-matter).

## Notes

Our docs support "callouts" with the `{{ notes }}` shortcode:

* Use notes in general to communicate important information.
* Try to limit the number of notes within a single page.
* The following note levels are supported:
  * Use `info`-level notes to convey general information.
  * Use `tip`-level notes to convey helpful ideas.
  * Use `warning`-level notes for information that, if missed, could lead to negative or unexpected consequences.

### Examples

```go
{{% notes type="info" %}}
This bit of info is important enough to call out, but not critical.
{{% /notes %}}

{{% notes type="tip" %}}
This bit of info is a great idea, that might be really helpful.
{{% /notes %}}

{{% notes type="warning" %}}
This bit of info is serious. If you missed it, bad things could happen.
{{% /notes %}}
```

## Paragraphs and Line Breaks

* Keep paragraphs short, rarely use 4 or more sentences in a single paragraph.
* When writing paragraphs and long sentences keep the entire paragraph on a single line and use "soft wrapping" in your IDE/editor.

## Blockquotes

* Use blockquotes only when directly quoting content from another source.

### Example

> This is something a person said.

## Lists

* Present instructional steps in lists.

## Content design

* Lead with content that excites and engages, end with exactly one call-to-action.
* Try and save links for the last 75% of the content.
* Use headings and lists to make content scannable and consumable.
* Use visuals: code, graphs, videos, architecture diagrams, etc.
* Highlight important points.
* Avoid emojis unless for notes or absolutely necessary.

## Product names and acronyms

Pulumi's product names are:

* Pulumi IaC
* Pulumi ESC
* Pulumi IDP
* Pulumi Insights
* Pulumi Cloud

These product names include acronyms, but have a different formatting style than acronyms, because we view the product name as an opaque identifier, not descriptive text. When referring to Pulumi products, always use the company name with the acronym, as a single term.

At first mention of a product, in any document, expand the acronym only, with the full form in parentheses after the product name:

* **Correct at first usage**: Pulumi IaC (Infrastructure as Code)
* **Correct at first usage**: Pulumi ESC (Environments, Secrets, and Configuration)
* **Correct at first usage**: Pulumi IDP (Internal Developer Platform)

After the first reference, use just the product name:

* **Correct for subsequent usage**: Pulumi IaC
* **Correct for subsequent usage**: Pulumi ESC
* **Correct for subsequent usage**: Pulumi IDP

Always capitalize product names correctly. Do not use variations like "Pulumi IAC", "Pulumi iac", "pulumi IaC", etc.

### Acronym usage

For acronyms that are not part of Pulumi product names, follow standard grammatical practices:

At first mention of an acronym in a document, use the spelled-out term followed by the acronym in parentheses:

* **Correct**: Custom Resource Definition (CRD)
* **Correct**: Virtual Private Cloud (VPC)
* **Correct**: Platform as a Service (PaaS)

For subsequent mentions, use just the acronym:

* **Correct**: The CRD defines how the custom resource should be structured.
* **Correct**: Deploy your application in a VPC for better security.

If an acronym is widely known and more commonly used than its spelled-out form (like API, HTTP, REST), you can use the acronym without spelling it out.

This approach follows standard documentation practices like those in the [Google Developer Documentation Style Guide](https://developers.google.com/style/abbreviations). Feel free to reference the Google style guide for a longer, more nuanced explanation of correct usage for acronyms that are _not_ part of product names.

### Referring to Pulumi commands or UI elements

* References to the Pulumi CLI or CLI commands should be enclosed in backticks (e.g., `pulumi up`).
* References to UI elements within a webpage should be **bold**. (e.g., "Go to the **Account** page in the Pulumi Console and select **sync profile with GitHub**").
* Use arrows to indicate a navigation. (e.g., "Go to **FooPage** &gt; **BarItem**").

### Sections in tutorials

If a tutorial has more following tutorials, use a **Next steps** section at the end. If you're linking to other reference material, use **Learn more**.

## Blog post authoring

For instructions on contributing to the [Pulumi blog](https://www.pulumi.com/blog/), [see BLOGGING.md](BLOGGING.md).

## Additional resources

* Markdownlint will help enforce syntactically valid Markdown and is available as a [CLI tool](https://github.com/igorshubovych/markdownlint-cli#installation) or as a [Visual Studio Code plugin](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint).
* [Writing inclusive documentation](https://developers.google.com/style/inclusive-documentation) (Google).
