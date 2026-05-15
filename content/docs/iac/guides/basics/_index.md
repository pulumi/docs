---
title_tag: "Basics | Pulumi Guides"
meta_desc: Learn fundamental practices for organizing Pulumi projects, securing your infrastructure, and managing deployments.
title: Basics
h1: Basics
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Basics
        parent: iac-using-pulumi
        weight: 10
        identifier: iac-guides-basics
aliases:
    - /docs/iac/using-pulumi/
---

Whether you're just starting with Pulumi or looking to refine your workflow, these guides cover essential practices for organizing infrastructure code, securing deployments, and managing changes with confidence.

These fundamentals apply across all cloud providers and help you build maintainable infrastructure from the start.

## Guides

**[Organizing projects & stacks](/docs/iac/guides/basics/organizing-projects-stacks/)** - Learn how to structure your infrastructure code into projects and stacks. Understand when to split infrastructure into multiple projects versus using a single project with multiple stacks.

**[Least privilege security](/docs/iac/guides/basics/iac-least-privileges/)** - Implement security best practices by granting only the minimum permissions needed for infrastructure operations. Learn how to configure cloud provider credentials with appropriate access controls.

**[Update plans](/docs/iac/guides/basics/update-plans/)** - Preview and review infrastructure changes before applying them. Update plans help you catch unintended modifications and coordinate changes across teams.

**[Pulumi Cloud vs. OSS](/docs/iac/guides/basics/pulumi-cloud-vs-oss/)** - Compare open source Pulumi with Pulumi Cloud across state backends, access management, secrets and configuration, policy enforcement, and workflows.

**[Using a DIY backend](/docs/iac/guides/basics/using-a-diy-backend/)** - Configure a self-managed state backend with AWS S3, Azure Blob Storage, Google Cloud Storage, PostgreSQL, or the local filesystem.
