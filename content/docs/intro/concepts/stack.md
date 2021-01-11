---
title: "Stacks"
meta_desc: An in depth look at Pulumi Stacks and their usage.
menu:
  intro:
    parent: concepts
    weight: 4

aliases: ["/docs/reference/stack/"]
---

Every Pulumi program is deployed to a **stack**. A stack is an isolated, independently [configurable]({{< relref "config" >}})
instance of a Pulumi program. Stacks are commonly used to denote different phases of development (such as **development**, **staging** and **production**) or feature branches (such as **feature-x-dev**, **jane-feature-x-dev**).

A project can have as many stacks as you need. By default, Pulumi creates a stack for you when you start a new project. The stack recognizes the current directory as the default name for your program.

## Create a stack {#create-stack}

To create a new stack, use `pulumi stack init stackName`. This creates an empty stack `stackName` and sets it as the *active* stack. The project that the stack is associated with is determined by finding the nearest `Pulumi.yaml` file.

The stack name must be unique within a project. Stack names may only contain alphanumeric characters, hyphens, underscores, or periods.

```bash
$ pulumi stack init staging
```

If you are using Pulumi in your organization, by default the stack will be created in your user account. To target the organization, name the stack using `orgName/stackName`:

```bash
$ pulumi stack init broomllc/staging
```

Fully qualified stack names also include the project name, in the form `orgName/projectName/stackName`, and this fully-qualified format is required in some contexts. In most contexts, the shorthands `orgName/stackName` or `stackName` are valid and use the default organization and the current project context.

Note that while stacks with applied configuration settings will often be accompanied by `Pulumi.<stack-name>.yaml` files, these files are not created by `pulumi stack init`. They are created and managed [with `pulumi config`]({{< relref "/docs/reference/cli/pulumi_config" >}}).

## Listing stacks

To see the list of stacks associated with the current project (the nearest `Pulumi.yaml` file), use `pulumi stack ls`.

```bash
$ pulumi stack ls
NAME                                      LAST UPDATE              RESOURCE COUNT
jane-dev                                  4 hours ago              97
staging*                                  n/a                      n/a
test                                      2 weeks ago              121
```

## Select a stack

The top-level `pulumi` operations `config`, `preview`, `update` and `destroy` operate on the *active* stack. To change the active stack, run `pulumi stack select`.

```bash
$ pulumi stack select jane-dev

$ pulumi stack ls
NAME                                      LAST UPDATE              RESOURCE COUNT
jane-dev*                                 4 hours ago              97
staging                                   n/a                      n/a
test                                      2 weeks ago              121
```

To select a stack that is part of an organization, use the fully-qualified stack name, either `orgName/stackName` or `orgName/projectName/stackName`:

```bash
$ pulumi stack select mycompany/prod

$ pulumi stack ls
NAME                                      LAST UPDATE              RESOURCE COUNT
mycompany/prod*                            4 hours ago              97
mycompany/staging                          4 hours ago              97
dev                                       n/a                      n/a
```

## Deploy a project

To deploy your project to the currently selected stack, run `pulumi up`. The operation uses the latest [configuration values]({{< relref "/docs/intro/concepts/config" >}}) for the active stack.

{{% notes "info"%}}
Your stack can distinguish between execution for `preview` versus for `update` by using [pulumi.runtime.isDryRun()]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi/runtime#isDryRun" >}}).
{{% /notes %}}

## View stack resources

To view details of the currently selected stack, run `pulumi stack` with no arguments. This displays the metadata, resources and output properties associated with the stack.

```bash
$ pulumi stack
Current stack is jane-dev:
    Last updated 1 week ago (2018-03-02 10:26:09.850357 -0800 PST)
    Pulumi version v0.11.0
    Plugin nodejs [language] version 0.11.0
    Plugin aws [resource] version 0.11.0

Current stack resources (3):
    TYPE                                             NAME
    pulumi:pulumi:Stack                              webserver-jane-dev
    aws:ec2/securityGroup:SecurityGroup              web-secgrp
    aws:ec2/instance:Instance                        web-server-www

Current stack outputs (2):
    OUTPUT                                           VALUE
    publicDns                                        ec2-18-218-85-197.us-east-2.compute.amazonaws.com
    publicIp                                         18.218.85.197

Use `pulumi stack select` to change stack; `pulumi stack ls` lists known ones
```

