---
title: Learn Pulumi
linktitle: Learn
meta_desc: Learn Pulumi with hands-on examples, video lessons, live workshops, and tutorials, from your first stack to managing infrastructure at scale.
description: Hands-on examples, video lessons, live workshops, and tutorials to take you from your first stack to managing your whole infrastructure estate.

# Two large cards at the top of the page. An absolute href is treated as
# external; the image is optional and the card renders without it.
spotlight:
    - title: Dev Hub
      description: Hands-on tutorials, ready-to-run templates, and example programs you can clone and deploy. Search by cloud, language, or use case.
      image: /images/learn/dev-hub.svg
      href: /dev-hub/
      cta: Browse the Dev Hub
    - title: Pulumi Academy
      description: Learn by watching. Video lessons walk through Pulumi concepts step by step, at your own pace.
      image: /images/learn/academy.svg
      href: https://academy.pulumi.com
      cta: Start watching

# The "For humans" / "For agents" pair. Drop the `agents` key to render the
# humans card on its own.
new_to_pulumi:
    title: New to Pulumi?
    humans:
        label: For humans
        description: Install the CLI, pick your cloud, and deploy your first stack.
        cta: Get started
        href: /docs/get-started/
        # Icon-only marks (the square 32x32 variants), not the wordmark SVGs, so
        # the tiles stay compact.
        clouds:
            - label: AWS
              logo: /logos/tech/aws-logo.svg
              href: /docs/iac/get-started/aws/
            - label: Azure
              logo: /logos/tech/azure-logo.svg
              href: /docs/iac/get-started/azure/
            - label: Google Cloud
              logo: /logos/tech/gcp-logo.svg
              href: /docs/iac/get-started/gcp/
            - label: Kubernetes
              logo: /logos/tech/kubernetes.svg
              href: /docs/iac/get-started/kubernetes/
    agents:
        label: For agents
        description: Paste this into Claude Code, Cursor, Codex, or whichever agent you already use.
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
    count: 4
---
