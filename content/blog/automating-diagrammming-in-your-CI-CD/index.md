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

## Native Pulumi diagramming with GitHub actions

Pulumi's built-in `pulumi stack graph` command generates architecture diagrams directly from your deployed infrastructure state. This approach provides a reliable foundation for automated diagramming since it reflects your actual deployed resources rather than just the code.

Here's a complete GitHub Actions workflow that deploys infrastructure and automatically generates diagrams:

```yaml
name: Pulumi Deploy & Diagram

on:
  push:
    branches: [main]

jobs:
  deploy:
    name: Deploy & Generate Diagram
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - uses: pulumi/actions@v5
        with:
          command: up
          stack-name: dev
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

      - name: Install Pulumi CLI
        run: |
          curl -fsSL https://get.pulumi.com | sh
          echo "$HOME/.pulumi/bin" >> $GITHUB_PATH

      - name: Generate Architecture Diagram
        run: pulumi stack graph architecture.dot --stack dev
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

      - name: Install Graphviz
        run: sudo apt-get update && sudo apt-get install -y graphviz

      - name: Generate PNG from DOT file
        run: dot -Tpng architecture.dot -o architecture.png

      - name: Upload Architecture Diagrams
        uses: actions/upload-artifact@v4
        with:
          name: architecture-diagrams
          path: |
            architecture.dot
            architecture.png
```

### How the workflow works

This workflow follows a straightforward pattern that ensures your diagrams always reflect your deployed infrastructure:

1. **Deploy first**: The workflow uses the official `pulumi/actions@v5` action to deploy your infrastructure changes. This ensures the state reflects your latest code.

2. **Generate diagram from state**: The `pulumi stack graph` command reads your deployed stack's state and generates a DOT format file containing the resource relationships and dependencies.

3. **Convert to visual format**: Graphviz converts the DOT file into a PNG image that's easy to view and share.

4. **Archive as artifacts**: Both the raw DOT file and the rendered PNG are uploaded as GitHub Actions artifacts, making them downloadable from the workflow run.

### Key advantages and limitations

**Highest accuracy**: Since diagrams are generated from deployed state rather than code, they reflect your actual infrastructure including any drift or manual changes. This is the biggest advantage of the native approach.

**Zero maintenance**: Once set up, diagrams update automatically with every deployment without any manual intervention.

**Multiple formats**: The DOT format can be converted to various output formats (PNG, SVG, PDF) depending on your needs.

**Audit trail**: Each workflow run preserves the diagram as an artifact, creating a visual history of your infrastructure changes.

However, this approach has some limitations:

**Fixed styling**: You're locked into Pulumi's diagram style and layout algorithms, with limited customization options.

**Basic aesthetics**: The generated diagrams are functional but not always aesthetically polished compared to hand-crafted or AI-generated alternatives.

**Technical focus**: Diagrams show all resources and relationships, which can be overwhelming for non-technical stakeholders who need higher-level architectural views.

### Accessing your diagrams

After each workflow run, you can download the generated diagrams from the Actions tab in your repository. Click on any workflow run, scroll to the "Artifacts" section, and download the `architecture-diagrams` package.

For a more sophisticated setup, you could extend this workflow to automatically commit diagrams back to your repository, post them to Slack, or integrate them with your documentation system.
