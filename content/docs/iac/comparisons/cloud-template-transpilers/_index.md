---
title_tag: "Pulumi vs. Cloud Template Transpilers"
meta_desc: Learn about the major differences between Pulumi and cloud template transpiler solutions like AWS CDK and Troposphere.
title: Cloud Template Transpilers
h1: Cloud Template Transpilers
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Cloud Template Transpilers
        parent: iac-comparisons
        identifier: iac-comparisons-transpilers
        weight: 4
    concepts:
        parent: vs
        weight: 2
aliases:
- /docs/intro/vs/cloud_template_transpilers/
- /docs/concepts/vs/cloud-template-transpilers/
- /docs/iac/concepts/vs/cloud-template-transpilers/
---

Because of [the challenges of writing raw YAML/JSON by hand](/docs/concepts/vs/cloud-templates), several notable projects exist to compile higher-level languages into intermediate formats for deployment. Two such projects are AWS Cloud Development Kit (CDK), an AWS Labs project created in 2018, and CDK for Terraform (CDKTF), a HashiCorp project created in 2020 and [deprecated](/blog/cdktf-is-deprecated-whats-next-for-your-team/) in 2025.

Like Pulumi, these projects allow you to author infrastructure as code using general-purpose languages like TypeScript, Python, Go, and others. Unlike Pulumi, however, whose open-source engine understands these languages, a _transpiler_
(a.k.a., [_source-to-source compiler_](https://en.wikipedia.org/wiki/Source-to-source_compiler)), translates this code
into an intermediate format — e.g., [AWS CloudFormation YAML](/docs/concepts/vs/cloud-templates/cloudformation/) for CDK, or Terraform JSON for CDKTF. The resulting files and related assets are then submitted to their respective deployment engines to provision infrastructure.

To learn more about how Pulumi compares to some of these services in detail, see the following comparison docs:

* [Pulumi vs. AWS Cloud Development Kit (CDK)](/docs/iac/comparisons/cloud-template-transpilers/aws-cdk/)
* [Pulumi vs. CDK for Terraform (CDKTF)](/docs/iac/comparisons/cloud-template-transpilers/cdktf/)
