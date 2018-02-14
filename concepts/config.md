---
title: "Configuration"
---

Often, your Placeholder program will need configuration values that change independently from the program itself. For instance, you may want to use a different size of AWS EC2 instance depending on whether the program is deployed to a development or production stack. 

Settings that are specific to a stack are defined in `Pulumi.yaml` and are set via the `pulumi config` verbs. 



## Defining stack settings {#config-stack}

## Additional

Features to document
- Read config from stdin (useful for secrets and public keys). See https://github.com/pulumi/pulumi/issues/670#issuecomment-364835504
- 