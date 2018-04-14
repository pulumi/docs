---
title: "JavaScript and TypeScript"
redirect_from: "/concepts/npm-packages.html"
---

<!-- LINKS -->
[Configure your NPM client]: ../install/configure-npm.html
[`pulumi.Config`]: ./packages/pulumi/classes/_config_.config.html
[Using configuration values in JavaScript]: ./config.html#javascript
<!-- END LINKS -->

## Getting Started

The fastest way to get started with Pulumi JavaScript is by using a template.  From the directory in which you'd like to create a new project:

```
$ pulumi new javascript
Your project was created successfully.
```

This will leave behind a `Pulumi.yaml` file, containing some minimal metadata about your project (including a name and description which you may wish to change), a `package.json` file, where you will specify your dependencies (see #npm-packages below), and an `index.js` file, containing your program.

## Using Pulumi NPM Packages {#npm-packages}

The first thing you'll want to do is install the Pulumi SDK package.  This is listed in the template's `package.json` file.  Normally you'd just run `npm install` or `yarn install` at this time, however to use any `@pulumi` packages, you'll first need to follow the instructions in [Configure your NPM client].

> **Note:** Because Pulumi is still in Private Beta, packages aren't publicly available on NPM yet.  This is why the manual NPM client configuration is required.  As soon as Pulumi is public, all packages will be too.

All Pulumi packages are regular NPM packages, and live in the `@pulumi` organization scope.  The four most commonly used packages are `@pulumi/pulumi`, `@pulumi/aws`, `@pulumi/cloud` and `@pulumi/cloud-aws`, and they are specified as usual in the `dependencies` section of `package.json`.

For example, if a program used **all** the `@pulumi/*` packages, it would have the following `package.json`. 

```json
"dependencies": {
    "@pulumi/pulumi": "^0.11.0",
    "@pulumi/aws": "^0.11.0",
    "@pulumi/cloud": "^0.11.0",
    "@pulumi/cloud-aws": "^0.11.0"
}
```

Most of the time, you will not need to use all of the packages.  To install the resulting dependencies, run `npm install` as usual, and they will be downloaded and placed into `node_modules`.  If you'd like to update an existing project's dependencies and check for newer versions, simply run `npm install --update`.

> **Note:** If you see an error such as `npm ERR! 403 Forbidden: @pulumi/pulumi@^0.11.0`, that means that your NPM client is not configured with the correct token. Follow the steps in instructions in [Configure your NPM client].

### Adding a new dependency {#packages}

To add a new package from the `@pulumi` namespace, run `npm install --save @pulumi/package-name`.  The following packages are available:

- `@pulumi/pulumi`: the core Pulumi JavaScript SDK package
- `@pulumi/aws`: the AWS resource provider package, for programming AWS directly
- `@pulumi/azure`: the Azure resource provider package, for programming Azure directly
- `@pulumi/kubernetes`: the Kubernetes resource provider package, for programming Kubernetes directly
- `@pulumi/cloud`: Pulumi's high-level, cross-cloud programming framework
- `@pulumi/cloud-aws`: the implementation package for Pulumi's cloud framework, for use when targeting AWS

> **Note:** To use `@pulumi/cloud` on AWS, you must also include the package `@pulumi/cloud-aws`.

More packages are on their way, so please keep an eye out.  Please also let us know if there are specific packages you'd like to see sooner!

## Node.js runtime

Any Node.js version after 6.10.x is supported, as long it is under **Active LTS** or is the **Current** stable release.

## Using Pulumi configuration values

To use configuration values in JavaScript, use the [`pulumi.Config`] class. For more information, see [Using configuration values in JavaScript].

## TypeScript

You can elect to write Pulumi programs in TypeScript to get additional verification and tooling benefits.  To use TypeScript, some additional steps are required, because you will be compiling code using the TypeScript compiler.

The fastest way to get started with Pulumi in TypeScript, is to use a template:

```
$ pulumi new typescript
Your project was created successfully.
```

This will auto-generate all the basic artifacts required to use TypeScript.  But you may also perform the steps manually if you prefer.

### 1. Update package.json

Update your `package.json` to look like the following (with your own values for `name`, `version`, etc.).  This
is what tells Node.js and NPM what packages you depend on, where to find your code's entry points, and so on:

```json
{
    "name": "my-package",
    "version": "1.0.0",
    "main": "bin/index.js",
    "typings": "bin/index.d.ts",
    "scripts": {
        "build": "tsc"
    },
    "devDependencies": {
        "typescript": "^2.5.3",
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

Create a `tsconfig.json` file with the TypeScript compiler settings and a list of your program files:

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

### 4. Build

Before running `pulumi preview` or `pulumi update`, you should run `tsc` or `yarn build`. If you use Visual Studio Code, you can also do a continuous background build.

Tools like VS Code will give you completion lists, live error reporting and inline documentation help.

![Pulumi TypeScript in VS Code](../images/reference/vscode.png){:width="700px"}
