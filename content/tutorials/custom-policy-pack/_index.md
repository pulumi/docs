---
title: "Creating a Custom Policy Pack"
title_tag: "Creating a Custom Policy Pack"
layout: module
description: Learn how to enforce compliance and security requirements by creating a custom policy pack with Pulumi Crossguard.
meta_desc: Learn how to enforce compliance and security requirements by creating a custom policy pack with Pulumi Crossguard using Python and TypeScript.
weight: 10
summary: |
   Pulumi CrossGuard uses policy-as-code to enforce best practices, compliance, and security requirements across your infrastructure. A policy pack is a collection of policies that can be versioned and reused across projects.

   In this tutorial, you will create a custom policy pack that enforces specific policies for your AWS resources, such as enabling S3 bucket versioning, restricting EC2 instance types, and requiring resource tags.
      
youll_learn:
    - How to define policies using Python and TypeScript
    - How to group policies into a policy pack
    - How to deploy and enforce the policy pack in your Pulumi organization
    - How to define policies involving multiple resources

prereqs:
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - The [Pulumi CLI](/docs/install/)
    - Install [Node.js](https://nodejs.org/en/download/) or [Python](https://www.python.org/downloads/)
    - Configure your [AWS Credentials](https://www.pulumi.com/docs/iac/get-started/aws/begin/#configure-pulumi-to-access-your-aws-account)
    - Familiarity with infrastructure-as-code and Pulumi
---

{{% notes type="info" %}}
This tutorial focuses on [AWS](/docs/iac/get-started/aws/) resources, however the same techniques can be used for any resource managed by Pulumi, including [Azure](/docs/iac/get-started/azure/), [Google Cloud Platform](/docs/iac/get-started/gcp/), [Kubernetes](/docs/iac/get-started/kubernetes/), etc.
{{% /notes %}}
