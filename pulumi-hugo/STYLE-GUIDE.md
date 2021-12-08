# Style Guide

This document defines some general styles we adhere to in the docs.

## Words are important

- Instead of _guys_ try _folks_, _yall_, or _everyone_
- Instead of _crazy_ try _wild_
- Instead of _click_ use _select_
- Instead of _dummy_ use _placeholder_
- Avoid using gendered language
- Avoid using violent language (e.g., _kill_)
- Avoid pop-culture references

Want to learn about why these words should be avoided?
Check out [Google's inclusive documentation guide](https://developers.google.com/style/inclusive-documentation).

## Headings

- You should be able to scan the headings of a document and get a good sense of the page
- Every page should have exactly one h1
- Don't skip heading levels in Markdown files, e.g., if your previous heading level was a 2, the next heading should be a 2 or a 3, but not a 4 or 5

## Links

- Link text should be descriptive and be understandable outside of the context that it is in.
- Avoid link text like _here_, _click here_, _see here_

## Notes and Warnings

Our docs currently support two kinds of note: `info`-level and `warning`-level.

- Use notes in general to communicate important information
- Try and limit the number of notes within a single page
- Use `info`-level notes to convey general information
- Use `warning`-level notes for information that if missed, could lead to negative consequences

### Examples

```
{{% notes type="info" %}}
This bit of info is important enough to call out, but not critical.
{{% /notes %}}

{{% notes type="warning" %}}
This bit of info is serious. If you missed it, bad things could happen.
{{% /notes %}}
```

## Blockquotes

- Use blockquotes only when you are quoting content from another source.

### Example

> This is something a person said.
