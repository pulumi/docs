---
title: Organization Templates
title_tag: Get started with Organization Templates
h1: Building Developer Portals with Organization Templates
meta_desc: Lean how to build template projects and configure them to work with your Pulumi organization.
menu:
  pulumicloud:
    weight: 1
    parent: developer-portals
---

{{% notes "info" %}}
Organization Templates are only available to organizations using the Enterprise and Business Critical editions.

If you would like to use this feature, [contact us](/contact?form=sales) to upgrade.
{{% /notes %}}

A large number of public project templates are provided by Pulumi in our [examples](https://github.com/pulumi/examples) and [templates](https://github.com/pulumi/templates) repos. These can be useful for teams starting from scratch; however, as your business and infrastructure grows in complexity it is likely you will want new Pulumi projects to include some custom, internal functionality not provided by these public templates.

Pulumi allows you to define _Organization Templates_ to help get projects off the ground faster. This enables you to provide new Pulumi projects with consistent code structure, conventions, or best practices.

## Defining an Organization Template

A template can be hosted in a public or private GitHub repository, and its only requirement is that it must contain a valid `Pulumi.yaml` at the root or within a subdirectory of the repository. A single repository can provide multiple templates from various subdirectories.

The `Pulumi.yaml` file can optionally contain a `template` section, which typically includes a `config` section for specifying required config values for the project. Each config value can have a `description` and a `default` value. Config values can be marked as [`secret`](/docs/concepts/secrets), which ensures values in templated project will be stored with secure encryption.

```yaml
name: my-aws-project
runtime: nodejs
description: My AWS project description
template:
  config:
    aws:region:
      description: The AWS region to deploy into
      default: us-west-2
    myAccessToken:
      description: My access token
      secret: true
```

The above snippet includes an `aws:region` configuration value with a default value of `us-west-2`, as well as a `myAccessToken` secret without a default value.

When a project is created from a template, the resulting project will include:

* A modified `Pulumi.yaml` file, which reflects the new project's name and description.
* A new `Pulumi.<stack>.yaml` file, which includes populated configuration values as specified in the `template` section of the source `Pulumi.yaml`.
* A copy of all other files co-located with the source `Pulumi.yaml`.

Any occurrences of `${PROJECT}` or `${DESCRIPTION}` -- in `Pulumi.yaml` or any other files -- will be replaced with their respective values.

## Using Organization Templates within your Pulumi organization

A Pulumi organization admin can configure their organization to use Organization Templates with the [New Project Wizard](/docs/pulumi-cloud/developer-portals/new-project-wizard). By doing so, your organization's members will be able to:

* Template and configure new Pulumi projects from their browser.
* Automatically push code for new projects into new or existing GitHub repositories.
* Configure [Pulumi Deployments](/docs/pulumi-cloud/deployments) to automatically work with new projects.

### Prerequisites

#### GitHub App

You will need the Pulumi GitHub application installed and connected to your Pulumi organization in order to configure [Deployment settings](/docs/pulumi-cloud/deployments/reference/#deployment-settings) on new projects.
See the GitHub app [installation instructions](/docs/pulumi-cloud/deployments/reference/#github-app-installation) for more details.

{{% notes "info" %}}
Granting the app access to _some_ or _all_ of your GitHub repos will impact how the New Project Wizard behaves.

If you grant the app access to _all_ repos, the New Project Wizard will allow users to create projects in new repositories. If the app only has access to _some_ repos, users will only be able to create new projects within _existing_ repositories.
{{% /notes %}}

#### GitHub OAuth

You will also need to authorize Pulumi with GitHub in order to use private repositories as template sources.
This authorization is needed in order to act on your behalf (and not as the Pulumi GitHub app) when fetching and creating private repositories.
More specifically, this ensures that only repositories your GitHub user would normally have access can be used as template sources.

Navigating to your organization's "Settings → Integrations" tab will show an "Organization Template Sources" section. If you have not already authorized you will see an "Authorize GitHub" button. Click the button and accept the required permissions.

### Organization settings

Navigate to the "Integrations" tab to configure the Pulumi New Project Wizard to define your Organization Templates Source.
Enter sources as `github.com/<owner>/<repo>/<optional subdirectory>`. A source can be a directory containing either a `Pulumi.yaml`, or other subdirectories with their own `Pulumi.yaml` files. For example, these are both valid sources:

* `github.com/pulumi/templates` (all public Pulumi templates)
* `github.com/pulumi/templates/aws-typescript` (a specific public template)

Private repositories work similarly as long as your GitHub user has access to the repository.

After you have configured template sources, the New Project Wizard will allow users to use those sources when creating new projects with Deployments.
