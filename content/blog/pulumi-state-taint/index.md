---
title: "Precise Resource Replacement with Pulumi State Taint"

date: 2025-08-31

draft: false

meta_desc: "Pulumi CLI v3.192.0 introduces state taint and untaint commands for precise control over resource replacements without code changes."

meta_image: meta.png

authors:
    - meagan-cojocar

tags:
    - pulumi-cli
    - releases

social:
    twitter: |
        🎯 Precise resource control is here!
        
        Pulumi CLI v3.192.0 adds `pulumi state taint` and `pulumi state untaint` commands.
        
        Mark resources for replacement without changing your code. Perfect for corrupted VMs, expired certs, or stuck Kubernetes objects.
        
        [link]
    
    linkedin: |
        🚀 New in Pulumi CLI v3.192.0: Surgical Infrastructure Replacement
        
        Sometimes the fastest path to healthy infrastructure is a targeted replacement. A VM with a corrupted disk, a certificate that needs regeneration, or a Kubernetes object stuck in a bad state.
        
        Now you can handle these scenarios without refactoring code or editing state files:
        
        ✅ `pulumi state taint <resource-urn>` - Mark for replacement
        ✅ `pulumi state untaint <resource-urn>` - Cancel the replacement  
        ✅ Normal `pulumi preview` and `pulumi up` workflow
        
        Clean, surgical, predictable. The way infrastructure management should be.
        
        Available now in CLI v3.192.0 → [link]
        
        #InfrastructureAsCode #DevOps #Pulumi

---

Sometimes infrastructure needs a clean slate. A VM with a corrupted disk, an expired certificate, or a stuck Kubernetes object. [Pulumi CLI v3.192.0](https://github.com/pulumi/pulumi/releases/tag/v3.192.0) introduces `pulumi state taint` and `pulumi state untaint` commands that let you mark resources for replacement—especially valuable when you have state access but restricted cloud permissions.

<!--more-->

## The New Commands

- **`pulumi state taint <resource-urn>`** - Mark a resource for replacement
- **`pulumi state untaint <resource-urn>`** - Cancel the replacement (use `--all` to untaint all resources)

> **Note**: This provides the same functionality as `pulumi up --replace <urn>`, but lets you mark resources upfront and preview changes before the update. This can be preferred when the `pulumi up` happens later in CI/CD, where arranging for `--replace` flags would be tedious.

## Why This Matters

The taint and untaint commands solve several infrastructure management challenges. For example, many organizations restrict direct cloud access to production environments, allowing changes only through CI/CD pipelines. In these cases, you can access Pulumi state but not cloud APIs directly—taint lets you mark problematic resources for replacement and let the next automated deployment handle the actual changes, no emergency access requests required.

## Workflow

```bash
# 1. Find the resource URN
pulumi stack --show-urns

# 2. Mark for replacement
pulumi state taint urn:pulumi:production::webapp::aws:ec2/instance:Instance::web-server

# 3. Preview the changes
pulumi preview

# 4. Apply the replacement
pulumi up

# Optional: Cancel the taint
pulumi state untaint urn:pulumi:production::webapp::aws:ec2/instance:Instance::web-server
```

## Get Started

Available now in [Pulumi CLI v3.192.0](https://github.com/pulumi/pulumi/releases/tag/v3.192.0). Try it in a development stack first to get familiar with the workflow.

This feature originated from feedback in [issue #11657](https://github.com/pulumi/pulumi/issues/11657). See the [v3.192.0 release notes](https://github.com/pulumi/pulumi/releases/tag/v3.192.0) for full details. Have feedback or ideas? Join the discussion in the [Pulumi CLI repository](https://github.com/pulumi/pulumi).
