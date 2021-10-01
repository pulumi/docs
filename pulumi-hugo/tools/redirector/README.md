# Redirector

Redirector -- a terribly-written tool that adds/updates the `aliases` front-matter key
for any content that is being moved. It is best used for moving content in bulk.

## Usage

First, make sure you have renamed the directory before running the tool.

```
cd tools/redirector
go run . -logtostderr <oldDir> <newDir>
```

For example, if I wanted to move the `resources` to `events-workshops` under `themes/default/content`, I'd first rename
`resources` to `events-workshops` then run:

```bash
cd tools/redirector
# ../../ because we are inside the tools/redirector folder when running the command.
go run . -logtostderr ../../themes/default/content/resources ../../themes/default/content/events-workshops
```

## Thoughts

Keeping aside the perhaps bad code quality the approach taken by this tool warrants some
explanation as to why it was done that way.

* Yes, Markdown parsing is possible using https://github.com/yuin/goldmark but you'll still
need to parse and walk the AST to modify the markdown and then write it back to the file on your own.
The parser are concerned with parsing from markdown and rendering it to HTML.
* Parsing just the front-matter is also possible. For example, `goldmark` supports extensions and `goldmark-meta`
is one such extension to extract front-matter. But that strips useful comments from the front-matter. You'll
still need to figure out a way to "update" the front-matter in the original file.
* Then there's https://github.com/gernest/front which also unmarshals the yaml front-matter and thus has the same
problems outlined previously.

All of that led to the simple line-by-line read approach. It hasn't been tested with a wide range of files but
hopefully works for most cases despite being less sophisticated.
