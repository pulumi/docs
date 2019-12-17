---
title: Other
meta_desc: This page walks-through how you can modify the Pulumi CLI to support your own
           CI system or perhaps even update an existing one.
menu:
    userguides:
        parent: cont_delivery
        weight: 2

aliases:
- /docs/reference/cd-supporting-new-ci/
- /docs/console/continuous-delivery/other/
---

If Pulumi doesn't already support your CI/CD system, this guide
walks you though how to create a new CI/CD system for surfacing
data in the Pulumi Console.

## Overview

The Pulumi CLI already supports enhanced metadata for several popular CI/CD systems. We have tried to make it easy for contributors to add/update support for CI systems. This document walks-through how you can modify the Pulumi CLI to support your own CI system or perhaps even update an existing one.

The detection of metadata in a CI environment depends on some key environment variables that a CI system injects into the build environment of their build agents. The Pulumi CLI uses those environment variables to try and determine the values for the following properties:

- CI System Name
- Build Type
- Build URL
- Commit SHA
- PR Number
- Commit Message

The above metadata about your CI environment is then used to provide an enhanced experience in the [Pulumi Console](https://app.pulumi.com) when you look at your stack activity log. The metadata from your CI environment combined with the information about your Git repository allows us to provide links to things such as the Pull Request on github.com or the commit that triggered a PR build.

![A Stack update entry in the Pulumi Console](/images/docs/reference/supporting-new-ci/stack-update.png)

In order to add support for your CI system, you should be somewhat familiar in working with [Go](https://golang.org/).

## How Does It Work?

There are 2 parts to the CLI for it to be able to correctly detect the environment variables of a CI system.

1. Detecting in which CI system the Pulumi CLI is currently running
1. Detecting additional environment variables for a specific CI system

In the [`pulumi/pulumi`](https://github.com/pulumi/pulumi) repo the [`pkg/util/ciutil`](https://github.com/pulumi/pulumi/tree/master/pkg/util/ciutil) contains all of the logic necessary for the above. Every stack `preview` or `update` calls the functions exported from this package.

### Detecting The CI System

- Add an entry to the local `map` in [`detect.go`](https://github.com/pulumi/pulumi/blob/master/pkg/util/ciutil/detect.go) where all of the CI systems are registered.
- When you add the entry, you have two options, either use the `baseCI` as the CI System implementation or add a specific implementation that overrides the `DetectVars` function. More on this later in the next section.

For example, here's the `AppVeyor` entry.

```go
AppVeyor: baseCI{
		Name:            AppVeyor,
		EnvVarsToDetect: []string{"APPVEYOR"},
},
```

The `EnvVarsToDetect` is used by the `IsCI()` in [`systems.go`](https://github.com/pulumi/pulumi/blob/master/pkg/util/ciutil/systems.go), which iterates through the environment variables that a certain CI system is known to set in its build agents. Some CI systems set specific _values_ in certain environment variables, and in such cases you should use `EnvValuesToDetect`. An example for the latter is `Codeship`. See its entry in the `detectors` map.

### Detecting Additional Metadata About A CI Build

A CI build could have been triggered by a PR or a push build. In the case of the former, the linked PR number is useful so that the Pulumi Console can add a link to it in the source repo of your stack. Note that the detection is done on a best-effort basis. We support linking to the following Git-based version control systems:

- Atlassian Bitbucket
- Azure DevOps
- GitHub
- GitLab

All of the above source control systems have a concept of a PR, and PR builds, as well as push builds.

- Add a new file to the [`pkg/util/ciutil`](https://github.com/pulumi/pulumi/tree/master/pkg/util/ciutil) folder with the name of the CI system for which you are adding support.
- Define a new struct for the CI system and add `baseCI` to its definition. Refer to any of other pre-existing implementations, such as the [`travis.go`](https://github.com/pulumi/pulumi/blob/master/pkg/util/ciutil/travis.go) file.
- Implement the `DetectVars()` function. This is the function where you should construct a new instance of the `Vars` struct and set its properties accordingly.

That's it! Send us a new [PR](https://github.com/pulumi/pulumi/pulls) in the [`pulumi/pulumi`](https://github.com/pulumi/pulumi) repo with your addition. We would love to help you get that merged as soon as possible.

## Using A Fallback

If the CI system you are using is not currently detected by Pulumi, you can set the `PULUMI_CI_SYSTEM` environment variable. Then the following environment variables can be used to surface CI system metadata for an update.

- `PULUMI_CI_SYSTEM`
- `PULUMI_CI_BUILD_ID`
- `PULUMI_CI_BUILD_TYPE`
- `PULUMI_CI_BUILD_URL`
- `PULUMI_CI_PULL_REQUEST_SHA`

You can also find these variables in the [`generic.go`](https://github.com/pulumi/pulumi/blob/master/pkg/util/ciutil/generic.go) file in the [`pkg/util/ciutil`](https://github.com/pulumi/pulumi/tree/master/pkg/util/ciutil) folder.
