---
title: "Run Pulumi with Any TypeScript Version"

date: 2024-04-16T10:28:28+02:00

draft: false

meta_desc: The latest version of Pulumi's Node.js SDK now lets you easily pick the version of TypeScript to use.

meta_image: meta.png

authors:
    - julien-poissonnier

tags:
    - typescript
    - nodejs
    - user-experience

---

Pulumi allows you to use the best features of programming languages to build your infrastructure while ensuring compatibility with your current development environments. To this end Pulumi provides a seamless experience when authoring TypeScript programs, managing the compilation of your program for you. With the latest release of our Node.js SDK, we've made this even more flexible by making it easier than ever to choose the version of TypeScript you want to use.

<!--more-->

Each new release of TypeScript comes with new features and improved type checking, as well as support for the latest JavaScript features. Using the latest version of TypeScript provides you with the maximum flexibility for creating types and gives you more confidence that your program will behave as expected.

Until now, Pulumi's seamless experience was limited to using Pulumi's builtin TypeScript version 3.8. If you wanted to use a more recent version, you had to introduce a build step to your project and let Pulumi run in [plain Javascript mode](https://www.pulumi.com/docs/languages-sdks/javascript/#disabling-built-in-typescript-support). With the release of the [Pulumi Node.js SDK 3.113.0](https://www.npmjs.com/package/@pulumi/pulumi) you can now use any version of TypeScript by adding it as a dependency to your project's `package.json` file.

Pulumi supports all TypeScript versions from 3.8 and up, including [TypeScript 5.4](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-4.html).

If you have an existing project, you can upgrade your project to the latest versions of TypeScript and Pulumi by running:

```bash
npm add typescript@^5.4.5 @pulumi/pulumi@^3.113.0
```

We have also updated our [Pulumi templates](https://github.com/pulumi/templates) to include the latest version of TypeScript. To create a new project, run:

```bash
pulumi new
```

Adding TypeScript as a dependency to your project is optional, as TypeScript and ts-node are optional peer dependencies of the Node.js SDK. This makes it easy to use a single version of TypeScript or ts-node within monorepos. To ensure backward compatibility, Pulumi ships with bundled versions of TypeScript 3.8 and ts-node 7, and falls back to these versions if they are not installed in your project's node modules.

## Example

Let's show an example of how to use one of TypeScripts's new features with Pulumi. TypeScript 4.1 introduced [Template Literal Types](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html), which allow you to build types using template literals. Imagine you wanted to enforce that names of S3 buckets are all lower case and always start with a given prefix. Of course you can check this at runtime, but with Template Literal Types this can be enforced during typechecking.

```typescript
type prefix = `acme_corp`
type BucketName = Lowercase<`${prefix}_${string}`>;
```

We can create a custom Bucket subclass that expects a name matching our new `BucketName` type.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

type prefix = `acme_corp`
type BucketName = Lowercase<`${prefix}_${string}`>;

class AcmeCorpBucket extends aws.s3.Bucket {
    constructor(name: BucketName, args?: aws.s3.BucketArgs, opts?: pulumi.CustomResourceOptions) {
        super(name, args, opts);
    }
}

const myBucketWrong = new AcmeCorpBucket("MyBucket");
// ❌ Fails typechecking with: Argument of type '"MyBucket"' is not assignable to parameter of type '`acme_corp_${Lowercase<string>}`'.ts(2345)

const myBucketWrongAgain = new AcmeCorpBucket("acme_corp_MyBucket");
// ❌ Fails typechecking with: Argument of type '"acme_corp_MyBucket"' is not assignable to parameter of type '`acme_corp_${Lowercase<string>}`'.ts(2345)

const myBucketCorrect = new AcmeCorpBucket("acme_corp_my_bucket");
// ✅ Passes typechecking
```

This example shows just one of [Typescript's many new features](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-4.html) that have shipped since version 3.8, and now all are available for you to use in your Pulumi programs without jumping through hoops.

## Conclusion

We recently shipped improved support for [Node.js monorepos](/blog/nx-monorepo/), and with the latest version of the Pulumi Node.js SDK, we further improved how Pulumi integrates into your development environment by letting you easily pick the version of TypeScript to use.
