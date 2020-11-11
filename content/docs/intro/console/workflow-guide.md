---
title: Workflow Guide
meta_desc: Use the Workflow Guide available in the Pulumi Console to automate your stack.
---

The workflow guide is a guided experience in the Pulumi Console that offers customized CI/CD
workflows for your stacks. The starter workflows use best-practices in configuring a pipeline
to automate updating your stack.

<!--more-->

The guide offers two options to get started:

* Use a service that provides both a version control system and a CI/CD service
* Or, just get the starter workflow for a CI/CD service of your choice customized for your stack
without going through the guide

![Start Workflow Guide](/images/docs/reference/console/start-workflow-guide.png)

In addition to the guided experience, the workflow guide also offers best practice hints for stacks that do not
have a VCS configuration.

Here's a look at the various ways the workflow guide helps your team members in the Console.

The dashboard page will show you any recent stacks that were updated and if they have VCS configuration. If not, a quick navigation
link is provided to help users configure VCS.

![Dashboard](/images/docs/reference/console/dashboard-page.png)

A quick look at the Activity page for a stack quickly reveals which of the updates were run from a CI/CD pipeline and which ones were not.

![Activity](/images/docs/reference/console/update-activity.png)

## Using The Same Service For VCS and CI/CD

There are many benefits for a team to choose a single service for all of their team collaboration needs. This section reviews
how the guide helps your teams configure VCS and CI/CD using the identity that you signed-up with.

### Configuring a VCS

> VCS configuration applies to the Pulumi project in which your stack is created.

Select an identity you wish to use to setup VCS, as well as a CI/CD pipeline for the stack.

Some services such as Atlassian Bitbucket, GitHub, GitLab offer both a version control system as well as a CI/CD service.
So this might be a convenient option if your team wishes to keep everything related to your
Pulumi project on a single service.

> For SAML and Email-based identity users, the guide will not be able to provide smart
> links to a specific service due to the nature of the identity itself. However, the
> guide still provides a customized CI/CD workflow for your stack that you can use.

After you choose an identity, the guide will provide you with a quick link
to create a new repository in the target service as well as the instructions for
ensuring that Pulumi correctly recognizes the VCS configuration.

![Configure VCS](/images/docs/reference/console/configure-vcs.png)

Complete each step and check-off the appropriate step. When all steps under the
**Configure VCS** step are complete click the **Next** button. The guide will confirm
that your VCS configuration has been recognized and will automatically move you to the
next step.

![Complete Configre VCS](/images/docs/reference/console/configure-vcs-complete.png)

### Configure CI/CD secrets

Now that your Pulumi project is configured to use a VCS your team can collaborate with you easily.
Most importantly, your Pulumi project is safe from accidents on your local machine!

If you start the workflow guide having configured the VCS for your project already, the guide recognizes the state correctly
and progress you to the next step automatically. You can see the repository that your project is integrated with by clicking
on the Configure VCS step marker. Here's an example of how that looks:

![VCS configured](/images/docs/reference/console/vcs-configured.png)

The Configure CI/CD step will help you configure secrets that will be used by your Pulumi stack.
For supported services, the guide will provide a convenient link to the respective location
where you can configure the secrets that will be used in the CI/CD pipeline that you will
setup next. This includes configuring the [Pulumi Access Token]({{< relref "/docs/intro/console/accounts-and-organizations/accounts#access-tokens" >}})
that will be used by the Pulumi CLI to do a non-interactive login.

The guide provides a convenient way to create a Pulumi Access Token without needing to leave the page.

![Pulumi Access Token](/images/docs/reference/console/pulumi-access-token.png)

In the following example the guide is being used to configure a GitHub Actions workflow. So the guide provides a direct link to configure
secrets for your workflow.

![Configure CI/CD Secrets](/images/docs/reference/console/configure-ci-cd-secrets.png)

> Need help configuring your cloud provider? Find yours on the [Cloud Providers]({{< relref "/docs/intro/cloud-providers" >}}) page and view its setup page.

### Add the workflow

Once your secrets are configured, the next step gives you the relevant workflow to add to your repository.
The workflow is customized for the current stack, so you can be sure that you are configuring a workflow that uses
the correct stack configuration. This is especially useful if you are configuring CI/CD for a non-dev stack.

![Add Workflow](/images/docs/reference/console/add-workflow.png)

> Be sure to commit the new workflow file to a separate branch and not directly to your primary branch. This will create a new pull request for you.

The workflow is configured to run a `pulumi preview` for Pull Request
pipelines. This way you can catch problems with changes to your infrastructure _before_ the changes are approved/merged.

### Validation

In the previous step you committed a new workflow configuration by creating a new Pull Request. This will trigger a new pipeline build
that will run the `pulumi preview` command. Click the **Next** button to make the guide check for and validate the CI configuration.

Congratulations on configuring a version control system and an automated pipeline for your stack! 🎉

If your pull request build failed, don't worry we have a [troubleshooting guide]({{< relref "/docs/guides/continuous-delivery/troubleshooting-guide" >}}) for you!

## Get the workflow only

If instead of using the step-by-step guide, you want to access just the workflow for a specific CI/CD service and
configure VCS on your own, you can do that by simply selecting a service from the drop-down to get started. You will
still be able to get a workflow template that is customized to your stack even if you choose this option.

> This option is more suitable for teams that want to use different services for their VCS repo and CI/CD needs. For example, you want
> to be able to use Azure Pipelines with a GitHub repository and just want the workflow template for Azure Pipelines.

![Get Workflow](/images/docs/reference/console/get-workflow.png)
