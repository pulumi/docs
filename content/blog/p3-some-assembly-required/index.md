---
title: "Pulumi Patterns and Practices Platform (P3): Some Assembly Required"
allow_long_title: true
date: 2024-11-11
draft: false
social_media: "Assembly instructions for building the Pulumi Patterns and Practices
  Platform (P3) reference architecture of a Pulumi-based internal developer platform
  (IDP)."
meta_desc: "Assembly instructions for building the Pulumi Patterns and Practices Platform
  (P3) reference architecture of a Pulumi-based internal developer platform (IDP)."
meta_image: meta.png
authors:
  - troy-howard
tags:
  - platform-engineering
  - patterns-and-practices-platform
  - developer-experience-devex
  - devsecops
  - architecture
  - enterprise
  - devops
search:
  keywords:
    - platform
    - architecture
    - internal developer
    - developer experience
---

Setting up an internal developer platform (IDP) can be a daunting task. There are a lot of tools out there that do some of the work for you, but none of them do all of it. Pulumi P3 is no different. Pulumi Patterns & Practices Platform (P3) is a [reference architecture](https://www.pulumi.com/blog/pulumi-patterns-and-practices/) that we will be describing, and providing code for, through this series of articles.

<!--more-->

We will never try to sell you on the idea that you can simply download a package, click next a few times, and achieve transformative success. That’s because any effective IDP will require some customization and integration to work within your environment.

Tools that purport to have it all figured out have only figured out how to manipulate you into a false narrative they have constructed in a vacuum, where all your organizational needs fit neatly into a few boxes they’ve decided on for you. And also charge you for. In addition to everything else you’re being charged for. Ultimately you’ll still need to build a lot yourself and these products rarely give guidance on how to do that. 

When we first started hearing about our customers using Pulumi as an internal developer platform (IDP), we were frankly surprised, as our goals were primarily for Pulumi to be the best developer experience in infrastructure. But it makes sense. All the parts are there, some assembly required. Our goal with Pulumi Patterns and Practices Platform (P3) is to help with that assembly process.

Starting with our [previous blog post](https://www.pulumi.com/blog/pulumi-patterns-and-practices/) on the topic, and continuing here, we are examining this use case, and attempting to formalize that into a collection of reusable components and some guidance on how you can skip the marketing pitches and pricing charts, and get straight to the hard work of building your own highly customized internal developer platform with Pulumi at its core.

## Pulumi P3: Bill of Materials

Previously we identified the [essential qualities of an effective IDP](https://www.pulumi.com/blog/pulumi-patterns-and-practices/#an-effective-internal-developer-platform). Those were consistency, reproducibility, visibility, security and compliance, auditability, developer experience. In the [last half of the post](https://www.pulumi.com/blog/pulumi-patterns-and-practices/#a-holistic-view-of-the-patterns-and-practices-platform-reference-architecture) we discussed which parts of Pulumi could be used to meet those needs. That looks like: 
* **Consistency**: [component resources](https://www.pulumi.com/learn/abstraction-encapsulation/component-resources/), [organization templates](https://www.pulumi.com/docs/pulumi-cloud/developer-portals/templates/), [drift detection](https://www.pulumi.com/docs/pulumi-cloud/deployments/drift/)
* **Reproducibility**: [stacks](https://www.pulumi.com/learn/building-with-pulumi/understanding-stacks/), [deployments](https://www.pulumi.com/docs/pulumi-cloud/deployments/), [versioned data](https://www.pulumi.com/ai/answers/xig35anR7ibjAP5MhHDyxC/time-travel-queries-on-snowflake-dynamic-tables)
* **Visibility**: [Pulumi Insights](https://www.pulumi.com/product/pulumi-insights/), [Pulumi Copilot](https://www.pulumi.com/product/copilot/)
* **Security and Compliance**: [RBAC](https://www.pulumi.com/docs/pulumi-cloud/access-management/teams/), [GitHub Teams](https://www.pulumi.com/docs/pulumi-cloud/access-management/teams/#github-based-teams), [SAML-SSO](https://www.pulumi.com/docs/pulumi-cloud/access-management/saml/), [Pulumi ESC](https://www.pulumi.com/product/esc/), [Pulumi Crossguard](https://www.pulumi.com/crossguard/) 
* **Auditability**: [audit logging](https://www.pulumi.com/docs/pulumi-cloud/audit-logs/)
* **Developer Experience**: [Python/Go/JavaScript/C#](https://www.pulumi.com/docs/languages-sdks/), [popular IDE support](https://www.pulumi.com/blog/next-level-iac-breakpoint-debugging/), [command-line tools](https://www.pulumi.com/docs/cli/), [deeply hackable](https://www.pulumi.com/automation/)

That’s all great, and much of that is already built-into Pulumi without the need for you to do anything at all. So, what parts do you actually need to set up and configure? Here’s the bill of materials (BOM) to set up your own instance of Pulumi P3:

### Bill of Materials:
* **Authentication and Identity Management**:
    * A GitHub organization that matches your Pulumi Cloud organization
    * GitHub Teams users and roles that match your organizational structure and security needs

* **Secrets, Configuration, and Policy**:
    * Pulumi ESC environments to manage secrets across clouds
    * Pulumi Crossguard policy packs that capture your company policies

* **Developer Experience**:
    * A set of reusable multi-language components for cross-cutting concerns/common services
    * A set of organization templates that match your common use cases

Let’s go through each of those and briefly discuss what it looks like to set that up. 

## Authentication and identity management

We highly recommend using GitHub for code management. So much so that we have deeply integrated GitHub into Pulumi Cloud across a number of features. While we support [alternatives such as GitLab](https://www.pulumi.com/docs/pulumi-cloud/organizations/#gitlab-identity-provider), this will be the easiest and more feature-rich way to configure your platform.

In Pulumi Cloud, you have the ability to create organizations. A [Pulumi Cloud organization](https://www.pulumi.com/docs/pulumi-cloud/organizations/) can help you manage teams, roles, stacks, settings, and provide a dashboard across the entire organization. Pulumi Cloud also allows you to use a variety of identity providers to login, including GitHub.

For simplicity’s sake, we suggest that you start with your GitHub organization. [Create the GitHub organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch), [set up teams](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams), and [add members](https://docs.github.com/en/organizations/organizing-members-into-teams/adding-organization-members-to-a-team) to those teams, assigning either admin or user [roles](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles) to each member. 

Next, in Pulumi Cloud, create an organization ***with exactly the same name*** as your GitHub organization, and choose GitHub as your identity provider. When a Pulumi organization is backed by a GitHub organization, then only members of that GitHub organization may be added to the Pulumi organization. Similarly, as soon as someone loses access to the GitHub organization, they will no longer have access to the Pulumi organization. You will also be able to [import your GitHub teams](https://www.pulumi.com/docs/pulumi-cloud/access-management/teams/#github-based-teams) directly into Pulumi Cloud. Then assign your users to the same roles in Pulumi Cloud teams as they have in the associated GitHub teams.

{{< figure src="teams-gh-pulumi.png" caption="Figure: Mapping GitHub orgs, teams, and roles to Pulumi">}}

Finally, you can [map teams to stacks](https://www.pulumi.com/docs/pulumi-cloud/access-management/teams/#granting-access-to-stacks-within-teams) to grant access at specific permission levels. If you’re not familiar with [Pulumi Stacks](https://www.pulumi.com/docs/concepts/stack/), a stack is a materialized instance of a specific set of cloud resources, as defined in a Pulumi program.

## Pulumi ESC: Managing credentials, configuration, and other secrets

In order to deploy a stack you will need secrets such as cloud credentials and other configuration values that are provided to the deployment engine. Pulumi ESC is a secure system for managing secrets. They are organized by *[environments](https://www.pulumi.com/docs/concepts/environments/)*.

An example set of environments might look something like this:

**Example:** AWS login/credentials
```yaml
# aws-creds ESC environment
values:
    creds:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789012:role/pulumi-environments-oidc
          sessionName: pulumi-environments-session
          duration: 1h
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.creds.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.creds.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.creds.sessionToken}
```

**Example:** Default production environment to use `us-east-1` region
```yaml
# aws-production ESC environment
imports:
  - aws-creds
values:
  aws:
    region: us-east-1
  pulumiConfig:
    aws:region: ${aws.region}
```

**Example:** Default staging environment to use `us-west-2` region
```yaml
# aws-staging ESC environment
imports:
  - aws-creds
values:
  aws:
    region: us-west-2
  pulumiConfig:
    aws:region: ${aws.region}
```

Here we define three environments for AWS: 
* `aws-creds`: sets up login via OpenID Connect (OIDC) and provides standard environment variables containing AWS credentials to the Pulumi program
* `aws-production`: imports everything from `aws-creds` then sets the region to `us-east-1`
* `aws-staging`: does the same, but sets the region to `us-west-2`.

Using that in a Pulumi program is as simple as adding the following settings to your stack config:

```yaml
# Pulumi.staging.yaml
environment:
  - aws-staging
```

In this manner, you can configure separate environments for staging and production, with a complex set of configuration values and secrets, using different environments for each one. From the developer’s perspective they would only need to change `aws-staging` to `aws-production` when they go to deploy their stack.

Another strong benefit of this approach is that all secrets will be encrypted both in-flight and at-rest. Pulumi waits until the last moment to decrypt secrets at runtime. By default, uses automatic, per-stack encryption keys provided by Pulumi Cloud, but you could use a [provider of your own choosing](/docs/concepts/secrets/#configuring-secrets-encryption) instead.

## Pulumi Crossguard: Policy-as-Code

Pulumi Crossguard allows you to check and enforce policies on your deployments. Policies are rules, written in code, that run during deployments to check that the resources are conforming to the necessary criteria. You can use off-the-shelf policies like [AWSGuard](https://www.pulumi.com/docs/using-pulumi/crossguard/awsguard) and [Pulumi Compliance-Ready Policies](https://github.com/pulumi/compliance-policies/) or write your own.

Either way you end up with a *policy pack* that you can apply to your entire Pulumi organization via Pulumi Cloud. 

Here’s an example policy that checks for the presence of a tag `user:Stack` on a S3 bucket:

```python
from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ResourceValidationPolicy,
)

def s3_check_required_tags(args, report_violation):
    if args.resource_type == "aws:s3/bucket:Bucket":
        if ("tags" not in args.props or
                "user:Stack" not in args.props["tags"]):
            report_violation("S3 Bucket is missing required user:Stack tag.")

PolicyPack(
    name="bucket-tags",
    enforcement_level=EnforcementLevel.MANDATORY,
    policies=[
        ResourceValidationPolicy(
            name="s3-tags",
            description="Ensure required tags are present on S3 buckets.",
            validate=s3_check_required_tags,
        ),
    ],
)
```

If the tag isn’t on the resource, it blocks the deployment with an error message. The error message would look something like this: 
```
Policies:
    ❌ bucket-tags@v0.0.1
        - [mandatory]  s3-tags  (aws:s3/bucket:Bucket: my-bucket)
          Ensure required tags are present on S3 buckets.
          S3 Bucket is missing required user:Stack tag.
```

This allows you to implement company-specific policies that can be as simple or complex as you need them to be. 

To apply this across your entire organization, you can [publish this policy pack to Pulumi Cloud](https://www.pulumi.com/docs/using-pulumi/crossguard/get-started/#enforcing-a-policy-pack), with the following commands:

```shell
$ pulumi policy publish myorg
$ pulumi policy enable myorg/my-policy-pack latest
```

Some other great features of Crossguard are the ability to [version policies](https://www.pulumi.com/docs/using-pulumi/crossguard/faq/#how-do-i-version-a-policy-pack), define multiple [policy groups](https://www.pulumi.com/docs/using-pulumi/crossguard/core-concepts/#policy-groups), and create [remediation policies](https://www.pulumi.com/blog/remediation-policies/) that automatically fix policy violations when possible. We will cover these topics in a future post where we go deeper on how to use policies effectively.

## Multi-Language Components (MLC)

In Pulumi, a *[component resource](https://www.pulumi.com/docs/concepts/resources/components/)* is something that your developers can import in their Pulumi program, instantiate and modify. These are made available via a *[provider](https://www.pulumi.com/docs/concepts/resources/providers/)*, which is in turn, made available to Pulumi via a *[provider package](https://www.pulumi.com/docs/using-pulumi/pulumi-packages/)*. There are many of these already available in the [Pulumi Registry](https://www.pulumi.com/registry/). However, in a custom internal developer platform you can define your own components, and bake appropriate settings/configuration directly into the underlying code.

A *multi-language component (MLC)* is even more useful. You can author your component in your language of choice and then generate a SDK that surfaces that component into all of the languages that Pulumi supports. For example, your platform team might be comfortable writing in Python, but the developers that write your microservices might use Go, and the developers who write the front-end apps might use Node.js. Both teams might need to deploy apps and infrastructure into your Kubernetes cluster. With multi-language components you can write a component in Python that abstracts away all the details of your custom Kubernetes cluster, and make that available to both teams, in both Go, Node.js, and any other language that Pulumi supports. 

To build a MLC, you’ll follow these basic steps to create the component, provider, provider package, and generate the multi-language SDK:
1. Fork one of the component provider boilerplate repos for [Python](https://github.com/pulumi/pulumi-component-provider-py-boilerplate), [TypeScript](https://github.com/pulumi/pulumi-component-provider-ts-boilerplate), or [Go](https://github.com/pulumi/pulumi-component-provider-go-boilerplate).
2. Update the package and code-generator configuration files, which name your component and package, define the inputs and outputs, and declare the dependencies.
3. Implement the component in your preferred language. 
4. Generate an SDK for the other languages.
5. Deploy the package.

Here’s a quick example of creating a custom S3 Bucket component in Python, that complies with the tagging policy we built earlier:

```python
from pulumi_aws import s3
import pulumi

class TaggedBucket(pulumi.ComponentResource):

    def __init__(self, name, opts = None):
        super().__init__('mycorp:index:TaggedBucket', name, None, opts)

        # Create a bucket and add a custom tag to it.
        bucket = s3.Bucket(
            f'{name}-bucket',
            tags={
                'user:Stack': pulumi.get_stack()
            },
            opts=ResourceOptions(parent=self))

        self.register_outputs({
            'bucket': bucket,
            'websiteUrl': bucket.website_endpoint,
            'bucketDnsName': bucket.bucketDomainName
        })

```

This shows the component implementation in isolation from the provider/packaging/SDK boilerplate. In this code sample, we’re creating a component called `TaggedBucket` that creates a S3 bucket, and adds a tag `user:Stack` with the current stack name as its value. A developer could now use this in a TypeScript Pulumi program as such, and this resource would automatically have the tags added to it.

```javascript
import * as mycorp from "mycorp/mycorp-components";

const taggedBucket = new mycorp.TaggedBucket("example");

export const bucket = taggedBucket.bucket;
export const url = taggedBucket.websiteUrl;
export const dnsName = taggedBucket.bucketDnsName;
```

If you want to see how to create MLCs in more detail, check out [this video](https://www.youtube.com/watch?v=_RXvNS5N8A8) that walks you through the entire process, and [this repo](https://github.com/jaxxstorm/pulumi-productionapp) for the code shown in the video. In a follow-up post in this series, we will build some reference MLCs that do things like implement a time-to-live (TTL) for stacks in your staging environment, automate drift detection, and automatically instrument your developer’s deployments with observability tools integrated by default.

## Organization templates and the New Project Wizard

The final piece that ties all this together are *[organization templates](https://www.pulumi.com/docs/pulumi-cloud/developer-portals/templates/)*. You may have used some of our [built-in templates](https://www.pulumi.com/templates/) when you learned how to use Pulumi. These are great for basic use cases, but the real magic happens when you bring together your custom components and custom security environments to create personalized templates which represent the internal use cases for your organization.

Pulumi’s [New Project Wizard](https://www.pulumi.com/docs/pulumi-cloud/developer-portals/new-project-wizard/) reads these templates and provides an in-browser way to create a new project and deploy it. Running one of these templates will commit and push code to GitHub, and trigger an initial deployment – all in a few clicks and without leaving the browser.

Each template needs the following parts:
* A `Pulumi.yaml` describing the template and its configuration values
* A GitHub repo (public or private) containing the code for the templated Pulumi program

Here’s an example of a simple template using the components and environments we described above.

```yaml
# Pulumi.yaml
name: ${PROJECT}
description: ${DESCRIPTION}
runtime: python
template:
  description: A Python Pulumi program that creates a tagged bucket.
```

```python
"""__main__.py: A minimal Pulumi program"""

import pulumi
import mycorp

# Create an AWS resource (S3 Bucket)
tagged_bucket = mycorp.TaggedBucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name', tagged_bucket.bucket)
```

```yaml
# Pulumi.production.yaml
environment:
  - aws-production
```

```yaml
# Pulumi.staging.yaml
environment:
  - aws-staging
```

The `Pulumi.yaml` sets up the template and will populate the name and description from the settings provided during the template dialogue. The custom `TaggedBucket` component will create an S3 bucket, which will be tagged with `user:Stack` set to the name of the stack. Default stack configurations are provided for the `staging` and `production` environments which map to our two ESC environments, `aws-production` and `aws-staging`.

## How it all works together

With all of that in place, from the developer’s perspective, all they need to do is create a new project from the template, answering three questions: the stack name, the name of the project, and an optional description.

If the developer names the stack `staging` it will automatically apply the `aws-staging` ESC environment, which will include the AWS credentials and set the region to `us-west-2`. However, if the developer names the stack `production` it will get the `aws-production` ESC environment setting it to use the `us-east-1` region. The name of the stack will be stored in a tag on the resource.

Pulumi Crossguard will apply the `bucket-tags` policy check to see if the resource has the required `user:Stack` tag set and will allow the deployment to proceed only if it has that tag. If a developer created a standard S3 Bucket instead of using our internal `TaggedBucket` component, and failed to add the required tag, they will get an error message from our custom policy when they try to deploy.

Later, we can create additional automation that might do something like delete anything tagged `staging` after two weeks, or run drift detection on anything tagged `production`. We will be exploring these concepts in more detail in later posts.

### More to Come

While setting up the Pulumi Patterns and Practices Platform (P3) reference architecture is not a simple click-to-deploy, hopefully this high-level tour of the various parts you need to assemble shows that really, it is only a matter of creating a few carefully constructed YAML files and snippets of code, and wiring them together properly. You can start small and build out your platform over time. 

The next few posts in this series will go beyond these simple examples, showing much more complicated implementations of all of these pieces, and recommend some best practices for managing your infrastructure with this platform. 

And if you are already ready to get your hands on Pulumi after this introduction, feel free to [create an account](https://www.pulumi.com/signup/) and follow some of our [Getting Started](https://www.pulumi.com/docs/get-started/) guides to see how easy simple use cases are and begin to imagine how that same developer experience will scale up to your entire organization.

To learn more, you can watch the following video which provides a high level overview of how Pulumi works:

<div class="rounded-md shadow border border-gray-300 w-3/4 mx-auto my-4" style="position: relative; padding-bottom: 40.25%; height: 0; overflow: hidden;">
    <iframe
        src="//www.youtube.com/embed/Q8tw6YTD3ac?rel=0"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;"
        allowfullscreen=""
        title="Introduction to Pulumi in Three Minutes"
        srcdoc="<style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img{position:absolute;width:100%;top:0;bottom:0;margin:auto}</style><a href=https://www.youtube.com/embed/Q8tw6YTD3ac?autoplay=1><img src='/images/home/youtube-getting-started.png' alt='Introduction to Pulumi in Three Minutes'></a>">
    </iframe>
</div>

## Pulumi Cloud

The Pulumi Cloud is a fully managed service that helps you adopt Pulumi's open source SDK with ease. It provides built-in state and secrets management, integrates with source control and CI/CD, and offers a web console and API that make it easier to visualize and manage infrastructure. It is free for individual use, with features available for teams.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Create an Account</a>
