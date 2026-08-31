---
title: Audit log events
title_tag: Pulumi Cloud Audit Log Event Reference
h1: Audit log events
meta_desc: The complete catalog of events Pulumi Cloud records in an organization's audit log, grouped by the product area each event belongs to.
menu:
  administration:
    name: Audit log events
    parent: administration-reference
    identifier: administration-reference-audit-log-events
    weight: 2
pulumi_cloud_feature: audit-logs
no_edit_this_page: true
---

Every event Pulumi Cloud can record in an organization's [audit log](/docs/administration/concepts/audit-logs/), grouped by the product area it belongs to. To view or export your organization's log, see [Audit logs](/docs/administration/concepts/audit-logs/).

Each entry lists:

- **Event** — the name shown in the Pulumi Cloud console and in the `event` field of an exported log.
- **Event ID** — the stable identifier to match on when you process an exported log programmatically.
- **Description** — what the event records, followed where applicable by the permission level the action required, or a note that the event was raised by a failed authentication or authorization check.

{{< audit-log-events-updated >}}

This list is generated from the Pulumi Cloud API, so it stays in step with what your organization's log actually records.

{{< audit-log-events >}}
