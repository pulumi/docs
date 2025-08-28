---
title: "Automatic Diagram Generation for Always-Accurate Diagrams"
h1: "Automatic Diagram Generation for Always-Accurate Diagrams"
authors: 
  - "elisabeth-lichtie"
tags: ["aws", "diagram", "architecture", "CI/CD", "anthropic", "claude", "github", "actions"]
meta_desc: "Automate tedious diagramming work in you CI/CD pipelines to maintain always-accurate architecture diagrams."
date: "2025-08-28"
meta_image: "Automatic_Diagramming.png"

summary: |
    Architecture diagrams are tedious to create and become outdated the moment infrastructure changes. When you manage infrastructure with Pulumi's infrastructure as code, you can automatically generate accurate diagrams directly from your IaC definitions. With Pulumi's preview capabilities, you can anticipate changes before deployment. Learn how to integrate automated diagram generation into your CI/CD pipeline using AI, Pulumi's native diagramming tools, and GitHub actions.
---

Architecture diagrams are one of the most tedious aspects of infrastructure management. Teams spend countless hours manually creating and updating visual representations of their systems, only to watch them become stale the moment infrastructure changes.

When you manage your infrastructure in code, it's possible to automatically generate accurate, up-to-date diagrams directly from your IaC definitions and state. Pulumi's preview capabilities let you anticipate exactly what changes will result from code modifications before deployment, providing the perfect foundation for automated diagramming workflows.

In this post, we'll explore two practical approaches to automating diagram generation in your CI/CD pipeline:

1. **Native Pulumi diagramming**: Using Pulumi's built-in diagramming capabilities to generate basic architecture diagrams that you can retrieve from GitHub Actions' artifact archive
2. **AI-powered diagramming**: Leveraging the Claude app with Mermaid and Pulumi preview to generate detailed diagrams and automatically add them to pull requests for infrastructure changes

Both approaches eliminate manual diagramming work while ensuring your documentation stays current with your actual infrastructure.

Pulumi's ongoing investment in AI capabilities will soon unlock even more powerful possibilities: organization-wide diagramming patterns and styles, project-level and organization-level views beyond individual stacks, and diagrams intelligently customized for different stakeholders with varying levels of detail and visibility. The examples in this post are just the beginning of how Pulumi's AI-enabled approach will transform infrastructure documentation.
