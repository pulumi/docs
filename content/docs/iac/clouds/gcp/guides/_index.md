---
title_tag: "Google Cloud Guides | Pulumi IaC"
title: Guides
h1: Google Cloud guides
meta_desc: Guides for working with Google Cloud services using Pulumi's GCP provider.
meta_image: /images/docs/meta-images/docs-clouds-google-cloud-meta-image.png
menu:
  iac:
    name: Guides
    identifier: gcp-clouds-guides
    parent: google-clouds
    weight: 1

aliases:
- /docs/clouds/gcp/guides/
---

This section contains guides for working with Google Cloud using Pulumi. If you are unsure which Google Cloud
package to use for your project, see [Choosing a Pulumi GCP provider](providers/) for a comparison of the
available packages and guidance on when to use each one.

The guides use the following packages:

- [GCP Classic provider (`@pulumi/gcp`)](/registry/packages/gcp/) — the primary, recommended provider for managing
  Google Cloud resources
- [Google Cloud Native provider (`@pulumi/google-native`)](/registry/packages/google-native/) — a provider built
  directly on Google Cloud REST API discovery documents (not actively maintained; new projects should use the GCP
  Classic provider)

## Getting started

- [Choosing a provider](providers/)
- [Get started with Google Cloud](/docs/iac/get-started/gcp/)
