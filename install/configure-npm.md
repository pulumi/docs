---
title: "Configure your NPM client"
---

While Pulumi is in private preview, `@pulumi` packages are not publicly available on npmjs.org. Use the following instructions to access them via the NPM proxy hosted at npmjs.pulumi.com. 

> **NOTE:** If you received an NPM token in your private beta welcome email, you may ignore it in favor of the simpler instructions below.

<!-- TODO WHITELIST: update this text when whitelist flow is eliminated -->
1.  Login in to the Pulumi Console and copy your [Pulumi access token](https://pulumi.com/account). (If you don't yet have an account, logging in will create an account for you.)

1.  Run the following commands, using the token you copied. This configures NPM to use a different registry for `@pulumi` packages.

    ```bash
    $ npm config set @pulumi:registry=https://npmjs.pulumi.com/
    $ npm config set //npmjs.pulumi.com/:_authToken=YOUR_PULUMI_TOKEN
    ```

> If you see an error such as `npm ERR! 403 Forbidden`, there is likely a problem with your NPM configuration. Open the file `.npmrc` in your home directory, and ensure it has only the following lines:
```
//npmjs.pulumi.com/:_authToken=YOUR_PULUMI_TOKEN
@pulumi:registry=https://npmjs.pulumi.com/
```
