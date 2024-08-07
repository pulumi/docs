---
title_tag: Migrating & Importing Resources | Pulumi Tutorials
title: Migration and Imports
layout: module
description: Explore how to import resources and migrate from other platforms to Pulumi.
meta_desc: In this tutorial, we will explore how you can bring resources created by other tools like CDK or Terraform into Pulumi.
index: 4
meta_image: meta.png
youll_learn:
    - How to import individual cloud resources with the Pulumi CLI
    - How to import multiple resources using structured data files
    - How to import cloud resources in code, within a Pulumi program
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts#access-tokens)
    - Familiarity with JavaScript, TypeScript, or Python
    - Familiarity with Hashicorp Terraform (optional)
    - Completion of the [Pulumi Fundamentals](/tutorials/pulumi-fundamentals/) and [Building with Pulumi](/tutorials/pulumi-fundamentals/) tutorials, or practical experience with Pulumi.
aliases:
    - /learn/importing/
---

In this tutorial, you'll learn how to bring existing cloud resources created outside of Pulumi (whether created by hand or with other tools such as AWS CDK or Hashicorp Terraform) into Pulumi to manage them going forward.
