---
title: Organizing Projects and Stacks
meta_desc: An overview of best practices when organizing and structuring cloud projects and stacks.
menu:
  userguides:
    name: Organizing Projects and Stacks
    weight: 8

aliases: [
  "/docs/reference/organizing-stacks-projects/",
  "/docs/intro/concepts/organizing-stacks-projects/"
]
---

[Projects]({{< relref "/docs/intro/concepts/project" >}}) and [stacks]({{< relref "/docs/intro/concepts/stack" >}}) are intentionally flexible so that they can accommodate
diverse needs across a spectrum of team, application, and infrastructure scenarios. This is very much like how Git
repos work and, much like Git repos, there are varying approaches to organizing your code within them. That said,
there are some clear best practices that, when followed, will ensure Pulumi works seamlessly for your situation. This
article describes some of the most common approaches and when to choose one over another.

## Tradeoffs

Everything described below is on a spectrum of tradeoffs. Remember that each project is a collection of code,
and that each stack is a unit of deployment. Each stack has its own separate configuration and secrets, role-based access controls (RBAC) and policies, and concurrent deployments.

## Monolithic

It's very common to start with a _monolithic_ project/stack structure. In this model, a single project defines
the infrastructure and application resources for an entire vertical service.

Each stack typically corresponds to a distinct _environment_ for that service, such as production, staging, and many
testing and development instances. There might even be multiple environments within each of these dimensions, such as
a production environment in each of the US east coast, west coast, Europe, and Asia.

Most users will start a monolithic structure, for a few good reasons:

* **Simplicity.** Having a single project and collection of stacks is, quite simply, the easiest thing you could
  possibly do. Pulumi diffs edits to your application and infrastructure code, and so this approach leaves the
  hard work of doing incremental deployments and tracking dependencies to the Pulumi engine.

* **Versioning.** By placing all code in one project, it's easier to share and version logic within your project.
  Of course, Pulumi supports package managers, so sharing across projects is also possible, but it entails dealing
  with packages which means introducing a loosely-coupled versioning boundary with distinct update cadences.

* **Agility.** All of the above means that using a monolithic approach will almost always lead to the best
  productivity and therefore agility. For small projects or teams, this is usually the right place to start.

Although a monolithic structure is where most users begin their Pulumi journey, we find that most will ultimately
migrate to a finer grained decomposition of projects and stacks.

## Micro-Stacks

At the other end of the spectrum is a pattern we call _micro-stacks_. This is equivalent to microservices,
only in project and stack form. In this model, a project is broken into separately managed smaller projects, often across
different dimensions. This approach has several advantages:

* **Independence.** Although Pulumi can diff changes and make only those updates mandated by a code edit,
  certain projects sometimes deploy at radically different cadences and it makes sense to enforce this separation
  in the project structure. For instance, a service that revs every day may not be appropriate to live in the same project as
  critical infrastructure that changes infrequently and which demands intense scrutiny whenever it does.

* **Security.** In large organizations, it's important to use RBAC to secure access to individual aspects
  of your cloud infrastructure and applications. Perhaps you want to ensure your DevOps Architect is the only
  person who can approve changes to fundamental networking and clustering infrastructure, for example.

* **Complexity and Performance.** For many real-world services, there are a multitude of build artifacts. This
  includes traditional software builds (in Java, .NET, C++, etc), Docker image builds, and serverless function
  packaging. Putting all of these in one place may increase build times unless a hermetic build system with
  excellent caching has been used (and, even then, caching across CI/CD machines can be difficult). Breaking apart
  pieces that can be built independently can increase agility and improve performance, particularly when they
  evolve at different rates and/or are managed by different teams.

Here are a few, non-exhaustive, examples, of how one might go about splitting up a monolithic project structure:

* Each micro-service in your architecture might get its own project.

* Application container images may be rebuilt and published independent of infrastructure projects.

* Similarly, application concepts like containers and serverless functions may be deployed independently.

* Core, low-level infrastructure -- like networks and cluster orchestrators -- may be independent from other
  infrastructure and applications resources.

* You may have one or more data tiers that are deployed and independently backed up.

Even with this alternative breakdown, it's likely your stack structure will mirror that described earlier. For
each project, you are apt to have multiple environments such as production, staging, testing, etc. And, indeed,
you may have inter-dependencies between your stacks -- something that Pulumi supports in a first-class manner.

## Aligning to Git Repos

Because Pulumi is a natural choice for enabling GitOps-style continuous deployment, many users opt to align their
project structure to their Git repo structure. Organizations that prefer mono-repos often prefer monolithic
project structures, and organizations that prefer fine-grained repos tend to prefer micro-project structures.

This alignment is not a requirement, of course. We have many users who have chosen to have multiple projects in a
single Git repo -- or the reverse, using Git submodules, they might deploy code from multiple Git repos in a single
Pulumi project. However, most users find that a close alignment between Git repo structure and Pulumi project
structure enables seamless continuous deployment.

