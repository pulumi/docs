---
title: Some new file
meta_desc: Here is a description of the page to appease the linter so we can get a visible preview.
---

Here's some text. It's followed by an unmatched code fence.

```

Here's some more text. It should be rendered as a paragraph, but of course it isn't, because the backticks above suggest to the rendered that it should be "contained" in code block.

Now here's some HTML, inside of which is a tagged code fence:

<div>

```plain
hello
```

</div>

Everything after this is busted.

If you delete the code fence on line 8, all will be well.

If you delete the HTML tags, things are a bit better in that the layout no longer breaks, but the result is still wrong because of the backticks.
