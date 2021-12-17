---
title: "Organizational Patterns - A Single Infra Repo"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2021-12-17T05:46:04-06:00

# Draft posts are visible in development, but excluded from production builds.
# Set this property to `false` before submitting your post for review.
draft: false

meta_desc: In this first post of a series, we explore an important organizational pattern of using Pulumi - the centralized platform infrastructure repository.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png


authors:
    - matt-stratton

tags:
    - development-environment

---

Using Pulumi is more than just writing code and components. In addition to common software development practices, there are also a number of success patterns related to how your company or team builds and deploys Pulumi programs to successfully build, deploy, and manage your infrastructure and applications. In this first post of a series, I will explore one of these patterns - the centralized platform infrastructure repository.

<!--more-->

An emergent organizational pattern these days is that of a centralized "platform" team, which has various product and service teams (or squads) as internal customers. In this approach, the platform team takes responsibility for the tooling and infrastructure - if it's not directly product related, it usually falls under the responsibility of the platform team. The platform team provides functionality and platforms to be consumed by the product teams.

For many of the examples I'll be using to illustrate this pattern, I refer to a conversation I had recently with Jacob Foard, who is the Tech Lead for the Platform Team at [GreenPark Sports](https://greenparksports.com/). This pattern is used at GreenPark Sports, and he was very clear about the benefits of the pattern.

One of the key concepts to keep in mind is that when providing a platform, it is made up of more than just the compute and other resources provided by AWS, GCP, Azure, or even your own Kubernetes implementations. The platform also includes the infrastructure that is shared between the various teams, such as monitoring and observability tooling, version control/pipeline services, as well as secret and key management.

In this pattern, your main infrastructure repository is made up of directories for each product/service that your teams use, in addition to directories for each higher level shared service. Each of these directories is itself a Pulumi program. So it would look something like this:

```
├── bluth-apps
│   ├── apps
│   │   ├── apps.go
│   │   ├── bananastand.go
│   │   ├── suddenvalley.go
│   ├── main.go
│   ├── Pulumi.dev.yaml
│   └── Pulumi.prod.yaml
├── datadog
│   ├── main.go
│   └── Pulumi.prod.yaml
├── github
│   ├── main.go
│   └── Pulumi.prod.yaml
├── pkg
│   ├── datadog
│   ├── pagerduty
│   └── vault
└── .etc
```

In the above (fictional, but inspired by the GreenPark Sports pattern) example, the Bluth Company has two main services that are used in all of its environments ("Banana Stand" and "Sudden Valley"). The main `apps.go` file is the entry point that simply calls functions from each of the various apps to "set up" those apps, as well as the common infrastructure that an environment might require (networks, storage, etc). Note that the way you structure your code is up to you, and likely will vary depending upon the runtime for your particular Pulumi program, but this is the general idea.

Similarly, the `github` and `datadog` directories are Pulumi programs that are responsible for the "core" infrastructure for those services (perhaps creating roles, etc). The `pkg` directory is a directory that contains packages that are used by the other programs to implement that infrastructure. Again, the `pkg` convention is used by Go, but other runtimes will have a similar approach.

## Examples

These examples are not complete runnable code, but used to illustrate the pattern. While these examples are using Go, they are written in a way that is compatible with any language that supports the Pulumi language.

`main.go`

```go
package main

import (
    "github.com/bluthcompany/infra/bluth-apps/apps"
    "github.com/bluthcompany/infra/pkg/datadog"
    "github.com/bluthcompany/infra/pkg/github"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create the apps.
       apps.SetupApps(ctx, bananastand, suddenvalley)

        // Create the infrastructure.
        datadog.CreateInfrastructure(ctx)
        github.CreateInfrastructure(ctx)

        return nil
    })
}
```

`apps.go`

```go
package apps
import (
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func SetupApps(
    ctx *pulumi.Context,

    setupBananaStand(ctx)
    setupSuddenValley(ctx)

)
```

`bananastand.go`

```go
package apps
// imports, etc
func setupBananaStand(ctx *pulumi.Context) {
    // Create the banana stand.
}
```

## Setting up a new service in the platform repository

If a service/product team has a new service they want infrastructure for, they simply add a new `myapp.go` file to the `apps` directory for their service, and add it to the `apps.go` file to make sure it is called. This is then submitted as a pull request for the platform team to review.

One important part of this pattern is that the platform team does not want to be a "blocker" for the product and service teams. It's key to make sure that you have more than one person able to review and merge these pull requests, and to add sufficient testing into your CI/CD pipeline for this infrastructure repository.

## Variations on this pattern

In the fictional Bluth example, there is one Pulumi program that is used regardless of environment, and the different configurations are handled by the use of stacks. However, there are situations where you might have complex enough differences between your environments where the amount of conditionals you require in your code to handle this would make for very challenging maintenance and understanding of the code! This is the case with GreenPark Sports, so in their implementation, instead of a single `bluth-apps` directory at the root of the repo, you would instead have `bluth-prod`, `bluth-dev`, etc.

This approach does generate duplication of code, and it can provide challenges at scale, but it is up to you and your teams to determine the tradeoffs of the branching/conditional logic vs separate programs.

## Conclusion

This pattern works well depending upon the makeup of your teams and services. It is a pattern that facilitates collaboration between teams and focuses on having a central platform team that enables product teams, rather than getting in their way.

Watch for the next posts in this series, where we will dig into some other patterns as well!
