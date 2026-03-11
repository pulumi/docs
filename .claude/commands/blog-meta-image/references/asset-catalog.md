# Asset Catalog Reference

All assets live in `.claude/commands/blog-meta-image/assets/`. Paths in the feature JSON config are relative to the `--assets-dir` directory. The `feature_image` path in the meta JSON config must be an absolute path.

## Templates

Located in `templates/`. Two sets of PNGs:

- **Feature templates** — 1884×1256px. Used as the blog post's visual feature image. Mascot/static variants are used as-is; logo variants get SVG logos composited onto circular placeholders.
- **Meta template** — 1200×628px (`meta.png`). Used as the OpenGraph image. The chosen feature image is scaled and composited offset-right behind the title text.

### Feature Templates (1884×1256)

| Filename | Type | Description |
|----------|------|-------------|
| feature-neo.png | mascot | Neo / AI-focused Pulumipus design |
| feature-platform.png | mascot | Platform engineering design |
| feature-rocket.png | mascot | Rocket / deployment and automation design |
| feature-shield.png | mascot | Shield / security and compliance design |
| feature-tutorial.png | mascot | Tutorial / learning and education design |
| feature-logo-1.png | 1-logo | Single large circular logo placeholder |
| feature-logo-2.png | 2-logo | Two circular logo placeholders |
| feature-logo-3.png | 3-logo | Three circular logo placeholders |

### Meta Assets (1200×628)

The meta image is built from scratch (solid `#20054E` background) rather than from a template PNG. Two overlay assets are composited on top of the feature image:

| Filename | Type | Description |
|----------|------|-------------|
| meta-overlay.png | overlay | Full-bleed gradient/vignette composited over the feature image |
| meta-logo.png | logo | Pulumi wordmark (175×44), placed bottom-left at x=90, 40px from bottom |

`meta.png` is no longer used and kept only for reference.

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

## Text Defaults

From `catalog.yaml` (applied to the meta image only):

- **Font**: inter-bold.woff (static bold, always white #FFFFFF)
- **Letter-spacing**: -0.025em (tighter tracking)
- **Line-height**: 110% of font size
- **X position**: 90px from left edge (aligned with Pulumi logo)
- **Y position**: 80px from top edge (top-anchored, flows downward)
- **Max width**: 700px (text area on left half)
- **Font size**: variable (60-104px depending on title length)

## Feature Template Selection Guide

| Topic / Signal | Recommended Feature Template |
|---------------|------------------------------|
| **AI / ML / LLM** | neo |
| **Platform engineering / IDP** | platform |
| **Deployment / automation / CI/CD** | rocket |
| **Security / compliance / policy** | shield |
| **Tutorial / how-to / learning** | tutorial |
| **Cloud provider specific** | logo variant with provider logo(s) |
| **Multi-technology** | logo variant with 2-3 relevant logos |
| **Abstract / conceptual** | wireframe mascot |

## Composition Rules

1. **Text is always white** — all templates have dark-enough backgrounds for white text readability
2. **Text stays on the left** — max_width of 700px prevents text from overlapping the right-side mascot/logos
3. **Logos go on white placeholders** — the compose script centers logos within the measured placeholder bounds
4. **1-3 logos max** — template determines slot count; select the template matching logo count
5. **Font size scales with title length** — shorter titles get larger fonts for visual impact
