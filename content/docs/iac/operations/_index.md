---
title_tag: "Operations | Pulumi IaC"
meta_desc: Run Pulumi day-to-day — stack management, continuous delivery pipelines, and troubleshooting techniques for managing infrastructure after it's deployed.
title: Operations
h1: Operations
meta_image: /images/docs/meta-images/docs-meta.png
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

**[Stack management](/docs/iac/operations/stack-management/)** - Day-to-day stack operations including targeted updates, update plans, and editing state files when recovery is needed.

**[Continuous delivery](/docs/iac/operations/continuous-delivery/)** - Integrate Pulumi with your CI/CD platform of choice. Reference setups for Argo CD, GitHub Actions, GitLab CI/CD, Jenkins, and more.

**[Troubleshooting](/docs/iac/operations/troubleshooting/)** - Diagnose and recover from common failures including update conflicts, destroy failures, interrupted updates, and CI/CD pipeline issues.

**[Least privilege security](/docs/iac/operations/iac-least-privileges/)** - Configure cloud provider credentials with the minimum permissions needed for safe infrastructure operations.
