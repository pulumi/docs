---
title_tag: "Pulumi Cloud: Audit Logs"
meta_desc: Pulumi's audit logs allow you to account for user activity within your organization. Learn how to view, interpret, and export audit logs here.
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

## Automated export

{{< pulumi-cloud "audit-log-export" />}}

Pulumi Cloud supports continuously exporting audit log events to external destinations.

### Export to AWS S3

Export audit logs to an Amazon S3 bucket. See the [AWS S3 export guide](/docs/administration/guides/export-audit-logs/aws-s3/) for setup instructions.

### Export to Microsoft Sentinel

Export audit logs to Microsoft Sentinel for SIEM analysis. See the [Microsoft Sentinel export guide](/docs/administration/guides/export-audit-logs/azure-sentinel/) for setup instructions.

## Manual export

### Export audit logs using the console

To export audit logs using the console:

1. Navigate to the organization's **Settings**.
1. Navigate to **Audit Logs**.
1. Select **Download**.

### Exporting audit logs using the API

{{% notes type="info" %}}
See [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/audit-logs/) for full details of the API endpoint to export audit log events. This API is rate-limited and only intended for occasional use, see automated export section above if you need frequent export.
{{% /notes %}}

### Supported audit log formats

The Pulumi Cloud REST API supports multiple formats for exporting audit log events.

#### JSON format

The JSON format is composed of the following fields:

| Field | Description |
|---------------------------|---------------------------|
| timestamp | the Unix timestamp of when the event was recorded |
| sourceIP | IP Address of the client originating the request to invoke this event |
| event | the name of the event |
| description | detailed description of the event that occurred |
| user | details of the user invoking the event (login, name, and avatar URL) |

#### CSV format

The CSV (comma separated values) format is composed of the following fields:

```
Timestamp, Name, Login, Event, Description, SourceIP, RequireOrgAdmin, RequireStackAdmin, AuthenticationFailure
```

| Field                     | Description                                                                                                             |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Timestamp             | the Unix timestamp of when the event was recorded                                                                   |
| Name                  | name of the user invoking the event                                                                                     |
| Login                 | username of the user invoking the event                                                                                 |
| Event                 | the name of the event                                                                                                   |
| Description           | detailed description of the event that occurred                                                                         |
| SourceIP              | IP Address of the client originating the request to invoke this event                                                   |
| RequireOrgAdmin       | indicates whether the event required organizational admin level permissions, the value will either be "true" or "false" |
| RequireStackAdmin     | indicates whether the event required stack admin level permissions, the value will either be "true" or "false"          |
| AuthenticationFailure | indicates whether the event occurred  due to an authentication failure, the value will either be "true" or "false"      |

#### CEF format

CEF (common event format) is an audit and logging event format supported by a wide range of SIEM (security information and event management) systems.

The format is as follows:

```
MMM dd hh:mm:ss host CEF:Version|Device Vendor|Device Product|Device Version|Device Event Class ID|Name|Severity|[Extension]
```

The following fields are part of the standard header defined by CEF:

**Device Vendor**, **Device Product**, **Device Version**: these are strings that uniquely identify the sending device

**Device Event Class ID**: string or integer identifying the type of event reported

**Name**: a human readable description of the event

**Severity**: severity level reflecting the importance of the event

**Extensions**: the extensions field is collection of key-value pairs. These keys come from a pre-defined set as well as some keys that we have
defined on our own. The following is a list of the keys we are setting on the extension field.

Pre-defined keys by the CEF standard:

| Key     | Description                                                                                                          |
|---------|------------------------------------------------------------------------------|
| dvchost | identifies the device host name.                                             |
| rt      | identifies the time at which the event related to the activity was received. |
| src     | identifies the source that an event refers to in an IP network.              |
| suser   | identifies the source user by user name.                                     |

Custom defined keys:

| Key                   | Description                                                                                                             |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------|
| orgID                 | the ID of the organization this event belongs to.                                                                       |
| userID                | the ID of the user who invoked this event.                                                                              |
| requireOrgAdmin       | indicates whether the event required organizational admin level permissions, the value will either be "true" or "false" |
| requireStackAdmin     | indicates whether the event required stack admin level permissions, the value will either be "true" or "false"          |
| authenticationFailure | indicates whether the event occurred  due to an authentication failure, the value will either be "true" or "false"      |

<a id="list-of-audit-log-events"></a>

## Learn more

- [Audit log events](/docs/administration/reference/audit-log-events/) — the complete catalog of the 150+ events Pulumi Cloud records, grouped by product area.
- [`pulumi org audit-log`](/docs/iac/cli/commands/pulumi_org_audit-log/) — list and export audit log entries from the command line.
- [Audit logs REST API](/docs/reference/cloud-rest-api/audit-logs/) — the endpoints behind the console's export, for scripted retrieval.
- [Export audit logs](/docs/administration/guides/export-audit-logs/) — continuous delivery to Amazon S3 or Microsoft Sentinel.
- [Pulumi ESC audit logs](/docs/esc/administration/audit-logs/) — how environment activity is recorded.
- [RBAC scopes](/docs/administration/reference/rbac-scopes/) — the permissions behind the "requires organization admin" note on individual events.
- [Least privilege](/docs/administration/guides/least-privilege/) — using audit logs to review and tighten the access your organization grants.
