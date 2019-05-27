---
title: Pulumi GitHub App
aliases: ["cd-github.html"]
expanded_url: /reference/service/
menu:
  reference:
    parent: teams
    weight: 4
---

<style>
    .img-bordered {
        border: 2px solid rgba(0,0,0,0.15);
    }
    .move-right {
        margin-left: 32px;
    }
    .move-right-small {
        margin-left: 8px;
    }
</style>

Pulumi's GitHub app integrates the results of Pulumi stack updates with GitHub. Once installed and
configured, it will show you any potential infrastructure changes on Pull Requests and commit Checks.
[See below](https://github.com/apps/pulumi) for information on how to install the Pulumi GitHub app
into your organization.

## Features

The Pulumi GitHub app will automatically add comments to Pull Requests with the results of any
stack changes. This includes a summary of how many resources were created, updated, and/or deleted.
This allows you to quickly see the changes caused by your Pulumi program without needing to leave
GitHub's Pull Request view, with a link to the richer details available on the
[Pulumi Cloud Console](https://app.pulumi.com).

<img src="/images/github-app/pr-comment.png" alt="Comment on Pull Request" class="img-bordered move-right">

Beyond Pull Request comments, the GitHub application also integrates with GitHub's [Checks API](https://blog.github.com/2018-05-07-introducing-checks-api/).
This provides even more detail about any resource changes, including the full update log.

<img src="/images/github-app/checks-detail.png" alt="Results on GitHub Check" width="600" class="img-bordered move-right">

## Installation and Configuration

Pulumi's GitHub workflow integration is a GitHub application you can install by visiting
[github.com/apps/pulumi](https://github.com/apps/pulumi) or clicking the button below.

<a href="https://github.com/apps/pulumi" target="_blank">
    <button class="button">INSTALL</button>
</a>

The Pulumi GitHub application is installed into a specific GitHub organization, and you can
configure it to only be used by certain repositories.

<img src="/images/github-app/installation.png" alt="Installation Page" width="450" class="img-bordered move-right">
<img src="/images/github-app/org-configuration.png" alt="Configuration Page" width="450" class="img-bordered move-right">

The Pulumi GitHub application does not have access to your source code. It will only report
status on pushes / pull requests that happen for repositories it is configured to access. You can
also uninstall the GitHub application at any time without impacting your stacks or
other Pulumi-managed resources.

## CI Integration

Once installed in your organization, any `pulumi preview` or `pulumi up` that is run in your CI
system will have its results reported back to GitHub.

Pulumi supports a wide array of CI/CD systems, and the Pulumi GitHub App should pick up your changes
automatically. For instructions for specific CI services, see one of our existing guides:

* [AWS Code Services]({{< relref "cd-aws-code-services.md" >}})
* [Azure DevOps]({{< relref "cd-azure-devops.md" >}})
* [CircleCI]({{< relref "cd-circleci.md" >}})
* [GitHub Actions]({{< relref "cd-github-actions.md" >}})
* [GitLab CI]({{< relref "cd-gitlab-ci.md" >}})
* [Travis]({{< relref "cd-travis.md" >}})

If you are using a system we don't support yet, please [file an issue](https://github.com/pulumi/pulumi/issues/new)
so we can add it.

By setting a few environment variables, you can ensure that any stack updates from your CI/CD environment will be
associated with your GitHub Pull Request.

- `PULUMI_CI_SYSTEM`. The name of whatever CI/CD system you are using. e.g. "Deploytron-9000".
- `PULUMI_CI_PULL_REQUEST_SHA` (optional). If your CI/CD system is deploying from a different git commit than the
  GitHub PR, such as the resulting merge commit, then set the `PULUMI_CI_PULL_REQUEST_SHA` to the origional
  commit SHA, matching what is found on the Pull Request.

## GitHub UI

There are two places that Pulumi update results will be displayed: Pull Requests or commit Check.

All Pulumi stack updates are reported to the GitHub Checks API. You can see the results of each
commit check by "Code" tab's "Commits" page, and then clicking the ✅ or ❌ icon.

For Pull Requests, you can see the checks on the "Checks" tab as well.

<img src="/images/github-app/checks.png" alt="GitHub Checks Tab" width="600" class="img-bordered move-right">

Every stack that was impacted by the CI job is then listed in the left.

<img src="/images/github-app/checks-detail.png" alt="GitHub Check Result" width="600" class="img-bordered move-right">

If the CI build originated from a pull request, e.g. the Travis CI job had type `pull_request`,
then the results will be placed as a comment on the Pull Request as well.

<img src="/images/github-app/pr-comment.png" alt="Comment on Pull Request" width="600" class="img-bordered move-right">
