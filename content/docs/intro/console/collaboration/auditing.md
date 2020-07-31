---
title: Audit Logs
meta_desc: "This is a guide on how to audit your organization's infrastructure as code activity"
---

<div class="note note-info" role="alert">
    <p>
        Audit Logs are only available with the <strong>Pulumi Enterprise Edition</strong>.
    </p>
</div>

## Overview

Audit logs enable you to track the activity of users within an
organization. They attempt to answer what a user did, when
they did it and where. They help answer these questions
by recording user actions.

Pulumi's audit logs allow you to account for the activity your
users are taking within your organization. These logs are available to
organizations with an Enterprise level subscription. The logs are immutable and
and record all user actions. Auditing makes the activity
of members in an organization attributable.
The logs capture the UNIX timestamp of the event, the user
who invoked the action, the event that took place, and the source IP
of the call the user made.

## Viewing Audit Logs in the Console

Audit logs are available to organizations with an Enterprise level subscription
only. If you are an organization administrator, you can view your organization's audit logs,
by selecting your organization from the organization drop down. Then click on the settings tab.
On the left nav-bar you should see a tab called Audit Logs. Clicking here will allow you to view
the most recent audit logs for your organization.

<img src="/images/docs/guides/self-hosted/auditlogs.png">

This will show the most recent events in decending order. You can
also filter logs by a particular user by clicking on the user's avatar. Doing so will
filter out the events performed by the user you selected.

Audit logs can also be exported to a downloadable csv format. The logs can be exported through the UI Console
by clicking on the `DOWNLOAD` button in the upper left hand corner of the audit logs view.

## Exporting Audit Logs through the API

The audit logs can be exported through the API using the following endpoint. A `startTime`
query parameter must be passed and is used to query audit records _before_ the specified
`startTime` (UNIX timestamp).

```
GET https://api.pulumi.com/api/orgs/${org}/auditlogs/export?startTime=${time}
```

Optionally, a user to filter by can also be specified as a query parameter to filter audit logs
pertaining only to a specifc user.

```
GET https://api.pulumi.com/api/orgs/${org}/auditlogs/export?startTime=${time}&userFilter=${user}
```

Example using curl:

```
curl \
    -H 'Accept: application/vnd.pulumi+4' \
    -H 'Authorization: token abcdefghijklmnopqrstuvwxyz' \
    -H 'Content-Type: application/csv' \
    --compressed \
    'https://api.pulumi.com/api/orgs/${org}/auditlogs/export?startTime=${startTime}'
```

> _Note: Substitute `${org}`, `${user}`,  and `${time}` for your actual values - e.g. `org`, `username`, and `1583460637`._

## Supported Audit Log Formats

We currently support two formats for exporting audit logs through the API. The two formats we currently support
are CSV and CEF. These formats can be specified by appending the `format` query parameter as follows, `format=csv`
or `format=cef`. CSV is the default, so if no format is specified the logs will be returned as CSV.

```
GET https://api.pulumi.com/api/orgs/${org}/auditlogs/export?startTime=${time}&format=cef
```

### CEF Format Support

CEF is an audit and logging event format that is supported by a wide range of SIEMs. The format is as follows:

```
MMM dd hh:mm:ss host CEF:Version|Device Vendor|Device Product|Device Version|Device Event Class ID|Name|Severity|[Extension]
```

The following fields are part of the standard header defined by CEF:
**Device Vendor**, **Device Product**, **Device Version**: these are strings that uniquely identify the sending device

**Device Event Class ID**: string or integer identifying the type of event reported

**Name**: a human readable description of the event

**Severity**: severity level reflecting the importance of the event

The Extension section is collection of key-value pairs. These keys come from a pre-defined set as well as some keys that we have
defined on our own.

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
