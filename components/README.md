# components

We use [Stencil.js](https://stenciljs.com/), a
[web-component](https://developer.mozilla.org/en-US/docs/Web/Web_Components) compiler that
lets us write custom elements and manage them with TypeScript. Unless you're planning on
authoring your own components, this section probably won't be all that interesting to you
-- but if you are, great! You've come to the right place.

## Start with the docs

[They're right here](https://stenciljs.com/docs/introduction). There isn't much, and a
brisk read through them will help you get oriented quickly.

If you're familiar with React or Angular, Stencil components operate similarly: values are
passed into components as HTML attributes (which Stencil calls "props"), and events are
handled using native DOM events and propagation. Encapsulation, composition, use the
platform, etc.

## Redux

We also use Stencil's built-in [support for
Redux](https://stenciljs.com/docs/stencil-redux) for managing state, both in-page and
between pageviews by serializing to local storage. Together, these two tools let us manage
the DOM more declaratively, treating the Redux container as the single source of truth.
Install the [devtools extension](https://github.com/zalmoxisus/redux-devtools-extension)
for additional fun and occasional profit.

## Creating a new component

Please _do not_ simply copy and paste an existing component to create a new one -- that's
what generators are for. Stencil has a lovely component generator you can invoke simply by
running:

```
yarn run generate
```

... and following the prompts. For the tag name, please use the convention
`pulumi-somenoun`, and Stencil.js will take care of the rest. By default, you'll be
offered the option of creating a stylesheet and both unit and end-to-end tests. Accept
all, then change the file extension of the CSS file to `.scss`.

## Developing and testing your component

Stencil ships with a development server that runs on port 3333. (It runs independently of
the Hugo development server.) To use it, from the project root, run:

```
make serve_components
```

... and browse to http://localhost:3333. There, you'll see a single HTML page (whose
source you'll find at `/components/src/index.html`) that you can use as a sandbox for
developing and testing your components in isolation. Any changes you make to that page
will be reflected immediately, and changes to the components themselves will trigger a
recompile and be copied into Hugo site at `/static/js/`. So if you're running `make serve`
in one shell and `make serve_components` in another, saving a component will trigger a
reload of the Hugo site as well. (I chose to keep these as separate targets simply because
most users who run `make serve` won't need be able to work on components concurrently.)

## Styling components

Stencil supports both Sass and the [Shadow
DOM](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM).
However, because most of our styling is handled with
[TailwindCSS](https://tailwindcss.com/) and customizations, we opt out of Shadow DOM and
simply style the components externally, using the Sass defined in
`/assets/sass/components`. Other than behavior fundamental to your component (e.g.,
visibility), most of the styling you apply -- color, type, padding, and so on -- should
happen there, and not be expressed as raw CSS alongside your component definition.

## Available components

### pulumi-chooser

This component creates a set of tabs for selecting content, like a language, OS, or cloud
provider. It can operate either as a self-closing component with no children or as a
container with one or more `pulumi-choosable` components as its children. In both cases,
by default, the `options` you provide will be set globally and persist between pageviews.

Available chooser types are:

* `cloud`, with supported options `aws`, `azure`, and `gcp`
* `os`, with supported options `macos`, `linux` and `windows`
* `language`, with supported options `javascript`, `typescript`, `python`, `go`, `csharp`, `fsharp`, and `visualbasic`.
* `k8s-language`, with supported options `typescript`, `typescript-kx`, and `yaml`

Options will be ordered automatically by the component; variable sort order is not exposed
in the component API.

If you want to present a chooser that works independently of what's globally stored, use
the `mode="local"` attribute, as indicated in the example below.

When a chooser's options don't line up with what's stored globally -- e.g., if a user's
default language is C#, but the chooser doesn't have a C# option -- the chooser switches
into local mode and displays the first available tab and `pulumi-choosable`, in order to
ensure something always appears on the page.

#### Usage

This chooser sets the selected `os` to persist between pages.

```
<pulumi-chooser type="os" options="macos,windows,linux" />
```

This chooser operates in local mode, meaning it ignores whatever happens to be set on the
global store. Useful if you want to present content that may be deliberately different
from content more relevant to the user's general preferences.

```
<pulumi-chooser type="os" options="macos,windows,linux" mode="local">
    <pulumi-choosable type="os" value="macos">Some Mac Stuff</pulumi-choosable>
    <pulumi-choosable type="os" value="windows">Some Windows Stuff</pulumi-choosable>
    <pulumi-choosable type="os" value="linux">Some Linux Stuff</pulumi-choosable>
</pulumi-chooser>
```

This chooser groups a set of options, but hides its controls by providing an
`option-style` (which is `tabbed` by default):

```
<pulumi-chooser type="os" options="macos,windows,linux" option-style="none">
    <pulumi-choosable type="os" value="macos">Some Mac Stuff</pulumi-choosable>
    <pulumi-choosable type="os" value="windows">Some Windows Stuff</pulumi-choosable>
    <pulumi-choosable type="os" value="linux">Some Linux Stuff</pulumi-choosable>
</pulumi-chooser>
```

This is useful if you have a set of related items you want to toggle based on a value on
the global store (e.g., language-specific types, filenames and the like).

### pulumi-choosable

This component can be supplied either as a child of a chooser, as indicated above, or on
its own, in which case it'll simply honor whatever's in the global store.

#### Usage

```
<body>
    <div>
        <pulumi-choosable type="os" value="macos">
            I'll only appear when the user's preferred OS is Mac. Otherwise, you'll never see me.
        </pulumi-choosable>
        ...
```

#### Shortcodes (and some gotchas)

In Markdown files, you can express these choosers either as HTML alone or with
[Hugo shortcodes](https://gohugo.io/content-management/shortcodes/). For example:

```
{{< chooser language "typescript,go,csharp" >}}
```

.. will render:

```
<div>
    <pulumi-chooser type="language" options="typescript,go,csharp"></pulumi-chooser>
</div>
```

Similarly:

```
{{< chooser cloud "aws,azure,gcp" >}}

{{% choosable cloud aws %}}

Some AWS stuff.

{{% /choosable %}}

{{% choosable cloud azure %}}

Some Azure stuff.

{{% /choosable %}}

{{% choosable cloud gcp %}}

Some GCP stuff.

{{% /choosable %}}

{{< /chooser >}}
```

.. will render:

```
<div>
    <pulumi-chooser type="cloud" options="aws,azure,gcp">
        <div>
            <pulumi-choosable type="cloud" values="aws" mode="">Some AWS stuff.</pulumi-choosable>
        </div>
        <div>
            <pulumi-choosable type="cloud" values="azure" mode="">Some Azure stuff.</pulumi-choosable>
        </div>
        <div>
            <pulumi-choosable type="cloud" values="gcp" mode="">Some GCP stuff.</pulumi-choosable>
        </div>
    </pulumi-chooser>
</div>
```

A few things to note:

* Pay attention to how you nest `chooser` and `choosable` shortcodes. [Hugo shortcodes](https://gohugo.io/content-management/shortcodes/) work with both
  `<>` and `%%` delimiters, but the two behave very differently: `%` will cause content to be
  Markdown-rendered, `<` and `>` will not. So for example:

  ```
  {{< some-shortcode >}}

    This content will *not* be rendered as Markdown.

  {{< /some-shortcode >}}

  {{% some-shortcode %}}

    This content *will* be.

  {{% /some-shortcode %}}
  ```

  You need to be careful about double-rendering, though. For example, this is okay: the outer
  container won't be rendered as Markdown, but the inner children will be.

  ```
  {{< some-parent >}}

    <some-component>
        Just some regular HTML, here.
    </some-component>

    {{% some-child %}}
        [Some Markdown]("http://some-link").
    {{% /some-child %}}

    {% some-child %}}
        [Some more Markdown]("http://some-link").
    {{% /some-child %}}

  {{< /some-parent >}}
  ```

  If you did this, however:

  ```
  {{% some-parent %}}

    <some-component>
        Just some regular HTML, here.
    </some-component>

    {{% some-child %}}
        [Some Markdown]("http://some-link").
    {{% /some-child %}}

    {% some-child %}}
        [Some more Markdown]("http://some-link").
    {{% /some-child %}}

  {{% /some-parent %}}
  ```

  ... the nested shortcodes would be rendered twice -- first by virtue of their being
  wrapped in a `%`-delimited shortcode, and then a second time when the parent's content
  is rendered itself. Sometimes this turns out okay, but if you're rendering source code,
  where indentation matters, you can wind up with some terrible results.

  So as a rule, avoid nesting `%`-delimited shortcodes. Decide which shortcode will be responsible
  for rendering, and use `%`s on that one, `<>`s on descendants.

* The containing `div`s emitted by the `chooser` and `choosable` shortcodes are
  intentional and in most cases required, because the template renderers we're using today
  don't know how to handle [custom
  elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements)
  like these, so wrapping them in a standard HTML tag is necessary. (It's not necessary in
  HTML layouts files, though -- only in Markdown files.)

* By default, active choosables will inherit `display: block;`, but you can override this
  behavior by passing the [TailwindCSS](https://tailwindcss.com/) utility class `inline`
  in the chooser (typically in conjunction with `option-style="none"`:

```
<p>
    It looks like you're on a
    <pulumi-chooser type="os" options="macos,windows,linux" option-style="none" class="inline">
        <pulumi-choosable type="os" value="macos">Mac</pulumi-choosable>
        <pulumi-choosable type="os" value="windows">Windows</pulumi-choosable>
        <pulumi-choosable type="os" value="linux">Linux</pulumi-choosable>
    </pulumi-chooser>
    computer. Nice!
</p>
```

### pulumi-tooltip

This component shows a tooltip bubble over its children on mouseover (or touch). The
content of the bubble is specified using the `content`
[slot](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot).

The component also exposes `show()` and `hide()` methods for programmatic control over the
bubble's visibility.

#### Usage

##### HTML

```
<pulumi-tooltip>
    <i class="fas fa-question-circle"></i>
    <span slot="content">
        You hovered over the icon!
    </span>
</pulumi-tooltip>
```

##### JavaScript

```
<pulumi-tooltip id="my-tooltip">
    <i class="fas fa-question-circle"></i>
    <span slot="content">
        You called the show() method!
    </span>
</pulumi-tooltip>

<script>
    var tooltip = document.querySelector("#my-tooltip");

    tooltip
        .show()
        .then(function() { console.log("The tooltip is visible."); });

    tooltip
        .hide()
        .then(function() { console.log("The tooltip is not visible."); });
</script>
```

## Questions?

Blame Christian. Also, he's happy to help.
