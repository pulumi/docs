---
title: "Configure Your NPM Client"
---

While Pulumi is in private preview, `@pulumi` packages are not publicly available on npmjs.org, and must be accessed through the Pulumi NPM proxy hosted at npmjs.pulumi.com.

If you used the easy install script for Mac and Linux (available at [get.pulumi.com/install.sh](https://get.pulumi.com/install.sh)), no additional configuration is required. If you're on Windows or have used the manual installer, run this command in a terminal:

```bash
$ npm config set @pulumi:registry=https://npmjs.pulumi.com/
```
