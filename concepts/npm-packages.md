---
title: "Pulumi NPM packages"
---

## Referencing packages from your Pulumi program

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

### Adding a new dependency

To add a new package from the `@pulumi` namespace, run `npm install @pulumi/package-name`. The following packages are available. 

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
