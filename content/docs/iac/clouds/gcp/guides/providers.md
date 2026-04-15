---
title_tag: "Choosing a Pulumi GCP Provider"
title: Choosing a Provider
h1: Choosing a Pulumi GCP Provider
meta_desc: Learn when to use the GCP Classic and Google Cloud Native packages for managing Google Cloud infrastructure with Pulumi, and how to migrate between them.
meta_image: /images/docs/meta-images/docs-clouds-google-cloud-meta-image.png
menu:
  iac:
    parent: gcp-clouds-guides
    name: Choosing a Provider
    identifier: gcp-guides-providers
    weight: 0
aliases:
- /docs/clouds/gcp/guides/providers/
---

Pulumi offers two packages for working with Google Cloud at the provider level, plus a pair of smaller component
libraries for specific use cases. This guide explains what each package does, how they compare, and which one to
choose for your project.

{{% notes type="info" %}}
For all new Google Cloud projects, use the **[GCP Classic provider (`@pulumi/gcp`)](/registry/packages/gcp/)**. It
is the primary, actively maintained choice with the broadest resource coverage, documentation, and community
support. The Google Cloud Native provider is no longer actively maintained and is not recommended for new projects.
{{% /notes %}}

## Packages at a glance

### Providers

| | [GCP Classic](/registry/packages/gcp/) | [Google Cloud Native](/registry/packages/google-native/) |
|---|---|---|
| **Node.js** | `@pulumi/gcp` | `@pulumi/google-native` |
| **Python** | `pulumi_gcp` | `pulumi_google_native` |
| **Go** | `github.com/pulumi/pulumi-gcp/sdk/v8/go/gcp` | `github.com/pulumi/pulumi-google-native/sdk/go/google` |
| **.NET** | `Pulumi.Gcp` | `Pulumi.GoogleNative` |
| **Java** | `com.pulumi.gcp` | `com.pulumi.googlenative` |
| **Built on** | Terraform Google provider (via Pulumi TF bridge) | Google Cloud REST API discovery documents |
| **Resource coverage** | Comprehensive | Limited to REST API discovery resources |
| **Maintenance status** | Actively maintained | Not actively maintained (last release: Nov 2023) |
| **Best for** | All new and existing projects | Legacy projects; not recommended for new use |

### Component libraries

Component libraries build on top of the GCP Classic provider and package common patterns into higher-level
constructs. They are not separate providers — they do not have their own state and they do not replace the GCP
provider.

| | [GCP Global CloudRun](/registry/packages/gcp-global-cloudrun/) | [Google Cloud static website](/registry/packages/google-cloud-static-website/) |
|---|---|---|
| **Covers** | Multi-region Cloud Run with global load balancing | Static website hosting on Cloud Storage |

## GCP Classic provider

