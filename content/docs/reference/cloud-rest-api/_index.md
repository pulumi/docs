---
title: Pulumi Cloud REST API
title_tag: "Pulumi Cloud: REST API Reference"
meta_desc: Learn how to interact with Pulumi Cloud programmatically using the REST API for automation and integration.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    reference:
        parent: reference-home
        weight: 3
        identifier: cloud-rest-api
aliases:
  - /docs/reference/service-rest-api/
  - /docs/intro/insights/api/
  - /docs/reference/cloud-rest-api/
  - /docs/pulumi-cloud/cloud-rest-api/
  - /docs/pulumi-cloud/reference/
---

{{< notes type="info" >}}
**Note:** Copilot has evolved into [Pulumi Neo](/product/neo/), your AI platform engineer. Some features or functionality described here may differ from the latest version.
{{< /notes >}}

The Pulumi Cloud REST API allows you to automate and integrate with Pulumi Cloud programmatically. The API is used by the Pulumi CLI to interact with Pulumi Cloud, but it's also available for users to create their own custom automation and integrations.

With the REST API, you can:

- Manage organizations, projects, and stacks
- Create, track, and control deployments
- Apply and enforce policies
- View and export audit logs
- Query and search resources under management
- Access and publish to the Pulumi Registry
- Configure environments, schedules, and more

## API Resources

The Pulumi Cloud REST API is organized into the following resource categories:

- [API Basics](/docs/reference/cloud-rest-api/api-basics/) - Endpoint URL, authentication, and required headers
- [Audit Logs](/docs/reference/cloud-rest-api/audit-logs/) - Access audit log data
- [Copilot](/docs/reference/cloud-rest-api/copilot/) - Access AI-powered infrastructure assistance
- [Data Export](/docs/reference/cloud-rest-api/data-export/) - Export data from Pulumi Cloud
- [Deployment Runners](/docs/reference/cloud-rest-api/deployment-runners/) - Manage deployment runners
- [Deployments](/docs/reference/cloud-rest-api/deployments/) - Configure and manage Pulumi Deployments
- [Environments](/docs/reference/cloud-rest-api/environments/) - Manage deployment environments
- [Insights Accounts](/docs/reference/cloud-rest-api/insight-accounts/) - Work with Insights accounts
- [OAuth Token Exchange](/docs/reference/cloud-rest-api/oauth-token-exchange/) - Exchange OAuth tokens
- [OIDC Issuers](/docs/reference/cloud-rest-api/oidc-issuers/) - Configure OIDC authentication
- [Organizations](/docs/reference/cloud-rest-api/organizations/) - Manage organization settings and members
- [Personal Access Tokens](/docs/reference/cloud-rest-api/personal-access-tokens/) - Create and manage access tokens
- [Policy Groups](/docs/reference/cloud-rest-api/policy-groups/) - Manage groups of policy
- [Policy Packs](/docs/reference/cloud-rest-api/policy-packs/) - Work with policy packs
- [Policy Results](/docs/reference/cloud-rest-api/policy-results/) - View policy evaluation results from Pulumi Insights
- [Registry](/docs/reference/cloud-rest-api/registry/) - Interact with the Pulumi Registry
- [Resource Search](/docs/reference/cloud-rest-api/resource-search/) - Search for resources
- [Resources Under Management](/docs/reference/cloud-rest-api/resources-under-management/) - Query managed resources
- [Schedules](/docs/reference/cloud-rest-api/schedules/) - Configure scheduled tasks
- [Services](/docs/reference/cloud-rest-api/services/) - Interact with service information
- [Stack Config](/docs/reference/cloud-rest-api/stack-config/) - Manage configuration settings for stacks
- [Stack Policy](/docs/reference/cloud-rest-api/stack-policy/) - Apply and manage policy on stacks
- [Stack Tags](/docs/reference/cloud-rest-api/stack-tags/) - Manage metadata tags on stacks
- [Stack Updates](/docs/reference/cloud-rest-api/stack-updates/) - Manage the update lifecycle for stacks
- [Stacks](/docs/reference/cloud-rest-api/stacks/) - Create, update, and manage Pulumi stacks
- [Webhooks](/docs/reference/cloud-rest-api/webhooks/) - Create and manage webhooks for organizations and stacks
