---
title: Pulumi GitHub App (preview)
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


> The Pulumi GitHub app is currently in preview, and we will be expanding the feature set
> over the comming weeks and months. If you have any feedback, suggestions, or bug reports, please
> let us know in the [Pulumi Community Slack](https://slack.pulumi.io/).

## Features

The Pulumi GitHub app will automatically add comments to Pull Requests with the results of any
stack changes. This includes a summary of how many resources were created, updated, and/or deleted.
This allows you to quickly see the changes caused by your Pulumi program without needing to leave
GitHub's Pull Request view, with a link to the richer details available on [pulumi.com](https://pulumi.com).

![Comment on Pull Request](/images/github-app/pr-comment.png){:class="img-bordered"}{:class="move-right"}

Beyond Pull Request comments, the GitHub application also integrates with GitHub's new [Checks API](https://blog.github.com/2018-05-07-introducing-checks-api/).
This provides even more detail about any resource changes, including the full update log.

![Results on GitHub Check](/images/github-app/checks-detail.png){:width="600px"}{:class="img-bordered"}{:class="move-right"}

## Installation and Configuration

Pulumi's GitHub workflow integration is a GitHub application you can install by visiting
[github.com/apps/pulumi](https://github.com/apps/pulumi) or clicking the button below.

<a href="https://github.com/apps/pulumi" target="_blank">
    <button class="button">INSTALL</button>
</a>

The Pulumi GitHub application is installed into a specific GitHub organization, and you can
configure it to only be used by certain repositories.

![Installation Page](/images/github-app/installation.png){:width="450px"}{:class="img-bordered"}{:class="move-right"}
![Configuration Page](/images/github-app/org-configuration.png){:width="450px"}{:class="img-bordered"}{:class="move-right-small"}

The Pulumi GitHub application does not have access to your source code. It will only report
status on pushes / pull requests that happen for repositories it is configured to access. You can
also uninstall the GitHub application at any time without impacting your stacks or
other Pulumi-managed resources.

## CI Integration

Once installed in your organization, any `pulumi preview` or `pulumi update` that is run in your CI
system will have its results reported back to GitHub.

Currently, Pulumi's GitHub application only supports Travis CI. (For instructions on configuring
Travis, see [our guide](https://pulumi.io/reference/cd-travis.html).) If you would like
GitHub workflow integration for another CI system, please let us know.

While the system is in preview, you will also need to set the following environment variable
on your CI build machine.

```
export PULUMI_PERSIST_PREVIEWS="1"
```

That's it! When Travis CI performs a build that runs `pulumi preview` or `pulumi update`, the
results will be reported on the corresponding Git commit or Pull Request.

## GitHub UI

There are two places that Pulumi update results will be displayed: Pull Requests or commit Check.

All Pulumi stack updates are reported to the GitHub Checks API. You can see the results of each
commit check by "Code" tab's "Commits" page, and then clicking the ✅ or ❌ icon.

For Pull Requests, you can see the checks on the "Checks" tab as well.

![GitHub Checks Tab](/images/github-app/checks.png){:width="600px"}{:class="img-bordered"}{:class="move-right"}

Every stack that was impacted by the CI job is then listed in the left.

![GitHub Check Result](/images/github-app/checks-detail.png){:width="600px"}{:class="img-bordered"}{:class="move-right"}

If the CI build originated from a pull request, e.g. the Travis CI job had type `pull_request`,
then the results will be placed as a comment on the Pull Request as well.

![Comment on Pull Request](/images/github-app/pr-comment.png){:width="600px"}{:class="img-bordered"}{:class="move-right"}