## Stack Outputs {#outputs}

A stack can export values as stack outputs. These outputs are shown during an update, can be easily retrieved with the Pulumi CLI, and are displayed in the Pulumi Console. They can be used for important values like resource IDs and computed IP addresses and DNS names.

Stack outputs can be viewed via `pulumi stack output` and are shown on the stack information page on app.pulumi.com.

### **JavaScript code**

```javascript
exports.publicDns = ...
exports.publicIp  = ...
```

### **CLI**

```bash
$ pulumi stack output
Current stack outputs (2):
    OUTPUT                                           VALUE
    publicDns                                        ec2-18-218-85-197.us-east-2.compute.amazonaws.com
    publicIp                                         18.218.85.197
```

The values of specific properties can also be retrieved directly, which is useful when writing scripts that use these output values.

```bash
$ pulumi stack output publicIp
18.218.85.197
```

The right-hand side of a stack export can be a regular value, an Output, or a Promise (effectively, a Promise is the same as an Input). The actual values are resolved at the end of `pulumi up`.

Stack exports are effectively JSON serialized, though quotes are removed when exporting strings.
For example, this program:

```typescript
pulumi.export("x", "hello")
pulumi.export("o", {'num': 42})
```

produces the following stack outputs:

```bash
$ pulumi stack output x
hello
$ pulumi stack output o
{"num": 42}
```

The full set of outputs can be rendered as JSON by using `pulumi stack output --json`:

```bash
$ pulumi stack output --json
{
  "x": "hello",
  "o": {
      "num": 42
  }
}
```

> Note: If you export an actual resource, it too will be JSON serialized. This usually isn’t what you want, especially because some resources are quite large. If you only want to export the resource’s ID or name, for example, just export those properties directly.

Stack outputs respect secret annotations and are encrypted appropriately. If a stack contains any secret values, their plaintext values will not be shown by default. Instead, they will be displayed as [secret]({{< relref "" >}}) in the CLI. Pass `--show-secrets` to `pulumi stack output` to see the plaintext value.

## Import and export a stack deployment

A stack can be exported to see the raw data associated with the stack. This is useful when manual changes need to be applied to the stack due to changes made in the target cloud platform that Pulumi is not aware of. The modified stack can then be imported to set the current state of the stack to the new values.

{{% notes "info"%}}
This is a powerful capability that subverts the usual way that Pulumi manages resources and ensures immutable and repeatable infrastructure deployments. Importing an incorrect stack specification could lead to orphaning of cloud resources or the inability to make future updates to the stack. Use care when using the import and export capabilities.
{{% /notes %}}

```bash
$ pulumi stack export --file stack.json

$ pulumi stack import --file stack.json
```

## Delete a stack

To delete a stack with no resources, run `pulumi stack rm`. Removing the stack will remove all stack history from pulumi.com and will delete the stack configuration file `Pulumi.<stack-name>.yaml`.

If a stack still has resources associated with it, they must first be deleted via `pulumi destroy`. This command uses the latest configuration values, rather than the ones that were last used when the program was deployed.

To force the deletion of a stack that still contains resources-potentially orphaning them-use `pulumi stack rm --force`.

## Stack tags

Stacks have associated metadata in the form of tags, with each tag consisting of a name and value. A set of built-in tags are automatically assigned and updated each time a stack is updated (such as `pulumi:project`, `pulumi:runtime`, `pulumi:description`, `gitHub:owner`, `gitHub:repo`, `vcs:owner`, `vcs:repo`, and `vcs:kind`). To view a stack's tags, run [`pulumi stack tag ls`]({{< relref "/docs/reference/cli/pulumi_stack_tag_ls" >}}).

{{% notes "info" %}}
Stack tags are only supported when logged into the [Pulumi Service backend]({{< relref "/docs/intro/concepts/state" >}}).
{{% /notes %}}

