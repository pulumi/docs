---
title: "Spinnaker"
meta_desc: "This page provides an overview of how to use Pulumi Plugin for Spinnaker to run Pulumi apps."

menu:
    userguides:
        parent: cont_delivery
        weight: 1
---

This page provides an overview of how to use the Pulumi Plugin for Spinnaker to run Pulumi apps. Pulumi doesn't require
any particular arrangement of stacks or workflow to work with a CI/CD system, so the steps described here can be altered
to fit into any existing type of deployment setup.

## Prerequisites

### Spinnaker installation

> [Spinnaker Plugin Creator's Guide](https://spinnaker.io/docs/guides/developer/plugin-creator/).

This solution requires a version of Spinnaker that supports plugins as well as the Pulumi Plugin for Spinnaker itself.

* Spinnaker v1.19.4+ (version 1.23.x is recommended)
* Halyard 1.34+

For the latest compatibility information, see the [version compatibility table](https://github.com/pulumi/spinnaker-preconfigured-job-plugin#version-compatibility)
in the plugin repository.

Additionally, your Spinnaker instance should have been deployed using the [distributed installation](https://www.spinnaker.io/setup/install/environment/#distributed-installation)
method (i.e. Kubernetes).

### Pulumi

This guide assumes you are using the default Pulumi Service [managed backend](https://www.pulumi.com/docs/intro/concepts/state/#backends).
To sign-up for a new Pulumi account, head over to the [Pulumi Service](https://app.pulumi.com/signup).
The Pulumi Plugin for Spinnaker referenced in this guide supports specifying alternate backend URLs.

## Pulumi Stack And Branch Mappings

> Learn more about [Stacks](https://www.pulumi.com/docs/intro/concepts/stack/).

The sample pipeline (shown later) below acts on a hypothetical stack: `dev`. The name `dev` is used for demonstration
purposes only. You may choose a different name that best suits your use case.

* Depending on your use-case, you may want to create the Pulumi Stack ahead of time.
* You can create a new stack in the [Pulumi Service](https://app.pulumi.com/site/new-project).
* Alternatively, you can also run `pulumi new [template]` to create a [template project]({{< relref "/docs/reference/cli/pulumi_new" >}})
on your machine and push it to your Version Control System (VCS) repository.
  
The source code used as an [example](https://github.com/pulumi/examples/tree/master/kubernetes-ts-nginx) in this guide
uses TypeScript. The example infrastructure code creates a Kubernetes `Deployment` using the `nginx` container image.
If you modify the sample app or wish to create the `Deployment` resource in a different Kubernetes cluster, follow the
setup guide for the [Kubernetes provider](https://www.pulumi.com/registry/packages/kubernetes/installation-configuration/)
to ensure that Pulumi can access that Kubernetes cluster.

The example in this topic shows you how to deploy a Kubernetes resource; however, you can use any of the other
cloud providers in the [Registry](https://www.pulumi.com/registry) that Pulumi supports.

## Pulumi Plugin For Spinnaker

The Pulumi plugin executes a preconfigured job as a Kubernetes batch job. The job uses the container image you specify
in the Spinnaker pipeline UI.

By default, the plugin suggests using the [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) container image available publicly on Docker Hub.
Alternatively, you can also try to use one of the other language-specific images that are available under the [`pulumi`](https://hub.docker.com/u/pulumi) org on Docker Hub.

If you would like to use your own container image for the job, ensure that the following requirements are met:

* Your container should include the Pulumi CLI, and any necessary language runtime tools, such as `node`, `python`, `dotnet`, or `go`.
* If your container image is in a private registry, your Spinnaker cluster must have the proper credentials to pull from the registry.

The preconfigured job will also need to access your VCS to clone the repo into the container.
See the next section about configuring secrets to learn how you can use private VCS repos with the plugin.

### Secrets

To pass sensitive secrets to the Kubernetes batch job run by the plugin, define a [Kubernetes `Secret`](https://kubernetes.io/docs/concepts/configuration/secret/).

{{% notes type="warning" %}}
The `Secret` resource must be in the same namespace as the Pulumi stage input when you configure the pipeline.
{{% /notes %}}

Sensitive secrets such as the Pulumi Access Token, the cloud provider credentials, or even your VCS credentials
(eg. GitHub, Bitbucket, GitLab), should be defined as key/value pairs in the `Secret` resource.

If you are using either the Pulumi-managed or the self-hosted [service backend]({{< relref "/docs/intro/concepts/state" >}}), get a
[Pulumi Access Token](https://app.pulumi.com/account/tokens) for the Pulumi account that you will use in your pipeline.
Save the value of the token with the key `PULUMI_ACCESS_TOKEN` in your Kubernetes `Secret` resource.

If you do not use the Pulumi Service backend, the `PULUMI_ACCESS_TOKEN` is optional. Instead, you should make sure that Pulumi has the credentials to access whichever backend URL you do choose to use.

Here's an **example** `Secret` resource applied in a Spinnaker installation.

{{% notes "info" %}}
If your Spinnaker Kubernetes cluster was created using Pulumi, then instead of writing this YAML, you could deploy the [Secret](https://www.pulumi.com/docs/reference/pkg/kubernetes/core/v1/secret/) resource using Pulumi too.
{{% /notes %}}

```yaml
# Defining a Secret resource in your K8s cluster is optional based on how you plan to use the Pulumi preconfigured job plugin.
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

You can set any environment variables required for the specific providers you plan to use in your Pulumi app. For more information, see the Setup page for a given [provider](https://www.pulumi.com/registry/packages/).

For private VCS repos, you can save the Personal Access Token used to clone your repo into the batch job container. This means when you configure the Stage in the Spinnaker Pipelines UI, you can reference the same key names in the URL you specify. For example, the environment variables in the URL `https://$(GIT_USERNAME):$(GIT_PAT)@github.com/owner/repo` will automatically resolve to the correct values as per your Secret resource inside the preconfigured job container.

{{% notes type="warning" %}}
Do not surround the placeholder variables with `{` and `}` unless you are actually using a [pipeline expression](https://spinnaker.io/guides/user/pipeline/expressions/).
{{% /notes %}}

## Installing The Spinnaker Plugin

Before you can install the plugin, you'll need to add the Pulumi plugins repository for Spinnaker to your
Halyard configuration. Depending on your Spinnaker installation, you might have to run the following commands using `sudo`.

```
# Add the Pulumi plugins repository for Spinnaker
hal plugins repository add pulumi --url https://raw.githubusercontent.com/pulumi/spinnaker-plugins-repository/master/repositories.json

# Now add the plugin
hal plugins add Pulumi.PreConfiguredJobPlugin --enabled true --version <version> --extensions pulumi.PreConfiguredJobStage
```

{{% notes "info" %}}
Starting with version 0.1.0 of the Pulumi preconfigured job plugin, you must also install a custom Deck UI plugin as part of the setup process. Previously, the Deck UI was auto-generated by Spinnaker and didn't require a separate installation step. For information on how to install the DeckUI plugin, see [Add the Deck UI plugin](https://github.com/pulumi/spinnaker-preconfigured-job-plugin#add-the-deck-ui-plugin) in the Pulumi plugin for Spinnaker README.
{{% /notes %}}

```
# Finally, apply the service updates
hal deploy apply
```

Before you can access the newly-added plugin in the Deck UI, you must wait for the old `orca` Pod to be replaced with a new one in your cluster. This action can take a few minutes depending on the size of your cluster.

To check the state of the running pods, run `kubectl -n spinnaker get pods`. This will print the pods in the
`Spinnaker` namespace as well as the age of the pod.

## Plugin Configuration

Navigate to your Spinnaker instance's Deck UI, and in the pipeline that you wish to run Pulumi, click the `Add Stage`
button at the appropriate pipeline branch and find the `Run Pulumi` stage.
The Pulumi stage's UI shows you tooltips to help you fill in the values of the various input properties.

Spinnaker Pipelines support [pipeline expressions](https://www.spinnaker.io/guides/user/pipeline/expressions/) that
allow you to dynamically fill in values of inputs based on the execution of previous stages.

## Sample Pipeline (Optional)

To follow along with this example, clone the Nginx Kubernetes [example](https://github.com/pulumi/examples/tree/master/kubernetes-ts-nginx) into your own repo.

Creating a pipeline in Spinnaker is easy and offers many integration options for your GitOps workflow.
In the sample pipeline we will show you how to add the Pulumi stage and create a Kubernetes resource.

1. Create a new Pipeline and click the **Add Stage** button. This will allow you to pick from a list of available stages,
  including the Pulumi stage which you would have added above.
1. Configure the inputs for the Pulumi stage accordingly.
   As previously mentioned in this guide, you can use [pipeline expressions](https://www.spinnaker.io/guides/user/pipeline/expressions/)
   for your stage inputs.
1. Set the value of the **Command** input to `preview`.

1. Add a [Manual Judgement](https://www.spinnaker.io/guides/tutorials/codelabs/safe-deployments/#adding-a-manual-judgment-to-deployment-pipelines)
stage to the pipeline and then let's add the Pulumi stage again, but this time we'll set the **Command** input to `up`.
Set the **Command Args** input to `-s dev --yes`, assuming your stack's name is `dev`. The `--yes` is needed since you
would be running `pulumi up` non-interactively.

1. In the end, your pipeline should look like this:

    ![Full Pipeline](/images/docs/guides/continuous-delivery/spinnaker/full-pipeline.png)

1. Go back to the main Pipelines view and click on the **Start Manual Execution** link next to your pipeline.
Once the job starts execution, you should see a **Console Output** link. Clicking it will open a modal that will show
you the current output.

    {{% notes "info" %}}
If you are running Spinnaker on your machine, it can take several minutes before the job starts to execute and the logs are visible. If you see a`ContainerCreating` error, it means the pod running the job isn't ready yet.
    {{% /notes %}}

Once the pipeline is complete, assuming you have not modified the example app, the `nginx` container would have been
deployed to the `default` namespace. Get the pod IP by running a `kubectl` command and `curl`-ing the IP to see the response:

```bash
kubectl get pods -o wide

curl http://<POD_IP>
```

## FAQs

**Can I get colored log output from Pulumi?**

Yes! Simply pass the Pulumi CLI arg `--color always`. Now when you open the `Console Output` modal, you should see
colors in the log output. Note that the colored logs are only visible starting with v0.2.0 of the plugin.

**Can I use the plugin if my VCS repo is hosted on an enterprise Git server?**

Yes. Make sure that the credentials (username and the personal access token) for the Git repo are defined in the
Kubernetes `Secret` and use the key names as placeholders in the repo URL you specify in the pipeline stage UI.

**How do I set the cloud credentials for Pulumi?**

Similar to specifying Git credentials, you can define your cloud provider credentials in the same secret resource
which will be mapped as environment variables that Pulumi can read.

**Can I use custom container images for the RunJob container?**

Yes. Make sure that your custom image satisfies the following requirements:

* Your container should include the Pulumi CLI, and any necessary language runtime tools, such as `node`, `python`,
  `dotnet`, or `go`.
* If your container image is in a private registry, your Spinnaker cluster must have the proper credentials to pull
  from the registry.

The following links may be helpful in building your own custom image:

* [Pulumi container images](https://github.com/pulumi/pulumi/tree/master/docker)
* [Pulumi on Docker Hub](https://hub.docker.com/u/pulumi)

## Next Steps

We showed you a simple example of how you can get started with using Pulumi in your Spinnaker instance.

* Check out [detailed examples for Pulumi](https://www.pulumi.com/docs/tutorials/).
* Learn how to use the multitude of [providers](https://www.pulumi.com/docs/reference/pkg/) available with Pulumi.
* We hope that you find the plugin useful in running Pulumi in your Spinnaker instance. If you run into problems or
  would like to provide feedback, we encourage you to open an issue in the [plugin repo](https://github.com/pulumi/spinnaker-preconfigured-job-plugin).
  The plugin is free and open-source.
* Lastly, whether you are looking to use Pulumi to deploy a Spinnaker installation on your favorite cloud and have
  questions about it, or you want to simply participate in the various conversations happening with our community of
  users, feel free to drop by our [Community Slack](https://slack.pulumi.com).
