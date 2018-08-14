---
title: "JavaScript and TypeScript"
redirect_from: "npm-packages.html"
redirect_from: "install/configure-npm.html"

---

The fastest way to get started in JavaScript is using a template.  From the directory in which you'd like to create a new project:

```bash
$ pulumi new javascript
Your project was created successfully.
```

This will create a `Pulumi.yaml` [project file](./project.html), a `package.json` file for dependencies, and an `index.js` file, containing your program. The name of the directory is used as the project name in `Pulumi.yaml`.

## Pulumi packages

All Pulumi packages are regular NPM packages in the [`@pulumi` organization scope](https://www.npmjs.com/org/pulumi) on NPMJS.

To add a new package from the `@pulumi` namespace, run `npm install --save @pulumi/package-name`.  The following packages are available:

- [@pulumi/pulumi](https://www.npmjs.com/package/@pulumi/pulumi): the core Pulumi JavaScript SDK package
- [@pulumi/aws](https://www.npmjs.com/package/@pulumi/aws): the AWS resource provider package, for programming AWS directly
- [@pulumi/aws-infra](https://www.npmjs.com/package/@pulumi/aws-infra): infrastructure components on top of `@pulumi/aws`
- [@pulumi/aws-serverless](https://www.npmjs.com/package/@pulumi/aws-serverless): easily create Lambda functions that subscribe to AWS events
- [@pulumi/cloud](https://www.npmjs.com/package/@pulumi/cloud): Pulumi's high-level, cross-cloud programming framework
- [@pulumi/cloud-aws](https://www.npmjs.com/package/@pulumi/cloud-aws): the implementation package for Pulumi's cloud framework, for use when targeting AWS
- [@pulumi/kubernetes](https://www.npmjs.com/package/@pulumi/kubernetes): the Kubernetes resource provider package, for programming Kubernetes directly
- [@pulumi/azure](https://www.npmjs.com/package/@pulumi/azure): the Azure resource provider package, for programming Azure directly
- [@pulumi/gcp](https://www.npmjs.com/package/@pulumi/gcp): the Google Cloud Platform resource provider package

> **Note:** To use `@pulumi/cloud` on AWS, you must also include the package `@pulumi/cloud-aws`.

## Node.js runtime

Any Node.js version after 6.10.x is supported, as long it is under **Active LTS** or is the **Current** stable release.

## Using Pulumi configuration values

To use configuration values in JavaScript, use the [`pulumi.Config`] class. For more information, see [Using configuration values in JavaScript].

## TypeScript

You can elect to write Pulumi programs in TypeScript to get additional verification and tooling benefits. As of version 0.15.0, Pulumi supports TypeScript natively so you don't need to explicitly run `tsc` on your program before running `pulumi`

If you would like full control of the TypeScript build process, you can compile ahead of time, and point your package.json main entry point at the compiled JavaScript instead. If you do this, you can disable the [automatic compilation of TypeScript files](#disabiling-built-in-typescript-support).

The fastest way to get started with Pulumi in TypeScript, is to use a template:

```bash
$ pulumi new typescript
Your project was created successfully.
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

![Pulumi TypeScript in VS Code](../images/reference/vscode.png){:width="700px"}

## Disabiling built in TypeScript support

When using the built in TypeScript support, Pulumi sets the following compiler settings, which may not be overriden:

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
[`pulumi.Config`]: pkg/nodejs/@pulumi/index.html#Config
[Using configuration values in JavaScript]: ./config.html#javascript
<!-- END LINKS -->
