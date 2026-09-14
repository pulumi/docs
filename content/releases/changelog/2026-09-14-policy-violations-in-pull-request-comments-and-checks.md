---
title: "Policy violations now appear in pull request comments and checks"
date: 2026-09-14
meta_desc: "Pulumi Cloud now lists policy pack violations in pull request comments and commit checks on GitHub, GitLab, Bitbucket, and Azure DevOps."
authors:
    - michael-fallihee
---

When a preview or update runs with a policy pack, the pull request comment and commit check that Pulumi Cloud posts now include a **Policy violations** section. It shows how many mandatory and advisory violations were found, then lists each one with its policy pack, policy name, the resource it flagged, and the violation message. Developers can now view why a preview failed from their pull request without opening Pulumi Cloud.

The section appears on GitHub, GitLab, Bitbucket, and Azure DevOps, for previews as well as updates. Pull request comments list up to 40 violations; check run details include the full list.

See the [version control integrations](/docs/integrations/version-control/) and [policy](/docs/discovery-governance/policy/) docs for details.
