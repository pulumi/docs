---
title: Releases
meta_desc: A running log of major platform updates from the Pulumi team.

# Opt this section into JSON and RSS feeds (built in config/_default/config.yml).
# JSON -> /releases/index.json (layouts/releases/list.json)
# RSS  -> /releases/rss.xml    (layouts/releases/rss.xml)
outputs:
  - HTML
  - JSON
  - RSS

# A single, newest-first list of release-page entries. Each entry has a `type`:
#   - updates:   a lightweight month of items, rendered inline on the list page
#                as <details> disclosures. Each item: { title, description, url?, tier? }
#                — description is required.
#   - release:   a pointer to a full release. Everything else — the card's title,
#                description, and image, plus the feed's items (sourced from the
#                detail page's section cards: title, description, url, tier) — is
#                read from the detail page at `url`. Only `date` (for ordering)
#                and `url` live here, so there is nothing to hand-sync.
# The list page, JSON (/releases/index.json), and RSS (/releases/rss.xml) all
# render from this array, sorted by `date` descending (newest month first).
entries:
  - type: updates
    label: June 2026 Updates
    date: 2026-06-24
    items:
      - title: "Neo code reviews: AI code review built for infrastructure"
        description: "Neo reviews each pull request as an agent — reading the code, the preview plan, and the resulting infrastructure diff together — and posts inline findings on the affected lines."
        url: /blog/neo-code-reviews/
      - title: "Browse and publish private Terraform modules in the Pulumi Cloud registry"
        description: "Publish your existing Terraform and OpenTofu modules to the Pulumi Cloud private registry with the tooling you already use, and browse them in the console — a drop-in migration path from HCP Terraform."
        tier: Enterprise
      - title: "Dark mode for the docs"
        description: "😎 The Pulumi docs now offer a light, dark, and system theme toggle."
        url: /docs/
      - title: "Individual user authentication for GitHub Enterprise Server"
        description: "Self-hosted GitHub Enterprise operations now run as the individual user who triggered them, so pull requests, commits, and comments are attributed to that person and respect their permissions."
        url: /docs/integrations/version-control/github-app/#individual-user-authentication-for-github-enterprise-server
        tier: Business Critical
      - title: "One CLI for Pulumi ESC with pulumi env"
        description: "The standalone esc CLI is retiring in favor of pulumi env, so a single Pulumi CLI now manages your IaC, Deployments, and ESC environments."
        url: /docs/esc/
      - title: "Universal Search: a Cmd/Ctrl+K command palette for Pulumi Cloud"
        description: "A keyboard-first command palette (Cmd/Ctrl+K) jumps you to any stack, environment, resource, or member without leaving the page you're on."
      - title: "Trigger deployments from Git tags on any supported VCS"
        description: "Push a git tag to trigger a deployment, with optional glob filters, across GitHub, GitLab, Bitbucket, Azure DevOps, and Custom VCS."
        url: /blog/trigger-deployments-on-git-tags/
      - title: "Pulumi CLI v3.245–v3.248: pulumi logs ls/rm, stack new, richer do and neo"
        description: "June's CLI releases add pulumi logs ls/rm, rename stack init to stack new, and bring richer pulumi do and pulumi neo workflows."
        url: https://github.com/pulumi/pulumi/releases

  - type: release
    date: 2026-05-19   # for ordering; title, label, and feed items come from the detail page
    url: /releases/agentic-infrastructure-era/
---
