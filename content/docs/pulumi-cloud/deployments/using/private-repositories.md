---
title_tag: "Private Git Repositories | Pulumi Deployments"
meta_desc: Learn how to configure Pulumi Deployments to access private Git repositories
title: "Private Git Repositories"
h1: "Private Git Repositories"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    parent: pulumi-cloud-deployments-using
    weight: 3
---

When working with Pulumi Deployments, you may need to access private Git repositories.

## Private Dependency Packages

If your Pulumi Deployment requires access to private GitHub repositories, e.g. your program uses a private Go module, it is necessary to configure an SSH key with access to the required repos. Without the correct configuration, the Deployment will be unable to access those private artifacts, and the deployment may fail.

The following will allow you to configure a private key and allow access to GitHub using SSH to pull down the appropriate artifacts properly:

1. Add the following code into the `Pre-run commands` and toggle on `Skip automatic dependency installation step` in Advanced Settings:

    ```bash
    mkdir /root/.ssh && printf -- "$SSHKEY" > /root/.ssh/id_ed25519
    chmod 600 /root/.ssh/id_ed25519
    ssh-keyscan github.com >> ~/.ssh/known_hosts
     cd .. && git config --global --add url.\"git@github.com:\".insteadOf \"https://github.com\"
    ```

   ![SSH Key Prerun Command](../../limit-prerun-cmd.png)

2. Add the `$SSHKEY` field as a secret environment variable:

![SSH Key Env Variable](../../limit-env.png)
