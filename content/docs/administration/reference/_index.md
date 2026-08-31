---
title: Reference
title_tag: Pulumi Cloud Administration Reference
h1: Reference
meta_desc: Lookup material for administering Pulumi Cloud — the catalogs of RBAC scopes and audit log events, the log export formats, and the Cloud REST API.
menu:
  administration:
    name: Reference
    parent: administration-home
    identifier: administration-reference
    weight: 40
---

Enumerations you consult rather than read end to end.

- [RBAC scopes](/docs/administration/reference/rbac-scopes/) — the complete catalog of permission scopes, grouped by the entity they apply to.
- [Audit log events](/docs/administration/reference/audit-log-events/) — every event Pulumi Cloud records in an organization's audit log, grouped by product area.
- [Audit log formats](/docs/administration/reference/audit-log-formats/) — the fields carried by each of the JSON, CSV, and CEF audit log export formats.

To administer your organization programmatically, see the [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/) — endpoints for organizations, teams, access tokens, stacks, and environments. It authenticates with the same [access tokens](/docs/administration/concepts/access-tokens/) as the CLI, and you can call any endpoint with [`pulumi api`](/docs/iac/cli/api/).
