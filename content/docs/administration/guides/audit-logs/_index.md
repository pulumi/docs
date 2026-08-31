---
title: Audit Logs
title_tag: Pulumi Cloud Audit Log Guides
h1: Audit logs
meta_desc: Download your Pulumi Cloud organization's audit log on demand, or stream it continuously to an external system for long-term retention and analysis.
menu:
  administration:
    name: Audit Logs
    parent: administration-guides
    identifier: administration-guides-audit-logs
    weight: 4
pulumi_cloud_feature: audit-logs
aliases:
  - /docs/administration/guides/export-audit-logs/
---

Pulumi Cloud retains [audit logs](/docs/administration/concepts/audit-logs/) for a limited window. Exporting them to a system you control gives you long-term retention and lets you correlate Pulumi activity with the rest of your security tooling.

There are two ways to get events out.

## Manual export

Pull a range of events on demand from the console, the CLI, or the REST API. Useful for an ad hoc investigation or a one-time archive.

- [Manual export](/docs/administration/guides/audit-logs/manual-export/)

## Automated export

{{< pulumi-cloud "audit-log-export" />}}

Configure a destination once, and Pulumi Cloud delivers new events to it continuously — no manual downloads or API polling. Neither destination backfills history, so events are delivered forward from the time you enable the export.

- [Export to AWS S3](/docs/administration/guides/audit-logs/aws-s3/)
- [Export to Microsoft Sentinel](/docs/administration/guides/audit-logs/azure-sentinel/)

## Learn more

- [Audit log formats](/docs/administration/reference/audit-log-formats/) — the fields each of the JSON, CSV, and CEF export formats carries.
- [Audit logs](/docs/administration/concepts/audit-logs/) — what audit logs record and how to view them in the console.
