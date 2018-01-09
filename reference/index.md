---
layout: default
nav_section: "reference"
---

# Reference documentation

- [Using the Pulumi CLI](./cli-commands.html)
- [Using TypeScript](./typescript.html)
- [Known issues](./known-issues.html)

## Pulumi library packages

All Pulumi packages are available in your favorite package manager.  For now, this means NPM, since Pulumi only
supports JavaScript and TypeScript to start (although more languages are on their way).

The following three packages are included in the Pulumi Cloud SDK by default.  Before using any of them, please
remember to run `npm link <package>` or `yarn link <package>` in the consuming Cloud Application's root directory.

Below you will find detailed API documentation for these packages:

* [pulumi](../packages/pulumi)
* [@pulumi/aws](../packages/pulumi-aws)
* [@pulumi/cloud](../packages/pulumi-cloud)

