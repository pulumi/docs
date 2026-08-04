---
title: Learn Pulumi
linktitle: Learn
meta_desc: Learn Pulumi with hands-on examples, guided video courses, live workshops, and tutorials, from your first stack to managing infrastructure at scale.
description: Hands-on examples, guided video courses, live workshops, and tutorials to take you from your first stack to managing your whole infrastructure estate.

# Two large cards at the top of the page. An absolute href is treated as
# external; the image is optional and the card renders without it.
spotlight:
    - title: Dev Hub
      description: Hands-on tutorials, ready-to-run templates, and example programs you can clone and deploy. Search by cloud, language, or use case.
      image: /images/learn/dev-hub.svg
      href: /dev-hub/
      cta: Browse the Dev Hub
    - title: Pulumi Academy
      description: Guided video courses taught by the Pulumi team, covering everything from infrastructure as code fundamentals to secrets management and platform engineering.
      image: /images/learn/academy.svg
      href: https://academy.pulumi.com
      cta: Start a course

# The "For humans" / "For agents" pair. Drop the `agents` key to render the
# humans card on its own.
new_to_pulumi:
    title: New to Pulumi
    description: Install the CLI, pick your cloud, and deploy your first stack.
    humans:
        label: For humans
        cta: Get started
        href: /docs/get-started/
        clouds:
            - label: AWS
              logo: /logos/tech/aws.svg
              href: /docs/iac/get-started/aws/
            - label: Azure
              logo: /logos/tech/azure.svg
              href: /docs/iac/get-started/azure/
            - label: Google Cloud
              logo: /logos/tech/gcp.svg
              href: /docs/iac/get-started/gcp/
            - label: Kubernetes
              logo: /logos/tech/k8s.svg
              href: /docs/iac/get-started/kubernetes/
    agents:
        label: For agents
        description: Paste this into Claude Code, Cursor, Codex, or whichever coding agent you already use.
        prompt: Fetch https://www.pulumi.com/onboard.md and follow its instructions to get me started with Pulumi.
        prompt_label: Copy prompt
        links:
            - label: Agent Skills
              href: /docs/ai/skills/
            - label: Pulumi MCP server
              href: /docs/ai/mcp-server/

# Upcoming events fill the grid first; `on_demand` slugs fill the remainder. A
# slug that no longer resolves is skipped and back-filled with the most recent
# recording, so the grid is always `count` cards.
events:
    title: Workshops and events
    count: 6
    on_demand:
        - from-zero-to-production-in-kubernetes
        - infrastructure-as-code-google-cloud
        - getting-started-with-iac-on-aws-python
        - multi-service-application-with-azure-container-apps
        - day-2-autonomous-infrastructure-management
        - getting-started-with-infrastructure-agents

# Ordered slugs from data/blog_series.yml, beginner-first. Capped at 4.
series:
    title: Blog series
    slugs:
        - kubernetes-getting-started
        - iac-best-practices
        - cloud-systems
        - platform-engineering-pillars

tutorials:
    title: Latest tutorials
    count: 3
---
