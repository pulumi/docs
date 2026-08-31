---
title_tag: "Pulumi Cloud: Audit Logs"
meta_desc: Pulumi's audit logs let you account for user activity within your organization. Learn what they record and how to view them here.
title: "Audit Logs"
h1: Pulumi Cloud audit logs
menu:
  administration:
        name: Audit Logs
        parent: administration-concepts
        weight: 9
        identifier: administration-concepts-audit-logs
aliases:
- /docs/administration/security-compliance/audit-logs/
- /docs/intro/console/collaboration/auditing/
- /docs/intro/console/auditing/
- /docs/intro/pulumi-service/audit-logs/
- /docs/intro/pulumi-cloud/audit-logs/
- /docs/pulumi-cloud/audit-logs/
- /docs/pulumi-cloud/admin/audit-logs/
- /docs/administration/security-compliance/
pulumi_cloud_feature: audit-logs
---

## Overview

Audit logs enable you to track the activity of users within an
organization. They display what a user did, when
they did it and where by recording user actions.

Pulumi's audit logs allow you to account for the activity your
users are taking within your organization. The logs are immutable
and record all user actions. Auditing makes the activity
of members in an organization attributable.
The logs capture the UNIX timestamp of the event, the user
who invoked the action, the event that took place, and the source IP
of the call the user made.

## View audit logs

Only organization admins can view audit logs.

To view audit logs:

1. Navigate to the organization's **Settings**.
1. Navigate to **Audit Logs**.

This will show the most recent events in descending order. You can
also filter logs by a particular user by selecting their profile picture.

<img src="/images/docs/guides/self-hosted/auditlogs.png" alt="Audit logs view in Pulumi Cloud">

<a id="automated-export"></a>

## Export audit logs

Pulumi Cloud can download audit log events on demand from the console, the CLI, or the REST API, and can continuously deliver them to Amazon S3 or Microsoft Sentinel. See the [audit log guides](/docs/administration/guides/audit-logs/) for every procedure, and [Audit log formats](/docs/administration/reference/audit-log-formats/) for the fields each export format carries.

<a id="list-of-audit-log-events"></a>

## Learn more

- [Audit log events](/docs/administration/reference/audit-log-events/) — the complete catalog of the 150+ events Pulumi Cloud records, grouped by product area.
- [`pulumi org audit-log`](/docs/iac/cli/commands/pulumi_org_audit-log/) — list and export audit log entries from the command line.
- [Audit logs REST API](/docs/reference/cloud-rest-api/audit-logs/) — the endpoints behind the console's export, for scripted retrieval.
- [Audit log guides](/docs/administration/guides/audit-logs/) — downloading a log on demand, or delivering it continuously to Amazon S3 or Microsoft Sentinel.
- [Audit log formats](/docs/administration/reference/audit-log-formats/) — the fields carried by the JSON, CSV, and CEF exports.
- [Pulumi ESC audit logs](/docs/esc/administration/audit-logs/) — how environment activity is recorded.
- [RBAC scopes](/docs/administration/reference/rbac-scopes/) — the permissions behind the "requires organization admin" note on individual events.
- [Least privilege](/docs/administration/guides/least-privilege/) — using audit logs to review and tighten the access your organization grants.