The [GCP Classic provider](/registry/packages/gcp/) is the primary and recommended package for managing Google
Cloud infrastructure with Pulumi. It is built on the
[Terraform Google provider](https://github.com/hashicorp/terraform-provider-google) via the
[Pulumi Terraform bridge](https://github.com/pulumi/pulumi-terraform-bridge), which translates the mature
HashiCorp Google provider into native Pulumi resources. This gives you access to a comprehensive, well-tested
interface to Google Cloud services, refined by a large community over many years.

The GCP Classic provider covers the full breadth of Google Cloud services: Compute Engine, Cloud Storage, Google
Kubernetes Engine, Cloud Run, Cloud SQL, Pub/Sub, BigQuery, IAM, networking, and much more. It follows a
predictable naming convention where resource types map closely to the underlying Terraform resource names (e.g.,
`gcp.storage.Bucket`, `gcp.compute.Instance`, `gcp.container.Cluster`).

For all Google Cloud infrastructure — whether you are starting a new project or maintaining an existing one —
the GCP Classic provider is the right choice. Its resources are thoroughly documented, support all Pulumi features
(including import, state management, and drift detection), and are actively updated to track new Google Cloud
services and API changes.

## Google Cloud Native provider

The [Google Cloud Native provider](/registry/packages/google-native/) was originally built directly on Google
Cloud's REST API discovery documents, enabling same-day coverage of newly launched resources. However, this
provider is no longer actively maintained. Its last release was in November 2023, and it has not been updated
to reflect changes in the Google Cloud API since then.

{{% notes type="warning" %}}
The Google Cloud Native provider is **not recommended for new projects**. Users on Google Cloud Native who need
continued access to Google Cloud resources should migrate to the GCP Classic provider. See
[Migrating from Google Cloud Native to GCP Classic](#migrating-from-google-cloud-native-to-gcp-classic) below.
{{% /notes %}}

If you are maintaining a project that already uses the Google Cloud Native provider, it will continue to function
for resources that have not changed since November 2023. However, you should plan a migration to the GCP Classic
provider to ensure access to new resource types, bug fixes, and ongoing support.

## Component libraries

### GCP Global CloudRun

[GCP Global CloudRun](/registry/packages/gcp-global-cloudrun/) provides a higher-level component for deploying
Cloud Run services with global load balancing. It abstracts the complexity of configuring a Cloud Run service
alongside a global HTTPS load balancer, making it straightforward to expose a containerized workload to the
public internet with a global anycast IP address.

### Google Cloud static website

[Google Cloud static website](/registry/packages/google-cloud-static-website/) is a component for hosting a
static website on Cloud Storage. It handles bucket creation, public access configuration, and optional CDN
setup, making it easy to deploy a static site to Google Cloud with minimal boilerplate.

## Choosing the right package

For any new project on Google Cloud, use the GCP Classic provider. It is the only actively maintained provider
with comprehensive resource coverage, and it is the choice recommended by Pulumi.

If you have a specific use case for which no lower-level provider resource exists, consider whether the GCP
Global CloudRun or Google Cloud static website component libraries cover it. For all other resources, work
directly with `@pulumi/gcp`.

Avoid starting new projects with the Google Cloud Native provider. Its maintenance has ceased, and users with
existing projects on it should migrate to the GCP Classic provider as described below.

## Migrating from Google Cloud Native to GCP Classic

If you have an existing project using the Google Cloud Native provider, migrating to the GCP Classic provider
will give you access to actively maintained resources, bug fixes, and ongoing support.

The general migration approach is:

1. **Identify your Google Cloud Native resources.** Review your Pulumi program for imports from
   `@pulumi/google-native` (TypeScript/JavaScript), `pulumi_google_native` (Python), or equivalent packages in
   other languages.

2. **Find the GCP Classic equivalents.** Most resources in the Google Cloud Native provider have a direct
   counterpart in the GCP Classic provider under the `gcp.*` namespace. For example:
   - `google-native.storage/v1.Bucket` → `gcp.storage.Bucket`
   - `google-native.compute/v1.Instance` → `gcp.compute.Instance`
   - `google-native.container/v1.Cluster` → `gcp.container.Cluster`

3. **Rewrite your resource definitions.** Update your program to use GCP Classic resource types and property
   names. Property names and structures will differ in some cases, so consult the
   [GCP Classic API docs](/registry/packages/gcp/api-docs/) for each resource.

4. **Import existing resources.** Use `pulumi import` to bring your existing Google Cloud resources under the
   management of the GCP Classic provider, rather than destroying and recreating them. This requires the resource
   type and its Google Cloud resource ID. See the [import documentation](/docs/iac/adopting-pulumi/import/) for
   full details.

5. **Remove the Google Cloud Native provider** from your project's dependencies once all resources have been
   migrated.

The migration is resource-by-resource and can be done incrementally — you do not need to migrate an entire stack
at once. Running both providers in the same stack during a phased migration is supported.

## Using the GCP Classic provider

The following example demonstrates the GCP Classic provider creating a Cloud Storage bucket and a Cloud Run
service — two of the most commonly used Google Cloud resources:

{{< example-program path="gcp-providers-classic" >}}

When you run `pulumi up`, Pulumi provisions both resources and records their state in your
[Pulumi Cloud](https://app.pulumi.com) backend, giving you a full audit history and enabling collaboration across
your team.

## Next steps

- [GCP Classic provider documentation](/registry/packages/gcp/)
- [GCP Classic provider API docs](/registry/packages/gcp/api-docs/)
- [GCP Classic provider how-to guides](/registry/packages/gcp/how-to-guides/)
- [Get started with Google Cloud](/docs/iac/get-started/gcp/)
- [Importing existing infrastructure](/docs/iac/adopting-pulumi/import/)
