---
title: "Spinnaker"
meta_desc: "This page provides an overview of how to use Pulumi plugin for Spinnaker to run Pulumi apps."

menu:
    userguides:
        parent: cont_delivery
        weight: 1
---

This page provides an overview of how to use the Pulumi plugin for Spinnaker to run Pulumi apps. Pulumi doesn't require any particular arrangement of stacks or workflow to work in a
CI/CD system. So the steps described here can be altered to fit into any existing type of deployment setup.

## Prerequisites

### Spinnaker installation

> For a full overview of Spinnaker Plugins, please see the official plugin creator's [guide](https://www.spinnaker.io/guides/developer/plugin-creators/overview/).

Plugins are a recent addition to Spinnaker and as such require a more recent version to use plugins as well as the Pulumi plugin for Spinnaker, which this guide will show you how to use. 

* Spinnaker v1.19.4+
* Halyard 1.34+

Additionally, your Spinnaker instance should have been deployed using the [distributed installation](https://www.spinnaker.io/setup/install/environment/#distributed-installation) method (i.e. Kubernetes). If you are using any other installation method, although the plugin shown in this document will not work, you may be able to apply similar concepts to your installation.

### Pulumi Account

This guide assumes you are using the default Pulumi Service [managed backend](https://www.pulumi.com/docs/intro/concepts/state/#backends). The Spinnaker plugin referenced in this guide supports specifying alternate backend URLs.

To sign-up for a new Pulumi account and get started quickly, head over to the [Pulumi Console](https://app.pulumi.com/signup).

## Pulumi Plugin For Spinnaker

The Pulumi plugin executes a pre-configured job as a Kubernetes batch job. The job runs whichever container image you choose to use for executing the Pulumi apps. The only requirement for the image that the batch job uses is that it should contain the Pulumi CLI, and any necessary language runtime tools, such as `node`, `python`, `dotnet`, or `go`.
By default, the plugin uses the [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) container image available publicly on Docker Hub. If you would like to use a private image you can do so, ensuring that your Spinnaker cluster has the right credentials to pull an image from a private registry. Please contact your Spinnaker administrator if you are unsure whether you can use a public image.
The pre-configured job will also need to access your VCS to clone the repo into the container. See the next section about configuring secrets to learn how you can use private repos with the plugin.

### Secrets

To pass sensitive secrets to the Kubernetes batch job run by the plugin, you'll need to define a [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/). The secret will need to be in the same namespace as the namespace used to run the pre-configured job.
Sensitive secrets such as the Pulumi Access Token, the cloud provider credentials, or even your Git VCS credentials (eg. GitHub, Bitbucket, GitLab), should be defined as key/value pairs in the Secret resource. 

If you are using the service backend, either the Pulumi-managed or the self-hosted one, you'll need to get a [Pulumi Access Token](https://app.pulumi.com/account/tokens) for the Pulumi account that you'll use in your pipeline. Save the value of the token with the key `PULUMI_ACCESS_TOKEN` in your Kubernetes Secret resource.

Here's an example Secret resource applied to a Spinnaker installation.

```yaml
apiVersion: v1
kind: Secret
metadata:
  # Remember the name of this secret.
  name: pulumi-secrets
  # The namespace of this Secret and the namespace used by the plugin should match.
  # Learn more about Plugin Configuration in the next section.
  namespace: spinnaker
data:
  # Any key/value pairs defined here will be injected as environment variables
  # available to the container in which your Pulumi app will be run.
  PULUMI_ACCESS_TOKEN: dGVzdA==
  AWS_ACCESS_KEY_ID: dGVzdA==
  AWS_SECRET_ACCESS_KEY: dGVzdA==
  # If your Pulumi app is stored in a private repo, you may specify the username/password
  # here and then use the corresponding "key" names as placeholders in the URL you specify
  # later in the Pipeline Stage.
  GIT_USERNAME: dGVzdA==
  GIT_PAT: dGVzdA==
```

As you can see above you can set any environment variables required for the specific providers you plan to use in your Pulumi app. Learn more about provider setup [here](https://www.pulumi.com/docs/intro/cloud-providers/).
For private Git repos, you can save the Personal Access Token used to clone your repo into the batch job container. Then when you configure the Stage in your Spinnaker Pipeline you can reference the same key names in the URL you specify.
For example, `https://$(GIT_USERNAME):$(GIT_PAT)@github.com/owner/repo`. The env vars will automatically resolve to the values as per your Secret resource inside the pre-configured job container.

## Installing The Spinnaker Plugin

> While using the Pulumi plugin is optional, doing so will help reduce the maintenance of the manual steps required to run Pulumi in Spinnaker.

Installing the plugin is comprised of two steps. First, you'll need to add the relevant plugin repository to your Halyard configration using the `hal` CLI. Then, you can add the plugin itself.

```
# Add the Pulumi plugins repository for Spinnaker
hal plugins repository add pulumi --url https://raw.githubusercontent.com/pulumi/spinnaker-plugins-repository/master/repositories.json

# Add the plugin itself
hal plugins add Pulumi.PreConfiguredJobPlugin --enabled true --version 0.0.1 --extensions pulumi.PreConfiguredJobStage

# Apply the updates
hal deploy apply
```

> Depending on your Spinnaker installation you might have to run the above commands using `sudo`. 

## Plugin Configuration

There are two configuration opportunities available with the plugin:
* Global
* Per-stage

### Global configuration

> At this time, updating global plugin configuration requires editing your Halyard configuration file manually.

The plugin offers some global configuration options. At the time of this writing, the following configuration options are supported:

* `account` - The account to be used to run the pre-configured job. Add Kubernetes accounts using the [`hal config provider kubernetes add`](https://www.spinnaker.io/reference/halyard/commands/#hal-config-provider-kubernetes-account-add) command.
* `credentials` - The credentials to use to run the pre-configured job.
* `namespace` - The namespace in which to run the pre-configured job. Secret resources must also exist in the same namespace.

To set the above configuration properties, open the `~/.hal/config` file where your Halyard installation exists. This typically requires SSH'ing into a Pod if your Spinnaker installation is done using the distributed installation method. Scroll-down to the plugins section and find the `Pulumi.PreConfiguredJobPlugin` section. Under `config:`, configure the above properties as you desire.

> Don't forget to run `hal deploy apply` after modifying your `~/.hal/config`.

### Per-stage configuration

Navigate to your Spinnaker instance's Deck UI, and in the Pipeline that you wish to run Pulumi, click the `Add Stage` button at the appropriate Pipeline branch and find the `Pulumi` stage.
The Pulumi stage's UI shows you tooltips to help you fill in the values of the various input properties.

Spinnaker Pipelines support [Pipeline Expressions](https://www.spinnaker.io/guides/user/pipeline/expressions/) that allow you to dynamically fill in values of inputs.

## Next Steps

* Checkout more detailed examples for Pulumi [here](https://www.pulumi.com/docs/tutorials/).
* Learn how to use the multitude of providers available with Pulumi [here](https://www.pulumi.com/docs/reference/pkg/).
* We hope that you find the plugin useful in running Pulumi in your Spinnaker instance. If you run into problems or would like to provide feedback, we encourage you to open an issue in this [repo](https://github.com/pulumi/spinnaker-preconfigured-job-plugin). The plugin is free and open-source.
* Lastly, please feel free to drop by our [Community Slack](https://slack.pulumi.com) and participate in the conversation.
