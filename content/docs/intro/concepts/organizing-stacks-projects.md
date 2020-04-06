---
title: Organizing Projects and Stacks
meta_desc: An overview of best practices when organization and structuring cloud projects and stacks.
menu:
  intro:
    parent: concepts
    weight: 5

aliases: ["/docs/reference/organizing-stacks-projects/"]
---

[Projects]({{< relref "project" >}}) and [stacks]({{< relref "stack" >}}) are intentionally flexible so that they can accommodate
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

Most users will start a monolithic structure, for a few good reasons

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

## Inter-Stack Dependencies {#inter-stack-dependencies}

Let's imagine that Acmecorp decides to define its cluster infrastructure in one project and consume it from another.
Perhaps one project, `infra`, defines the Kubernetes cluster and another, `services`, deploys
services into it. Let's further imagine we are doing this across three distinct environments, production, staging,
and testing. In that case, we'll have six distinct stacks, that pair up together:

* `acmecorp/infra/production` provides the cluster used by `acmecorp/services/production`
* `acmecorp/infra/staging` provides the cluster used by `acmecorp/services/staging`
* `acmecorp/infra/testing` provides the cluster used by `acmecorp/services/testing`

The way Pulumi programs communicate information for external consumption is by using stack exports. For example,
our infrastructure stack might export the Kubernetes configuration information needed to deploy into a cluster:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
exports.kubeConfig = ... a cluster's output property ...;
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
export const kubeConfig = ... a cluster's output property ...;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
pulumi.export("kubeConfig", ... a cluster's output property ...)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
ctx.Export("kubeConfig", /*...a cluster's output property...*/)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
class ClusterStack : Stack
{
    [Output] public Output<string> KubeConfig { get; set; }

    public ClusterStack()
    {
        // ... a cluster is created ...

        this.KubeConfig = ... a cluster's output property ...
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

The challenge here is that our services project needs to ingest this output during deployment so that it can
connect to the Kubernetes cluster provisioned in its respective environment.

The Pulumi programming model offers a way to do this with its `StackReference` resource type. For example:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const k8s = require("@pulumi/kubernetes");
const pulumi = require("@pulumi/pulumi");
const env = pulumi.getStack();
const infra = new pulumi.StackReference(`acmecorp/infra/${env}`);
const provider = new k8s.Provider("k8s", { kubeconfig: infra.getOutput("kubeConfig") });
const service = new k8s.core.v1.Service(..., { provider: provider });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";
const env = pulumi.getStack();
const infra = new pulumi.StackReference(`acmecorp/infra/${env}`);
const provider = new k8s.Provider("k8s", { kubeconfig: infra.getOutput("kubeConfig") });
const service = new k8s.core.v1.Service(..., { provider: provider });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi import get_stack, ResourceOptions, StackReference
from pulumi_kubernetes import Provider, core

env = get_stack()
infra = StackReference(f"acmecorp/infra/{env}")
provider = Provider("k8s", kubeconfig=infra.get_output("kubeConfig"))
service = core.v1.Service(..., ResourceOptions(provider=provider))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  "fmt"

  "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
  pulumi.Run(func(ctx *pulumi.Context) error {
    slug := fmt.Sprintf("acmecorp/%v/%v", ctx.Project(), ctx.Stack())
    stackRef, err := pulumi.NewStackReference(ctx, slug, nil)

    kubeConfig := stackRef.GetOutput(pulumi.String("kubeConfig"))
    // ...
    return nil
  }
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Kubernetes.Core.V1;

class AppStack : Stack
{
    public AppStack()
    {
        var cluster = new StackReference($"acmecorp/infra/{Deployment.Instance.StackName}");
        var kubeConfig = cluster.RequireOutput("KubeConfig").Apply(v => v.ToString());
        var provider = new Provider("k8s", new ProviderArgs { KubeConfig = kubeConfig });
        var options = new ComponentResourceOptions { Provider = provider };
        var service = new Service(..., ..., options);
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

The `StackReference` constructor takes as input a string of the form `<organization>/<project>/<stack>`, and lets
you access the outputs of that stack.

In this above example, we construct a stack reference to a specific stack in this project which has the same name
as our current stack (i.e. when deploying the "staging" stack of the above program, we reference the "staging" stack)
from the infra project. Once we have that resource, we can fetch the `kubeConfig` output variable with the `getOutput`
function.  From that point onwards, Pulumi understands the inter-stack dependency for scenarios like cascading updates.

## Aligning to Git Repos

Because Pulumi is a natural choice for enabling GitOps-style continuous deployment, many users opt to align their
project structure to their Git repo structure. Organizations that prefer mono-repos often prefer monolithic
project structures, and organizations that prefer fine-grained repos tend to prefer micro-project structures.

This alignment is not a requirement, of course. We have many users who have chosen to have multiple projects in a
single Git repo -- or the reverse, using Git submodules, they might deploy code from multiple Git repos in a single
Pulumi project. However, most users find that a close alignment between Git repo structure and Pulumi project
structure enables seamless continuous deployment.

In this model, there is a rough correspondence between a Git repo and a Pulumi project, and a Git branch and
its associated Pulumi stack. Please read more about
[how these mapping are maintained here]({{< relref "/docs/guides/continuous-delivery" >}}).

## Tagging Stacks

Stacks have associated metadata in the form of name/value tags. You can assign custom tags to stacks (when logged into the [Pulumi Service backend]({{< relref "state" >}})) to customize how stacks are listed in the [Pulumi Console](https://app.pulumi.com). For example, if you have many projects with separate stacks for production, staging, and testing environments, it may be useful to group stacks by environment instead of by project. To do this, you could assign a custom `environment` tag to each stack, assigning a value of `production` to each production stack, `staging` to each staging stack, etc. Then in the Pulumi Console, you'll be able to group stacks by `Tag: environment`. Please read more about [how to manage stack tags here]({{< relref "stack#stack-tags" >}}).

## Examples

See also the use of multiple projects and stacks in [Kubernetes the Prod Way]({{< relref "/docs/guides/crosswalk/kubernetes" >}}), which contains a tutorial, reference architecture, and collection of prod-first code
examples that demonstrate industry best-practices for **using Kubernetes** in contexts where an
**organization of people** must ship **production applications.**
