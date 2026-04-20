---
meta_desc: The Pulumi Registry hosts reusable packages, templates, and policy packs for infrastructure deployments. The Registry API lists, retrieves, publishes, and manages packages, templates, and policy packs in the Registry.
---

The Pulumi Registry hosts reusable packages, templates, and policy packs
for infrastructure deployments. The Registry API allows you to list,
retrieve, publish, and manage packages, templates, and policy packs in the
Pulumi Registry.

## Registry identifiers

Resources in the Registry are identified by a three-part identifier:
`{source}/{publisher}/{name}`.

- **Source** indicates the package's origin. For example:
  - `pulumi`: packages published directly to the public Pulumi registry
  - `opentofu`: OpenTofu packages bridged to Pulumi
  - `private`: organization-specific private registry packages
- **Publisher** is the organization that owns the package. For private
  packages this matches the organization's canonical name; for public
  packages it is managed by Registry administrators.
- **Name** is the unique identifier for the package within its source and
  publisher.

See the [Pulumi Registry](/registry/) for the browsable catalog.
