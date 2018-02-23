---
title: "Pulumi NPM packages"
---

## Referencing packages from your Pulumi program

As of release `0.10`, packages in the `@pulumi` namespace have been moved to an NPMJS registry, accessible through an NPM proxy. The package `pulumi` still uses the `npm link` workflow. 

The packages `@pulumi/aws`, `@pulumi/cloud` and `@pulumi/cloud-aws` are regular NPM packages and should be specified in the `dependencies` section of `package.json`. As a best practice, Pulumi programs should only list the packages they strictly depend on.

> NOTE: In the next major release, the `pulumi` package will be moved to the same NPM workflow as the other packages.

For example, if a program used **all** the `@pulumi/*` packages, it would have the following `package.json`. 

```json
"dependencies": {
  "@pulumi/aws": "^0.10.0",
  "@pulumi/cloud": "^0.10.0",
  "@pulumi/cloud-aws": "^0.10.0"
},
"peerDependencies": {
  "pulumi": "latest"
},
```

### Installing packages 
To install npm dependencies, do the following:

1.  Set up your login credentials for the Pulumi NPM proxy (see [Logging in to the Pulumi NPM proxy](#proxy-login)).

1.  Run `npm install` to restore `@pulumi` packages.

1.  Run `npm link pulumi` to install the `pulumi` peer dependency. Note that `npm link` must always be re-run whenever you run `npm install`.

### Adding a new dependency

To add a new package from the `@pulumi` namespace, run `npm install @pulumi/package-name`. The following packages are available. 

- `@pulumi/aws`
- `@pulumi/cloud`
- `@pulumi/cloud-aws`

> NOTE: versions of Pulumi packages prior to `0.10.0` are only supported via the `npm link` workflow.

## Logging in to the Pulumi NPM proxy {#proxy-login}

While Pulumi is in private preview, `@pulumi` packages are only available through the Pulumi NPM proxy. 

1.  To authenticate against this proxy, set the environment variable `PULUMI_ACCESS_TOKEN` to your [Pulumi access token](../managed-cloud/console.html#account-page).

1.  To configure your NPM client, add the following to `~/.npmrc`. Note that the ${PULUMI_ACCESS_TOKEN} syntax is valid and will be auto-expanded by the NPM client.

    ```
    @pulumi:registry=https://npmjs.pulumi.com/
    //npmjs.pulumi.com/:_authToken=${PULUMI_ACCESS_TOKEN}
    ```
