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
| feature-shape-circle.png | Outline circle — general-purpose abstract (focus, wholeness) |
| feature-shape-square.png | Outline square — general-purpose abstract (building blocks, components) |
| feature-shape-diamond.png | Outline diamond — general-purpose abstract (decisions, data flow, networking) |
| feature-shape-hexagon.png | Outline hexagon — Kubernetes-adjacent, modules, packages |
| feature-shape-lock.png | Outline lock — security, secrets, encryption, access control |
| feature-shape-shield.png | Outline shield — security posture, compliance, policy (shape counterpart to feature-shield.png) |
| feature-shape-speech-bubble.png | Outline speech bubble — community, Q&A, announcements, AI chat/agents |
| feature-shape-sync-diamond.png | Outline diamond with sync arrows — CI/CD, automation, deployments, drift |

The eight `feature-shape-*` templates are dual-use: the center takes either a **solid phosphor icon** (fill weight, flat-tinted `#C3BDFF`) or a **single small logo**.

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

**feature-shape-\*** (all eight, one shared centered placeholder):
- Placeholder: x=772, y=458, 340×340px (center 942,628 — the shape's clear space)
- A phosphor icon renders at 290px (25px padding); a logo renders ~228px (standard placeholder padding)

## Icons

Located in `icons/`. Solid **fill-weight** [Phosphor](https://phosphoricons.com) icons for the center of the `feature-shape-*` templates, always flat-tinted violet-primary dark (`#C3BDFF`) by the compose script.

Fetched on demand and cached (committed) here, named `<slug>-fill.svg`:

```
https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/<slug>-fill.svg
```

On a 404, search phosphoricons.com for the correct kebab-case slug. Never use the regular/bold/duotone weights.

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
| **Security, secrets, encryption, access control** | shape: lock (icon or logo centerpiece) |
| **Security posture, compliance, policy** | shape: shield |
| **Community, Q&A, announcements, AI chat/agents** | shape: speech bubble |
| **CI/CD, automation, deployments, drift** | shape: sync diamond |
| **Kubernetes, modules, packages, components** | shape: hexagon |
| **Topic with a strong phosphor-icon match but no single obvious logo** | shape: circle / square / diamond (pick by icon silhouette fit) |

## Composition Rules

1. **Logos go on the circular placeholders** — the compose script centers each logo within the measured placeholder bounds
2. **1-3 logos max** — the template determines the slot count; select the template matching the logo count
3. **Tint** — logos are tinted into Pulumi's lavender accent by default (`overlay` mode); use `color` mode to preserve internal contrast
4. **Shape templates take one centerpiece** — either `icon` (a phosphor fill SVG, always overlay-tinted `#C3BDFF`) or a single-entry `logos` list, never both
