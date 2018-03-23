---
title: "▶ Configure your NPM client"
---

While Pulumi is in private preview, `@pulumi` packages are not publicly available on npmjs.org. If you are a customer of the Pulumi Managed Cloud beta, use the [Pulumi NPM proxy](#proxy-login). Otherwise, follow the steps in [Authenticate with an NPM token](#configure-npmrc).

## Authenticate to the Pulumi NPM proxy {#proxy-login}

These steps are for customers of the Pulumi Managed Cloud beta.

1.  Login in to the Pulumi Console and copy your [Pulumi access token](../managed-cloud/console.html#account-page).

1.  Set the environment variable `PULUMI_ACCESS_TOKEN` to the value you copied, in either `~/.bashrc` or in  System Properties on Windows.

1.  Add the following to `$HOME/.npmrc`. Note that the `${PULUMI_ACCESS_TOKEN}` syntax will be auto-expanded by your NPM client.

    ```
    @pulumi:registry=https://npmjs.pulumi.com/
    //npmjs.pulumi.com/:_authToken=${PULUMI_ACCESS_TOKEN}
    ```

## Authenticate with an NPM token {#configure-npmrc}

Use the NPM token provided to you when you joined the private beta.

-   If you already use NPM with private packages, create an `.npmrc` file in your project directory. See [npmrc documentation](https://docs.npmjs.com/files/npmrc).

-   Otherwise, run `npm config` to set the token globally:

    ```
    $ npm config set //registry.npmjs.org/:_authToken YOUR_TOKEN_HERE
    ```
