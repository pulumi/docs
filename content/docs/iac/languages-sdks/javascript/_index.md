---
title_tag: "TypeScript and Node.js | Languages & SDKs"
meta_desc: Learn to use Node.js languages like JavaScript and TypeScript with Pulumi for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
title: TypeScript (Node.js)
h1: Pulumi & TypeScript & JavaScript (Node.js)
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: TypeScript (Node.js)
        parent: iac-languages
        weight: 1
        identifier: iac-languages-javascript
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
    - /docs/languages-sdks/javascript/
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

## TypeScript Versions

Pulumi ships with a bundled version of TypeScript 3.8.3 and uses this compiler by default. You can use a different version by adding the desired version of TypeScript to your package.json file. When Pulumi runs a TypeScript program, it will first attempt to load the compiler from the local node_modules directory, and then fallback to the bundled version. Pulumi supports all TypeScript versions from 3.8 and up, including the latest TypeScript 5 release.

```json
{
    "name": "my-package",
    "version": "1.0.0",
    "dependencies": {
        ...
        "typescript": "^5.4.2",
        ...
    }
}
```

## Disabling built in TypeScript support

You can disable the built in TypeScript support by changing the `runtime` setting in `Pulumi.yaml` to look like the following:

```yaml
runtime:
  name: nodejs
  options:
    typescript: false
```

## Native ESM Support

The default Pulumi templates compile TypeScript code to [CommonJS](https://nodejs.org/api/modules.html) modules. You can use ESM syntax like `import` or `export` in your code, but it will be compiled to CommonJS behind the scenes.

If you wish to instead use [ESM](https://nodejs.org/api/esm.html) natively, you can set the `type` field in your `package.json` to `module`. This will tell Node.js to treat your package as an ESM package.

```json
{
    "name": "my-package",
    "version": "1.0.0",
    "type": "module",
    ...
}
```

Your `tsconfig.json` file should also be updated to ensure that TypeScript outputs ESM, by setting the [`module`](https://www.typescriptlang.org/tsconfig/#module) and [`moduleResolution`](https://www.typescriptlang.org/tsconfig/#moduleResolution) fields to `nodenext`.

```json
{
    "compilerOptions": {
        ...
        "module": "nodenext",
        "moduleResolution": "nodenext",
        ...
    }
}
```

Install a recent version of `typescript` and `ts-node`.

```bash
npm install typescript@^5
npm install ts-node@^10
```

{{< notes >}}
When using a version of `@pulumi/pulumi` older than 3.183.0, you need to instruct Pulumi to use the `ts-node/esm` loader by setting the `nodeargs` option in the [`runtime`](https://www.pulumi.com/docs/iac/concepts/projects/project-file/#runtime-options) options in `Pulumi.yaml`. More recent versions automatically configure this.

```yaml
name: project-using-native-esm
runtime:
  name: nodejs
  options:
    nodeargs: "--loader ts-node/esm --no-warnings"
```

Note that if you provide any of the `--loader`, `--import` or `--require` arguments in `nodeargs`, Pulumi will not automatically configure an ESM loader, and you have to specify one yourself, for example `--loader ts-node/esm` as above, or `--import tsx` when using [tsx](https://tsx.is).

{{< /notes >}}

## Using ESM only modules with CommonJS Pulumi templates

Older versions of Node.js do not support loading ESM modules using the `require` function (`require` is part of CommonJS, the default runtime targetted by TypeScript in the Pulumi templates). You may encounter an error like the following:

`Error [ERR_REQUIRE_ESM]: require() of ES Module /Users/alice/pulumi/projects/esm-test-project/node_modules/@kubernetes/client-node/dist/index.js from /Users/alice/pulumi/projects/esm-test-project/index.ts not supported.`

To resolve this issue, you can either follow the instructions above to convert your project to ESM, or upgrade to a recent version of Node.js that supports `require`ing ESM modules. At time of writing this is at least [v20.19.0](https://github.com/nodejs/node/releases/tag/v20.19.0) (2025-03) or [v22.12.0](https://github.com/nodejs/node/releases/tag/v22.12.0) (2024-12).

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

## Dev Versions

Pulumi SDKs also publish pre-release versions, that include all the latest changes from the main development branch.  If you would like to install them, you can use the `dev` tag to do so.  For example using `npm` you can use `npm add @pulumi/pulumi@dev`, and similarly for `yarn` `yarn add @pulumi/pulumi@dev`.

## Package Documentation

The following reference documentation resources are available:

* The [Pulumi SDK `@pulumi/pulumi`](/docs/reference/pkg/nodejs/pulumi/pulumi) allows you to work with with basic Pulumi constructs. You will need to reference it in most Pulumi IaC programs.
* The [Pulumi Policy SDK `@pulumi/policy`](/docs/reference/pkg/nodejs/pulumi/policy) allows you to author Pulumi Policy as Code policies. You will need to reference it when authoring Pulumi Policy as code.
* For managing resources in a Pulumi IaC program, you can find the relevant SDK reference docs for a given provider in [the Pulumi Registry](/registry/).
