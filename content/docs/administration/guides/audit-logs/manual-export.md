---
title_tag: "Export Pulumi Cloud Audit Logs on Demand"
meta_desc: Download a range of Pulumi Cloud audit log events on demand from the console, the Pulumi CLI, or the Pulumi Cloud REST API.
title: "Manual Export"
h1: Export audit logs manually
menu:
  administration:
        name: Manual Export
        parent: administration-guides-audit-logs
        weight: 1
pulumi_cloud_feature: audit-logs
---

Pull a range of audit log events on demand, without configuring a destination first. Use this for an ad hoc investigation or a one-time archive. To deliver events continuously instead, see [Export audit logs](/docs/administration/guides/audit-logs/).

## Export from the console

To export audit logs using the console:

1. Navigate to the organization's **Settings**.
1. Navigate to **Audit Logs**.
1. Select **Download**.

## Export using the CLI

The Pulumi CLI can read and export audit log events without leaving your terminal:

```bash
# Print recent events
pulumi org audit-log list --org <org-name>

# Write a CSV export to a file
pulumi org audit-log export --org <org-name> --format csv > audit-logs.csv
```

`export` accepts `csv` (the default) or `cef` for `--format`, and narrows the result with `--event-type`, `--user`, and `--start-time`. Passing `--output json` wraps the response body in a JSON envelope with the format and base64-encoded data, which is easier to consume from a script.

{{% notes type="info" %}}
`pulumi org audit-log` is marked experimental, so its flags may change. See [`pulumi org audit-log`](/docs/iac/cli/commands/pulumi_org_audit-log/) for the full command reference.
{{% /notes %}}

## Export using the REST API

{{% notes type="info" %}}
See [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/audit-logs/) for full details of the API endpoint to export audit log events. This API is rate-limited and only intended for occasional use. If you need frequent export, use [automated export](/docs/administration/guides/audit-logs/) instead.
{{% /notes %}}

## Learn more

- [Audit log formats](/docs/administration/reference/audit-log-formats/) — the fields each of the JSON, CSV, and CEF export formats carries.
