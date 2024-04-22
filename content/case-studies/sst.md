---
title_tag: SST | Case Studies
title: "SST: Moving Away from CDK"
description: |
    SST builds a new version of SST (Ion) on Pulumi instead of CDK because of its limitations around speed, error handling, leaky abstractions, non-AWS provider support, and more.  
meta_desc: Read why SST switched to Pulumi and stopped using CDK because of its limitations around speed, error handling, leaky abstractions, non-AWS provider support, and more.

customer_name: SST
customer_logo: /logos/customers/sst-logo.svg
customer_url: https://sst.dev/blog/moving-away-from-cdk.html
redirect_to: https://sst.dev/blog/moving-away-from-cdk.html

---

## Read the Blog

   SST is working on a new version of SST called Ion. The current iteration of SST is based off of AWS CDK and CloudFormation. There are significant limitations to SST because of its dependencies on CDK and CloudFormation. CloudFormation is a proprietary cloud-based service that is opaque and CDK is only transpiling down to CloudFormation and doesn't create any infrastructure. This creates issues around speed, error handling, leaky abstractions, and state management. For Ion, SST uses Pulumi's engine underneath, which provides greater transparency and control over how the code executes and the infrastructure that is provisioned. Read Jay V's (Founder & CEO of SST) blog post on "[Moving away from CDK](https://sst.dev/blog/moving-away-from-cdk.html)".
   