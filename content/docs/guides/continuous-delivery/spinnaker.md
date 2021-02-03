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

> [Spinnaker Plugin Creator's Guide](https://www.spinnaker.io/guides/developer/plugin-creators/overview/).

This solution requires a version of Spinnaker that supports plugins as well as the Pulumi Plugin for Spinnaker itself.

* Spinnaker v1.19.4+ (version 1.23.x is recommended)
* Halyard 1.34+

**Note**: Refer to the [version compatibility table](https://github.com/pulumi/spinnaker-preconfigured-job-plugin#version-compatibility)
in the plugin repository.

Additionally, your Spinnaker instance should have been deployed using the [distributed installation](https://www.spinnaker.io/setup/install/environment/#distributed-installation)
method (i.e. Kubernetes).

### Pulumi

This guide assumes you are using the default Pulumi Service [managed backend](https://www.pulumi.com/docs/intro/concepts/state/#backends).
To sign-up for a new Pulumi account, head over to the [Pulumi Console](https://app.pulumi.com/signup).
The Pulumi Plugin for Spinnaker referenced in this guide supports specifying alternate backend URLs.

## Pulumi Stack And Branch Mappings

> Learn more about [Stacks](https://www.pulumi.com/docs/intro/concepts/stack/).

The sample pipeline (shown later) below acts on a hypothetical stack: `dev`.

* Depending on your use-case, you may want to create the Pulumi Stack ahead of time.
* You can create a new stack in the [Pulumi Console](https://app.pulumi.com/site/new-project).
* Alternatively, you can also run `pulumi new [template]` to create a [template project]({{< relref "/docs/reference/cli/pulumi_new" >}})
on your machine and push it up to your VCS repo.
  
The source code used as an [example](https://github.com/pulumi/examples/tree/master/kubernetes-ts-nginx) in this guide
uses `TypeScript`. The example infrastructure code creates a Kubernetes `Deployment` using the `nginx` container image.
If you modify the sample app or wish to create the `Deployment` resource in a different Kubernetes cluster, follow the
setup guide for the [Kubernetes provider](https://www.pulumi.com/docs/intro/cloud-providers/kubernetes/setup/)
to ensure that Pulumi can access that Kubernetes cluster.

> While the example shows you how to deploy a Kubernetes resource, there are many other [cloud providers](https://www.pulumi.com/docs/intro/cloud-providers/)
> that Pulumi supports.

**Note**: The names used above are purely for demonstration purposes only.
You may choose a naming convention that best suits your organization.

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

To pass sensitive secrets to the Kubernetes batch job run by the plugin, define a [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/).
The secret will need to be in the same namespace as the namespace used to run the preconfigured job.
Sensitive secrets such as the Pulumi Access Token, the cloud provider credentials, or even your VCS credentials
(eg. GitHub, Bitbucket, GitLab), should be defined as key/value pairs in the Secret resource.

If you are using the service backend, either the Pulumi-managed or the self-hosted one, you'll need to get a
[Pulumi Access Token](https://app.pulumi.com/account/tokens) for the Pulumi account that you'll use in your pipeline.
Save the value of the token with the key `PULUMI_ACCESS_TOKEN` in your Kubernetes Secret resource.

The `PULUMI_ACCESS_TOKEN` is optional if you don't use the Pulumi Service backend. Instead, you should make sure that
Pulumi has the credentials to access whichever backend URL you do choose to use.

Here's an **example** Secret resource applied in a Spinnaker installation.

> Tip: If your Spinnaker Kubernetes cluster was created using Pulumi, then instead of writing this YAML, you could
> deploy the [Secret](https://www.pulumi.com/docs/reference/pkg/kubernetes/core/v1/secret/) resource using Pulumi too.

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

You can set any environment variables required for the specific providers you plan to use in your Pulumi app.
Learn more about [provider setup](https://www.pulumi.com/docs/intro/cloud-providers/).
For private VCS repos, you can save the Personal Access Token used to clone your repo into the batch job container.
Then when you configure the Stage in the Spinnaker Pipelines UI you can reference the same key names in the URL you specify.
For example, `https://$(GIT_USERNAME):$(GIT_PAT)@github.com/owner/repo`. The env vars will automatically resolve to the
values as per your Secret resource inside the preconfigured job container.

⚠️ Don't surround the placeholder variables with `{` and `}` unless you really are using a [pipeline expression](https://spinnaker.io/guides/user/pipeline/expressions/).

## Installing The Spinnaker Plugin

Before you can install the plugin, you'll need to add the Pulumi plugins repository for Spinnaker to your
Halyard configuration.

```
# Add the Pulumi plugins repository for Spinnaker
hal plugins repository add pulumi --url https://raw.githubusercontent.com/pulumi/spinnaker-plugins-repository/master/repositories.json

# Now add the plugin
hal plugins add Pulumi.PreConfiguredJobPlugin --enabled true --version <version> --extensions pulumi.PreConfiguredJobStage
```

> Depending on your Spinnaker installation you might have to run the above commands using `sudo`.

⚠️ Starting from version 0.1.0 of the Pulumi preconfigured job plugin, there is a custom Deck UI plugin that you also must
install. Previously, the Deck UI was auto-generated by Spinnaker and didn't require a separate installation step.
See the [instructions](https://github.com/pulumi/spinnaker-preconfigured-job-plugin#add-the-deck-ui-plugin) on how to
install the Deck UI plugin as well.

```
# Finally, apply the service updates
hal deploy apply
```

**Note**: Before you can access the newly-added plugin in the Deck UI, you must wait for the old `orca` Pod to be
replaced with a new one in your cluster. This can take anywhere from a minute to a few depending on the size of your cluster.
To check the state of the running pods you may run `kubectl -n spinnaker get pods`. This will print the pods in the
`Spinnaker` namespace as well as the age of the pod.

## Plugin Configuration

Navigate to your Spinnaker instance's Deck UI, and in the pipeline that you wish to run Pulumi, click the `Add Stage`
button at the appropriate pipeline branch and find the `Run Pulumi` stage.
The Pulumi stage's UI shows you tooltips to help you fill in the values of the various input properties.

Spinnaker Pipelines support [pipeline expressions](https://www.spinnaker.io/guides/user/pipeline/expressions/) that
allow you to dynamically fill in values of inputs based on the execution of previous stages.

## Sample Pipeline (Optional)

> The following steps assume that you have cloned this Kubernetes [example](https://github.com/pulumi/examples/tree/master/kubernetes-ts-nginx)
> into your own repo.

Creating a pipeline in Spinnaker is easy and offers many integration options for your GitOps workflow.
In the sample pipeline we will show you how to add the Pulumi stage and create a Kubernetes resource.

* Create a new Pipeline and click the **Add Stage** button. This will allow you to pick from a list of available stages,
  including the Pulumi stage which you would have added above.
* Configure the inputs for the Pulumi stage accordingly.
  * As previously mentioned in this guide, you can use [pipeline expressions](https://www.spinnaker.io/guides/user/pipeline/expressions/)
    for your stage inputs.
* Note that we are setting the value of the **Command** input to `preview`.

Add a [Manual Judgement](https://www.spinnaker.io/guides/tutorials/codelabs/safe-deployments/#adding-a-manual-judgment-to-deployment-pipelines)
stage to the pipeline and then let's add the Pulumi stage again, but this time we'll set the **Command** input to `up`
instead of `preview`. In the end, your pipeline should look like this:

![Full Pipeline](/images/docs/guides/continuous-delivery/spinnaker/full-pipeline.png)

Go back to the main Pipelines view and click on the **Start Manual Execution** link next to your pipeline.
Once the job starts execution, you should see a **Console Output** link. Clicking it will open a modal that will show
you the current output.

**Note**: If you are running Spinnaker on your machine, it can take a while before the job starts to execute and the logs
are visible. If you see an error about `ContainerCreating` it means the pod running the job isn't ready yet.

Once the pipeline is complete, assuming you have not modified the example app, the `nginx` container would have been
deployed to the `default` namespace. Get the pod IP by running a `kubectl` command and `curl`-ing the IP to see the response:

```
kubectl get pods -o wide

curl http://<POD_IP>
```

## FAQs

**Can I get colored log output from Pulumi?**

Yes! Simply pass the Pulumi CLI arg `--color always`. Now when you open the `Console Output` modal, you should see
colors in the log output. Note that the colored logs are only visible starting with v0.2.0 of the plugin.

**How do I use the plugin with an enterprise VCS repo such as GitHub Enterprise?**

The plugin allows you to specify custom container images. One option is to build the container image with the SSH
credentials baked-in. This allows you to specify a "git SSH" URL. Consult with your Spinnaker administrator before you
do this.

The other option is to create a Personal Access Token and create a Secret resource that you reference in your stage.
You can then use the key names as placeholders in the HTTPS version of your repo URL.

**How do I specify my cloud credentials?**

As mentioned before you can define a `Secrets` resource whose key/value pairs will be mapped as environment variables.
The key names need to match the environment variables that a cloud provider supports.

The other option is similar to baking the container image with SSH credentials. You can also bake any configuration
files used by the cloud provider in the container image. For example, `~/.aws/config` and `~/.aws/credentials`.
You also have the option to override stack configuration from the pipeline stage by passing the `-c` flag and specify
certain cloud provider settings that way. Again, taking AWS as an example, `-c aws:profile <profile name from ~/.aws/config>`.

## Next Steps

We showed you a simple example of how you can get started with using Pulumi in your Spinnaker instance.

* Check out [detailed examples for Pulumi](https://www.pulumi.com/docs/tutorials/).
* Learn how to use the multitude of [providers](https://www.pulumi.com/docs/reference/pkg/) available with Pulumi.
* We hope that you find the plugin useful in running Pulumi in your Spinnaker instance. If you run into problems or
  would like to provide feedback, we encourage you to open an issue in this [repo](https://github.com/pulumi/spinnaker-preconfigured-job-plugin).
  The plugin is free and open-source.
* Lastly, whether you are looking to use Pulumi to deploy a Spinnaker installation on your favorite cloud and have
  questions about it, or you want to simply participate in the various conversations happening with our community of
  users, feel free to drop by our [Community Slack](https://slack.pulumi.com).
