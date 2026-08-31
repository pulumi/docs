---
title: Audit log formats
title_tag: Pulumi Cloud Audit Log Format Reference
h1: Audit log formats
meta_desc: The fields carried by each Pulumi Cloud audit log export format — JSON, CSV, and CEF — for parsing an exported log or wiring one into a SIEM.
menu:
  administration:
    name: Audit log formats
    parent: administration-reference
    identifier: administration-reference-audit-log-formats
    weight: 3
pulumi_cloud_feature: audit-logs
---

The fields carried by each format Pulumi Cloud writes an [audit log](/docs/administration/concepts/audit-logs/) export in. Consult these when you parse an exported log or map it into a SIEM. For how to produce an export, see the [audit log guides](/docs/administration/guides/audit-logs/).

## JSON format

JSON is the format the audit log REST API returns by default. Each response carries a page of events and a continuation token for the next page:

```json
{
  "auditLogEvents": [
    {
      "timestamp": 1756400000,
      "sourceIP": "203.0.113.42",
      "event": "stack-update-started",
      "description": "A stack update started.",
      "user": {
        "name": "Alex Rivera",
        "githubLogin": "arivera",
        "avatarUrl": "https://avatars.githubusercontent.com/u/1234567"
      },
      "tokenName": "ci-deploy"
    },
    {
      "timestamp": 1756399820,
      "sourceIP": "198.51.100.7",
      "event": "member-added",
      "description": "A member was added to an organization.",
      "user": {
        "name": "Dana Okonkwo",
        "githubLogin": "dokonkwo",
        "avatarUrl": "https://avatars.githubusercontent.com/u/7654321"
      },
      "reqOrgAdmin": true
    }
  ],
  "continuationToken": "eyJ0aW1lc3RhbXAiOjE3NTYzOTk5MDB9"
}
```

Each event carries the following fields. Only `timestamp`, `sourceIP`, `event`, `description`, and `user` are always present; the rest appear when they apply to the event.

| Field | Description |
|-----------------------|---------------------------|
| timestamp | Unix epoch timestamp (seconds) when the event occurred |
| sourceIP | IP address of the client that triggered the event |
| event | the audit event type identifier (for example, `stack-update-started`, `member-added`) |
| description | human-readable description of the event |
| user | the user who performed the action (display name, login, and avatar URL) |
| tokenID | ID of the access token used to authenticate, if applicable |
| tokenName | name of the access token used to authenticate, if applicable |
| reqOrgAdmin | whether the action required the organization ADMIN role |
| reqStackAdmin | whether the action required stack admin privileges |
| authFailure | whether this event represents a failed authentication attempt |
| actorName | display name of the non-human actor (for example, a deploy token name) that triggered the event |
| actorUrn | Pulumi URN of the non-human actor that triggered the event |

## CSV format

The CSV (comma separated values) format is composed of the following fields:

```plain
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

## CEF format

CEF (common event format) is an audit and logging event format supported by a wide range of SIEM (security information and event management) systems.

The format is as follows:

```plain
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
