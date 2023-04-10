# Style Guide

This document defines some general styles we adhere to in the docs.

## Language

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

* Ensure that readers are able to scan the headings of a page and get an effective overview of the page's content.
* Every page should have exactly one `h1`.
* Headings levels should only increment one level at a time.  E.g., if your previous heading level was an `h2`, the next heading must be an `h2` or an `h3`, but not, e.g., an `h4` or `h5`.
* Docs and registry headings should use sentence case (i.e., first letter of the first word of is capitalized).

## Links

* Link text should be descriptive and have meaning outside of the surrounding context: Avoid link text like _here_, _click here_, _see here_ and instead link to the title of the linked page, e.g. "see [Pulumi Pricing](https://www.pulumi.com/pricing/)".  (While this practice benefits all readers, it is of particular important for visually impared users who use screen readers and often jump through the links of a document.)
* When changing the URL for an already existing page, add a redirect by using a [Hugo alias](https://gohugo.io/content-management/urls/#yaml-front-matter).

## Notes and Warnings

Our docs currently support two kinds of note: `info`-level and `warning`-level.

* Use notes in general to communicate important information.
* Try to limit the number of notes within a single page.
* Use `info`-level notes to convey general information.
* Use `warning`-level notes for information that, if missed, could lead to negative or unexpected consequences.

### Examples

```go
{{% notes type="info" %}}
This bit of info is important enough to call out, but not critical.
{{% /notes %}}

{{% notes type="warning" %}}
This bit of info is serious. If you missed it, bad things could happen.
{{% /notes %}}
```

## Paragraphs and Line Breaks

* Keep paragraphs short, rarely use 4 or more sentences in a single paragraph.

* When writing paragraphs and long sentences, use one of the following:

    * Keep the entire paragraph on a single line
      and use "soft wrapping" in your IDE/editor.
    * Use [semantic line breaks](https://sembr.org/)
      to break the paragraph across multiple lines.

    **Do not** "reflow" paragraphs. This causes too much diff noise.

    <details>
    <summary>Rationale</summary>

    There are two aspects to think about with this choice:

    - editable: how easy is it to suggest changes to the text
    - reviewable: how easy is it to tell what changed

    And we have three high-level options:

    - all on one line

        ```plain
        This is a pargraph all on one line. This paragraph is easy to edit because you can suggest changes to the whole paragraph in one go. When anything in this paragraph changes, GitHub will highlight which words changed.
        ```

    - semantic line breaks

        ```plain
        This pargraph uses semantic line breaks.
        Line breaks are introduced between sentences,
        and where appropriate, even within sentences.
        This makes it easy to review and edit individual sentences or clauses.
        When something in a sentence changes,
        the lines that follow it don't get touched.
        ```

    - reflowed to a fixed maximum line length

        ```plain
        This pargraph is split across multiple lines, but it has been run
        through the editor's reflow function to a maximum line length. This
        makes it difficult to review because most changes to any sentence will
        also show the following sentences as changed, and GitHub's word-diff
        will be less useful there. This is also difficult to edit because
        suggested changes won't be able to account for reflowing: GitHub's
        comment box doesn't have reflow support.
        ```

    In short, only *all on one line* and *semantic line breaks* leave the text
    adequately editable and reviewable.
    </details>

## Blockquotes

* Use blockquotes only when directly quoting content from another source.

### Example

> This is something a person said.

## Lists

* Present instructional steps in lists.

## Content Design

* Lead with content that excites and engages, end with exactly one call-to-action.
* Try and save links for the last 75% of the content.
* Use headings and lists to make content scannable and consumable.
* Use visuals: code, graphs, videos, architecture diagrams, etc.
* Highlight important points.

## Additional Resources

* Markdownlint will help enforce syntactically valid Markdown and is available as a [CLI tool](https://github.com/igorshubovych/markdownlint-cli#installation) or as a [Visual Studio Code plugin](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint).
* [Writing inclusive documentation](https://developers.google.com/style/inclusive-documentation) (Google).
