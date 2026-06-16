---
title_tag: "Private Sources | Pulumi Deployments"
meta_desc: Configure Pulumi Deployments to access private Git repositories and private package feeds during a deployment.
title: "Private Sources"
h1: "Private Sources"
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
- /docs/pulumi-cloud/deployments/using/private-repositories/
- /docs/deployments/deployments/using/private-repositories/
menu:
  deployments:
    name: Private Sources
    parent: deployments-guides
    weight: 40
---

A Pulumi Deployment runs in an isolated environment that, by default, can only reach public repositories and package registries. If your program pulls code or packages from private sources, you need to give the deployment credentials to reach them. This page covers the two most common cases:

- **Private Git dependencies** — a Go module, a [Pulumi component](/docs/iac/concepts/components/), or any other dependency your program fetches directly from a private Git repository.
- **Private package feeds** — a private npm, PyPI, or NuGet registry that hosts your packages.

{{% notes type="info" %}}
This page is about private dependencies that a deployment pulls *during a run*. To deploy from a private repository that holds your Pulumi program itself, configure source control through the [Pulumi GitHub App](/docs/using-pulumi/continuous-delivery/github-app/) instead — that grants Pulumi Deployments access to the program's own repository.
{{% /notes %}}

## Private Git dependencies

When your program depends on code in another private Git repository — for example a private Go module, or a [component](/docs/iac/concepts/components/) referenced from a private repo — the deployment needs Git access to clone it. Configure an SSH key with read access to the required repositories and tell Git to use SSH for GitHub. The same mechanism works regardless of the language or the kind of dependency, because the deployment is ultimately performing a `git clone`.

1. Add the following code to the **Pre-run commands** and toggle on **Skip automatic dependency installation step** in **Advanced Settings**. This writes the SSH key, trusts GitHub's host key, and rewrites `https://github.com` URLs to use SSH so private clones authenticate with your key:

    ```bash
    mkdir /root/.ssh && printf -- "$SSHKEY" > /root/.ssh/id_ed25519
    chmod 600 /root/.ssh/id_ed25519
    ssh-keyscan github.com >> ~/.ssh/known_hosts
    cd .. && git config --global --add url.\"git@github.com:\".insteadOf \"https://github.com\"
    ```

1. Add `SSHKEY` as a **secret** environment variable on the deployment, with the contents of a private key that has read access to the repositories you need. Marking it secret ensures the value is encrypted and never shown in logs.

Because the `insteadOf` rule applies to all of GitHub, a single key with access to every required repository covers multiple private dependencies at once — there is no per-repository configuration to repeat.

## Private package feeds

If your dependencies come from a private package registry rather than a Git repository, authenticate to that registry instead of configuring SSH. Provide the registry token as a secret environment variable, then write the appropriate per-language configuration in the **Pre-run commands**:

- **npm**: Add the registry and auth token to a project `.npmrc`, for example:

    ```bash
    printf -- "//registry.example.com/:_authToken=%s\n@my-scope:registry=https://registry.example.com/\n" "$NPM_TOKEN" > .npmrc
    ```

- **PyPI**: Point `pip` at your index using a token-authenticated URL, for example via `PIP_INDEX_URL`:

    ```bash
    export PIP_INDEX_URL="https://__token__:$PYPI_TOKEN@pypi.example.com/simple"
    ```

- **NuGet**: Register the source with credentials:

    ```bash
    dotnet nuget add source https://nuget.example.com/v3/index.json --name private --username pulumi --password "$NUGET_TOKEN" --store-password-in-clear-text
    ```

In each case, store the token (`NPM_TOKEN`, `PYPI_TOKEN`, `NUGET_TOKEN`) as a **secret** environment variable so it is encrypted and kept out of logs. Leave **Skip automatic dependency installation step** off if you want Pulumi Deployments to install dependencies after your pre-run commands have configured the feed.
