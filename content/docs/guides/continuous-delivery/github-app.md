---
title: Pulumi GitHub App
meta_desc: Pulumi's GitHub app integrates the results of Pulumi stack updates. It
           will show you any potential infrastructure changes on Pull Requests and commit Checks.
menu:
    userguides:
        parent: cont_delivery
        weight: 1

aliases:
- /docs/reference/cd-github/
- /docs/console/continuous-delivery/github-app/
---

Pulumi's GitHub app integrates the results of Pulumi stack updates with GitHub. Once installed and
configured, it will show you any potential infrastructure changes on Pull Requests and commit Checks.
[See below](https://github.com/apps/pulumi) for information on how to install the Pulumi GitHub app
into your organization.

## Features

The Pulumi GitHub app will automatically add comments to Pull Requests with the results of any
stack changes. This includes a summary of how many resources were created, updated, and/or deleted.
This allows you to quickly see the changes caused by your Pulumi program without needing to leave
GitHub's Pull Request view, with a link to the richer details available on the
[Pulumi Console](https://app.pulumi.com).

![Comment on Pull Request](/images/docs/github-app/pr-comment.png)

Beyond Pull Request comments, the GitHub application also integrates with GitHub's [Checks API](https://blog.github.com/2018-05-07-introducing-checks-api/).
This provides even more detail about any resource changes, including the full update log.

![Results on GitHub Check](/images/docs/github-app/checks-detail.png)

## Installation and Configuration

Pulumi's GitHub workflow integration is a GitHub application you can install by visiting
[github.com/apps/pulumi](https://github.com/apps/pulumi) or clicking the button below.

<a class="btn" href="https://github.com/apps/pulumi" target="_blank">
    INSTALL
</a>

The Pulumi GitHub application is installed into a specific GitHub organization, and you can
configure it to only be used by certain repositories.

![Installation Page](/images/docs/github-app/installation.png)

![Configuration Page](/images/docs/github-app/org-configuration.png)

The Pulumi GitHub application does not have access to your source code. It will only report
status on pushes / pull requests that happen for repositories it is configured to access. You can
also uninstall the GitHub application at any time without impacting your stacks or
other Pulumi-managed resources.

## CI Integration

Once installed in your organization, any `pulumi preview` or `pulumi up` that is run in your CI
system will have its results reported back to GitHub.

Pulumi supports a wide array of CI/CD systems, and the Pulumi GitHub App should pick up your changes
automatically. For instructions for specific CI services, see one of our existing guides:

* [AWS Code Services]({{< relref "/docs/guides/continuous-delivery/aws-code-services.md" >}})
* [Azure DevOps]({{< relref "/docs/guides/continuous-delivery/azure-devops.md" >}})
* [CircleCI]({{< relref "/docs/guides/continuous-delivery/circleci.md" >}})
* [GitHub Actions]({{< relref "/docs/guides/continuous-delivery/github-actions.md" >}})
* [GitLab CI]({{< relref "/docs/guides/continuous-delivery/gitlab-ci.md" >}})
* [Travis]({{< relref "/docs/guides/continuous-delivery/travis.md" >}})

If you are using a system we don't support yet, please [file an issue](https://github.com/pulumi/pulumi/issues/new)
so we can add it.

By setting a few environment variables, you can ensure that any stack updates from your CI/CD environment will be
associated with your GitHub Pull Request.

* `PULUMI_CI_SYSTEM`. The name of whatever CI/CD system you are using. e.g. "Deploytron-9000".
* `PULUMI_CI_PULL_REQUEST_SHA` (optional). If your CI/CD system is deploying from a different git commit than the
  GitHub PR, such as the resulting merge commit, then set the `PULUMI_CI_PULL_REQUEST_SHA` to the origional
  commit SHA, matching what is found on the Pull Request.

## GitHub UI

There are two places that Pulumi update results will be displayed: Pull Requests or commit Check.

All Pulumi stack updates are reported to the GitHub Checks API. You can see the results of each
commit check by "Code" tab's "Commits" page, and then clicking the ✅ or ❌ icon.

For Pull Requests, you can see the checks on the "Checks" tab as well.

![GitHub Checks Tab](/images/docs/github-app/checks.png)

Every stack that was impacted by the CI job is then listed in the left.

![GitHub Check Result](/images/docs/github-app/checks-detail.png)

If the CI build originated from a pull request, e.g. the Travis CI job had type `pull_request`,
then the results will be placed as a comment on the Pull Request as well.

![Comment on Pull Request](/images/docs/github-app/pr-comment.png)
