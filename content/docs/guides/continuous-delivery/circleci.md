---
title: CircleCI
meta_desc: This page details how to use CircleCI CI/CD to deploy Pulumi stacks.
menu:
    userguides:
        parent: cont_delivery
        weight: 1

aliases:
- /docs/reference/cd-circleci/
- /docs/console/continuous-delivery/circleci/
---

This page details how to use [CircleCI](https://circleci.com/) to deploy Pulumi stacks.

You can refer to [CircleCI's documentation](https://circleci.com/docs/2.0/config-intro/#section=configuration)
for information on how to configure your CircleCI jobs and workflows.

When it comes to integrating Pulumi, just like Like other CI/CD services, it is generally a matter
of downloading the Pulumi command-line tool and running `pulumi up` from within the CircleCI
environment. However, [Pulumi Orbs for CircleCI](https://circleci.com/orbs/registry/orb/pulumi/pulumi)
enable a standard way to do this integration, without needing any custom scripting.

## Pulumi Orbs

The Pulumi orbs for CircleCI takes care of the mechanics of downloading and installing the Pulumi
command-line tool, so that you can just focus on the specific steps to deploy your stacks within
your CircleCI configuration.

> For the most up-to-date information about Pulumi orbs, refer to the Pulumi page within the CircleCI
> orb registry at [https://circleci.com/orbs/registry/orb/pulumi/pulumi](https://circleci.com/orbs/registry/orb/pulumi/pulumi).

The following CircleCI `config.yaml` shows the Pulumi orbs in-action. It references the
`pulumi/pulumi@1.0.0` orb package, and then downloads starts Pulumi using the  `pulumi/login` orb,
and finally updates a stack using the `pulumi/update` orb.

```yaml
version: 2.1
orbs:
  pulumi: pulumi/pulumi@1.0.0
jobs:
  build:
    docker:
      - image: circleci/node:7.10
    working_directory: ~/repo
    steps:
      - checkout
      - pulumi/login
      - run:
          command: |
            npm install
            npm run build
      - pulumi/update:
          stack: website-prod
```

Integrating Pulumi into CircleCI starts with the `pulumi/login` orb, which will take care of
downloading the Pulumi command-line tool if it is not on the current `$PATH`. It will then run
`pulumi login` using available credentials.

You can either specify the Pulumi access token with the `access-token` parameter, or default to using
the `$PULUMI_ACCESS_TOKEN` environment variable. Using the environment variable is preferred, as you
can secure store that using secure [project-level configuration](https://circleci.com/docs/2.0/env-vars/#setting-an-environment-variable-in-a-project) within CircleCI.

### Reference

The full [reference documentation](https://github.com/pulumi/circleci#orb-reference) for the Pulumi
orbs can be found along side their source code [on Github](https://github.com/pulumi/circleci).