Custom tags can be assigned to a stack by running [`pulumi stack tag set <name> <value>`]({{< relref "/docs/reference/cli/pulumi_stack_tag_set" >}}) and can be used to customize the grouping of stacks in the [Pulumi Console](https://app.pulumi.com). For example, if you have many projects with separate stacks for production, staging, and testing environments, it may be useful to group stacks by environment instead of by project. To do this, you could assign a custom tag named `environment` to each stack. For example, running `pulumi stack tag set environment production` assigns a custom `environment` tag with a value of `production` to the active stack. Once you've assigned an `environment` tag to each stack, you'll be able to group by `Tag: environment` in the Pulumi Console.

As a best practice, custom tags should not be prefixed with `pulumi:`, `gitHub:`, or `vcs:` to avoid conflicting with built-in tags that are assigned and updated with fresh values each time a stack is updated.

Tags can be deleted by running [`pulumi stack tag rm <name>`]({{< relref "/docs/reference/cli/pulumi_stack_tag_rm" >}}).

## Stack References {#stackreferences}

Stack references allow you to access the outputs of one stack from another stack. [Inter-Stack Dependencies]({{< relref "organizing-stacks-projects#inter-stack-dependencies" >}}) allow one stack to reference the outputs of another stack.

To reference values from another stack, create an instance of the `StackReference` type using the fully qualified name of the stack as an input, and then read exported stack outputs by their name:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const pulumi = require("@pulumi/pulumi");
const other = new pulumi.StackReference("acmecorp/infra/other");
const otherOutput = other.getOutput("x");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
const other = new pulumi.StackReference("acmecorp/infra/other");
const otherOutput = other.getOutput("x");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi import StackReference

other = StackReference(f"acmecorp/infra/other")
other_output = other.get_output("x");
```

{{% /choosable %}}
{{% choosable language go %}}

```go
other, err := pulumi.NewStackReference(ctx, "acmecorp/infra/other", nil)
if err != nil {
    return err
}
otherOutput := other.GetOutput(pulumi.String("x"))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var other = new StackReference("acmecorp/infra/other");
var otherOutput = other.GetOutput("x");
```

{{% /choosable %}}

{{< /chooser >}}

Stack names must be fully qualified, including the organization, project, and stack name components, in the format `<organization>/<project>/<stack>`. For individual accounts, use your account name for the organization component.

To expand on this further, imagine you need to define a cluster's infrastructure in one project and consume it from another.
Perhaps one project, `infra`, defines a Kubernetes cluster and another, `services`, deploys
services into it. Let's further imagine you are doing this across three distinct environments: production, staging,
and testing. In that case, you will have six distinct stacks that pair up in the following ways:

* `mycompany/infra/production` provides the cluster used by `mycompany/services/production`
* `mycompany/infra/staging` provides the cluster used by `mycompany/services/staging`
* `mycompany/infra/testing` provides the cluster used by `mycompany/services/testing`

The way Pulumi programs communicate information for external consumption is by using stack exports. For example,
your infrastructure stack might export the Kubernetes configuration information needed to deploy into a cluster:

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

The challenge in this scenario is that the services project needs to ingest this output during deployment so that it can
connect to the Kubernetes cluster provisioned in its respective environment.

The Pulumi programming model offers a way to do this with its `StackReference` resource type. For example:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const k8s = require("@pulumi/kubernetes");
const pulumi = require("@pulumi/pulumi");
const env = pulumi.getStack();
const infra = new pulumi.StackReference(`mycompany/infra/${env}`);
const provider = new k8s.Provider("k8s", { kubeconfig: infra.getOutput("kubeConfig") });
const service = new k8s.core.v1.Service(..., { provider: provider });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";
const env = pulumi.getStack();
const infra = new pulumi.StackReference(`mycompany/infra/${env}`);
const provider = new k8s.Provider("k8s", { kubeconfig: infra.getOutput("kubeConfig") });
const service = new k8s.core.v1.Service(..., { provider: provider });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi import get_stack, ResourceOptions, StackReference
from pulumi_kubernetes import Provider, core

env = get_stack()
infra = StackReference(f"mycompany/infra/{env}")
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
    slug := fmt.Sprintf("mycompany/infra/%v", ctx.Stack())
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
        var cluster = new StackReference($"mycompany/infra/{Deployment.Instance.StackName}");
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

In the above example, you construct a stack reference to a specific stack in this project which has the same name
as your current stack (i.e. when deploying the "staging" stack of the above program, you reference the "staging" stack)
from the infra project. Once you have that resource, you can fetch the `kubeConfig` output variable with the `getOutput`
function. From that point onwards, Pulumi understands the inter-stack dependency for scenarios like cascading updates.
