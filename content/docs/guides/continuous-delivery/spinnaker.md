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

> Full overview of [Spinnaker Plugins](https://www.spinnaker.io/guides/developer/plugin-creators/overview/).

Plugins are a recent addition to Spinnaker and as such require a more recent version to use plugins as well as the Pulumi plugin for Spinnaker, which this guide will show you how to use.

* Spinnaker v1.19.4+
* Halyard 1.34+

Additionally, your Spinnaker instance should have been deployed using the [distributed installation](https://www.spinnaker.io/setup/install/environment/#distributed-installation) method (i.e. Kubernetes). If you are using any other installation method, although the plugin shown in this document will not work, you may be able to apply similar concepts to your installation.

### Pulumi

This guide assumes you are using the default Pulumi Service [managed backend](https://www.pulumi.com/docs/intro/concepts/state/#backends). The Spinnaker plugin referenced in this guide supports specifying alternate backend URLs.
To sign-up for a new Pulumi account, head over to the [Pulumi Console](https://app.pulumi.com/signup).

## Pulumi Stack And Branch Mappings

> Learn more about [Stacks](https://www.pulumi.com/docs/intro/concepts/stack/).

The sample pipeline (shown later) below acts on a hypothetical stack: `dev`.

* Depending on your use-case, you may want to create the Pulumi Stack ahead of time.
* To create a new stack, you have a couple of options, you may create it in the [Pulumi Console](https://app.pulumi.com/site/new-project) directly.
* Alternatively, you can also run `pulumi new [template]` to create a [template project]({{< relref "/docs/reference/cli/pulumi_new" >}}).
  
The source code for the stack is in a repository in GitHub cloned from this [example](https://github.com/pulumi/examples/tree/master/kubernetes-ts-nginx) and uses `TypeScript` as the language.
The example infrastructure code creates a Kubernetes `Deployment` using the `nginx` container image.
If you modify the sample app or wish to create the `Deployment` resource in a different Kubernetes cluster, follow the setup guide for the [Kubernetes provider](https://www.pulumi.com/docs/intro/cloud-providers/kubernetes/setup/)
to ensure that Pulumi can access that Kubernetes cluster.

> While the example shows you how to deploy a Kubernetes resource, there are many other [cloud providers](https://www.pulumi.com/docs/intro/cloud-providers/) that Pulumi supports.

**Note**: The names used above are purely for demonstration purposes only.
You may choose a naming convention that best suits your organization.

## Pulumi Plugin For Spinnaker

The Pulumi plugin executes a pre-configured job as a Kubernetes batch job. The job runs whichever container image you choose to use for executing the Pulumi apps. The only requirement for the image that the batch job uses is that it should contain the Pulumi CLI, and any necessary language runtime tools, such as `node`, `python`, `dotnet`, or `go`.
By default, the plugin suggests using the [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) container image available publicly on Docker Hub.
Alternatively, you can also try to use one of the other language-specific images that are available under the [`pulumi`](https://hub.docker.com/u/pulumi) org on Docker Hub.

If you would like to use a private image for the job you can do so, but ensure that your Spinnaker cluster has the right credentials to pull an image from a private registry.
Contact your Spinnaker administrator if you are unsure whether you can use a public image.

The pre-configured job will also need to access your VCS to clone the repo into the container. See the next section about configuring secrets to learn how you can use private repos with the plugin.

### Secrets

To pass sensitive secrets to the Kubernetes batch job run by the plugin, you'll need to define a [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/). The secret will need to be in the same namespace as the namespace used to run the pre-configured job.
Sensitive secrets such as the Pulumi Access Token, the cloud provider credentials, or even your Git VCS credentials (eg. GitHub, Bitbucket, GitLab), should be defined as key/value pairs in the Secret resource.

If you are using the service backend, either the Pulumi-managed or the self-hosted one, you'll need to get a [Pulumi Access Token](https://app.pulumi.com/account/tokens) for the Pulumi account that you'll use in your pipeline. Save the value of the token with the key `PULUMI_ACCESS_TOKEN` in your Kubernetes Secret resource.

Here's an example Secret resource applied to a Spinnaker installation.

> Tip: If your Spinnaker Kubernetes cluster was created using Pulumi, then instead of writing this YAML, you could deploy the [Secret](https://www.pulumi.com/docs/reference/pkg/kubernetes/core/v1/secret/) resource using Pulumi too.

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
  PULUMI_ACCESS_TOKEN: <base64EncodedValue>
  AWS_ACCESS_KEY_ID: <base64EncodedValue>
  AWS_SECRET_ACCESS_KEY: <base64EncodedValue>
  ...
  ...
  # If your Pulumi app is stored in a private repo, you may specify the username/password
  # here and then use the corresponding "key" names as placeholders in the URL you specify
  # later in the Pipeline Stage.
  GIT_USERNAME: <base64EncodedValue>
  GIT_PAT: <base64EncodedValue>
```

To create this resource in your Spinnaker cluster, run:

```
kubectl apply -f secrets.yaml
```

As you can see above you can set any environment variables required for the specific providers you plan to use in your Pulumi app. Learn more about [provider setup](https://www.pulumi.com/docs/intro/cloud-providers/).
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

**Note** Before you can access the newly-added plugin in the Deck UI, you must wait for the old `orca` Pod to be replaced with a new one in your cluster. This can take anywhere from a minute to a few depending on the size of your cluster.
To check the state of the running pods you may run `kubectl -n spinnaker get pods`. This will print the pods in the `Spinnaker` namespace as well as the age of the pod.

## Plugin Configuration

There are two configuration opportunities available with the plugin:

* Global
* Per-stage

### Global configuration

> At this time, updating global plugin configuration requires editing your Halyard configuration file manually.

The plugin offers the following global configuration options.

* `account` - The account to be used to run the pre-configured job. Add Kubernetes accounts using the [`hal config provider kubernetes add`](https://www.spinnaker.io/reference/halyard/commands/#hal-config-provider-kubernetes-account-add) command.
* `credentials` - The credentials to use to run the pre-configured job.
* `namespace` - The namespace in which to run the pre-configured job. Secret resources must also exist in the same namespace.

To set the above configuration properties, open the `~/.hal/config` file where your Halyard installation exists. This typically requires SSH'ing into a Pod if your Spinnaker installation is done using the distributed installation method. Scroll-down to the plugins section and find the `Pulumi.PreConfiguredJobPlugin` section. Under `config:`, configure the above properties as you desire.

> Don't forget to run `hal deploy apply` after modifying your `~/.hal/config`.

### Per-stage configuration

Navigate to your Spinnaker instance's Deck UI, and in the Pipeline that you wish to run Pulumi, click the `Add Stage` button at the appropriate Pipeline branch and find the `Pulumi` stage.
The Pulumi stage's UI shows you tooltips to help you fill in the values of the various input properties.

Spinnaker Pipelines support [pipeline expressions](https://www.spinnaker.io/guides/user/pipeline/expressions/) that allow you to dynamically fill in values of inputs.

## Sample Pipeline

> The following steps assume that you have cloned this Kubernetes [example](https://github.com/pulumi/examples/tree/master/kubernetes-ts-nginx) into your own repo.

Creating a Pipeline in Spinnaker is easy and offers many integration options for your GitOps workflow.
In the sample pipeline, however, we will show you how to add the Pulumi stage and create a Kubernetes resource.

* Create a new Pipeline and click the **Add Stage** button. This will allow you to pick from a list of available stages, including the Pulumi stage which you would have added above.
* Configure the inputs for the Pulumi stage accordingly.
  * As previously mentioned in this guide, you can use [pipeline expressions](https://www.spinnaker.io/guides/user/pipeline/expressions/) for your stage inputs.
* Note that we are setting the value of the **Command** input to `preview`.

![Pulumi Stage](/images/docs/guides/continuous-delivery/spinnaker/pipeline-stage.png)

Add a [Manual Judgement](https://www.spinnaker.io/guides/tutorials/codelabs/safe-deployments/#adding-a-manual-judgment-to-deployment-pipelines) stage to the pipeline and then let's add the Pulumi stage again, but this time we'll set the **Command** input to `up` instead of `preview`.
In the end, your pipeline should look like this:

![Full Pipeline](/images/docs/guides/continuous-delivery/spinnaker/full-pipeline.png)

Go back to the main Pipelines view and click on the **Start Manual Execution** link next to your pipeline.
Check the logs from Pulumi as the Pulumi stage runs. The logs update in near real-time.

![Pulumi Stage](/images/docs/guides/continuous-delivery/spinnaker/pipeline-logs.png)

Once the pipeline is complete, assuming you have not modified the example app, the `nginx` container would have been deployed to the `default` namespace.
Get the pod IP by running a `kubectl` command and `curl`-ing the IP to see the response:

```
kubectl get pods -o wide

curl http://POD_IP
```

## Next Steps

We showed you a simple example of how you can get started with using Pulumi in your Spinnaker instance.

* Checkout [detailed examples for Pulumi](https://www.pulumi.com/docs/tutorials/).
* Learn how to use the multitude of [providers](https://www.pulumi.com/docs/reference/pkg/) available with Pulumi.
* We hope that you find the plugin useful in running Pulumi in your Spinnaker instance. If you run into problems or would like to provide feedback, we encourage you to open an issue in this [repo](https://github.com/pulumi/spinnaker-preconfigured-job-plugin). The plugin is free and open-source.
* Lastly, whether you are looking to use Pulumi to deploy a Spinnaker installation on your favorite cloud and have questions about it, or you want to simply participate in the various conversations happening with our community of users, feel free to drop by our [Community Slack](https://slack.pulumi.com).
