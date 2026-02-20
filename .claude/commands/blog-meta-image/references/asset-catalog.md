# Asset Catalog Reference

All assets live in `.claude/commands/blog-meta-image/assets/`. Paths in the JSON config are relative to the `--assets-dir` directory.

## Templates

Located in `templates/`. Pre-composed 1200x628 PNGs with Pulumi logo, background gradient, and grid lines baked in.

### Dark Theme (deep purple gradient)

| Filename | Type | Description |
|----------|------|-------------|
| dark-flying.png | mascot | 3D Pulumipus flying with wings spread and sunglasses |
| dark-closeup.png | mascot | 3D teal Pulumipus head closeup with big sunglasses |
| dark-wireframe.png | mascot | Purple line-art wireframe outline of Pulumipus |
| dark-shield.png | mascot | 3D Pulumipus holding a shield with sunglasses |
| dark-logo-1.png | 1-logo | Large half-pill white placeholder on right |
| dark-logo-2.png | 2-logo | Two stacked rounded-square white placeholders |
| dark-logo-3.png | 3-logo | Three staggered rounded-square white placeholders |

### Light Theme (lighter purple gradient)

| Filename | Type | Description |
|----------|------|-------------|
| light-flying.png | mascot | 3D Pulumipus flying (lighter bg) |
| light-closeup.png | mascot | 3D Pulumipus closeup (lighter bg) |
| light-wireframe.png | mascot | Wireframe Pulumipus (lighter bg) |
| light-shield.png | mascot | 3D Pulumipus with shield (lighter bg) |
| light-logo-1.png | 1-logo | Large half-pill placeholder (lighter bg) |
| light-logo-2.png | 2-logo | Two stacked placeholders (lighter bg) |
| light-logo-3.png | 3-logo | Three staggered placeholders (lighter bg) |

### Logo Placeholder Positions (measured from PNGs)

These positions are stored in `catalog.yaml` and used by the compose script automatically.

**1-logo templates** (dark-logo-1, light-logo-1):
- Placeholder: x=678, y=72, 522x476px (large half-pill shape)

**2-logo templates** (dark-logo-2, light-logo-2):
- Top: x=900, y=88, 200x182px
- Bottom: x=900, y=349, 200x181px

**3-logo templates** (dark-logo-3, light-logo-3):
- Top-left: x=822, y=116, 145x173px
- Mid-right: x=998, y=202, 145x173px
- Bottom-left: x=822, y=329, 145x173px

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

From `catalog.yaml`:

- **Font**: Inter.ttf (variable, weight 700, always white #FFFFFF)
- **Letter-spacing**: -0.03em (tighter tracking)
- **Line-height**: 110% of font size
- **X position**: 90px from left edge (aligned with Pulumi logo)
- **Y position**: 80px from top edge (top-anchored, flows downward)
- **Max width**: 700px (text area on left half)
- **Font size**: variable (60-104px depending on title length)

## Template Selection Guide

| Topic / Signal | Recommended Style |
|---------------|-------------------|
| **General blog post** | flying or closeup mascot |
| **Security / compliance** | shield mascot |
| **Technical / code-focused** | wireframe mascot |
| **Cloud provider specific** | logo template with provider logo(s) |
| **Multi-technology** | logo template with 2-3 relevant logos |
| **Fun / casual** | flying or closeup mascot |
| **Abstract / conceptual** | wireframe mascot |

## Composition Rules

1. **Text is always white** — all templates have dark-enough backgrounds for white text readability
2. **Text stays on the left** — max_width of 700px keeps text on the left side
3. **Logos go on white placeholders** — the compose script centers logos within the measured placeholder bounds
4. **1-3 logos max** — template determines slot count; select the template matching logo count
5. **Font size scales with title length** — shorter titles get larger fonts for visual impact
