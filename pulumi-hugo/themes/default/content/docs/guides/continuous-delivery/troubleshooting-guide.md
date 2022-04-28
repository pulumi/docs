---
title: Troubleshooting Pulumi in CI
meta_desc: This page walks through the common failures encountered while running Pulumi in CI, as well as tips on how to fix them.
menu:
    userguides:
        parent: cont_delivery
        weight: 2
---

In order to understand the errors encountered during an automated pipeline execution, it is important to understand
the steps involved in a typical CI configuration for Pulumi regardless of the CI service you are using.
The type of failure you experience is likely related to one of these steps.

## Overall Requirements

In order to run a Pulumi command, the following are required:

* A [Pulumi access token]({{< ref "/docs/intro/pulumi-service/accounts#access-tokens" >}}) for the account you wish to use.
[Create a token](https://app.pulumi.com/account/tokens) by logging in with the appropriate account.
* A stack that you would like to update the automated pipeline.
* Pulumi CLI available in the system `PATH`.
* Build tools (more on this below) based on the runtime of your Pulumi app.
* Dependencies for your Pulumi app.
* The right cloud provider credentials.

### Pulumi Access Token

Pulumi has the smarts to know when it is run inside of a CI service by detecting the environment configuration. When this happens,
Pulumi automatically executes a `pulumi login` command using the non-interactive mechanism.

#### Tips

* Ensure that the access token is saved in an environment variable called `PULUMI_ACCESS_TOKEN`.
  * Most services support marking environment variables as a secret. Your Pulumi Access Token is indeed a sensitive value
  and as such should be saved as a secret env var.
* Ensure that the environment variable is actually accessible to the job that is running the `pulumi` command.
* Several CI systems have the concept of restricting access to environment secrets to specific branches. So make sure that your branch and the job
running the `pulumi` command can access the env var.

### Stack Name

> Learn about [stacks]({{< relref "/docs/intro/concepts/stack" >}}) and their [configuration]({{< relref "/docs/intro/concepts/config" >}}).

A stack represents a specific configuration state for your infrastructure resources. For a typical CI pipeline, the stack must have been created
beforehand using the `pulumi stack init` command and in the **appropriate organization**.

#### Tips

* Ensure that the account represented by the token you are using has access to the stack.

  This can lead to 404s being returned from the Pulumi Service because the token is invalid for any number of reasons.
  One way to check this is, that you are able to navigate to the stack in the [Pulumi Service](https://app.pulumi.com) using the same account you are using in CI.

* Ensure that you use the fully-qualified stack name when passing the stack name to `pulumi` commands.

  A fully-qualified stack name is of the format `<org_name>/<project_name>/<stack_name>`.
  For example, for a stack called `production` in an org called `pulumi` and project `slack-bot`, its FQDN is `pulumi/slack-bot/production`.
  Using an FQDN, thought optional, in your automated pipelines removes any ambiguity as to which stack is used,
  even though Pulumi determines the correct stack by automatically taking into account the project name in your
  `Pulumi.yaml` file. It makes it explicit for anyone in your team looking at the CI configuration.

* Ensure that you are running the `pulumi` command from the folder containing the `Pulumi.yaml` file that contains your Pulumi project's name.
* If your stack has configuration, then the stack configuration file must also be co-located with the project file.

  For example, for a stack named `production`, the `Pulumi.production.yaml` file must exist alongside the `Pulumi.yaml`.
  If your Pulumi app is in a different folder, you can use the `--cwd` flag with almost every `pulumi` command.
  Learn more about the [global flags]({{< relref "/docs/reference/cli#options" >}}).

### Installing the Pulumi CLI

Depending on the CI service, there may be a few ways to install the Pulumi CLI. The following CI systems have native extensions that provide
an easy-to-use mechanism for installing and running the various `pulumi` commands.

* [Azure Pipelines Task Extension](https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task) - [Azure Guide]({{< relref "azure-devops" >}})
* GitHub Actions - [JavaScript Action](https://github.com/pulumi/action-install-pulumi-cli), [Docker Action](https://github.com/pulumi/actions) - [GitHub Actions Guide]({{< relref "github-actions" >}})

> Pulumi CLI is now pre-installed on GitHub Actions runners. However, if you need to install a specific version, you can always use one of the aforementioned actions.

* [CircleCI Orb](https://circleci.com/developer/orbs/orb/compute/pulumi) - [CircleCI Guide]({{< relref "circleci" >}})
* [Octopus Deploy Step Template](https://library.octopus.com/step-templates/76296cd1-7d8c-47e8-b33f-027ecd3ff6b5/actiontemplate-run-pulumi-(linux)) - [Octopus Deploy Guide]({{< relref "octopus-deploy" >}})
* [Spinnaker Plugin](https://github.com/pulumi/spinnaker-preconfigured-job-plugin) - [Spinnaker Guide]({{< relref "spinnaker" >}})

If you are using a CI system that does not have a native extension for installing the CLI, you can always run an inline script step
to [install the CLI manually]({{< relref "/docs/get-started/install" >}}).

#### Tips

* Ensure that the `pulumi` CLI is available in the environment across multiple steps.

  In most cases, the official Pulumi installation script will try to add `pulumi` to the system `PATH` automatically.

  This problem is especially prevalent for users using a Docker container-based pipeline. With most Docker container pipelines, the state of the container
  does not persist across steps, so you cannot split-out the installation step of the Pulumi CLI into another step and expect to use the modified environment
  in the following step. There are exceptions to this. Some CI services allow you to create a reusable template step that you can inject as a pre-cursor to other
  steps. This is a way to reduce repeating the installation step every time you would like to run `pulumi` command.

### Build Tools

Pulumi invokes the build tool that corresponds to your Pulumi project's runtime. If your pipeline is missing one of these tools,
Pulumi cannot run your infrastructure app. For example, if your Pulumi project uses the `nodejs` runtime, then making sure that a valid
version of `Node` installed along with `npm` or `yarn` depending on whichever package manager you are using to manage dependencies.

#### Tips

Ensure that your Pulumi project's build tools are installed on your CI runner's build agent.

  Many CI services offer built-in mechanisms to acquire language runtimes of a specific version.
  For example, GitHub Actions offers the `actions/setup-node` action that can install `node`, `npm`, and `yarn`. Similarly, there is a GitHub Action for installing
  the runtime for [Python](https://github.com/actions/setup-python), [Go](https://github.com/actions/setup-go), as well as [.NET](https://github.com/actions/setup-dotnet).

  If you are using a Docker container-based build, consider using one of Pulumi's [SDK images](https://github.com/pulumi/pulumi/tree/master/docker#sdk-images) for your respective language.

### Restoring Dependencies

Regardless of the language you pick for your Pulumi app, you will have dependencies on at least one other package or library. You must ensure that you
restore these dependencies before running a `pulumi` command. In the case of `.NET` and `Go` runtimes, those dependencies are automatically restored for you
when you run `pulumi preview` or `pulumi update --yes`.

#### Tips

* For `nodejs` and `python` runtimes, add a step prior to running any `pulumi` commands to restore the dependencies.
* For `dotnet` and `go` runtimes, the dependencies are restored for you automatically when you run `pulumi preview` or `pulumi update --yes`.
* There is an exception to restoring dependencies automatically for `.NET` when you use a private package feed. You must ensure that the
package(s) from the private feed are accessible or you can use a [pre-built binary]({{< relref "/docs/intro/concepts/project" >}})) with Pulumi to avoid rebuilding your `.NET` solution again.

> Note that if you do choose to use a pre-built binary, you will need to install the necessary Pulumi plugins manually using `pulumi plugin install`.

* You might be caching the library dependencies but not the Pulumi plugins. Some services offer dependency caching by capturing a specific folder and restoring
that folder when your pipeline executes. However, note that Pulumi dependencies have a post-install step that also pulls-down
a [plugin]({{< relref "/docs/intro/concepts/how-pulumi-works#resource-providers" >}}) binary from our CDN. So be sure to cache the plugins path as well.

  If in doubt about problems encountered during execution, clear out all caches and restore dependencies from scratch.

> Note that depending on the number of providers you use in your Pulumi app, the cache size can get big. Some CI services have
> restrictions on the max size of the cache.

### Cloud Provider Credentials

Cloud provider credentials are another common point of failure. The class of errors related to cloud provider credentials can include:

* Incorrect credentials (wrong account, mismatched keys, etc.)
* Keys with a strict access scope that don't have access to creating specific resources

#### Tips

* Make sure that the cloud provider credentials are made accessible to `pulumi` using a valid mechanism.
In almost all cases, specifying the credentials through environment variables will work.

  Some cloud providers also support authentication via their respective CLIs.
  For example, the Azure provider supports authentication via the Azure CLI.
  But if the Azure CLI is not properly authenticated (account doesn't have the right role, subscription etc.),
  then Pulumi will not be able to acquire the necessary credentials.

* Ensure that the step with the `pulumi` command can actually access to the environment variables containing the credentials.

  If your CI service has features that allow you to restrict which pipelines or steps in a pipeline can access the secrets, then ensure that
  your pipeline/steps can access them.
  Many CI services allow you to group steps in the form of `jobs` or `stages`. If you are using one of those, make sure that the `job` or `stage`
  in which you are running the `pulumi` command has the expected environment variables. Sometimes build agent environments get reset across
  jobs, stages etc. depending on how the CI service you are using works.

* Check that there are not typos in the name of the environment variables.

> Refer to the cloud providers in the [Registry]({{< relref "/registry" >}}) docs and the respective setup pages for each to find the correct
environment variables to use.

#### Still need help?

If the above tips don't help solve your particular issue, then there is always the power of the strong,
knowledgeable [Pulumi Slack Community](https://slack.pulumi.com). Signup is free and quick. In addition to other
community members, various members of the Pulumi team themselves hang out in the Slack channels and would be happy to help you.
