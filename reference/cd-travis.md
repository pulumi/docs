---
title: Travis
---

If you are using Travis as your CI system, follow the below instructions to get up and running with Pulumi for CD.

## Example Scripts

We will be using the scripts from [our Travis examples on GitHub](
https://github.com/pulumi/examples/tree/master/misc/travis).  There is currently only a single script:

* [`update-stack.sh`](https://github.com/pulumi/examples/blob/master/misc/travis/update-stack.sh) demonstrates the
  recommended way to build and invoke the Pulumi CLI to perform deployments based on your branching structure.

Please make sure to review `update-stack.sh` very carefully, as it contains policy around which branches map to
which Pulumi stacks.  You will want to customize this.

## Configuring Travis

First, add your Pulumi access token to your Travis settings as the `PULUMI_ACCESS_TOKEN` environment variable, either
via the `travis.yml` file, Travis CLI, or the Travis Web UI, however you typically do it ([see here for more
information](https://docs.travis-ci.com/user/environment-variables/)).  This ensures that you can login to the service.

> **Note:** You'll also need to configure your cloud provider credentials in the same way you do on your development
> machines.  This most often means provisioning a key specifically for CI, and then setting the environment variables so
> that the Travis machine can perform the necessary operations.  If you are using AWS, for example, you'll want to set
> `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.  Please consult your cloud provider's documentation.

Next, add three things to your `travis.yml` file.

1. In the `before_install` section, add a line to install the Pulumi version you're currently using, put it on the
`$PATH`, initialize the workspace, and then login to the service:

    ```yaml
    before_install:
        # Install the Pulumi SDK, add it to the $PATH, and initialize the workspace.
        - curl -L https://get.pulumi.com | bash -s -- --version 0.14.2
        - export PATH=$PATH:$HOME/.pulumi/bin
        - pulumi init
    ```

1. Add the line to perform the Pulumi update to the `script` section:

    ```yaml
    script:
        # Pre-deployment verification goes here ...
        # After any tests have been performed, do the Pulumi deployment:
        - ./scripts/update-stack.sh
        # Post-deployment verification goes here ...
    ```

After doing this, any pushes to the branches you have configured will perform CD using Pulumi.
