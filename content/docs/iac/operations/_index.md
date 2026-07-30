---
title_tag: "Operations | Pulumi IaC"
meta_desc: Run Pulumi day-to-day — stack management, continuous delivery, troubleshooting, debugging, and least-privilege security for infrastructure after it's deployed.
title: Operations
h1: Operations
menu:
    iac:
        name: Operations
        weight: 25
        parent: iac-home
        identifier: iac-operations
---

Once your Pulumi program is written and first deployed, "operations" is everything that happens next: rolling out changes safely, running Pulumi from CI/CD, diagnosing failures, and recovering from incidents.

These pages cover the Day 2 workflows for running Pulumi at scale.

## Sections

**[Stack management](/docs/iac/operations/stack-management/)** - Day-to-day stack operations: targeted updates, update plans, editing state files when recovery is needed, and configuring a self-managed (DIY) state backend.

**[Continuous delivery](/docs/iac/operations/continuous-delivery/)** - Integrate Pulumi with your CI/CD platform of choice. Reference setups for Argo CD, GitHub Actions, GitLab CI/CD, Jenkins, and more.

**[Troubleshooting](/docs/iac/operations/troubleshooting/)** - Diagnose and recover from common failures including update conflicts, destroy failures, interrupted updates, and CI/CD pipeline issues.

**[Debugging](/docs/iac/operations/debugging/)** - Attach a debugger, capture verbose logs, and trace performance for your Pulumi programs.

**[Docker images](/docs/iac/operations/docker-images/)** - Pulumi's officially published container images: what's in each, where to pull from, release cadence, and how to use them as a base for custom images.

**[Container image build caching and deployment reproducibility](/docs/iac/operations/container-image-reproducibility/)** - Build caching, digest-based tagging, and a build/deploy stack split for container images built with the Docker or Docker Build providers.

**[Least privilege](/docs/administration/security-compliance/least-privilege/)** - Apply least-privilege security across your Pulumi platform: cloud provider credentials, IaC and ESC access, and CI/CD. A recommended next step once your operational workflows are in place.
