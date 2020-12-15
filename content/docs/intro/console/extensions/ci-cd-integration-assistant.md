---
title: CI/CD Integration Assistant
meta_desc: An overview of the CI/CD integration assistant in the Pulumi Console.
---

> This feature is available on the Pulumi Team Pro and Enterprise editions.
> If you would like to try this feature, [start a trial](https://app.pulumi.com/site/organizations/add) now
> or contact us at <a href="mailto:sales@pulumi.com">sales@pulumi.com</a>.

The CI/CD integration assistant helps you integrate Pulumi into CI/CD systems for automatically deploying stacks.

<!--more-->

A version control system (VCS) provides team collaboration capabilities and ensures that the source code for your Pulumi project is not
just on a single developer's machine. Using a CI/CD system makes your team more productive, by automatically deploying your Pulumi stacks.
So that code is delivered to production -- meaning less of a lag between commits and what your end users are seeing.

The assistant contains a guided experience to help teams configure a VCS as well as automate it with a
CI/CD pipeline.

The wizard has two options to help you to get started with integrations:

* Use a single service that provides both a version control system and CI/CD pipelines
* Or, just get the starter workflow for a CI/CD service of your choice customized for your stack

![Start Workflow Wizard](/images/docs/reference/console/start-workflow-wizard.png)

The assistant also offers best practice hints for stacks that do not have a VCS configuration.
Here's how the assistant helps teams throughout the Console:

* The dashboard page shows recently updated stacks. The assistant alerts users by providing a quick navigation link to configure a VCS
for any stacks that don't have it.

* The **Activity** page for a stack allows users to scan the page quickly and tell which of the updates were run from a
CI/CD pipeline and which ones were not.

## Using The Same Service For VCS and CI/CD

There are several benefits for a team to choose a single service for all of their team collaboration needs.
This section reviews how the wizard helps your team configure VCS and CI/CD regardless of the VCS or identity provider
you use to connect to Pulumi.

### Configuring a VCS

> VCS configuration applies to the Pulumi project in which your stack is created.

Select an identity you wish to use to setup VCS, as well as a CI/CD pipeline for the stack.

Services such as Atlassian Bitbucket, GitHub, GitLab offer both a version control system as well as a CI/CD service.

* Bitbucket offers [Bitbucket Pipelines](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/)
* GitHub has [GitHub Actions](https://github.com/features/actions)
* GitLab has [GitLab CI/CD](https://docs.gitlab.com/ce/ci/)

This might be a convenient option if your team wishes to keep everything related to your Pulumi project on a single service.

> If your identity isn't tied to a VCS service, like SAML or Email, you will still be able to get a customized CI/CD
> workflow for your stack.

After you choose an identity, the wizard will provide you with a quick link
to create a new repository in the target service as well as the instructions for
ensuring that Pulumi correctly recognizes the VCS configuration.

Complete each step and check-off the appropriate step. When all of the tasks under the
**Configure VCS** step are complete click the **Next** button. The wizard will confirm
that your VCS configuration has been recognized and will automatically move you to the
next step.

### Configure CI/CD secrets

Now that your Pulumi project is configured to use a VCS your team can collaborate with you easily.
Most importantly, your Pulumi project is safe from accidents on your local machine!

If you start the CI/CD integration wizard having configured the VCS for your project already,
the wizard will skip to the next step automatically. You can see the repository that your project
is integrated with by clicking on the Configure VCS step marker.

The **Configure CI/CD** step will help you configure secrets that will be used by your Pulumi stack.
For supported services, the wizard will provide a convenient link to the respective location
where you can configure the secrets.

The wizard provides a convenient way to create a [Pulumi Access Token]({{< relref "/docs/intro/console/accounts-and-organizations/accounts#access-tokens" >}})
without needing to leave the page.

![Pulumi Access Token](/images/docs/reference/console/pulumi-access-token.png)

In the following example the wizard is being used to configure a GitHub Actions workflow.
So the wizard provides a direct link to configure secrets for your workflow.

> See the [Cloud Providers]({{< relref "/docs/intro/cloud-providers" >}}) page to find the setup page for your cloud provider.

### Add the workflow

Once the secrets are configured, the next step gives you the relevant workflow to add to your repository.
The workflow is customized for the current stack, so you can be sure that you are configuring a workflow that uses
the correct stack configuration.

![Add Workflow](/images/docs/reference/console/add-workflow.png)

> Be sure to commit the new workflow file to a separate branch and not directly to your primary branch. This will create a new pull request for you.

The workflow configuration provided by the wizard is configured to run a `pulumi preview` for pull request builds.
Pull request builds help you catch problems _before_ the changes are merged -- a very important consideration for infrastructure
that is likely hosting services critical to your business.

### Validation

In the previous step, you committed a new workflow configuration by creating a new pull request. This will trigger a new build
that will run the `pulumi preview` command. Click the **Next** button to validate the CI configuration.

Congratulations on configuring a version control system and an automated pipeline for your stack! 🎉

> If your pull request build failed, use the [CI/CD troubleshooting guide]({{< relref "/docs/guides/continuous-delivery/troubleshooting-guide" >}}) to diagnose the issue.

## Skip the line and get the workflow directly

If you want to access the workflow for a specific CI/CD service and configure VCS on your own,
you can do that by simply selecting a service from the drop-down to get started. You will
still get a workflow template that is customized to your stack.

> This option is more suitable for teams that want to use different services for their VCS repo and CI/CD needs. For example, you want
> to be able to use Azure Pipelines with a GitHub repository and just want the workflow template for Azure Pipelines.

![Get Workflow](/images/docs/reference/console/get-workflow.png)
