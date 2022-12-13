---
title: Pulumi vs. Cloud Template Transpilers
meta_desc: Learn about the major differences between Pulumi and cloud template transpiler solutions like AWS CDK and Troposphere.
linktitle: Cloud Template Transpilers
aliases:
  - /docs/intro/vs/cloud_template_transpilers/
---

Because of [the challenges of writing raw YAML/JSON by hand](/docs/intro/vs/cloud-templates), two notable
projects exist to compile higher-level languages into AWS CloudFormation YAML/JSON templates: Troposphere, a community-led open source project created in 2013; and AWS Cloud Development Kit (CDK), an AWS Labs project created in 2018.

Similar to Pulumi, these projects allow you to author infrastructure as code using general-purpose languages like TypeScript,
JavaScript, and Python. Unlike Pulumi, however, whose open-source engine understands these languages, a _transpiler_
(a.k.a., [_source-to-source compiler_](https://en.wikipedia.org/wiki/Source-to-source_compiler)), translates this code
into [AWS CloudFormation](/docs/intro/vs/cloud-templates/cloudformation/). The resulting file and related assets are then submitted to the closed-source AWS CloudFormation servers to provision infrastructure on AWS in the usual ways.

To learn more about how Pulumi compares to some of these services in detail, see the following comparison docs:

* [Pulumi vs. AWS Cloud Development Kit (CDK)](/docs/intro/vs/cloud-template-transpilers/aws-cdk)
