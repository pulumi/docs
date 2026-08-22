---
title: "Best Practices for Versioning IDP Components with SemVer"
date: 2026-06-25
meta_desc: "Apply SemVer to Pulumi IDP components with release contracts, deprecation windows, upgrade paths, and policy checks that protect downstream stacks."
meta_image: meta.png
feature_image: feature.png
authors:
    - pablo-seibelt
tags:
    - components
    - platform-engineering
    - semver
social:
    twitter: |
        IDP components need release discipline.

        Use SemVer, deprecation windows, upgrade paths, and Pulumi policy checks to protect downstream stacks.
    linkedin: |
        Internal Developer Platform components become product APIs once teams depend on them.

        This guide covers SemVer best practices for Pulumi components, including release contracts, deprecation windows, upgrade paths, and policy checks.
    bluesky: |
        IDP components are product APIs.

        Version Pulumi components with SemVer, deprecation windows, upgrade paths, and policy checks.
---

Platform engineering teams use Pulumi components to codify organizational standards and provide golden paths for developers. Shared component versioning quickly becomes a platform-wide concern when many stacks depend on the same building blocks. Without a clear versioning strategy, a simple update to a shared component can trigger unexpected resource replacements or build failures across a stack estate.

Semantic Versioning (SemVer) provides a predictable framework for communicating the nature of changes to your users. When applied to Pulumi components, it helps platform teams innovate rapidly while giving application developers the confidence to adopt new versions at their own pace.

This post establishes a concrete versioning and release policy for shared components, so you can roll users forward with fewer surprises in downstream stacks. By the end, you will have a SemVer-based workflow for publishing, deprecating, and safely migrating Pulumi components.

<!--more-->

## The component contract

In the context of a `ComponentResource`, the "public API" consists of its input arguments and its output properties. However, Pulumi components have an additional layer of compatibility: the resource state.

A breaking change in a component isn't just a TypeScript type error. It's any change that forces a resource replacement when a user didn't expect one. Common breaking changes include:

1. Removing or renaming an input property.
1. Changing the type of an input property in a way that isn't backward compatible.
1. Renaming a child resource within the component (which changes its URN).
1. Changing a property on a child resource that forces its replacement.

Understanding this contract is the first step toward a predictable versioning workflow.

## Versioning state safely

SemVer communicates intent, but Pulumi still needs enough information to preserve existing resources. When you rename a component, rename a child resource, change a component type token, or move children under a different parent, use [aliases](/docs/iac/concepts/resources/options/aliases/) to tell Pulumi how the old URN maps to the new one.

Aliases are part of the migration plan, not just a code cleanup detail. Keep them until the stacks that used the old shape have been updated. Removing aliases too early can turn a safe rename into an unexpected replacement for teams that upgrade later.

## Trunk-based development and conventional commits

To automate versioning, start with a trunk-based workflow. All development happens on short-lived feature branches that merge into a single `main` branch.
By using [Conventional Commits](https://www.conventionalcommits.org/), you can encode the SemVer impact directly into your git history:

* `feat:` triggers a **minor** version bump (e.g., v1.1.0).
* `fix:` triggers a **patch** version bump (e.g., v1.0.1).
* `BREAKING CHANGE:` in the footer (or a `!` after the type) triggers a **major** version bump (e.g., v2.0.0).

## Automating the release

With a clean commit history, you can use tools like `semantic-release`, Changesets, Release Please, or custom GitHub Actions to automate the release process. When a PR merges to `main`, the automation should:

1. Determine the next version based on the commits since the last tag.
1. Update the `package.json` or equivalent metadata file.
1. Generate a `CHANGELOG.md` summarizing the changes.
1. Create a new git tag (e.g., `v1.2.0`).

## Publishing to the private registry

Once the tag is pushed and the package is configured for registry publishing, you can publish to the [Pulumi Private Registry](/docs/idp/concepts/private-registry/) with `pulumi package publish`. This makes the new version discoverable, and the registry generates API documentation from the package schema.

```bash
# Tag and push
git tag v1.2.0
git push origin v1.2.0

# Publish to the registry
pulumi package publish github.com/acme/cloud-bucket@1.2.0
```

## Consumer pinning and updates

Application developers should pin their component usage to a specific major version or a compatible version range. This protects them from breaking changes while allowing them to receive non-breaking features and fixes according to your organization's upgrade policy.

In a Pulumi program, this typically means pinning the package version in `package.json`, `requirements.txt`, or `go.mod`. For components consumed via the [Private Registry](/docs/idp/concepts/private-registry/), the registry itself helps manage these versions.

## Previews and policy checks

Treat every component upgrade as an infrastructure change, not just a dependency update. Run `pulumi preview` against representative stacks before promoting a new component version, and review any resource replacements the preview reports.

For high-risk components, add checks where the relevant upgrade metadata is visible to the workflow. CI can require migration notes for v2 adoption or block unapproved major-version jumps in dependency files. Pulumi Policies can then enforce preview-visible guardrails, such as requiring `protect` on tagged or critical resources and validating resource inputs that represent your component contract.

## Managing deprecations

Before releasing a breaking change, use deprecation warnings to give users a heads-up. You can use `pulumi.log.warn` within your component constructor to notify users during a `pulumi up`.

```typescript
if (args.oldProperty) {
    pulumi.log.warn("oldProperty is deprecated and will be removed in v2.0.0. Use newProperty instead.", this);
}
```

## Rolling out v2

When it's time for a major release, provide a clear migration guide. This guide should explain why the change was made and provide code snippets showing how to upgrade.

If the changes are significant, consider supporting both v1 and v2 in parallel for a transition period. This allows teams to migrate at different speeds without blocking the platform team's progress.

By combining SemVer with the Pulumi Private Registry, platform teams can transform their infrastructure components from static scripts into a living, evolving product that scales with the organization.
