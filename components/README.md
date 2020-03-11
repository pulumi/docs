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
make serve-components
```

... and browse to http://localhost:3333. There, you'll see a single HTML page (whose
source you'll find at `/components/src/index.html`) that you can use as a sandbox for
developing and testing your components in isolation. Any changes you make to that page
will be reflected immediately, and changes to the components themselves will trigger a
recompile and be copied into Hugo site at `/static/js/`. So if you're running `make serve`
in one shell and `make serve-components` in another, saving a component will trigger a
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

## Questions?

Blame Christian. Also, he's happy to help.
