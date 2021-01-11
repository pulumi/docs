---
title: "Node.js (JavaScript, TypeScript)"
meta_desc: An overview of how to use Node.js languages like JavaScript and TypeScript for
           infrastructure as code on any cloud (AWS, Azure, GCP, Kubernetes, etc.).
menu:
  intro:
    parent: languages
    weight: 3

aliases: ["/docs/reference/javascript/"]
---

<img src="/logos/tech/logo-nodejs.png" align="right" width="150" style="padding:8px; margin-top: -64px">

Pulumi supports JavaScript programs running on Node.js using any of the [Current, Active and Maintenance LTS versions](https://nodejs.org/en/about/releases/).

Because programs are just JavaScript, you may elect to write them in any manner you'd normally write Node.js programs.
That includes TypeScript, CoffeeScript, or Babel, in addition to your favorite tools such as build systems, linters, or
test frameworks.

<a class="btn" href="https://nodejs.org/en/download/" target="_blank" title="Install Node.js">INSTALL NODE.JS</a>

## Getting Started

The fastest way to get started in JavaScript is using a template. From an empty directory in which you'd like to create a new project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new javascript
```

This will create a `Pulumi.yaml` [project file]({{< relref "../concepts/project" >}}), a `package.json` file for dependencies, and an `index.js` file, containing your program. The name of the directory is used as the project name in `Pulumi.yaml`.

## Pulumi Programming Model

The Pulumi programming model includes a core concept of `Input` and `Output` values, which are used to track how outputs of one resource flow in as inputs to another resource.  This concept is important to understand when getting started with JavaScript and Pulumi, and the [Inputs and Outputs]({{< relref "/docs/intro/concepts/inputs-outputs" >}}) documentation is recommended to get a feel for how to work with this core part of Pulumi in common cases.

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

Most Pulumi programs use the first option, but programs that need to do async work at the top level (such as calling [`getOutputValue`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#StackReference-getOutputValue" >}})) may find they want to use the second.

## TypeScript

You can elect to write Pulumi programs in TypeScript to get additional verification and tooling benefits. As of version 0.15.0, Pulumi supports TypeScript natively so you don't need to explicitly run `tsc` on your program before running `pulumi`

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
        "@types/node": "^10.0.0"
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

When using the built in TypeScript support, Pulumi sets the following compiler settings, which may not be overridden:

- target: "es6",
- module: "commonjs",
- moduleResolution: "node",
- sourceMap: "true",

If you need to change any of these settings, you can disable the built in TypeScript support by changing your the `runtime` setting in `Pulumi.yaml` to look like the following:

```yaml
runtime:
  name: nodejs
  options:
    typescript: false
```
