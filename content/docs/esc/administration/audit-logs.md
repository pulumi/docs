---
title_tag: Audit Logs | Pulumi ESC
meta_desc: Pulumi ESC audit logs allow you to account for user activity within your
  organization.
title: Audit Logs
h1: Pulumi ESC audit logs
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    name: Audit Logs
    parent: pulumi-esc-admin
    weight: 1
search:
  keywords:
    - logs
    - esc
    - audit
    - activity
    - timestamp
    - records
    - environment
---

{{% notes "info" %}}
Audit Logs are available to organizations using the Enterprise and Business Critical editions.
To learn more about editions, visit the [pricing page](/pricing/).
{{% /notes %}}

Audit logs enable you to track the activity of users within your ESC environments. Logs are immutable and record all user activity, providing critical visibility for security and compliance in your organization.

ESC audit logs allow you to:

- Monitor who accessed or modified secrets
- Track environment creation and configuration changes
- Ensure compliance with security policies
- Provide attributable records for security forensics

All ESC activities are recorded in Pulumi Cloud audit log system, capturing the timestamp, user identity, specific action taken, and source IP address for each event. You can download a CSV format or use Pulumi Cloud REST for exporting audit log events.

## View Audit Logs

To view audit logs as an organization admin:

1. Navigate to the organization's **Settings** tab.
1. Navigate to **Audit Logs** tab.

This will show the most recent events in descending order. You can also filter logs by a particular user by selecting their profile picture.

![View ESC audit logs in the ESC console](/docs/esc/assets/pulumi-view-audit-logs.png)

## ESC audit log events

| Event                                      | Description                                                                                                                                                       |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Environment Created                      | records the creation of an environment, including the timestamp, name, login, and description
| Environment Updated                      | records the updating of an environment, including the timestamp, name, login, and description                                                                         |
| Environment Deleted                      | records the deletion of an environment, including the timestamp, name, login, and description                                                                         |
| Environment Open                         | records the opening of an environment, including the timestamp, name, login, and description                                                                          |
| Environment Read                         | records the reading of an open environment, including the timestamp, name, login, and description                                                                     |
| Environment Read Open                    | records the opening and reading of an environment, including the timestamp, name, login, and description                                                              |
| Environment Unauthorized Open            | records the attempt to open an environment the user does not have permission to, including the timestamp, name, login, and description                                |
| Environment Tag Created                  | records the creation of an environment tag, including the timestamp, name, login, and description                                                                     |
| Environment Tag Updated                  | records the updating of an environment tag, including the timestamp, name, login, and description                                                                     |
| Environment Tag Deleted                  | records the deletion of an environment tag, including the timestamp, name, login, and description                                                                     |
| Environment Version Retracted            | records the retracting of an environment version, including the timestamp, name, login, and description                                                               |
| Environment Version Tag Open             | records the opening of an environment at a specific version tag, including the timestamp, name, login, and description                                                |
| Environment Version Tag Created          | records the creation of an environment version tag, including the timestamp, name, login, and description                                                             |
| Environment Version Tag Read             | records the reading of an environment version tag, including the timestamp, name, login, and description                                                              |
| Environment Version Tag Update           | records the updating of an environment version tag, including the timestamp, name, login, and description                                                             |
| Environment Version Tag Delete           | records the deletion of an environment version tag, including the timestamp, name, login, and description                                                             |
| Environment Decrypted                    | records the decryption of an environment, including the timestamp, name, login, and description                                                                       |
| Environment Clone                        | records the cloning of an environment, including the timestamp, name, login, and description                                                                          |
| Environment Restored                     | records the restoring of an environment, including the timestamp, name, login, and description                                                                        |
| Environment Schedule Created             | records the creation of an environment schedule, including the timestamp, name, login, and description                                                                |
| Environment Schedule Updated             | records the updating of an environment schedule, including the timestamp, name, login, and description                                                                |
| Environment Schedule Deleted             | records the deletion of an environment schedule, including the timestamp, name, login, and description                                                                |
| Environment Rotated                      | records the rotation of secrets in an environment, including the timestamp, name, login, and description                                                              |

For a full list of Pulumi Cloud audit log events see the [Pulumi Cloud audit logs](/docs/pulumi-cloud/admin/audit-logs/) documentation.

## Automating and manually exporting logs

Pulumi ESC leverages the same audit log infrastructure as the Pulumi Cloud platform. For detailed information on exporting, and managing audit logs, see the [Pulumi Cloud Audit Logs](/docs/pulumi-cloud/admin/audit-logs/) documentation.
