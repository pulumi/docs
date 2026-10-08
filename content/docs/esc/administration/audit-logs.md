---
title_tag: Audit Logs | Pulumi ESC
meta_desc: Pulumi ESC audit logs allow you to account for user activity within your organization.
title: Audit logs
h1: Pulumi ESC audit logs
menu:
    esc:
        name: Audit logs
        parent: pulumi-esc-admin
        weight: 1
pulumi_cloud_feature: audit-logs
---

Every operation on a Pulumi ESC environment is recorded in your organization's Pulumi Cloud audit log. ESC has no separate log: environment activity appears alongside stack, deployment, and organization activity, and each entry records the timestamp, the user, the action taken, and the source IP address.

That record is what lets you:

- Monitor who read or modified a secret
- Track environment creation and configuration changes
- Demonstrate compliance with your security policies
- Produce attributable records for security forensics

Viewing and exporting those entries works the same way for environments as for everything else in your organization.

## Learn more

- [Audit logs](/docs/administration/concepts/audit-logs/) — viewing logs in the console, exporting them, and the fields each entry carries.
- [Environment events](/docs/administration/reference/audit-log-events/#environments) — every environment operation ESC records, within the complete event catalog.
- [Audit log guides](/docs/administration/guides/audit-logs/) — downloading a log on demand, or delivering it continuously to Amazon S3 or Microsoft Sentinel.
- [`pulumi org audit-log`](/docs/iac/cli/commands/pulumi_org_audit-log/) — listing and exporting entries from the command line.
