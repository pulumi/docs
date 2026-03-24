---
title: "Introducing Bun as a Runtime for Pulumi"
date: 2026-03-23
draft: false
meta_desc: "Pulumi now supports Bun as a runtime for TypeScript programs, giving you faster startup times and a streamlined developer experience alongside Node.js."
meta_image: meta.png
feature_image: feature.png
authors:
    - julien-poissonnier
tags:
    - features
    - typescript
    - bun
schema_type: auto

# Optional: Social media promotional copy (for reference only, does not auto-post)
social:
    twitter:
    linkedin:
---

Last year we added support for [Bun as a package manager](/blog/bun-package-manager/) for Pulumi TypeScript projects. Today we're taking the next step: Bun is now a fully supported runtime for Pulumi programs. Set `runtime: bun` in your `Pulumi.yaml` and Bun will execute your entire Pulumi program, with no Node.js required. This was one of our [most requested features](https://github.com/pulumi/pulumi/issues/13904).

<!--more-->

## Why Bun?

[Bun](https://bun.sh/) is a JavaScript runtime designed as an all-in-one toolkit: runtime, package manager, bundler, and test runner. For Pulumi users, the most relevant advantages are:

- **Native TypeScript support**: Bun runs TypeScript directly without requiring [ts-node](https://typestrong.org/ts-node/) or a separate compile step.
- **Fast package management**: Bun's built-in package manager can install dependencies significantly faster than npm.
- **Node.js compatibility**: Bun [aims for 100% Node.js compatibility](https://bun.sh/docs/runtime/nodejs-apis), so the npm packages you already use with Pulumi should work out of the box.

With `runtime: bun`, Pulumi uses Bun for both running your program and managing your packages, giving you a streamlined single-tool experience.

## Getting started

To create a new Pulumi project with the Bun runtime, run:

```bash
pulumi new bun
```

This creates a TypeScript project configured to use Bun. The generated `Pulumi.yaml` looks like this:

```yaml
name: my-bun-project
runtime: bun
```

From here, write your Pulumi program as usual. For example, to create a random password using the `@pulumi/random` package:

```bash
bun add @pulumi/random
```

```typescript
import * as random from "@pulumi/random";

const password = new random.RandomPassword("password", {
    length: 20,
});

export const pw = password.result;
```

Then deploy with:

```bash
pulumi up
```

**Prerequisites:**

- [Bun](https://bun.sh/docs/installation) 1.3 or later
- [Pulumi](/docs/iac/download-install/) 3.227.0 or later

## Converting existing Node.js projects

If you have an existing Pulumi TypeScript project running on Node.js, you can convert it to use the Bun runtime in a few steps.

### 1. Update `Pulumi.yaml`

Change the `runtime` field from `nodejs` to `bun`:

Before:

```yaml
runtime:
  name: nodejs
  options:
    packagemanager: npm
```

After:

```yaml
runtime: bun
```

{{% notes type="info" %}}
When the runtime is set to `bun`, Bun is also used as the package manager — there's no need to configure a separate `packagemanager` option.
{{% /notes %}}

### 2. Update `tsconfig.json`

Bun handles TypeScript differently from Node.js with `ts-node`. Update your `tsconfig.json` to use [Bun's recommended compiler options](https://bun.sh/docs/typescript#suggested-compileroptions):

```json
{
    "compilerOptions": {
        "lib": ["ESNext"],
        "target": "ESNext",
        "module": "Preserve",
        "moduleDetection": "force",
        "moduleResolution": "bundler",
        "allowJs": true,
        "allowImportingTsExtensions": true,
        "verbatimModuleSyntax": true,
        "strict": true,
        "skipLibCheck": true,
        "noFallthroughCasesInSwitch": true,
        "noUncheckedIndexedAccess": true,
        "noImplicitOverride": true
    }
}
```

Key differences from a typical Node.js `tsconfig.json`:

- **[`module: "Preserve"`](https://www.typescriptlang.org/tsconfig/#module)** and **[`moduleResolution: "bundler"`](https://devblogs.microsoft.com/typescript/announcing-typescript-5-0/#moduleresolution-bundler)**: Let Bun handle module resolution instead of compiling to CommonJS. The `bundler` resolution strategy allows extensionless imports while still respecting `package.json` exports, matching how Bun resolves modules in practice.
- **[`verbatimModuleSyntax: true`](https://www.typescriptlang.org/tsconfig/#verbatimModuleSyntax)**: Enforces consistent use of ESM `import`/`export` syntax. TypeScript will flag any remaining CommonJS patterns like `require()` at compile time.

### 3. Switch to ESM

Bun makes it easy to go full ESM and it's the [recommended module format](https://bun.sh/docs/runtime/module-resolution) for Bun projects. Add `"type": "module"` to your `package.json`:

```json
{
    "type": "module"
}
```

With [ECMAScript module (ESM)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) syntax, one place that needs updating is the [program entrypoint](/docs/iac/languages-sdks/javascript/#enabling-async-support). In CommonJS TypeScript projects, async programs are written using `export =`. In ESM, you use a standard `export default` instead:

```typescript
// CommonJS (Node.js default)
export = async () => {
    const bucket = new aws.s3.BucketV2("my-bucket");
    return { bucketName: bucket.id };
};

// ESM (used with Bun)
export default async () => {
    const bucket = new aws.s3.BucketV2("my-bucket");
    return { bucketName: bucket.id };
};
```

That said, the main reason to use an async entrypoint function in CommonJS is to be able to `await` data sources and other async calls before declaring resources. In ESM — including Bun — [top-level `await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#top_level_await) just works, so you can skip the wrapper function entirely and `await` directly at the module level:

```typescript
import * as aws from "@pulumi/aws";

const azs = await aws.getAvailabilityZones({ state: "available" });

const buckets = azs.names.map(az => new aws.s3.BucketV2(`my-bucket-${az}`));

export const bucketNames = buckets.map(b => b.id);
```

### 4. Update the Pulumi SDK

Make sure you're running `@pulumi/pulumi` version 3.226.0 or later:

```bash
bun add @pulumi/pulumi@latest
```

### 5. Install dependencies and deploy

```bash
pulumi install
pulumi up
```

## Bun as runtime vs. Bun as package manager

With this release, there are now two ways to use Bun with Pulumi:

| Configuration | Bun's role | Node.js required? |
|---|---|---|
| `runtime: bun` | Runs your program and manages packages | No |
| `runtime: { name: nodejs, options: { packagemanager: bun } }` | Manages packages only | Yes |

Use `runtime: bun` for the full Bun experience. The package-manager-only mode is still available for projects that need Node.js-specific features like function serialization.

## Known limitations

The following Pulumi features are not currently supported when using the Bun runtime:

{{% notes type="warning" %}}

- **[Callback functions (magic lambdas)](/docs/iac/clouds/aws/guides/lambda/)** are not supported. APIs like `aws.lambda.CallbackFunction` and event handler shortcuts (e.g., `bucket.onObjectCreated`) use [function serialization](/docs/iac/concepts/functions/function-serialization/) which requires Node.js `v8` and `inspector` modules that are only partially supported in Bun.
- **[Dynamic providers](/docs/iac/concepts/providers/dynamic-providers/)** are not supported. Dynamic providers (`pulumi.dynamic.Resource`) similarly rely on [function serialization](/docs/iac/concepts/functions/function-serialization/).

{{% /notes %}}

If your project uses any of these features, continue using `runtime: nodejs`. You can still benefit from Bun's fast package management by setting `packagemanager: bun` in your runtime options.

## Start using Bun with Pulumi

Bun runtime support is available now in [Pulumi 3.227.0](/docs/iac/download-install/). To get started:

- Create a new project: `pulumi new bun`
- Read the docs: [TypeScript (Node.js) SDK](/docs/iac/languages-sdks/javascript/)
- Report issues or share feedback on [GitHub](https://github.com/pulumi/pulumi/issues) or in the [Pulumi Community Slack](https://slack.pulumi.com)

Thank you to everyone who upvoted, commented on, and contributed to [the original feature request](https://github.com/pulumi/pulumi/issues/13904). Your feedback helped shape this feature, and we'd love to hear how it works for you.
