# Asset Catalog Reference

All assets live in `.claude/commands/blog-feature-image/assets/`. Paths in the feature JSON config are relative to the `--assets-dir` directory.

The 1200×628 OpenGraph/social card is **not** built here — it is generated on-brand at build time from the post title + the feature image (`scripts/meta-images/blog.mjs`).

## Templates

Located in `templates/`. Feature templates are 1884×1256px PNGs used as the blog post's visual feature image. Static variants are used as-is; logo variants get SVG logos composited onto circular placeholders.

### Feature Templates (1884×1256)

| Filename | Description |
|----------|--------------|
| feature-platform.png | Default, platform engineering, DevOps, Pulumi news and events |
| feature-neo.png  | For usage on Neo specific posts only |
| feature-rocket.png | Releases, new features, and announcements |
| feature-shield.png | Security, secrets, compliance, and policy |
| feature-lightbulb.png | Tutorials, how-tos, best practices, and guest posts |
| feature-logo-1.png | Single large circular logo placeholder |
| feature-logo-2.png | Two circular logo placeholders |
| feature-logo-3.png | Three circular logo placeholders |

### Logo Placeholder Positions (feature logo templates)

These positions are stored in `catalog.yaml` and used by the compose script automatically.

**feature-logo-1** (1 circle, ⌀680):
- Placeholder: x=602, y=288, 680×680px (circle center at 942,628 — image center)

**feature-logo-2** (2 circles, ⌀390):
- Left: x=499, y=432, 390×390px (center 694,627)
- Right: x=992, y=432, 390×390px (center 1187,627)

**feature-logo-3** (3 circles, ⌀390):
- Top: x=720, y=234, 390×390px (center 915,429)
- Bottom-left: x=499, y=630, 390×390px (center 694,825)
- Bottom-right: x=993, y=630, 390×390px (center 1188,825)

## Logos

Located in `logos/`. SVG product/technology logos placed on top of white placeholder shapes.

| Filename | Name | Tags |
|----------|------|------|
| 1password.svg | 1Password | 1password, password, security |
| amazon-ebs.svg | Amazon EBS | aws, amazon, ebs, storage |
| amazon-sagemaker.svg | Amazon SageMaker | aws, amazon, sagemaker, ml, ai |
| aws-cdk.svg | AWS CDK | aws, cdk, iac |
| aws-dark.svg | AWS (dark) | aws, amazon, cloud, dark |
| aws.svg | AWS | aws, amazon, cloud |
| azure-icon.svg | Azure (icon) | azure, microsoft, cloud |
| azure-storage.svg | Azure Storage | azure, microsoft, storage |
| azure.svg | Azure | azure, microsoft, cloud |
| bicep.svg | Bicep | bicep, azure, iac |
| bun.svg | Bun | bun, javascript, runtime |
| docker.svg | Docker | docker, containers |
| google-cloud-icon.svg | Google Cloud (icon) | gcp, google, cloud |
| google-cloud-logo.svg | Google Cloud | gcp, google, cloud |
| hashicorp-terraform.svg | Terraform | terraform, hashicorp, iac |
| huggingface.svg | Hugging Face | huggingface, ai, ml |
| kubernetes.svg | Kubernetes | kubernetes, k8s, containers |
| microsoft.svg | Microsoft | microsoft, windows |
| python.svg | Python | python, language |
| redis.svg | Redis | redis, database, cache |
| slack.svg | Slack | slack, messaging |
| typescript.svg | TypeScript | typescript, javascript, language |
| vercel.svg | Vercel | vercel, hosting, frontend |

## Feature Template Selection Guide

| Topic / Signal | Recommended Feature Template |
|---------------|------------------------------|
| **For usage on Neo specific posts only** | neo |
| **Default, platform engineering, DevOps, Pulumi news and events** | platform |
| **Releases, new features, and announcements** | rocket |
| **Security, secrets, compliance, and policy** | shield |
| **Tutorials, how-tos, best practices, and guest posts** | lightbulb |
| **Cloud provider or technology-specific content** | logo variant with provider/tech logos |

## Composition Rules

1. **Logos go on the circular placeholders** — the compose script centers each logo within the measured placeholder bounds
2. **1-3 logos max** — the template determines the slot count; select the template matching the logo count
3. **Tint** — logos are tinted into Pulumi's lavender accent by default (`overlay` mode); use `color` mode to preserve internal contrast
