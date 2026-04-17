---
title: Repository Strategy for Pulumi Packages
meta_desc: How to structure Git repositories when publishing Pulumi packages — covering versioning, cohesion, and monorepo trade-offs.
menu:
  iac:
    name: Repository Strategy
    parent: iac-guides-packages
    weight: 40
---

Effectively developing and managing [Pulumi packages](/docs/iac/concepts/packages/) is key to building your organization's platform with Pulumi. A package is the unit of versioning and distribution; the [components](/docs/iac/concepts/components/) inside it inherit the package's version. This guide describes Pulumi's recommended strategies for structuring the Git repositories you use to publish packages. Following these practices improves the reliability, maintainability, and delivery speed of the packages your organization builds and consumes.

## How Pulumi packages are versioned

Pulumi packages come in two flavors, and each is versioned and released differently. Understanding the release artifact for each flavor is the foundation for the repository-layout advice in this guide.

### Source-based packages

A [source-based plugin package](/docs/iac/guides/building-extending/components/packaging-components/#source-based-plugin-packages) is distributed as source code in a Git repository. The package's version is the Git tag on that repository. Publishing to the Pulumi IDP [Private Registry](/docs/idp/concepts/private-registry/) is a two-step flow, typically performed by a CI/CD pipeline that runs on tag:

1. Apply a semver Git tag (for example, `v1.2.3`) to the repository.
1. Run [`pulumi package publish`](/docs/iac/cli/commands/pulumi_package_publish/) to send the package metadata to Pulumi Cloud and place the package in the Private Registry. This step often runs automated tests before publishing.

Semver-tagged releases are only required for publishing to the Private Registry. Source-based packages referenced directly from a `Pulumi.yaml` file can use any Git ref (tag, branch, or commit), regardless of whether it is a valid semantic version.

### Executable-based packages

An [executable-based plugin package](/docs/iac/guides/building-extending/components/packaging-components/#executable-based-plugin-packages) is distributed as a pre-built plugin binary, typically alongside per-language SDKs published to package feeds (npm, PyPI, NuGet, Maven, the Go module proxy, or private equivalents). The package's version is the version embedded in the published binary and SDKs. Pulumi Cloud customers can additionally publish the package to the Private Registry via `pulumi package publish`. Releases are produced by a CI/CD pipeline that builds the plugin, generates the SDKs, and pushes everything to the relevant feeds.

In both cases, the released artifact is a single, semantically-versioned Pulumi package. That fact drives the central rule of repository strategy below.

## One repository per package

**A repository should contain exactly one Pulumi package**, regardless of package type. The package is the unit of versioning and release, so a repository that contains multiple packages either has to release them in lockstep (forcing unrelated work to share a version) or invent per-package release tooling that fights the way Pulumi naturally consumes packages. A 1:1 repository-to-package mapping keeps git tags, release artifacts, and version history aligned.

Multiple components inside a single package, on the other hand, are fine and expected — the components ship together at the package's version. The question to focus on is therefore not "how many components per repository?" but "which components belong together in the same package?"

## Pulumi's recommended approach

To keep package versioning intuitive as your usage of Pulumi grows, we recommend:

1. Define exactly one package per repository.
1. Group a cohesive set of components together inside that package.
1. Use multiple repositories — one per package — to manage the distinct packages your organization publishes.

The importance of these principles grows as your organization's adoption of Pulumi grows.

### What cohesive means in practice

By "cohesive," we mean components that are likely to be used together and therefore likely to change together. A good reference point is the [Amazon EKS package](https://www.pulumi.com/registry/packages/eks/) in the Pulumi Registry: it bundles a managed Kubernetes cluster component along with the supporting components needed to secure and operate it. These components are almost always used together and tend to evolve together, so a shared semantic version makes sense.

### Example: cohesive components in a single package

Suppose your organization has an `EksCluster` component and an `EksIam` component that represents AWS credentials for workloads running on the cluster. `EksCluster` consumes one or more `EksIam` instances internally to set up system-level processes, and you also expose `EksIam` to application teams so their pods can be granted access to AWS resources like S3 buckets.

Because `EksIam` is meaningful only in the context of an EKS cluster, and the two components will typically evolve together, group them in the same repository as a single package. One `PulumiPlugin.yaml` at the repository root defines the package, and the components live alongside it:

```text
eks-platform/
├── PulumiPlugin.yaml
├── components/
│   ├── EksCluster/
│   └── EksIam/
└── ...
```

By contrast, an unrelated component — say, a `StaticWebsite` component used by frontend teams — has no reason to share a release cadence with your EKS components and belongs in its own repository as a separate package.

## Challenges of bundling many components into a single package

It is technically possible to use a single monorepo containing one giant package for all of your organization's components, but Pulumi does not recommend this approach: it forfeits meaningful semantic versioning, which is how consumers know whether a given change is a bug fix, a new feature, or a breaking change.

When unrelated components share a package, every release of the package versions every component the same way, regardless of whether each component changed. This violates semver: consumers can no longer use the package version to tell whether a component they care about has actually changed.

Consider this sequence with two unrelated components, `ComponentA` and `ComponentB`, in the same package:

1. The package is released at `v1.0.0`. Both components are at `v1.0.0`.
1. An enhancement is made to `ComponentA`. The package is released at `v1.1.0`, even though `ComponentB` is unchanged.
1. A breaking change is made to `ComponentB`. The package is released at `v2.0.0`, even though `ComponentA` had no breaking change — or any change at all.

The version number is now decoupled from the actual evolution of each component, and consumers lose the signal that semver is meant to provide. Splitting unrelated components across separate, right-sized packages preserves the semver contract and keeps the upgrade story honest for the platform teams that consume your packages.

## Summary

A thoughtful repository strategy is essential for managing Pulumi packages at scale. Group cohesive components into one package per repository so they version and release together; use separate repositories for unrelated component groups so each package can evolve at its own pace. For details on the publishing mechanics, see [Publishing packages](/docs/iac/guides/building-extending/packages/publishing-packages/).
