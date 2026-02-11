---
title_tag: "Policy Findings | Pulumi Policies"
meta_desc: Learn about Policy Findings in Pulumi Policies and how to manage compliance in your cloud infrastructure.
title: Policy Findings
h1: Policy Findings
weight: 2
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    insights:
        name: Policy Findings
        parent: insights-policy
        weight: 40
aliases:
  - /docs/insights/policy/policy-as-code/policy-violations/
  - /docs/iac/crossguard/policy-violations/
  - /docs/using-pulumi/crossguard/policy-violations/
  - /docs/iac/packages-and-automation/crossguard/policy-violations/
  - /docs/iac/using-pulumi/crossguard/policy-violations/
  - /docs/insights/policy/policy-violations/
  - /docs/insights/policy/policy-packs/policy-violations/
---

## Overview

Policy Findings provides a centralized view for managing compliance across your cloud infrastructure. It extends policy enforcement beyond violation detection to include issue management and remediation workflows. The Policy Findings page is organized into three tabs:

1. **Overview tab:** Displays high-level compliance metrics and trends
1. **Compliance tab:** Shows policy-centric view for auditing and compliance reporting
1. **Issues tab:** Provides tools for triaging, assigning, and resolving policy issues

## Accessing Policy Findings

To access Policy Findings in Pulumi Cloud:

1. Navigate to your organization in Pulumi Cloud.
1. Select **Policy Findings** from the sidebar under the Policies section.

## Overview tab

The Overview tab provides an overview of your organization's security and compliance posture.

![Policy Findings Overview](/docs/insights/assets/policy-findings.png)

### Key metrics

The Overview tab displays two compliance scores:

**Policy compliance score:** The percentage of your enabled policy rules that are currently passing across your organization. When a policy pack is assigned to multiple policy groups, each policy in the pack is counted separately for each group assignment.

**Resource compliance score:** The percentage of your governed resources that are fully compliant with all applicable policies. Governed resources include both stack resources and account resources.

### Policy compliance overview

The policy compliance overview section displays a heatmap that shows compliance across your stacks or accounts and their assigned policy packs. This view allows you to identify which stacks or accounts have compliance issues with specific policy packs.

The heatmap displays:

- **Rows:** Your Pulumi stacks or cloud accounts (configurable via the "Group by" dropdown)
- **Columns:** The policy packs enabled in your organization
- **Percentages:** The number of passing policies divided by the total number of policies in each policy pack for that stack or account
- **N/A:** Indicates the policy pack is not assigned to that stack or account, or has never run

You can filter the columns to show specific policy packs and group the data by stacks or accounts to analyze compliance from different perspectives.

## Compliance tab

The Compliance tab provides a policy-centric view of your findings, grouping results by individual policies. This view allows you to review compliance on a per-policy basis and is useful during audits when reviewing controls from frameworks like CIS, NIST, or PCI DSS.

![Policy Findings Compliance](/docs/insights/assets/policy-compliance.png)

The table displays the total number of failing resources per policy, organized by policy group. You can filter and sort by severity, policy group, or policy pack to analyze compliance across your organization.

## Issues tab

The Issues tab allows you to manage policy findings as work items. You can triage, assign, prioritize, and track the remediation of policy issues.

![Policy Findings Issues](/docs/insights/assets/policy-issues.png)

The Issues tab displays all policy issues across your organization in a table showing the policy name, severity, priority, assigned team member, status, and resource type. You can filter issues by any of these attributes, sort by any column, and toggle between **All Issues** and **Active Issues** views. The drag-and-drop grouping interface allows you to group issues by various criteria.

### Managing issues

You can manage individual issues by selecting them from the table, or perform batch operations by selecting multiple issues using the checkboxes. Batch operations allow you to update priority, assignment, or status for multiple issues at once.

For organizations with access to Pulumi Neo, you can select multiple issues and use the **Remediate** button to trigger AI-powered remediation. This groups the selected issues by stack or account and creates one Neo task for each group.

For each issue, you can set:

- **Status:** Open, In Progress, Fixed, or Ignored
- **Priority:** P0 (critical) through P4 (low)
- **Assignment:** Assign to specific team members in your organization

These fields can be edited directly from the Issues tab or from the individual issue detail view.

### Issue details

Selecting an issue from the table opens the issue detail view, which provides comprehensive context about the finding. The detail view displays:

- **Policy information:** Policy pack name and version, policy group, policy group type (Audit or Preventative), and severity
- **Resource information:** Entity type (Stack or Insights-Account), entity project, entity name, issue resource ID, and cloud provider
- **Timestamps:** First seen and last updated dates
- **Issue description:** The violation message explaining what policy rule was violated
- **Policy description:** Additional context about the policy requirements

From this view, you can also assign the issue, update its status and priority, or trigger AI-powered remediation using the **Create Neo Task** button.

![Policy Issue Details](/docs/insights/assets/policy-issue-detail.png)

### Viewing the stack page

1. Navigate to the stack with a policy violation.
2. It will show on the bottom of the Overview page.

Clicking on a resource in a violated state will also show the policy finding on the Resource page. Viewing a stack update where a policy violation occurred will detail the policy finding.

## Accessing Policy Findings via API

Policy findings can be accessed programmatically through the Pulumi Cloud REST API, enabling custom workflows, integrations, and reporting.

For complete API documentation, see [Policy Results API](/docs/reference/cloud-rest-api/policy-results/).
