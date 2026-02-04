---
user-invocable: false
---

# Meta Image Selection

Select the appropriate meta_image path based on the documentation path.

## Path-Based Image Mapping

Use these rules to select the correct meta image for SEO:

- `iac/clouds/aws` → `/images/docs/meta-images/docs-clouds-aws-meta-image.png`
- `iac/clouds/azure` → `/images/docs/meta-images/docs-clouds-azure-meta-image.png`
- `iac/clouds/gcp` → `/images/docs/meta-images/docs-clouds-google-cloud-meta-image.png`
- `iac/clouds/kubernetes` → `/images/docs/meta-images/docs-clouds-kubernetes-meta-image.png`
- **All others** → `/images/docs/meta-images/docs-meta.png`

## Usage

Match the documentation path against the cloud provider paths above. If the path contains `iac/clouds/{provider}`, use the provider-specific image. Otherwise, use the default `docs-meta.png` image.
