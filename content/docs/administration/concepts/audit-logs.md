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

## List of audit log events

| Event                                    | Description                                                                                                      |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Auth Failure Organization Role           | indicates that a user tried to perform an operation but did not have the necessary organization role to do so    |
| Auth Failure SCIM Access Token           | indicates that a request to use an organization's SCIM support was made, but the provided auth token was invalid |
| Auth Failure Stack Permission            | indicates that a user tried to perform an operation but did not have the necessary stack permissions to do so    |
| Member Added                             | indicates the adding of a member to an organization                                                              |
| Member Removed                           | indicates the removal of a member from an organization                                                           |
| Member Role Changed                      | indicates the changing of a member's role in an organization                                                     |
| Organization Settings Changed            | indicates a change in organization settings                                                                      |
| Policy Group Created                     | indicates the creation of a policy group                                                                         |
| Policy Group Deleted                     | indicates the deletion of a policy group                                                                         |
| Policy Group Updated                     | indicates the updating of a policy group                                                                         |
| Policy Pack Created                      | indicates the creation of a policy pack                                                                          |
| Policy Pack Deleted                      | indicates the deletion of a policy pack                                                                          |
| Policy Pack Disabled                     | indicates the disabling of a policy pack                                                                         |
| Policy Pack Enabled                      | indicates the enabling of a policy pack                                                                          |
| Secret Decrypted                         | indicates the decryption of a secret value associated with a stack                                               |
| Stack Collaborator Added                 | indicates the adding of a collaborator to a stack                                                                |
| Stack Collaborator Permissions Changed   | indicates a change in permissions for a stack collaborator                                                       |
| Stack Collaborator Removed               | indicates the removal of a collaborator to a stack                                                               |
| Stack Created From Template              | indicates the creation of a stack from a template                                                                |
| Stack Created                            | indicates the creation of a stack                                                                                |
| Stack Deleted                            | indicates the deletion of a stack                                                                                |
| Stack Exported                           | indicates the exporting of a stack                                                                               |
| Stack Imported                           | indicates the importing of a stack                                                                               |
| Stack Renamed                            | indicates the renaming of a stack                                                                                |
| Stack Transferred to Organization        | indicates the transfer of a stack from one organization to another                                               |
| Stack Update Canceled                    | indicates the canceling of a stack update                                                                        |
| Stack Update Completed                   | indicates the completion of a stack update                                                                       |
| Stack Update Started                     | indicates the starting of a stack update                                                                         |
| Team Created                             | indicates the creation of a team in an organization                                                              |
| Team Deleted                             | indicates the deletion of a team from an organization                                                            |
| Team Updated                             | indicates the updating of a team in an organization                                                              |
| User Added New Identity to Their Account | indicates a user has associated a new identity with their Pulumi account                                         |
| User Login                               | indicates a user has successfully logged into the Pulumi Cloud                                                   |
| User Login Failed                        | indicates a user tried and failed to log into the Pulumi Cloud                                                   |
| SAML Configuration Updated               | indicates the organization's SAML configuration has been updated                                                 |
| Environment Created                      | indicates the creation of an environment                                                                         |
| Environment Updated                      | indicates the updating of an environment                                                                         |
| Environment Deleted                      | indicates the deletion of an environment                                                                         |
| Environment Open                         | indicates the opening of an environment                                                                          |
| Environment Read                         | indicates the reading of an open environment                                                                     |
| Environment Read Open                    | indicates the opening and reading of an environment                                                              |
| Environment Unauthorized Open            | indicates the attempt to open an environment the user does not have permission to                                |
| Environment Tag Created                  | indicates the creation of an environment tag                                                                     |
| Environment Tag Updated                  | indicates the updating of an environment tag                                                                     |
| Environment Tag Deleted                  | indicates the deletion of an environment tag                                                                     |
| Environment Version Retracted            | indicates the retracting of an environment version                                                               |
| Environment Version Tag Open             | indicates the opening of an environment at a specific version tag                                                |
| Environment Version Tag Created          | indicates the creation of an environment version tag                                                             |
| Environment Version Tag Read             | indicates the reading of an environment version tag                                                              |
| Environment Version Tag Update           | indicates the updating of an environment version tag                                                             |
| Environment Version Tag Delete           | indicates the deletion of an environment version tag                                                             |
| Environment Decrypted                    | indicates the decryption of an environment                                                                       |
| Environment Clone                        | indicates the cloning of an environment                                                                          |
| Environment Restored                     | indicates the restoring of an environment                                                                        |
| Environment Schedule Created             | indicates the creation of an environment schedule                                                                |
| Environment Schedule Updated             | indicates the updating of an environment schedule                                                                |
| Environment Schedule Deleted             | indicates the deletion of an environment schedule                                                                |
| Environment Rotated                      | indicates the rotation of secrets in an environment                                                              |
| Stack Provider Open                      | indicates the opening of a stack provider within an environment                                                  |
| Customer Managed Key Added               | indicates the adding of a new customer managed key                                                               |
| Customer Managed Key Set Default         | indicates the setting of a new default customer managed key                                                      |
| Customer Managed Key Disabled            | indicates the disabling of a customer managed key                                                                |
| Customer Managed Key Disabled All        | indicates the disabling of all customer managed keys                                                             |