In this model, there is a rough correspondence between a Git repo and a Pulumi project, and a Git branch and
its associated Pulumi stack. Read more about
[Continuous Delivery]({{< relref "/docs/guides/continuous-delivery" >}}).

## Tagging Stacks

Stacks have associated metadata in the form of name/value tags. You can assign custom tags to stacks (when logged into the [Pulumi Service backend]({{< relref "/docs/intro/concepts/state" >}})) to customize how stacks are listed in the [Pulumi Service](https://app.pulumi.com). For example, if you have many projects with separate stacks for production, staging, and testing environments, it may be useful to group stacks by environment instead of by project. To do this, you could assign a custom `environment` tag to each stack, assigning a value of `production` to each production stack, `staging` to each staging stack, etc. Then in the Pulumi Service, you'll be able to group stacks by `Tag: environment`. For more information, see [Stack tags]({{< relref "/docs/intro/concepts/stack#stack-tags" >}}).

## Examples

### Monorepo with base infrastructure project

Let's build an example of an organizational setup that leverages several different approaches to provide the most functionality and flexibility possible.

We start with a central base "infrastructure" project, which contains things that are common across multiple services (or perhaps even your entire organization!). This project can include resources like Azure Resource Groups or AWS VPCs.

Within this project, we create stacks for each unique configuration (often times stacks are related to SDLC environments like dev, staging, and production). These stacks are often deployed independently of each other and are often deployed in different regions. To use a metaphor, our Pulumi program code defines the shape of a dial, and the configuration in the different stack configuration files (e.g., `Pulumi.dev.yaml`, `Pulumi.staging.yaml`, `Pulumi.prod.yaml`) defines an actual dial setting. These "dial settings" might include things like subscription IDs, regions, etc. that are specific to that environment.

This project looks a bit like this:

```
├─ infrastructure
  ├── main.go
  ├── Pulumi.dev.yaml
  ├── Pulumi.staging.yaml
  └── Pulumi.prod.yaml
```

![A diagram showing how the different stacks in a project overlay with the program](img/infra-project.jpg)

Now that we have our base infrastructure, we can create a separate Pulumi project per application or service for each one's deployment and configuration that will include all the resources that the service needs, which are not provided by the base infrastructure project.

These projects can be part of the [same monorepo as the infrastructure project](https://www.pulumi.com/blog/organizational-patterns-infra-repo/), or they can be separate repos, depending upon your organizational needs. One of the advantages to keeping the infrastructure project in a separate repo/project is that there is likely a limited number of users we want to be able to deploy these things; not every individual team needs to be able to do this. In this example, we will use a monorepo, however.

Our example service is made up of an API and a database (RDS, CosmosDB, etc.). Our Pulumi program for the project defines the resources for the API and the database, and it can also deploy the actual code, as well. When we add our example service, our monorepo starts to look like this:

```
├── infrastructure
│   ├── main.go
│   ├── Pulumi.dev.yaml
│   ├── Pulumi.staging.yaml
│   └── Pulumi.prod.yaml
├── myApp
│   ├── main.go
│   ├── Pulumi.dev.yaml
│   ├── Pulumi.staging.yaml
│   └── Pulumi.prod.yaml
└── .etc
```

It's generally a good practice to keep our projects on the smaller side as this helps reduce the effect and impact of a deployment. If you have applications that require different rates of change, it may be useful to split them up into separate repos, aka micro-stacks.

As we consider making our approach even more accessible and robust across teams, we bring in the idea of [Component Resources]({{< relref "/docs/intro/concepts/resources/components" >}}), which are a way to group affiliated resources together according the standard practices of the organization.

Back to our example, our service needs a database and a subnet (or other networking). We can template these resources by creating a component resource, which abstracts these details away from the rest of the program. So now, any time someone needs to use Pulumi to add a standard application, they can call a resource called `Application` with its associated parameters (e.g., the container, parcel, folder). Behind the scenes, everything is being set up according to your organization's standards.

![A diagram showing how the different stacks in a project overlay with the program](img/application-project.jpg)

These component resources can be packaged up and stored alongside all of your other package management, so consumers in your organization can access them like any other library or package. If we want to add component resources to our monorepo example, it will look like this:

```
├── infrastructure
│   ├── main.go
│   ├── Pulumi.dev.yaml
│   └── Pulumi.prod.yaml
├── myApp
│   ├── main.go
│   ├── Pulumi.dev.yaml
│   ├── Pulumi.staging.yaml
│   └── Pulumi.prod.yaml
├── pkg
│   └──application
│     └── app.go
└── .etc
```

### Other examples

See also the use of multiple projects and stacks in [Crosswalk for Kubernetes]({{< relref "/docs/guides/crosswalk/kubernetes" >}}), which contains a tutorial, reference architecture, and collection of prod-first code examples that demonstrate industry best-practices for using Kubernetes in contexts where an organization of people must ship production applications.
