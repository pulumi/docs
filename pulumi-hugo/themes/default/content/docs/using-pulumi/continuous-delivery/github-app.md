---
title_tag: "Using Pulumi GitHub App | CI/CD"
meta_desc: Pulumi's GitHub app integrates the results of Pulumi stack updates. It
           will show you any potential infrastructure changes on Pull Requests and commit Checks.
title: Pulumi GitHub App
h1: Pulumi Github App
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    usingpulumi:
        parent: cont_delivery
        weight: 1

aliases:
- /docs/reference/cd-github/
- /docs/console/continuous-delivery/github-app/
- /docs/guides/continuous-delivery/github-app/
---

Pulumi's GitHub app displays the results of Pulumi stack update previews in pull requests and enables automatic stack deployments via [Pulumi Deployments](/docs/pulumi-cloud/deployments/). Once installed and
configured, it will show you any potential infrastructure changes on Pull Requests and commit checks. You can also configure `git push` to deploy workflows that update your stacks whenever a pull request is merged.

## Features

The Pulumi GitHub app will automatically add comments to Pull Requests with the results of any
stack changes. This includes a summary of how many resources were created, updated, and/or deleted.
This allows you to quickly see the changes caused by your Pulumi program without needing to leave
GitHub's Pull Request view, with a link to the richer details available on the
[Pulumi Cloud](https://app.pulumi.com).

![Comment on Pull Request](/images/docs/github-app/pr-comment.png)

Beyond Pull Request comments, the GitHub application also integrates with GitHub's [Checks API](https://blog.github.com/2018-05-07-introducing-checks-api/).
This provides even more detail about any resource changes, including the full update log.

![Results on GitHub Check](/images/docs/github-app/checks-detail.png)

## Installation and Configuration

1. [Sign in to your Pulumi account.](https://app.pulumi.com/signin)
2. Ensure you have selected the Pulumi organization you wish to use with the GitHub app by choosing it in the Organization drop-down.
3. Navigate to Settings > Integrations.
4. Select the "Install the Pulumi GitHub App" button.

    ![Install the Pulumi GitHub App](/images/docs/github-app/gha-install.png)

    If this page says you already have the app installed, you can stop here. If the page asks you to accept additional permissions for the app, please accept the permissions and stop here.

5. After selecting "Install" you will be directed to GitHub. Select the GitHub organization you wish to use.
6. Select which repos (or all repos) that the Pulumi GitHub App can have access to, and then select Install.
7. You will be redirected to app.pulumi.com. Return to the Settings > Integrations tab and confirm the GitHub App is installed on your desired organization.

![Turn on Pull Request Comments with Pulumi GitHub App](/images/docs/github-app/gha-installed.png)

If you installed the GitHub app in the past and the steps above aren't showing it as installed for your desired organization, please try the following:

1. Ensure you're a GitHub admin of the GitHub organization where you're installing the app.
2. Uninstall the app (via github.com) and re-install it following the steps above.

### Configure Git Push-to-Deploy with Pulumi Deployments

To set up a `git push`-to-deploy workflow using Pulumi Deployments, consult the [Pulumi Deployments documentation](/docs/pulumi-cloud/deployments/) after installing the Pulumi GitHub App.

## CI Integration

The Pulumi GitHub application will work with any CI/CD system. See our
[Continuous Delivery](/docs/using-pulumi/continuous-delivery/) guide for information on how to
integration Pulumi with whatever system you currently use.

Once installed in your organization, any `pulumi preview` or `pulumi up` that is run in your CI
system will have its results reported back to GitHub.

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

## GitHub Enterprise Server support

GitHub Enterprise Server is supported for [Pulumi Business Critical Edition](https://www.pulumi.com/enterprise/), for it to work, Pulumi has to provision the GitHub application into your GitHub instance.

### Installation

1. [Sign in to your Pulumi account.](https://app.pulumi.com/signin)
2. Ensure you have selected the Pulumi organization you wish to use with the GitHub app by choosing it in the Organization drop-down.
3. Navigate to Settings > Integrations.
4. Select the "GitHub Enterprise Server App" button.

    ![Install the Pulumi GitHub Enterprise Server App](/images/docs/github-app/gha-enterprise-server-install.png)

    If this page says you already have the app installed, you can stop here. If the page asks you to accept additional permissions for the app, please accept the permissions and stop here.

5. A dialog will pop-up requesting information about your GitHub installation.

    Complete your installation hostname and the type of account where you want to provision the App.

    ![GitHub Enterprise Server App Installation Dialog](/images/docs/github-app/gh-enterprise-installation-dialog.png)

    For Personal accounts, no extra information is required, click on the install button to continue.

    ![GitHub Enterprise Server App Installation Dialog for personal account](/images/docs/github-app/gh-enterprise-installation-dialog-personal.png)

    For Organization accounts, the organization name is required to continue.

    ![GitHub Enterprise Server App Installation Dialog for organization account](/images/docs/github-app/gh-enterprise-installation-dialog-organization.png)

6. After selecting "Install" you will be directed to GitHub where you will have to complete the Application name.

    ![GitHub App provisioning](/images/docs/github-app/gh-enterprise-installation-app-name.png)

7. The last step will be to select where do you want to install the application

    ![GitHub App installation](/images/docs/github-app/gh-enterprise-installation-selection.png)
