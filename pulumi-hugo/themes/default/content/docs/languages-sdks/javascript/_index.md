---
title_tag: "TypeScript and Node.js | Languages & SDKs"
meta_desc: Learn to use Node.js languages like JavaScript and TypeScript with Pulumi for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
title: TypeScript (Node.js)
h1: Pulumi & TypeScript & JavaScript (Node.js)
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  languages:
    identifier: javascript
    weight: 1
aliases:
- /docs/reference/javascript/
- /docs/reference/typescript/
- /docs/intro/languages/javascript/
- /docs/intro/languages/typescript/
- /javascript/
- /typescript/
---

<img src="/logos/tech/logo-nodejs.png" align="right" width="150" style="padding:8px; margin-top: -64px">

Pulumi supports writing your infrastructure as code in any JavaScript language running on Node.js using any of the [Current, Active and Maintenance LTS versions](https://nodejs.org/en/about/previous-releases).

Because programs are just JavaScript, you may elect to write them in any manner you'd normally write Node.js programs.
That includes TypeScript, CoffeeScript, or Babel, in addition to your favorite tools such as build systems, linters, or
test frameworks.

<a class="btn btn-secondary" href="https://nodejs.org/en/download/" target="_blank" title="Install Node.js">Install Node.js</a>

## Pulumi Programming Model

The Pulumi programming model defines the core concepts you will use when creating infrastructure as code programs using
Pulumi. [Concepts](/docs/intro/concepts) describes these concepts
with examples available in JavaScript and TypeScript. These concepts are made available to you in the Pulumi SDK.

The Pulumi SDK is available to Node.js developers as a NPM package. To learn more, [refer to the Pulumi SDK Reference
Guide](/docs/reference/pkg/nodejs/pulumi/pulumi).

The Pulumi programming model includes a core concept of `Input` and `Output` values, which are used to track how outputs of one resource flow in as inputs to another resource.  This concept is important to understand when getting started with JavaScript and Pulumi, and the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation is recommended to get a feel for how to work with this core part of Pulumi in common cases.

## Entrypoint

Pulumi executes your program by loading the entrypoint file as a Node module: `require("index.ts")`. By default, Pulumi will load `index.ts` or `index.js`. Alternatively, if you specify `main` within your `package.json`, Pulumi will load that module instead:

```json
{
    "name": "my-package",
    "version": "1.0.0",
    ...
    "main": "src/entry.ts"
}
```

{{< chooser language "javascript,typescript" >}}

Your entrypoint can either return a module object with properties for each stack output:

{{% choosable language "javascript" %}}

```javascript
// create resources
...
exports.out = myResource.output;
```

{{% /choosable %}}

{{% choosable language "typescript" %}}

```typescript
// create resources
...
export const out = myResource.output;
```

{{% /choosable %}}

Or alternatively, your entrypoint can export a top level `async` function that returns an object with members for each stack output.
Pulumi will automatically call this function and await the result:

{{% choosable language "javascript" %}}

```javascript
module.exports = async () => {
    // create resources
    return { out: myResource.output };
}
```

{{% /choosable %}}

{{% choosable language "typescript" %}}

```typescript
export = async () => {
    // create resources
    return { out: myResource.output };
}
```

{{% /choosable %}}

{{< /chooser >}}

Most Pulumi programs use the first option, but programs that need to do async work at the top level (such as calling [`getOutputValue`](/docs/reference/pkg/nodejs/pulumi/pulumi#StackReference-getOutputValue)) may find they want to use the second.

## TypeScript

You can elect to write Pulumi programs in TypeScript to get additional verification and tooling benefits. Pulumi supports TypeScript natively so you don't need to explicitly run `tsc` on your program before running `pulumi`.

If you would like full control of the TypeScript build process, you can compile ahead of time, and point your package.json main entry point at the compiled JavaScript instead. If you do this, you can disable the [automatic compilation of TypeScript files](#disabling-built-in-typescript-support).

The fastest way to get started with Pulumi in TypeScript, is to use a template:

```bash
$ mkdir myproject && cd myproject
$ pulumi new typescript
```

This will auto-generate all the basic artifacts required to use TypeScript. If you prefer, you can instead run the following manual steps.

### 1. Update package.json

Update your `package.json` to look like the following (with your own values for `name`, `version`, etc.).  This
is what tells Node.js and NPM what packages you depend on, where to find your code's entry points, and so on:

```json
{
    "name": "my-package",
    "version": "1.0.0",
    "devDependencies": {
        "@types/node": "^12.0.0"
    },
    "dependencies": {
        ... as before ...
    }
}
```

You can customize this however you'd like, such as adding test scripts, npm package dependencies, etc.  For more information on `package.json`, refer to [the NPM documentation](https://docs.npmjs.com/files/package.json).

### 2. Install dependencies

Run `npm install` or `yarn install` to install the new development-time dependencies to your `node_modules` directory.

### 3. Create tsconfig.json

When using Pulumi's built in TypeScript support, a `tsconfig.json` file is optional. However, defining one allows your to set additional TypeScript compiler options, for example not allowing implicit returns from a function. In addition, other tools like VS Code will use these settings to give you additional warnings at development time. Any options set in your `tsconfig.json` file will be picked up by Pulumi. We recommend creating a `tsconfig.json` file with the following settings:

```json
{
    "compilerOptions": {
        "strict": true,
        "outDir": "bin",
        "target": "es2016",
        "module": "commonjs",
        "moduleResolution": "node",
        "sourceMap": true,
        "experimentalDecorators": true,
        "pretty": true,
        "noFallthroughCasesInSwitch": true,
        "noImplicitReturns": true,
        "forceConsistentCasingInFileNames": true
    },
    "files": [
        "index.ts"
    ]
}
```

You may customize this however you'd like, including the TypeScript settings that work for you.  For
information on additional settings, see the [TypeScript documentation for `tsconfig.json`](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html).

Tools like VS Code will give you completion lists, live error reporting and inline documentation help.

<img src="/images/docs/reference/vscode.png" alt="Pulumi TypeScript in VS Code" width="700">

## Disabling built in TypeScript support

You can disable the built in TypeScript support by changing the `runtime` setting in `Pulumi.yaml` to look like the following:

```yaml
runtime:
  name: nodejs
  options:
    typescript: false
```

## Package Management

Pulumi has official support for NPM and Yarn Classic. Pulumi does
not support Yarn Plug'n'Play.

Pulumi defaults to using NPM. However, if Pulumi detects a `yarn.lock` file
in the project root, or the environment variable `PULUMI_PREFER_YARN=true`,
then Pulumi will use Yarn instead of NPM if the executable is available in the
path.

## Dependencies on Provider Packages within Component Packages

Some package management systems allow for different versions of a package to be installed concurrently.
You can include a package as a direct dependency in your project and another dependency could depend on the
same package too, but with a different version.

Suppose we are building a component package where you use `@pulumi/random`, major version 3.
In our `package.json` file for the component package, you have this:

```json
{
  "name": "components",
  "version": "1.0.0",
  ...
  "dependencies": {
    ...
    "@pulumi/random": "^3",
    ...
  },
  ...
}
```

In a project where you consume this component library, you can add more `random` resources, but now using
major v4:

```json
{
  "name": "components-consume",
  ...
  "dependencies": {
    ...
    "@pulumi/random": "^4",
    "components": "^1",
    ...
  },
  ...
}
```

In the situation where you mix major versions, the specification `^3` excludes major version `4`.
If we check on our dependency graph, we see two versions included

```sh
$ npm why @pulumi/random
@pulumi/random@v4.14.0
node_modules/@pulumi/random
  @pulumi/random@"^4.14.0" from the root project

@pulumi/random@v3.2.0 extraneous
  @pulumi/random@"^3" from components@1.0.0
    components@1.0.0
```

When you use a Pulumi NodeJS SDK for a provider, Pulumi will always use the plugin binary of the same version.
By having multiple versions of an SDK in our dependency graph, you will see multiple versions of the
default provider in your Pulumi state file as a result. The child `random` resources of components from your library
will be provisioned with plugin binary v3, while the top level `random` resources will use v4.

A similar situation would happen if you would pin the component library and the consuming project to explicit
but different versions. For instance, using `"4.11.0"` in the component library and `"4.14.0"` in the consuming
project would result in 2 default providers with exactly these versions.

If you only want to have a single version of the package and default provider, we suggest to use the caret
style notation in your component package. Use `^`, followed by the minimum version of the dependency, and
use a compatible version in your consuming project for your components to work correctly.
For instance, if `@pulumi/random` v4.8.2 contained a fix you rely on, use this in your library `package.json`:

```json
{
  "name": "components",
  "version": "1.0.0",
  ...
  "dependencies": {
    ...
    "@pulumi/random": "^4.8.2",
    ...
  },
  ...
}
```

When you use a version of `@pulumi/random` in your consuming project which is too old, NPM will warn you that you
need to upgrade.

## Package Documentation

In addition to the standard and cloud-agnostic packages the [Pulumi Registry](/registry/) houses 100+ Node.js packages.

### Standard Packages

<dl class="tabular">
    <dt>Pulumi SDK</dt>
    <dd><a href="/docs/reference/pkg/nodejs/pulumi/pulumi">@pulumi/pulumi</a></dd>
    <dt>Pulumi Policy</dt>
    <dd><a href="/docs/reference/pkg/nodejs/pulumi/policy">@pulumi/policy</a></dd>
    <dt>Pulumi Terraform</dt>
    <dd><a href="/docs/reference/pkg/nodejs/pulumi/terraform">@pulumi/terraform</a></dd>
</dl>

### Cloud-Agnostic Packages

<dl class="tabular">
    <dt>Pulumi Cloud Framework</dt>
    <dd>
        <a href="/docs/reference/pkg/nodejs/pulumi/cloud">@pulumi/cloud</a>
        <span class="ml-2 badge badge-preview">PREVIEW</span>
        <p>A highly productive, cloud-agnostic package for container and serverless programming.</p>
    </dd>
</dl>
