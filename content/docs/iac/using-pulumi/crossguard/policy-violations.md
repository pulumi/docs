---
title_tag: "Policy Violations | Pulumi CrossGuard"
meta_desc: Learn about Policy Violations in Pulumi CrossGuard and how to manage compliance
  in your cloud infrastructure.
title: Policy Violations
h1: Policy Violations
weight: 2
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    name: Policy violations
    parent: iac-using-pulumi-policy
    weight: 3
aliases:
  - /docs/using-pulumi/crossguard/policy-violations/
  - /docs/iac/packages-and-automation/crossguard/policy-violations/
search:
  keywords:
    - violations
    - crossguard
    - policy
    - compliance
    - infrastructure
    - learn
    - cloud
---

## Overview

Policy Violations occur when a resource in a stack or account does not comply with the policies defined in your Policy Packs. These violations are logged during deployments and can either block the update (mandatory) or issue a warning (advisory), depending on the enforcement level you have set.

## How to See Policy Violations

Policy Violations can be viewed in the Pulumi Cloud via the Policy Violations page. This page provides a centralized view of all violations across your organization, allowing you to filter and group them by various criteria such as Policy Pack, Project, Stack/Account, and Enforcement Level.

### Accessing the Policy Violations Page

1. Navigate to your organization in Pulumi Cloud.
2. Click on "Policy Violations" in the sidebar.
3. Here you will find all the policy violations in a central place.

![Policy Violations page](/images/docs/guides/crossguard/policy-violations.png)

### Viewing the Stack Page

1. Navigate to the stack with a policy violation.
2. It will show on the bottom of the Overview page.

Clicking on a resource in a violated state will also show the policy violation on the Resource page. Viewing a stack update where a policy violation occurred will detail the policy violation.

### Via API

Policy Violations can also be accessed programmatically via the Pulumi API for custom workflows and integrations.

For more details on using the API, refer to the [Pulumi API documentation](/docs/pulumi-cloud/cloud-rest-api/#list-policy-violations).
