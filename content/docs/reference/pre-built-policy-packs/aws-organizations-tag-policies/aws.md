---
title: "AWS"
meta_desc: AWS Organizations Tag Policies pack enforces tag policies configured in AWS Organizations.
h1: "AWS Organizations Tag Policies"
menu:
  reference:
    name: AWS Organizations Tag Policies
    parent: reference-pre-built-policy-packs
    identifier: reference-pre-built-policy-packs-aws-organizations-tag-policies
    weight: 6
---

The **AWS Organizations Tag Policies** pack validates that your infrastructure as code resources comply with tag policies configured in AWS Organizations. Built in partnership with AWS, this pack proactively blocks non-compliant deployments when resources are missing required tags. For complete documentation including prerequisites, setup instructions, and supported resources, see the [AWS Organizations Tag Policies integration guide](/docs/insights/policy/integrations/aws-organizations-tag-policies/).

## Policy

This pack includes a single resource policy:

| Policy Name | Description | Default Enforcement Level | Severity |
| ----- | ----- | ----- | ----- |
| aws-tag-policies-compliance-validation | Validates that resources have required tags as defined in AWS Organizations Tag Policies | advisory | low |
