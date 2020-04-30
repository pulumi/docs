---
title: AWS CDK and Troposphere
meta_desc: This page gives and overview of the major differences between Pulumi and
            AWS CDK & Troposphere.
linktitle: AWS CDK and Troposphere
menu:
  intro:
    parent: vs
    weight: 3
---

Because of [the challenges of writing raw YAML/JSON by hand]({{< prelref "cloud_templates" >}}), two notable
projects exist to compile higher-level languages into AWS CloudFormation YAML/JSON templates:

* **Troposphere**: a community-led open source project created in 2013
* **AWS Cloud Development Kit (CDK)**: an AWS Labs project created in 2018

Similar to Pulumi, these projects let you author infrastructure as code using general-purpose languages like TypeScript,
JavaScript, and Python. Unlike Pulumi, however, whose open source engine understands these languages, a _transpiler_
a.k.a., [_source-to-source compiler_](https://en.wikipedia.org/wiki/Source-to-source_compiler), translates this program
into [AWS CloudFormation YAML/JSON]({{< prelref "cloud_templates" >}}). The resulting markup file is then submitted
to the closed source AWS CloudFormation servers to provision infrastructure on AWS in the usual ways.

## Pulumi Supports Many Clouds

AWS CDK and Troposphere support AWS only. Pulumi supports the entire capabilities of Azure, Google Cloud Platform,
and cloud native technologies such as Kubernetes, _in addition_ to AWS. There are several other points outlined below,
but these are the top-level key differences.

## Summary of Major Differences

The transpiler approach gives you some of the benefits of Pulumi, with the following caveats:

* Troposphere and CDK only support the AWS platform. Pulumi supports many clouds, including _major cloud platforms_
  (such as Microsoft Azure, Google Cloud Platform, Kubernetes, and DigitalOcean), _on-premises and hybrid technologies_
  (such as VMWare vSphere and OpenStack), and _online SaaS offerings_ (like Cloudflare, Datadog, New Relic, and more).
  Furthermore, Pulumi is extensible, supports custom providers, and can bridge with any existing Terraform-based provider.

* Pulumi supports Cloud Native technologies, including Kubernetes, Helm Charts, Istio service
  meshes, and hosted Kubernetes clusters in any cloud (AWS EKS, Azure AKS, Google GKE, etc).

* Troposphere and CDK compile down to YAML and are therefore limited in what they can express. The Pulumi engine understands
  general-purpose language patterns, dependencies between objects, and therefore delivers a better overall experience.
  Pulumi also supports going beyond what you can express in YAML, such as building and publishing a Docker container image,
  authoring serverless functions in code, automating packaging and versioning of code, and so on.

* Pulumi's engine is [open source](https://github.com/pulumi/pulumi), whereas Troposphere and CDK depend on the closed
  source CloudFormation engine. This means more of Pulumi is accessible to community contributions.

* The Pulumi CLI and Console are co-designed to [make team collaboration simple]({{< prelref "/docs/intro/console" >}}),
  especially with organization-wide sharing of projects and stacks. This is closer to "GitHub for DevOps" and delivers
  a rich experience including diffs and previews of updates before they are made. Troposphere and CDK rely on
  CloudFormation which is known to be more challenging in these areas.

* Pulumi has a built-in configuration system that is super easy to use. Related, encrypted secrets
  give you an easy way to integrate secrets management best practices for database passwords, tokens, and other secrets. In
  contrast, AWS offers building block services like AWS KMS, AWS Secrets Manager, and AWS Systems Manager Parameter
  Store. However, using them in combination with one another in just the right way can be challenging. Pulumi leverages
  underlying building block services in your target cloud, or even HashiCorp Vault, to deliver an easy experience
  with secrets management automatic best practices built-in.

* Pulumi integrates with [a number of CI/CD providers]({{< prelref "/docs/guides/continuous-delivery" >}}) and
  source control systems (SCMs) out of the box, for easy continuous delivery with systems you might already be using.
  Although CloudFormation can be used in this manner, it requires manual configuration, and is designed to work
  best with AWS's own CodeBuild/Pipeline products.

* Pulumi integrates with your identity provider---including GitHub, GitLab, Atlassian, or
  [any SAML/SSO 2.0 provider]({{< prelref "/docs/guides/saml" >}}) (such as Azure Active Directory, Google G Suite,
  or Okta)---for auditing and access controls using your existing enterprise systems of record. AWS CloudFormation can
  be manually integrated with those systems with greater effort.

* Pulumi can use [custom state management]({{< prelref "/docs/intro/concepts/state#self-managed-backend" >}})
  and offers a self-hosting option for greater control, including "behind the firewall" on-premises and hybrid
  options. Troposphere and CDK exclusively rely on the server-side AWS CloudFormation runtime. Pulumi offers a free
  hosted backend as its default offering but gives you more flexibility and control.

Although Pulumi and the Troposphere and AWS CDK projects share a vision for the future of infrastructure as code using
general-purpose languages, Pulumi's many-cloud nature, embrace of modern Cloud Native technologies, and its open source
engine and modern SaaS that deeply understand language semantics and advanced orchestration significantly differentiate
the offerings.
