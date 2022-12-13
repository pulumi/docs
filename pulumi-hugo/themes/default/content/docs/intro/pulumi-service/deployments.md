---
title_tag: "Pulumi Service: Pulumi Deployments"
title: "Pulumi Deployments"
meta_desc: Pulumi Deployments is a new feature suite to power infrastructure and platform automation and unlock the scale of the cloud.
menu:
  intro:
    parent: pulumi-service
    weight: 8
---

{{% notes "info" %}}
Pulumi Deployments is currently in preview. [Request access](/product/pulumi-deployments) to use this feature.

Please post any bug reports or feature requests in the [Service Requests repo](https://github.com/pulumi/service-requests/issues/new/choose).
{{% /notes %}}

Pulumi Deployments is a Pulumi Service feature that automates the execution of your Pulumi programs in a secure, hosted environment. Deploy any stack with a click of a button, `git push`, or API call. Available in preview today.

You can use this feature on your Pulumi individual account or in a Pulumi organization.

## Click-to-deploy in the Console

Deploy infrastructure with the click of a button from the Pulumi Service console.

![deploy-actions](/images/docs/service/deploy-actions.png)

## Git push-to-deploy from GitHub

Configure automatic infrastructure deployments in response to `git push` events by installing and configuring the Pulumi GitHub App.

### GitHub App Installation

You'll need to install and configure the [Pulumi GitHub App](/docs/guides/continuous-delivery/github-app/#installation-and-configuration) to use push-to-deploy functionality. The app requires read access to your repos so it can clone your Pulumi programs and listen to merge commits to automatically trigger deployments on `git push`.

{{% notes type="warning" %}}

While the app can be installed via GitHub, it **must be installed through the Pulumi Service** using the steps below to ensure correct setup. Installing through the Pulumi Service ensures we have a connection from Pulumi to your GitHub user or organization.

{{% /notes %}}

Follow these steps:

1. Ensure you have selected the Pulumi organization you wish to use with Pulumi Deployments in the Organization drop-down.
2. Navigate to Settings > Integrations.
3. Select the "Install the Pulumi GitHub App" button.

    If this page says you already have the app installed, you can stop here. If the page asks you to accept additional permissions for the app, please accept the permissions and stop here.

4. After clicking "Install" you will be directed to GitHub. Select the GitHub organization you wish to use with Pulumi Deployments.
5. Select which repos (or all repos) Pulumi Deployments can have access to, and then Install.
6. You will be redirected to the Pulumi Service (app.pulumi.com). Return to the Settings > Integrations tab and confirm the GitHub App is installed on your desired organization.

If you installed the GitHub app in the past and the steps above aren't showing it as installed for your desired organization, please try the following:

- Ensure you're a GitHub admin of the GitHub organization where you're installing the app.
- Uninstall the app (via GitHub) and re-install it following the steps above. **Note:** Uninstalling the app will delete any push-to-deploy configurations you may have already setup.

### Deployment Settings

We need your GitHub repo and branch in order to connect a stack to Pulumi Deployments. Follow these steps to get a Deployment running:

1. Navigate to a stack you want to connect to Pulumi Deployments.
2. Go to Settings > Deploy.
3. Select the GitHub Repository with source context for Pulumi to Deploy.
4. Select the branch.
5. Ensure you have the required Environment Variables to run your repository.

### Create a Deployment

You can create a Deployment by using the Deploy Actions buttons or by pushing a commit to a GitHub pull request.

## Programmatic deployments via the Pulumi Service REST API

Pulumi Deployments REST API is a fully managed REST API to execute Pulumi programs with the Pulumi Service. This includes APIs to observe your deployment and all associated logs.

### Pulumi Deployments REST API Documentation

Refer to the [Pulumi Deployments REST API Documentation](/docs/reference/deployments-rest-api) for details on the API.

### Pulumi Deployments REST API Specs

A list of API specifications for preview:

- Each Pulumi Organization and Individual accounts have a limit of 10 concurrent Deployments
- Deployments are queued, meaning a stack will only have 1 Deployment running at a time
- An update ran through a Pulumi Deployment will timeout after 2 hours of update time
- Deployment logs are retained for 90 days
- Deployments are ran on a t3.large EC2 instance in an isolated AWS account
- Secret environment variables are encrypted end-to-end

## Automation via the Pulumi Automation API

Pulumi Deployments can be run via a remote workspace in Automation API.

Examples are available in the [Automation API Examples repo](https://github.com/pulumi/automation-api-examples).

### Automation API Examples

- [Go](https://github.com/pulumi/automation-api-examples/tree/main/go/remote_deployment)
- [Node.js](https://github.com/pulumi/automation-api-examples/tree/main/nodejs/remoteDeployment-tsnode)
- [Python](https://github.com/pulumi/automation-api-examples/tree/main/python/remote_deployment)
- [.NET](https://github.com/pulumi/automation-api-examples/tree/main/dotnet/RemoteDeployment)
