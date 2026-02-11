---
title: Organization templates
title_tag: Get started with organization templates
h1: Organization templates
meta_desc: Learn how to build template projects and configure them to work with your Pulumi organization.
menu:
  idp:
    name: Organization templates
    parent: idp-concepts
    weight: 20
    identifier: idp-concepts-organization-templates
aliases:
  - /docs/idp/developer-portals/templates/
  - /docs/pulumi-cloud/developer-platforms/templates/
  - /docs/pulumi-cloud/developer-portals/templates/
  - /docs/idp/concepts/templates
---

{{% notes "info" %}}
Organization Templates are only available to organizations using the Enterprise and Business Critical editions.

If you would like to use this feature, [contact us](/contact?form=sales) to upgrade.
{{% /notes %}}

A large number of public project templates are provided by Pulumi in our [examples](https://github.com/pulumi/examples) and [templates](https://github.com/pulumi/templates) repos. These can be useful for teams starting from scratch; however, as your business and infrastructure grow in complexity, it is likely you will want new Pulumi projects to include some custom, internal functionality not provided by these public templates.

Pulumi allows you to define _Organization Templates_ to help get projects off the ground faster. This enables you to provide new Pulumi projects with consistent code structure, conventions, or best practices.

## Template Publishing Approaches

Pulumi supports two approaches for managing organization templates:

### Registry-backed templates

Registry-backed templates, or Private Registry templates, are published directly to your organization's Private Registry using the `pulumi template publish` command. This approach offers:

- Semantic versioning: Full semver support with immutable version storage
- Simple publishing: Single CLI command to publish templates
- Version control: Track and manage template versions independently

### VCS-backed templates

VCS-backed templates are sourced from GitHub or GitLab repositories that you configure as template sources. This approach:

- Sources templates directly from your VCS repositories
- Requires VCS availability at template access time
- Integrates with your existing repository structure
- Templates are fetched on-demand from repositories

## Defining an Organization Template

### Template structure

All Pulumi templates require a valid `Pulumi.yaml` file at the root of the template directory. For registry-backed templates, this is the directory you publish. For VCS-backed templates, this can be at the repository root or within a subdirectory.

The `Pulumi.yaml` file must contain a `template` section to be recognized as a valid template. This section typically includes a `config` section for specifying required config values for the project. Each config value can have a `description` and a `default` value. Config values can be marked as [`secret`](/docs/concepts/secrets), which ensures values in templated projects will be stored with secure encryption.

```yaml
name: my-aws-project
runtime: nodejs
description: My AWS project description
template:
  displayName: "My AWS Project Template"
  description: "A template for AWS projects with best practices"
  config:
    aws:region:
      description: The AWS region to deploy into
      default: us-west-2
    myAccessToken:
      description: My access token
      secret: true
  metadata:
    category: "infrastructure"
    framework: "aws"
```

The above snippet includes:

- `displayName` and `description` for the template (optional but recommended)
- An `aws:region` configuration value with a default value of `us-west-2`
- A `myAccessToken` secret without a default value
- Custom metadata for categorization (optional)

When a project is created from a template, the resulting project will include:

- A modified `Pulumi.yaml` file, which reflects the new project's name and description.
- A new `Pulumi.<stack>.yaml` file, which includes populated configuration values as specified in the `template` section of the source `Pulumi.yaml`.
- A copy of all other files co-located with the source `Pulumi.yaml`.

Any occurrences of `${PROJECT}` or `${DESCRIPTION}` -- in `Pulumi.yaml` or any other files -- will be replaced with their respective values.

### Additional template files

Templates can include a `README.md` file in the same directory as the `Pulumi.yaml`. This README will be displayed in the Private Registry and helps users understand how to use the template. For registry-backed templates, the README is extracted during publishing and stored separately for fast access.

Templates can include any other files needed for the project (source code, configuration files, etc.). These files are copied when a project is created from the template.

## Publishing Registry-backed Templates

Registry-backed templates are published to your organization's Private Registry using the Pulumi CLI.

### Publishing a template

To publish a template to the Private Registry:

1. Create a directory containing your template files, including a `Pulumi.yaml` with a `template` section
1. Run the publish command:

```bash
pulumi template publish <directory> --name <template-name> --version <version>
```

**Example:**

```bash
pulumi template publish ./my-aws-template --name my-aws-template --version 1.0.0
```

### Command options

- `--name` (required): The name of the template
- `--version` (required): The semantic version of the template (e.g., "1.0.0")
- `--publisher` (optional): The organization to publish to (defaults to your default organization)

### Publishing requirements

- The template directory must contain a valid `Pulumi.yaml` with a `template` section
- The version must follow semantic versioning format (e.g., "1.0.0", "2.1.3")
- Each published version is immutable and cannot be modified

### Template versioning

Registry-backed templates support full semantic versioning:

- Publish multiple versions of the same template
- Users can specify a version when using a template
- Each version is stored immutably and independently
- Update templates by publishing new versions

**Example publishing a new version:**

```bash
# Publish version 1.0.0
pulumi template publish ./my-template --name my-template --version 1.0.0

# Later, publish version 1.1.0 with updates
pulumi template publish ./my-template --name my-template --version 1.1.0
```

### Using registry-backed templates

Once published, templates are available in your organization:

**From the CLI:**

```bash
# Use latest version
pulumi new private/my-org/my-template

# Use specific version
pulumi new private/my-org/my-template@1.0.0
```

**From the Pulumi Console:**

- Navigate to the Private Registry to browse templates
- Select a template to view its README and metadata
- Use the New Project Wizard to create projects from templates

## Using Organization Templates within your Pulumi organization

Organization templates are available to users in the [private registry](/docs/idp/concepts/private-registry/). They also power the New Project Wizard workflow.

By doing publishing organization templates, your organization's members will be able to:

- Discover template in the [private registry](/docs/idp/concepts/private-registry/).
- Configure and launch new Pulumi projects from their browser.
- Configure [Pulumi Deployments](/docs/pulumi-cloud/deployments) to automatically work with new projects.

## Configuring VCS-backed Templates

You can configure GitHub or GitLab repositories as template sources for VCS-backed templates.

### Prerequisites

#### Template sources

VCS-backed templates require that your Pulumi account has an integration configured with your preferred VCS vendor.

This can be set up by navigating to your organization's "Settings → Integrations" tab, under the "Organization Template Sources" section.
If you have not already authorized you will see an "Authorize GitHub" or "Authorize GitLab" button. Click the button and accept the required permissions.

#### Template destinations

VCS-backed template destinations only support GitHub as they leverage Deployments for Pulumi operations.
If you plan on using no-code or CLI deployment methods these prerequisites are not necessary.

##### GitHub OAuth

This authorization is needed in order to act on your behalf (and not as the Pulumi GitHub app) when fetching and creating private repositories.
More specifically, this ensures that only repositories your GitHub user would normally have access can be used as template sources.

Navigating to your organization's "Settings → Integrations" tab will show an "Organization Template Sources" section. If you have not already authorized the app you will see an "Authorize GitHub" button. Click the button and accept the required permissions. This can also be set up during the new [project wizard flow](/docs/idp/concepts/new-project-wizard/#github-oauth-application).

If you have OAuth App access restrictions enabled in your Github organization, you will also need to
[authorize the Pulumi Github App](https://docs.github.com/en/organizations/managing-oauth-access-to-your-organizations-data/approving-oauth-apps-for-your-organization)
in the "OAuth App Policy" settings.

##### GitHub App

You will need the Pulumi GitHub application installed and connected to your Pulumi organization in order to configure [Deployment settings](/docs/deployments/deployments/reference/#deployment-settings) on new projects.
See the GitHub app [installation instructions](/docs/deployments/deployments/reference/#github-app-installation) for more details.

{{% notes "info" %}}
Granting the app access to _some_ or _all_ of your GitHub repos will impact how the New Project Wizard behaves.

If you grant the app access to _all_ repos, the New Project Wizard will allow users to create projects in new repositories. If the app only has access to _some_ repos, users will only be able to create new projects within _existing_ repositories.
{{% /notes %}}

### Organization settings

Navigate to the "Integrations" tab to configure the Pulumi New Project Wizard to define your Organization Templates Source.
Enter sources as `github.com/<owner>/<repo>/<optional subdirectory>`. A source can be a directory containing either a `Pulumi.yaml`, or other subdirectories with their own `Pulumi.yaml` files. For example, these are both valid sources:

- `github.com/pulumi/templates` (all public Pulumi templates)
- `github.com/pulumi/templates/aws-typescript` (a specific public template)

Private repositories work similarly as long as your GitHub user has access to the repository.

After you have configured template sources, the private registry and New Project Wizard will allow users to use those sources when creating new projects with Deployments.
