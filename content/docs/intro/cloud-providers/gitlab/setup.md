---
title: GitLab Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi GitLab Provider.
---

The [Pulumi GitLab provider]({{< prelref "./" >}}) uses the GitLab SDK to manage and provision resources.

> Pulumi relies on the GitLab SDK to authenticate requests from your computer to GitLab. Your credentials are never sent
> to pulumi.com.

The [Pulumi GitLab Provider]({{< prelref "./" >}}) needs to be configured with GitLab credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `GITLAB_TOKEN`:

    ```bash
    $ export GITLAB_TOKEN=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set gitlab:token XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `gitlab:token` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-gitlab/blob/master/README.md).
