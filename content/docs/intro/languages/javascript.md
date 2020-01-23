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

Pulumi supports JavaScript programs running on Node.js version 8 and later.

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

This will create a `Pulumi.yaml` [project file]({{< relref "project" >}}), a `package.json` file for dependencies, and an `index.js` file, containing your program. The name of the directory is used as the project name in `Pulumi.yaml`.

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
        "@types/node": "^8.0.26"
    },
    "dependencies": {
        ... as before ...
    }
}
```

You can customize this however you'd like, such as adding test scripts, npm package dependencies, etc.  For more information on `package.json`, please refer to [the NPM documentation](https://docs.npmjs.com/files/package.json).

### 2. Install dependencies

Run `npm install` or `yarn install` to install the new development-time dependencies to your `node_modules` directory.

### 3. Create tsconfig.json

When using Pulumi's built in TypeScript support, a `tsconfig.json` file is optional. However, defining one allows your to set additional TypeScript compiler options, for example not allowing implicit returns from a function. In addition, other tools like VS Code will use these settings to give you additional warnings at development time. Any options set in your `tsconfig.json` file will be picked up by Pulumi. We recommend creating a `tsconfig.json` file with the following settings:

```json
{
    "compilerOptions": {
        "outDir": "bin",
        "target": "es6",
        "lib": [
            "es6"
        ],
        "module": "commonjs",
        "moduleResolution": "node",
        "declaration": true,
        "sourceMap": true,
        "stripInternal": true,
        "experimentalDecorators": true,
        "pretty": true,
        "noFallthroughCasesInSwitch": true,
        "noImplicitAny": true,
        "noImplicitReturns": true,
        "forceConsistentCasingInFileNames": true,
        "strictNullChecks": true
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

<!-- LINKS -->
[`pulumi.Config`]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config" >}}
[Using configuration values in JavaScript]: {{< relref "config#javascript" >}}
<!-- END LINKS -->
