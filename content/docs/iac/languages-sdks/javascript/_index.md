---
title_tag: "TypeScript and Node.js | Languages & SDKs"
meta_desc: Learn to use Node.js languages like JavaScript and TypeScript with Pulumi for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
title: TypeScript (Node.js)
h1: Pulumi & TypeScript (Node.js)
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

Pulumi supports writing your infrastructure as code using TypeScript and JavaScript on the Node.js runtime. Using a general-purpose language for infrastructure as code provides several key advantages:

- **Familiar syntax**: Write infrastructure code using the same languages and patterns you already know
- **Rich ecosystem**: Leverage the vast npm package ecosystem in your infrastructure code
- **Native tooling**: Use your existing IDE, linters, test frameworks, and other development tools without requiring plugins or extensions
- **Type safety**: When using TypeScript, catch errors at development time with strong typing and IntelliSense

## Installation requirements

### Runtime

Pulumi supports Node.js [Current, Active, and Maintenance LTS versions](https://nodejs.org/en/about/previous-releases). We recommend using the latest LTS version for the best experience.

### Package managers

Pulumi supports the following package managers:

- **npm**: Fully supported (default)
- **Yarn 1 (Classic)**: Fully supported
- **pnpm**: Fully supported
- **Bun**: Supported as a package manager only (not as a runtime)

{{< notes type="info" >}}
Dynamic providers may not work correctly with all package managers. If you encounter issues with dynamic providers, try using npm or Yarn 1.
{{< /notes >}}

Pulumi defaults to using npm. However, if Pulumi detects a `yarn.lock` file in the project root, or the environment variable `PULUMI_PREFER_YARN=true`, Pulumi will use Yarn instead if available. For pnpm, ensure `pnpm-lock.yaml` is present, and for Bun, ensure `bun.lockb` is present.

Pulumi does not support Yarn Plug'n'Play.

### Languages

Pulumi fully supports both TypeScript and JavaScript. You can use either language to write your Pulumi programs:

- **TypeScript**: Get additional type safety and IDE support with TypeScript (recommended)
- **JavaScript**: Write programs using standard JavaScript syntax

{{< notes type="info" >}}
While Pulumi supports JavaScript and any other language that compiles to JavaScript and runs on Node.js, our documentation examples and templates are primarily maintained in TypeScript. For the most consistent experience and up-to-date examples, we recommend using TypeScript.
{{< /notes >}}

Pulumi ships with a bundled version of TypeScript 3.8.3 for backward compatibility. However, Pulumi templates typically include a more recent TypeScript version in their `package.json`, which will take precedence over the bundled version. You can use any TypeScript version from 3.8 onwards, including the latest TypeScript 5 releases.

The Pulumi SDK is available to Node.js developers as an npm package. To learn more, refer to the [Pulumi SDK reference guide](/docs/reference/pkg/nodejs/pulumi/pulumi).

## Getting started

The fastest way to get started with Pulumi and Node.js is to use a TypeScript template:

```bash
$ pulumi new typescript
```

You can discover additional templates by running `pulumi new` with no arguments, or you can initialize a Pulumi program by supplying a specific URL to the `pulumi new` command. For example:

```bash
$ pulumi new https://github.com/pulumi/templates/tree/master/aws-typescript
```

See the [`pulumi new` documentation](/docs/iac/cli/commands/pulumi_new/) for full details.

### Program entrypoint

Pulumi executes your program by internally loading the entrypoint file as a Node module: `require("index.ts")`. By default, Pulumi will load `index.ts` or `index.js`. Alternatively, if you specify `main` within your `package.json`, Pulumi will load that module instead:

```json
{
    "name": "my-package",
    "version": "1.0.0",
    ...
    "main": "src/entry.ts"
}
```

{{< chooser language "typescript,javascript" >}}

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

{{< /chooser >}}

### Enabling async support

If you want to enable use of the `async` keyword, your entrypoint can export a top level `async` function that returns an object with members for each stack output. Pulumi will automatically call this function and await the result:

{{< chooser language "typescript,javascript" >}}

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

## Defining resources

Writing a Pulumi program in Node.js involves declaring infrastructure resources using resource constructors. Here are the key concepts:

- **Declare resources**: Create infrastructure resources by instantiating resource classes from provider packages. For example, `new aws.s3.Bucket("my-bucket")` creates an S3 bucket.
- **Inputs and outputs**: The Pulumi programming model uses `Input` and `Output` types to track dependencies between resources. Understanding how to work with inputs and outputs is essential for building infrastructure. See the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation for details.
- **Immutable infrastructure**: Once declared, resource properties are immutable within your program. Changes to resource definitions result in updates during the next deployment.
- **Stack outputs**: Export values from your program to make them accessible from the CLI or to other Pulumi programs. These are defined using module exports as shown in the entrypoint examples above.

The Pulumi SDK provides constructs for working with key Pulumi concepts. For more information, see:

- [Pulumi Concepts](/docs/iac/concepts/)
- [How Pulumi Works](/docs/iac/concepts/how-pulumi-works/)

## Program execution

Pulumi programs are most commonly executed using the Pulumi CLI commands such as `pulumi up`, `pulumi preview`, and `pulumi destroy`. The CLI handles authentication, state management, and orchestrating resource operations.

Alternatively, you can use the [Automation API](/docs/using-pulumi/automation-api/) to programmatically control the Pulumi engine from within your Node.js code. The Automation API allows you to:

- Embed Pulumi operations in regular Node.js applications
- Build custom deployment tools and workflows
- Create self-service infrastructure platforms

With Automation API, your Node.js code controls Pulumi, rather than Pulumi controlling your code.

## TypeScript

Pulumi supports TypeScript natively, so you don't need to explicitly run `tsc` on your program before running `pulumi`. When using Pulumi's built-in TypeScript support, a `tsconfig.json` file is optional, but defining one allows you to set additional TypeScript compiler options and enables better IDE integration. Any options set in your `tsconfig.json` file will be picked up by Pulumi.

If you would like full control of the TypeScript build process, you can compile ahead of time and point your `package.json` main entry point at the compiled JavaScript instead. If you do this, you can disable the [automatic compilation of TypeScript files](#disabling-built-in-typescript-support).

For information on configuring TypeScript, see the [TypeScript documentation for `tsconfig.json`](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html).

### TypeScript versions

Pulumi ships with a bundled version of TypeScript 3.8.3 for backwards compatibility. However, when Pulumi runs a TypeScript program, it will first attempt to load the compiler from the local `node_modules` directory, and then fall back to the bundled version. This means that if your `package.json` includes a TypeScript dependency (as Pulumi templates typically do), that version will be used instead.

Pulumi supports all TypeScript versions from 3.8 onwards, including the latest TypeScript 5 releases.

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

### Disabling built-in TypeScript support

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

## Documentation and resources

### Pulumi SDK

The [Pulumi SDK (`@pulumi/pulumi`)](/docs/reference/pkg/nodejs/pulumi/pulumi) contains the core constructs for working with Pulumi, including resources, configuration, stack outputs, and more. You will need to reference it in most Pulumi programs.

Pulumi SDKs also publish pre-release versions that include all the latest changes from the main development branch. If you would like to install them, you can use the `dev` tag. For example:

```bash
npm add @pulumi/pulumi@dev
```

Or with yarn:

```bash
yarn add @pulumi/pulumi@dev
```

### Policy SDK

The [Pulumi Policy SDK (`@pulumi/policy`)](/docs/reference/pkg/nodejs/pulumi/policy) allows you to author Pulumi Policy as Code policies for validating resource configurations.

### Provider packages

For managing resources in a Pulumi program, you can find the relevant SDK reference documentation for each provider in [the Pulumi Registry](/registry/).

When building component packages, see [Provider package version management](./provider-package-versions/) for guidance on handling provider package versions across component boundaries.

### Testing

- [Unit testing](/docs/iac/concepts/testing/unit/): Test your infrastructure code in isolation
- [Integration testing](/docs/iac/concepts/testing/integration/): Test your infrastructure deployments end-to-end
