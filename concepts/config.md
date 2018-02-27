---
title: "Configuration"
---

Often, your Colada program will need configuration values that change independently from the program itself. For instance, you may want to use a different size of AWS EC2 instance depending on whether the program is deployed to a development or production stack. 

Settings that are specific to a stack are defined in `Pulumi.yaml` and are set via the `pulumi config` verbs. 

## Defining stack settings {#config-stack}

To add a new stack setting in plaintext, 

## Using configuration values in code



## Additional

Features to document
- Any environment variables that are set locally will be passed to the running program
- Read config from stdin (useful for secrets and public keys). See https://github.com/pulumi/pulumi/issues/670#issuecomment-364835504. See https://github.com/pulumi/pulumi/issues/822 for a example of how you might use it with a public key.
- 