---
title: Pulumi CLI versions
meta_desc: This page provides an list of available versions of the Pulumi CLI.
menu:
  iac:
    name: Available versions
    weight: 4
    parent: iac-cli

aliases:
- /docs/iac/download-install/versions/
- /docs/reference/changelog/
- /docs/get-started/install/versions/
- /docs/get-started/download-install/versions/
---

<!--
  The table body is rendered from data/versions.json, which is regenerated
  from pulumi/pulumi release tags by scripts/get-cli-versions.js. To refresh
  it locally, run `make update-versions` (requires GITHUB_TOKEN). The CLI
  docs workflow (.github/workflows/pulumi-cli-docs.yml) runs the same
  script on every release. Edit the shortcode at
  layouts/shortcodes/changelog-table-body.html to change row layout.

  The matching `static/latest-version` file is written by the same
  workflow's "Update latest version" step.
-->

The current stable version of Pulumi is **{{< latest-version >}}**.

<table>
    <thead>
        <tr>
            <th scope="col" width="20%">Version</th>
            <th scope="col" width="20%">Date</th>
            <th scope="col" colspan="3" width="40%">Downloads</th>
            <th scope="col" width="20%">---</th>
        </tr>
    </thead>
    <tbody>
        {{< changelog-table-body >}}
    </tbody>
</table>
