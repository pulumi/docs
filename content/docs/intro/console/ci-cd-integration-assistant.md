---
title: CI/CD Integration Assistant
meta_desc: The CI/CD Integration Assistant helps you automate your Pulumi stack.
---

The CI/CD integration assistant contains a guided experience in the Pulumi Console that provides customized CI/CD
workflows for Pulumi stacks. The starter workflows use best-practices in configuring a pipeline
to automate updating a Pulumi stack.

<!--more-->

The wizard has two options to help you to get started with integrations:

* Use a service that provides both a version control system and a CI/CD service
* Or, just get the starter workflow for a CI/CD service of your choice customized for your stack
without going through the wizard

![Start Workflow Wizard](/images/docs/reference/console/start-workflow-wizard.png)

The CI/CD integration assistant also offers best practice hints for stacks that do not
have a VCS configuration.

Here's a look at the various ways the assistant helps your team members in the Console.

The dashboard page will show you any recent stacks that were updated and if they have VCS configuration. If not, a quick navigation
link is provided to help users configure VCS.

![Dashboard](/images/docs/reference/console/dashboard-page.png)

A quick look at the Activity page for a stack quickly reveals which of the updates were run from a CI/CD pipeline and which ones were not.

![Activity](/images/docs/reference/console/update-activity.png)

In addition to the above two features, the assistant also recognizes any "production"-like stacks created in your organization and emails
the creator to configure VCS and to automate the stack with a CI/CD pipeline, if the appropriate configuration is not found.

## Using The Same Service For VCS and CI/CD

There are many benefits for a team to choose a single service for all of their team collaboration needs. This section reviews
how the wizard helps your teams configure VCS and CI/CD using the identity that you signed-up with.

![Workflow Assistant Email](/images/docs/reference/console/cicd-integration-assistant-email.png)

### Configuring a VCS

> VCS configuration applies to the Pulumi project in which your stack is created.

Select an identity you wish to use to setup VCS, as well as a CI/CD pipeline for the stack.

Some services such as Atlassian Bitbucket, GitHub, GitLab offer both a version control system as well as a CI/CD service.
So this might be a convenient option if your team wishes to keep everything related to your
Pulumi project on a single service.

> For SAML and Email-based identity users, the wizard will not be able to provide smart
> links to a specific service due to the nature of the identity itself. However, the
> wizard still provides a customized CI/CD workflow for your stack that you can use.

After you choose an identity, the wizard will provide you with a quick link
to create a new repository in the target service as well as the instructions for
ensuring that Pulumi correctly recognizes the VCS configuration.

![Configure VCS](/images/docs/reference/console/configure-vcs.png)

Complete each step and check-off the appropriate step. When all steps under the
**Configure VCS** step are complete click the **Next** button. The wizard will confirm
that your VCS configuration has been recognized and will automatically move you to the
next step.

![Complete Configre VCS](/images/docs/reference/console/configure-vcs-complete.png)

### Configure CI/CD secrets

Now that your Pulumi project is configured to use a VCS your team can collaborate with you easily.
Most importantly, your Pulumi project is safe from accidents on your local machine!

If you start the CI/CD integration wizard having configured the VCS for your project already,
the wizard will skip to the next step automatically. You can see the repository that your project
is integrated with by clicking on the Configure VCS step marker. Here's an example of how that looks:

![VCS configured](/images/docs/reference/console/vcs-configured.png)

The **Configure CI/CD** step will help you configure secrets that will be used by your Pulumi stack.
For supported services, the wizard will provide a convenient link to the respective location
where you can configure the secrets.

The wizard provides a convenient way to create a [Pulumi Access Token]({{< relref "/docs/intro/console/accounts-and-organizations/accounts#access-tokens" >}})
without needing to leave the page.

![Pulumi Access Token](/images/docs/reference/console/pulumi-access-token.png)

In the following example the wizard is being used to configure a GitHub Actions workflow.
So the wizard provides a direct link to configure secrets for your workflow.

![Configure CI/CD Secrets](/images/docs/reference/console/configure-ci-cd-secrets.png)

> See the [Cloud Providers]({{< relref "/docs/intro/cloud-providers" >}}) page to find the setup page for your cloud provider.

### Add the workflow

Once the secrets are configured, the next step gives you the relevant workflow to add to your repository.
The workflow is customized for the current stack, so you can be sure that you are configuring a workflow that uses
the correct stack configuration.

![Add Workflow](/images/docs/reference/console/add-workflow.png)

> Be sure to commit the new workflow file to a separate branch and not directly to your primary branch. This will create a new pull request for you.

The workflow is configured to run a `pulumi preview` for Pull Request pipelines.
Pull Request builds help you catch problems with changes to your infrastructure _before_ the changes are approved/merged.

### Validation

In the previous step you committed a new workflow configuration by creating a new Pull Request. This will trigger a new pipeline build
that will run the `pulumi preview` command. Click the **Next** button to make the wizard check for and validate the CI configuration.

Congratulations on configuring a version control system and an automated pipeline for your stack! 🎉

If your pull request build failed, use the [CI/CD troubleshooting guide]({{< relref "/docs/guides/continuous-delivery/troubleshooting-guide" >}}) to diagnose the issue.

## Skip the line and get the workflow directly

If you want to access the workflow for a specific CI/CD service and configure VCS on your own,
you can do that by simply selecting a service from the drop-down to get started. You will
still get a workflow template that is customized to your stack.

> This option is more suitable for teams that want to use different services for their VCS repo and CI/CD needs. For example, you want
> to be able to use Azure Pipelines with a GitHub repository and just want the workflow template for Azure Pipelines.

![Get Workflow](/images/docs/reference/console/get-workflow.png)
