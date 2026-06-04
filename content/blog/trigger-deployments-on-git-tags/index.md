---
title: "Trigger Deployments on Git Tags"
date: 2026-06-04
draft: false
meta_desc: "Tie infrastructure deployments to your release tags. Push a version tag like v1.2.0 and let Pulumi Deployments run pulumi up automatically."
meta_image: meta.png
feature_image: feature.png
authors:
    - michael-fallihee
tags:
    - features
    - pulumi-cloud
    - announcements
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: "Pulumi Deployments can now trigger on git tag pushes. Push a version tag like v1.2.0 and Pulumi runs pulumi up automatically — across GitHub, GitLab, Bitbucket, Azure DevOps, and Custom VCS. Filter with glob patterns to deploy only the releases you care about."
    linkedin: "Many teams treat a git tag as the signal that a release is ready to ship. Pulumi Deployments now lets you act on that signal directly: configure tag-based triggers, push a version tag like v1.2.0, and Pulumi runs pulumi up automatically.\n\nTag triggers work across all five version control integrations — GitHub, GitLab, Bitbucket, Azure DevOps, and Custom VCS — and use the same glob-based filtering model as path filters, so you can deploy on every v* release while excluding pre-releases like v1.2.0-rc1.\n\nRead the announcement for how to set it up."
    bluesky: "Pulumi Deployments can now trigger on git tag pushes. Push a version tag like v1.2.0 and Pulumi runs pulumi up automatically — with glob-based tag filters so you only deploy the releases you choose."
---

A git tag is how many teams mark a release as ready. Pulumi Deployments can now act on that signal directly: configure a tag-based trigger, push a version tag like `v1.2.0`, and Pulumi automatically runs `pulumi up` for your stack. No extra pipeline glue, no manual click — your release tag *is* the deployment.

<!--more-->

## Why tags?

[Push to Deploy](/docs/deployments/deployments/using/triggers/#push-to-deploy) has long let you preview changes on a pull request and update a stack when commits merge to a branch. That branch-based model is a great fit for continuous delivery to shared development and QA environments, where every merge should flow straight through.

But promotion to production is often deliberate, not continuous. You merge throughout the day, then decide — separately — that a particular commit is the release. The conventional way to record that decision is a git tag: `v1.2.0`, `2026.06.0`, `release-2026-06-04`. Tagging is already part of most teams' release rituals.

Tag-based triggers connect that ritual to your infrastructure. Instead of wiring up a separate CI job to call the [Pulumi Deployments REST API](/docs/deployments/deployments/using/triggers/#rest-api) on a tag event, you configure the trigger once in your stack's deployment settings and let Pulumi handle the rest.

## How it works

Tag triggers are controlled by two settings on your stack's [deployment configuration](/docs/deployments/deployments/using/settings/):

- **Deploy on tag** — a toggle that enables running `pulumi up` when a matching tag is pushed.
- **Tag filters** — a list of glob patterns that decide which tag names qualify.

Tag filters use the same model as the [path filters](/docs/deployments/deployments/using/settings/#path-filtering) you may already know, except the patterns match against the tag name rather than changed file paths. A few examples:

- `v*` — deploy on any tag beginning with `v`, such as `v1.0.0` and `v2.3.1`.
- `v*` plus `!*-rc*` — deploy on release tags but skip release candidates like `v1.2.0-rc1`.
- `2026.*` — deploy on calendar-versioned releases such as `2026.06.0`.

Filters prefixed with `!` are exclusions, and an exclusion always wins over an include. With no filters configured and the toggle on, every tag push deploys. Deleting a tag never triggers a deployment.

When a tag push kicks off a deployment, Pulumi sets the `PULUMI_CI_TAG_NAME` environment variable to the tag name. Your pre-run commands or your Pulumi program can read it — for example, to stamp the release version onto a resource tag or an application config value.

## Works across every VCS integration

Tag triggers are available across all five version control integrations: [GitHub](/docs/integrations/version-control/github-app/), [GitLab](/docs/integrations/version-control/gitlab/), [Bitbucket](/docs/integrations/version-control/bitbucket/), [Azure DevOps](/docs/integrations/version-control/azure-devops-integration/), and [Custom VCS](/docs/integrations/version-control/custom-vcs/). For Custom VCS, send a webhook with the event type `tag_push` and a `tag` field, and the same filtering logic applies.

One note for existing GitLab users: GitLab integrations created before this feature did not subscribe to GitLab's tag push webhook events. To use tag triggers on a pre-existing GitLab integration, enable **Tag push events** on the existing group webhook in GitLab — there's no need to re-create the integration. New integrations subscribe automatically.

## Get started

You can configure tag triggers wherever you manage deployment settings today — the [Pulumi Cloud console](https://app.pulumi.com/signin), the [REST API](/docs/reference/cloud-rest-api/deployments/#patch-settings), or as code with the [`pulumiservice.DeploymentSettings`](/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource.

To try it out:

1. Open a stack's **Settings > Deploy** tab in the Pulumi Cloud console.
1. Enable **Deploy on tag** and add a tag filter such as `v*`.
1. Push a tag — `git tag v1.0.0 && git push origin v1.0.0` — and watch the deployment run.

For the full details, see the [deployment triggers](/docs/deployments/deployments/using/triggers/#deploying-on-git-tags) and [tag filtering](/docs/deployments/deployments/using/settings/#tag-filtering) documentation. We'd love to hear how you put tag-based deployments to work.
