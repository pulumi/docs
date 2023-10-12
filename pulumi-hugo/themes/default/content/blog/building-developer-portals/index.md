---
title: "Building Developer Portals with Pulumi"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2023-10-12

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Pulumi introduces a golden path for platform teams to enable their developers to provision new services from a set of best practice templates.


# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - meagan-cojocar

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
- developer-portals
- templates
- policy-as-code
- backstage


# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

At Pulumi, we work with organizations that range from a few platform team members to entire departments for managing infrastructure. Many organizations, like [Mercedes-Benz](https://www.pulumi.com/case-studies/mercedes-benz/), have built internal developer platforms on top of Pulumi to enable developers to self-serve infrastructure templates, and partners like [AWS Proton](https://www.pulumi.com/blog/aws-proton-pulumi/) and [Port](https://www.getport.io/blog/using-pulumi-with-an-internal-developer-portal) have built integrations with Pulumi to enable self-service scenarios. We are thrilled to have [announced yesterday](/blog/developer-portal-platform-teams) the launch of our new suite of tools to build internal developer portals with Pulumi, a result of working directly with our customers to understand their problems and how Pulumi can solve it.

<!--more-->

Pulumi launched [Pulumi Templates](/templates) last year, out of the box templates based for common architectures, such as serverless templates, container service templates and Kubernetes cluster templates. The introduction of these templates allows Pulumi customers to go from 0 to 1 much quicker, but as they scale their IaC complexity a need for custom templates arises. To address this, we are expending into managing custom templates as a self-service provisioning experience.

## Introduction to Developer Portals with Pulumi

{{< video title="The New Project Wizard in Pulumi Cloud" src="https://www.pulumi.com/uploads/npw.mp4" controls="false" autoplay="true" loop="true" >}}

Many of our customers are building their own developer portals on top of [Pulumi Automation API](https://www.pulumi.com/docs/using-pulumi/automation-api/) and [Pulumi Deployments](https://www.pulumi.com/docs/pulumi-cloud/deployments), but we also wanted to offer options for teams that cannot (or do not want to) build a custom solution. The suite of tools for building internal developer portals include:

1. New Project Wizard: Showcased in the GIF above, Pulumi Cloud now enables developers to provision infrastructure entirely via point-and-click in Pulumi Cloud with the new New Project Wizard experience. This offers a great out-of-the box developer portal experience for any team using Pulumi Cloud.
2. Organization Templates: Pulumi Cloud now supports registering your own custom templates for your organization which will be made available in the New Project Wizard. This enables platform teams to standardize infrastructure creation and distribute those best practices where developers are already spending their time.
3. Pulumi Backstage Plugin: For teams using Backstage, they can now integrate Pulumi directly within their Backstage instance, via support for a new Pulumi plugin as well as new Pulumi scaffolder actions.
4. `pulumi new` support for private templates: By default, `pulumi new` provides a number of templates provided by Pulumi, but now your organization can also use private templates.

### Key Benefits

**Ease of Deployment**: With this new functionality, you can quickly find and deploy the services you need, reducing the time and complexity of managing your cloud infrastructure. As a developer, if you are looking for a platform team sanctioned way to deploy a Kubernetes cluster, instead of chasing it down you can head to Pulumi Cloud, find the golden template and deploy it.

**Enhanced Distribution**: As a platform team member, share templates and configurations with your developers to ensure consistency and collaboration across your organization. It's as simple as adding the template to a repo and selecting that repo in Pulumi Cloud. Now all of your developers have access to it when they go to create new infrastructure.

**Combination with Other Features**: The new template experience seamlessly integrates with your existing Pulumi workflows, providing a unified experience across your infrastructure management. Increase your developer productivity by using this suite of features in combination with [Pulumi ESC](/docs/pulumi-cloud/esc). Attach an Environment to your template to have it come with configuration and secret values. Once the templates are deployed they will show in the Pulumi Cloud console use [Policies](/docs/using-pulumi/crossguard) over it, set up [Review Stacks](/docs/pulumi-cloud/deployments/review-stacks) on the new stack to get ephemeral environments tied to PRs, find the resources that were deployed with [Resource Search](/docs/pulumi-cloud/insights/search), and all the other Pulumi Cloud features.

**Extensibility**: You can leverage the out of the box New Project Wizard Experience or build developer portals with Pulumi yourself using any combination of: the Pulumi Backstage Plugin, `pulumi new` public and private templates, the Pulumi Backstage Plugin, Automation API, Pulumi Deployments, or the Pulumi Cloud REST API.

## Getting Started

### New Project Wizard

The New Project Wizard allows anyone in your organization to pick a template they want to install, create the repo or directory for it, and walk through configuring the deployment of that template. We’ve added support for configuring [Pulumi Deployments](/docs/pulumi-cloud/deployments/get-started/#new-project-wizard), meaning any template can be deployed without needing the Pulumi CLI locally, or any other CI/CD configuration. Follow these steps to be up and running with your infrastructure in a few clicks:

- You can either 1/ use the UI or 2/ use Deploy with Pulumi buttons. If using the UI, navigate to the “New Project” tab. Select “Use a template” if you’d like to create a fully featured project, or select “Use a starter” if you want to create a bare-bones project with only the minimal necessary boilerplate file structure and Pulumi code. If you are using [Deploy with Pulumi buttons](/docs/pulumi-cloud/pulumi-button), you can embed a button on your templates inside GitHub to enable point-and-click deployment of those templates.
- In order to use templates you will need to authorize Pulumi with GitHub so that it can clone private repositories as template sources and commit new code for your projects. Click the “Authorize GitHub” button and accept the required permissions if you would like to use templates.
- On the next screen select your deployment method. You may need to install the Pulumi GitHub app if you haven’t already to use Pulumi Deployments.
- You’ll now be prompted to enter some information about the project you’re about to create: the project and stack name, the configuration details specific to that template, the repo to use when committing your new project code, and optionally the Environment you want to use. Environments enable you to use a bundle of pre-configured secrets and configuration values without needing to re-specify all of them during project creation.
- After you’ve configured your project settings, you will be able to configure the behavior of Deployments, including when to trigger new Deployments and environment variables to include with your updates.

And just like that you have created a new project from a template that is deployed, without the use of the Pulumi CLI.

### Organization Templates

Pulumi now allows customers on the Pulumi Cloud Enterprise and Business Critical editions to define Organization Templates to help get projects off the ground faster. A Pulumi organization admin can specify an Organization Template Source (or Sources) which will then be populated in the New Project Wizard experience described above.

Navigate to the “Integrations” tab to define your Organization Templates Source. Enter sources as `github.com/<owner>/<repo>/<optional subdirectory>`. A source can be a directory containing either a Pulumi.yaml, or other subdirectories with their own Pulumi.yaml files. A single repository can provide multiple templates from various subdirectories. For example, these are both valid sources: `github.com/pulumi/templates` (all public Pulumi templates) and `github.com/pulumi/templates/aws-typescript` (a specific public template).

The Pulumi.yaml file can optionally contain a template section, which typically includes a config section for specifying required config values for the project. Each config value can have a description and a default value which can be overridden. Config values can be marked as secret, which ensures values in templated projects will be stored with secure encryption.

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

### Pulumi & Backstage

We’ve seen many developer portal technologies rapidly growing in popularity over the last few years. In particular, we’ve seen Pulumi users adopting [Backstage](https://backstage.io) and as a result we built the Pulumi Backstage Plugin to address the needs of organizations using Backstage and Pulumi together. There are now two ways to use Pulumi from within Backstage, you can leverage both or just one or the other:

1. Pulumi Scaffolder Backend Module
2. Pulumi Backstage Plugin

**Pulumi Scaffolder Backend Module**: The Pulumi Scaffolder Backend Module extends the scaffolding with two new actions: Pulumi New and Pulumi Up. The Pulumi New action is a custom action that allows you to create a new Pulumi project from a template using the `pulumi new` Pulumi CLI command. The Pulumi Up Action is a custom action that allows you to run the `pulumi up` command, which creates or updates resources in a stack.

```yaml
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: kubernetes-template
  title: Kubernetes Cluster
  description: |
    A template for creating a new Kubernetes Cluster.
  tags:
    - pulumi
    - kubernetes
spec:
  steps:
    - id: pulumi-new-component
      name: Cookie cut the component Pulumi project
      action: pulumi:new
      input:
        name: "${{ parameters.component_id }}-infrastructure"
        description: ${{ parameters.description | dump }}
        organization: ediri
        stack: ${{ parameters.stack }}
        template: "https://github.com/my-silly-organisation/microservice-civo/tree/main/infrastructure-${{ parameters.cloud }}-${{ parameters.language }}"
        config:
          "node:node_count": "${{ parameters.nodeCount }}"
        folder: .
```

With a few clicks, developers can create new software projects provisioned with best practices, with code managed in the right repositories, and with the right configurations, all from a self-service UI.

**Pulumi Backstage Plugin**: Backstage Plugins are extensions or add-ons to the core Backstage application that allow you to integrate additional tools, services, and functionalities into the platform, enhancing its capabilities and customizing it to meet the specific needs of your development environment.

The Pulumi Backstage Plugin extends Backstage by displaying essential details like the Pulumi stack, organization, project name, and description, as well as providing an activity view with aggregated information from the Pulumi Cloud. See a screenshot of the new Pulumi tab within Backstage below:

![Pulumi Backstage Plugin](./backstage-plugin.png)

Check out the [Pulumi Backstage Plugin](https://github.com/pulumi/pulumi-backstage-plugin) in the [Backstage Plugin directory](https://backstage.io/plugins/) or the [Roadie Pulumi Backstage Plugin guide](https://roadie.io/backstage/plugins/pulumi/) to get started today.

### Wrapping it up

The launch of this new functionality for internal developer portals marks a significant step forward in our commitment to providing powerful, turn-key tools for platform teams. We believe these features will enhance your experience with Pulumi, whether you're a seasoned cloud expert leading a team of platform engineers or just getting started on your IaC journey.

As always, we welcome your feedback in the [Pulumi Cloud Requests repository](https://github.com/pulumi/pulumi-cloud-requests/issues/new?assignees=&labels=kind%2Fenhancement&projects=&template=feature-request.md) and are here to support you every step of the way on your platform engineering journey.
