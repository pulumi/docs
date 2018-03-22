---
title: "▶ JavaScript and TypeScript"
redirect_from: "/concepts/npm-packages.html"
---

## Using Pulumi NPM Packages {#npm-packages}

As of release `0.10`, packages in the `@pulumi` namespace have been moved to an NPMJS registry, accessible through an NPM proxy.

The packages `@pulumi/pulumi`, `@pulumi/aws`, `@pulumi/cloud` and `@pulumi/cloud-aws` are regular NPM packages and should be specified in the `dependencies` section of `package.json`. As a best practice, Pulumi programs should only list the packages they strictly depend on.

For example, if a program used **all** the `@pulumi/*` packages, it would have the following `package.json`. 

```json
"dependencies": {
  "@pulumi/pulumi": "^0.10.0",
  "@pulumi/aws": "^0.10.0",
  "@pulumi/cloud": "^0.10.0",
  "@pulumi/cloud-aws": "^0.10.0"
}
```

### Installing packages 
To install NPM dependencies, do the following:

1.  Set up your login credentials for the Pulumi NPM proxy (see [Logging in to the Pulumi NPM proxy](#proxy-login)).

1.  Run `npm install` to restore `@pulumi` packages.

### Adding a new dependency {#packages}

To add a new package from the `@pulumi` namespace, run `npm install --save @pulumi/package-name`. The following packages are available. 

- `@pulumi/aws`
- `@pulumi/cloud`
- `@pulumi/cloud-aws`
- `@pulumi/pulumi`

> NOTE: to use `@pulumi/cloud` on AWS, you must also include the package `@pulumi/cloud-aws`.

> NOTE: versions of Pulumi packages prior to `0.10.0` are only supported via the `npm link` workflow.

## Logging in to the Pulumi NPM proxy {#proxy-login}

While Pulumi is in private preview, `@pulumi` packages are only available through the Pulumi NPM proxy. 

1.  To authenticate against this proxy, set the environment variable `PULUMI_ACCESS_TOKEN` to your [Pulumi access token](../managed-cloud/console.html#account-page).

1.  To configure your NPM client, add the following to `~/.npmrc`. Note that the `${PULUMI_ACCESS_TOKEN}` syntax will be auto-expanded by your NPM client.

    ```
    @pulumi:registry=https://npmjs.pulumi.com/
    //npmjs.pulumi.com/:_authToken=${PULUMI_ACCESS_TOKEN}
    ```

# TypeScript
You can write Pulumi programs in TypeScript to get additional verification and tooling benefits.  To use TypeScript,
apply the following four steps to an existing project.

### 1. Update package.json

Update your `package.json` to look like the following (with your own values for `name`, `version`, etc.).  This
is what tells Node.js and NPM what packages you depend on, where to find your code's entrypoints, and so on:

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
    "peerDependencies": {
        "@pulumi/aws": "*",
        "pulumi": "*"
    }
}
```

You can customize this however you'd like, such as adding test scripts, npm package dependencies, etc.  For more information on `package.json`, please refer to [the NPM documentation](https://docs.npmjs.com/files/package.json).

### 2. Install dependencies

Run `npm install` or `yarn install` to install the dependencies to your `node_modules` directory.

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
information on additional settings, see the [TypeScript documentation for `tsconfig.json`](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html.

### 4. Build

Before running `pulumi preview` or `pulumi update`, you should run `tsc` or `yarn build`. If you use Visual Studio Code, you can also do a continuous background build.

Tools like VS Code will give you completion lists, live error reporting and inline documentation help.

![Pulumi TypeScript in VS Code](../images/reference/vscode.png){:width="700px"}