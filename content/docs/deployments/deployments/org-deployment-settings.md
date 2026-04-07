---
title_tag: "Organization Deployment Settings | Pulumi Deployments"
meta_desc: Configure organization-wide deployment settings including review stack signal gating, label prefixes, and delimiters.
title: "Organization deployment settings"
h1: "Organization deployment settings"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  deployments:
    name: Organization settings
    parent: deployments-deployments
    weight: 75
    identifier: deployments-deployments-org-settings
---

Organization deployment settings allow administrators to configure deployment behavior across all stacks in an organization. These settings serve as defaults — individual stacks can override them via their `Pulumi.<stack>.deploy.yaml` file or the stack-level deployment settings API.

## Configuring organization deployment settings

Organization deployment settings can be configured in two ways:

### Pulumi Cloud UI

Navigate to your organization's **Deployments > Settings** tab, or go to **Settings > General > Deployments**. From here you can:

- **Enable review stack signal gating** — require matching labels or commit message signals before creating review stacks
- **Configure label prefixes** — customize which label prefixes trigger review stack creation
- **Configure delimiters** — customize the characters that separate a prefix from a custom stack name

### REST API

Use the organization deployment settings API to configure settings programmatically:

```bash
# Read current settings
curl -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  "https://api.pulumi.com/api/orgs/my-org/deployment-settings"

# Update settings
curl -XPUT -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  "https://api.pulumi.com/api/orgs/my-org/deployment-settings" \
  -d '{
    "reviewStackSignalGating": true,
    "reviewStackPrefixes": ["review-stack", "deploy"],
    "reviewStackDelimiters": [":", "/"]
  }'
```

## Review stack signal gating

When signal gating is enabled, review stacks are only created for pull requests that have a matching signal — either a label on the PR or a bracketed token in the PR title/body.

See [Review stacks > Signal gating](/docs/deployments/deployments/review-stacks/#signal-gating) for detailed configuration options, signal sources, and examples.

### Resolution order

Settings are resolved in the following order, with earlier levels taking priority:

1. **Per-stack** `reviewStackPrefixes` in `Pulumi.<stack>.deploy.yaml` or stack API
2. **Organization-wide** settings from this page
3. **Built-in defaults** (`reviewstack`, `reviewStack`, `review-stack`)

At any level, an empty list `[]` explicitly disables signal gating for that scope, reverting to legacy behavior where every PR creates a review stack.

## Permissions

Organization deployment settings require the **Organization Update** permission. This is available to organization administrators by default.

Changes to organization deployment settings are recorded in the [audit log](/docs/deployments/deployments/security-and-operations/#audit-logs).
