---
title: "Announcing Azure Classic v7"
date: 2026-10-31
meta_desc: "Azure Classic v7 brings ID-based parent references, consistent property names, and safer defaults. Here's what changed and how to upgrade."
allow_long_title: True
feature_image: feature.png
authors:
   - zaid-ajaj
tags:
   - azure
   - releases
category: product
---

Azure Classic v7, the latest major version of our Azure Classic provider, is now available. It's bridged from [Terraform AzureRM provider v5.9.0](https://registry.terraform.io/providers/hashicorp/azurerm/5.9.0) and brings more consistent APIs, safer defaults, and a cleanup of properties deprecated during v6. This post covers the improvements first, then the breaking changes to plan for when you upgrade.

{{% notes type="info" %}}
Starting a new project? We recommend using our own [Azure Native provider](/registry/packages/azure-native/), which is better supported and generated directly from the Azure Resource Manager API specifications and is our recommended provider for new Azure work. Azure Classic remains fully supported.
{{% /notes %}}


<!--more-->

## What's new

### Parent resources are referenced by ID

Many child resources now take a single ID for their parent instead of a name and a resource group. Storage containers, queues, shares, and tables take `storageAccountId`, blobs take `storageContainerId`, private DNS records take `privateDnsZoneId`, and Event Hubs take `namespaceId`:

```diff
 const container = new azure.storage.Container("container", {
-    storageAccountName: account.name,
+    storageAccountId: account.id,
 });
```

For storage and private DNS resources, the provider migrates existing state, so they aren't replaced when you upgrade.

### Consistent property names

Boolean properties now follow a single `xEnabled` pattern: `enableTcpReset` is now `tcpResetEnabled`, `enableBgp` is now `bgpEnabled`, and `enableRbacAuthorization` is now `rbacAuthorizationEnabled`. Misspelled names are fixed too, such as `moniterMetricsAfterDuration` on Data Factory pipelines, which is now `monitorMetricsAfterDuration`.

### Safer defaults

- TLS 1.0 and 1.1 are no longer accepted as minimum TLS versions on storage accounts, SQL servers, Redis caches, Event Hubs and Service Bus namespaces, and other resources.
- Storage accounts no longer allow public access to containers and blobs unless you set `allowNestedItemsToBePublic: true`.

## Breaking changes

Most breaking changes remove properties that were deprecated in v6. The ones most likely to affect you:

- **Resource provider registration is off by default.** `resourceProviderRegistrations` now defaults to `none`, so the provider no longer registers about 60 resource providers on your subscription. If a provider your program uses was never registered, `pulumi up` fails with `MissingSubscriptionRegistration`. Set `resourceProviderRegistrations: "legacy"` to keep the v6 behavior, or list what you need in `resourceProvidersToRegisters`. `skipProviderRegistration` was removed.
- **Some renamed booleans flip meaning.** When the old name ended in `Disabled`, the value inverts: `disableIpMasking: true` becomes `ipMaskingEnabled: false`.
- **Storage `id` outputs changed meaning.** The `id` of a container, queue, share, or table is now always its Azure Resource Manager ID, not its data-plane URL. Use the `url` output where you need the URL, and use `id` in place of the removed `resourceManagerId`.
- **Settings moved to dedicated resources.** Static website and queue settings moved from `storage.Account` to `storage.AccountStaticWebsite` and `storage.AccountQueueProperties`. Key Vault certificate contacts moved to `keyvault.CertificateContacts`.
- **Newly required inputs.** These include `nodeProvisioningProfile` on AKS clusters (`{ mode: "Manual" }` matches v6), `rbacAuthorizationEnabled` on Key Vaults (`false` for vaults that use access policies), and `tlsMinVersion` on HDInsight clusters.
- **Changed defaults.** A resource that relied on an old default shows a diff on the first preview after upgrading, so set the old value explicitly to keep the current behavior. AKS `oidcIssuerEnabled` now defaults to `true` and can't be turned off once on, and `powerbi.Embedded` now defaults to `Gen2`, which replaces existing Gen1 capacities.
- **Front Door rules were rewritten.** `cdn.FrontdoorRule` now matches the `cdn.FrontdoorBatchRuleSet` schema, so every condition and action block has a new name.

## Upgrading

1. Update the package to v7 and fix the compile errors. In Go, change import paths from `sdk/v6` to `sdk/v7`.
1. Run `pulumi refresh --run-program` so the provider rewrites existing state into the v7 shape.
1. Run `pulumi preview --diff` and review every replacement and every update to a property you didn't change.
1. Run `pulumi up`.

If you run into problems, [open an issue](https://github.com/pulumi/pulumi-azure/issues) on the provider's repository.
