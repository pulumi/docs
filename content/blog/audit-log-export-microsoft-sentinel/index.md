---
title: "Export Pulumi Cloud Audit Logs to Microsoft Sentinel"
date: 2026-04-08
meta_desc: "Pulumi Cloud now supports exporting audit logs to Microsoft Sentinel, giving security teams real-time visibility into infrastructure activity in their SIEM."
meta_image: meta.png
feature_image: feature.png
authors:
  - lynn-jung
tags:
  - pulumi-cloud
  - security
  - audit-logs
  - microsoft-sentinel
---

[Pulumi Cloud](/product/pulumi-cloud/) audit logs give organization admins a complete record of who did what, when, and from where across their infrastructure. Until now, automated export was limited to AWS S3. Today, we're adding support for exporting audit logs to [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/overview), bringing Pulumi activity data directly into your SIEM for real-time monitoring and alerting.

<!--more-->

The connector uses Sentinel's managed [Codeless Connector Framework](https://learn.microsoft.com/en-us/azure/sentinel/create-codeless-connector) — no Azure Functions, Logic Apps, or other compute to manage. Events flow every 5 minutes, and the template includes three pre-built analytic rules for excessive auth failures, stack deletions, and org membership changes.

## Getting started

The connector deploys as a Pulumi program using a template. There are two ways to set it up:

**From the Pulumi Cloud console**: Navigate to the **Stacks** page, select **Create project**, and choose the **Pulumi Audit Log Export to Azure Sentinel** template. Fill in your config values, select Pulumi Deployments as the deployment method, and select **Deploy**.

**From the CLI**:

```bash
mkdir sentinel-connector && cd sentinel-connector
pulumi new https://github.com/pulumi/sentinel-audit-log-connector
pulumi up
```

Both paths require a Pulumi access token (we recommend an org-scoped service token) and an Azure resource group with a Log Analytics workspace and Sentinel enabled. Full setup instructions are in the [Microsoft Sentinel export guide](/docs/administration/security-compliance/audit-logs/azure-sentinel/).

## What gets ingested

Every audit log event lands in a custom `PulumiAuditLogs_CL` table with typed columns for event metadata, user info, token details, and security flags. You can query it immediately with KQL:

```kql
PulumiAuditLogs_CL
| where Event_s == "stack-deleted"
| project TimeGenerated, UserName_s, Description_s, SourceIP_s
```

## Try it out

Microsoft Sentinel export is available today for organizations on the [Business Critical](/pricing/) edition.

- [Read the setup guide](/docs/administration/security-compliance/audit-logs/azure-sentinel/) to get started
- [View the connector source](https://github.com/pulumi/sentinel-audit-log-connector) on GitHub
- [Join the Community Slack](https://slack.pulumi.com/) to share feedback
