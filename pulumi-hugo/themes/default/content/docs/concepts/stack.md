---
title_tag: "Stacks | Pulumi Concepts"
meta_desc: Every Pulumi program is deployed to a stack and a project can have as many stacks as you need. Learn more about Pulumi stacks and how to use them.
title: Stacks
h1: Stacks
menu:
  concepts:
    weight: 2
aliases:
- /docs/reference/stack/
- /docs/tour/programs-exports/
- /docs/intro/concepts/stack/
---

Every Pulumi program is deployed to a _stack_. A stack is an isolated, independently [configurable](/docs/concepts/config/)
instance of a Pulumi program. Stacks are commonly used to denote different phases of development (such as `development`, `staging`, and `production`) or feature branches (such as `feature-x-dev`).

A project can have as many stacks as you need. By default, Pulumi creates a stack for you when you start a new project using the `pulumi new` command.

## Create a stack {#create-stack}

To create a new stack, use `pulumi stack init stackName`. This creates an empty stack `stackName` and sets it as the *active* stack. The project that the stack is associated with is determined by finding the nearest `Pulumi.yaml` file.

The stack name must be unique within a project. Stack names may only contain alphanumeric characters, hyphens, underscores, or periods.

```bash
$ pulumi stack init staging
```

The stack name is specified in one of the following formats:

1. `stackName`: Identifies the stack `stackName` in the current user account or default organization, and the project specified by the nearest `Pulumi.yaml` project file.
1. `orgName/stackName`: Identifies the stack `stackName` in the organization `orgName`, and the project specified by the nearest `Pulumi.yaml` project file.
1. `orgName/projectName/stackName`: Identifies the stack `stackName` in the organization `orgName` and the project `projectName`.  `projectName` must match the project specified by the nearest `Pulumi.yaml` project file.

{{% notes type="info" %}}
For [self-managed backends](/docs/concepts/state#using-a-self-managed-backend), the `orgName` portion of the stack name must always be the constant value `organization`.

Additionally, backends initialized with a Pulumi CLI older than v3.61.0 support only the first format (`stackName`). You can upgrade these to support the other formats with the `pulumi state upgrade` command. See [*State > Scoping*](/docs/concepts/state/#scoping) for more details.
{{% /notes %}}

Given the stack `my-org/my-project/dev`, the following are  all equivalent if the current organization is `my-org` and the current project is `my-project`:

```
my-org/my-project/dev
my-org/dev
dev
```

In some contexts, stack names will be presented in their fully-qualified format (`orgName/projectName/stackName`) even if provided using shorthand (`stackName` or `orgName/stackName`) as input.

{{% notes type="info" %}}
While stacks with applied configuration settings will often be accompanied by `Pulumi.<stack-name>.yaml` files, these files are not created by `pulumi stack init`. They are created and managed with [`pulumi config`](/docs/cli/commands/pulumi_config/). For information on how to populate your stack configuration files, see [Configuration](/docs/concepts/config/).
{{% /notes %}}

## Listing stacks

To see the list of stacks associated with the current project (the nearest `Pulumi.yaml` file), use `pulumi stack ls`.

```bash
$ pulumi stack ls
NAME                                      LAST UPDATE              RESOURCE COUNT
jane-dev                                  4 hours ago              97
staging*                                  n/a                      n/a
broomellc/test                            2 weeks ago              121
```

Stack names in the listing will be partially qualified if they are associated with an organization or project different from the default for the context.

## Select a stack

The top-level `pulumi` operations `config`, `preview`, `update` and `destroy` operate on the *active* stack. To change the active stack, run `pulumi stack select`.

```bash
$ pulumi stack select jane-dev

$ pulumi stack ls
NAME                                      LAST UPDATE              RESOURCE COUNT
jane-dev*                                 4 hours ago              97
staging                                   n/a                      n/a
broomellc/test                            2 weeks ago              121
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

## Generate an update plan

{{% notes type="warning" %}}
[Update plans](/docs/concepts/plans/) are currently in experimental preview and will only show up in `--help` if the environment variable `PULUMI_EXPERIMENTAL` is set to `true`.
{{% /notes %}}

To preview an update of the currently selected stack and save that plan run `pulumi preview --save-plan=plan.json`. The operation uses the latest [configuration values](/docs/concepts/config/) for the active stack.

{{% notes type="info"%}}
Your program code can distinguish between execution for `preview` and `update` operations by using [pulumi.runtime.isDryRun()](/docs/reference/pkg/nodejs/pulumi/pulumi/runtime#isDryRun).
{{% /notes %}}

## Update a stack

To update the currently selected stack, run `pulumi up`. If you saved a plan from a preview you can pass that in to constrain the update to only doing what was planned with `pulumi up --plan=plan.json`. The operation uses the latest [configuration values](/docs/concepts/config/) for the active stack.

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

## Stack tags

Stacks have associated metadata in the form of tags, with each tag consisting of a name and value. A set of built-in tags are automatically assigned and updated each time a stack is updated (such as `pulumi:project`, `pulumi:runtime`, `pulumi:description`, `gitHub:owner`, `gitHub:repo`, `vcs:owner`, `vcs:repo`, and `vcs:kind`). To view a stack's tags, run [`pulumi stack tag ls`](/docs/cli/commands/pulumi_stack_tag_ls).

{{% notes "info" %}}
Stack tags are only supported with the [Pulumi Cloud backend](/docs/concepts/state/).
{{% /notes %}}

Custom tags can be assigned to a stack by running [`pulumi stack tag set <name> <value>`](/docs/cli/commands/pulumi_stack_tag_set) and can be used to customize the grouping of stacks in the [Pulumi Cloud](https://app.pulumi.com). For example, if you have many projects with separate stacks for production, staging, and testing environments, it may be useful to group stacks by environment instead of by project. To do this, you could assign a custom tag named `environment` to each stack. For example, running `pulumi stack tag set environment production` assigns a custom `environment` tag with a value of `production` to the active stack. Once you've assigned an `environment` tag to each stack, you'll be able to group by `Tag: environment` in the Pulumi Cloud.

As a best practice, custom tags should not be prefixed with `pulumi:`, `gitHub:`, or `vcs:` to avoid conflicting with built-in tags that are assigned and updated with fresh values each time a stack is updated.

Tags can be deleted by running [`pulumi stack tag rm <name>`](/docs/cli/commands/pulumi_stack_tag_rm).

## Stack Outputs {#outputs}

A stack can export values as stack outputs. These outputs are shown during an update, can be easily retrieved with the Pulumi CLI, and are displayed in the Pulumi Cloud. They can be used for important values like resource IDs, computed IP addresses, and DNS names.

To export values from a stack, use the following definition in the top-level of the entrypoint for your project:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
exports.url = resource.url;
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
export let url = resource.url;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
pulumi.export("url", resource.url)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
ctx.Export("url", resource.Url)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
public class MyStack : Stack
{
    public MyStack()
    {
        ...
        this.Url = resource.Url;
    }

    // 'url' is the output name. By default, it would take the property name 'Url'.
    [Output("url")] Output<string> Url { get; set; }
}
 ```

{{% /choosable %}}
{{% choosable language java %}}

```java
public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        ctx.export("url", resource.url());
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
outputs:
  url: ${resource.url}
```

{{% /choosable %}}

{{< /chooser >}}

From the CLI, you can then use [`pulumi stack output url`](/docs/cli/commands/pulumi_stack_output) to get the value and incorporate into other scripts or tools.

The value of a stack export can be a regular value, an [Output](/docs/concepts/inputs-outputs/), or a `Promise` (effectively, the same as an [Input](/docs/concepts/inputs-outputs/)). The actual values are resolved after `pulumi up` completes.

Stack exports are effectively JSON serialized, though quotes are removed when exporting strings.

For example, the following statements:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
exports.x = "hello"
exports.o = {num: 42}
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
export let x = "hello";
export let o = {num: 42};
```

{{% /choosable %}}
{{% choosable language python %}}

```python
pulumi.export("x", "hello")
pulumi.export("o", {'num': 42})
```

{{% /choosable %}}
{{% choosable language go %}}

```go
ctx.Export("x", pulumi.String("hello"))
ctx.Export("o", pulumi.Map(map[string]pulumi.Input{
    "num": pulumi.Int(42),
}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
class MyStack : Stack
{
    [Output] public Output<string> x { get; set; }
    [Output] public Output<ImmutableDictionary<string, int>> o { get; set; }

    public MyStack()
    {
        this.x = Output.Create("hello");
        this.o = Output.Create(
            new Dictionary<string, int> { { "num", 42 } }
                .ToImmutableDictionary());
    }
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
public static void stack(Context ctx) {
    ctx.export("x", Output.of("hello"));
    ctx.export("o", Output.of(Map.of(
            "num", "42"
    )));
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
outputs:
  x: hello
  o:
    num: 42
```

{{% /choosable %}}

{{< /chooser >}}

produce the following stack outputs:

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

{{% notes "info" %}}
Note: If you export an actual resource, it too will be JSON serialized. This usually isn’t what you want, especially because some resources are quite large. For example, if you only want to export the resource’s ID or name, just export those properties directly.
{{% /notes %}}

Stack outputs respect secret annotations and are encrypted appropriately. If a stack contains any secret values, their plaintext values will not be shown by default. Instead, they will be displayed as secret in the CLI. Pass `--show-secrets` to `pulumi stack output` to see the plaintext value.

## Getting the Current Stack Programmatically

The {{< pulumi-getstack >}} function gives you the currently deploying stack, which can be useful in naming, tagging, or accessing resources.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let stack = pulumi.getStack();
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let stack = pulumi.getStack();
```

{{% /choosable %}}
{{% choosable language python %}}

```python
stack = pulumi.get_stack()
```

{{% /choosable %}}
{{% choosable language go %}}

```go
stack := ctx.Stack()
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var stack = Deployment.Instance.StackName;
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var stack = ctx.stackName();
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  stack: ${pulumi.stack}
```

{{% /choosable %}}

{{< /chooser >}}

## Stack References {#stackreferences}

Stack references allow you to access the outputs of one stack from another stack. Inter-Stack Dependencies allow one stack to reference the outputs of another stack.

To reference values from another stack, create an instance of the `StackReference` type using the fully qualified name of the stack as an input, and then read exported stack outputs by their name:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

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
{{% choosable language java %}}

```java
var other = new StackReference("acmecorp/infra/other");
var otherOutput = other.getOutput(Output.of("x"));
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  my-stack-reference:
    type: pulumi:pulumi:StackReference
    properties:
      name: acmecorp/infra/other

variables:
  stack_output: ${my-stack-reference.outputs["x"]}
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

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

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
{{% choosable language java %}}

```java
ctx.export("kubeConfig", /*...a cluster's output property...*/);
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
outputs:
  kubeConfig: ... # a cluster's output property
```

{{% /choosable %}}

{{< /chooser >}}

The challenge in this scenario is that the services project needs to ingest this output during deployment so that it can
connect to the Kubernetes cluster provisioned in its respective environment.

The Pulumi programming model offers a way to do this with its `StackReference` resource type. For example:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

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

  "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
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
{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Exports;
import com.pulumi.Pulumi;

import com.pulumi.core.Output;
import com.pulumi.kubernetes.Provider;
import com.pulumi.kubernetes.ProviderArgs;
import com.pulumi.kubernetes.core_v1.Service;
import com.pulumi.kubernetes.core_v1.ServiceArgs;
import com.pulumi.resources.ComponentResourceOptions;
import com.pulumi.resources.StackReference;


public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var cluster = new StackReference(String.format("mycompany/infra/%s", ctx.stackName()));
        var kubeconfig = cluster.requireOutput(Output.of("KubeConfig")).applyValue(String::valueOf);
        var provider = new Provider("k8s", ProviderArgs.builder().kubeconfig(kubeconfig).build());
        var options = ComponentResourceOptions.builder()
            .provider(provider)
            .build();
        var service = new Service("app-service", ServiceArgs.builder()
            ...
            .build(), options);
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  kubeConfig: ${my-stack-reference.outputs["KubeConfig"]}
resources:
  my-stack-reference:
    type: pulumi:pulumi:StackReference
    properties:
      name: mycompany/infra/${pulumi.stack}
  provider:
    type: pulumi:providers:kubernetes
    properties:
      kubeConfig: kubeConfig
  service:
    type: some:resource:type
    properties: ...
    options:
      provider: ${provider}
```

{{% /choosable %}}

{{< /chooser >}}

The `StackReference` constructor takes as input a string of the form `<organization>/<project>/<stack>`, and lets
you access the outputs of that stack.

In the above example, you construct a stack reference to a specific stack in this project which has the same name
as your current stack (i.e. when deploying the "staging" stack of the above program, you reference the "staging" stack)
from the infra project. Once you have that resource, you can fetch the `kubeConfig` output variable with the `getOutput`
function. From that point onwards, Pulumi understands the inter-stack dependency for scenarios like cascading updates.

### Reading outputs from stack references

Stack references support two ways of reading outputs from the referenced stack:

* `getOutput` returns an `Output` that provides gated access to the output value.
  The output value can be accessed and transformed with methods like `Output.apply`.
  This is useful when the output is used as an input to another resource.
* `getOutputDetails` returns an `OutputDetails` object that provides direct access to the output value.
  This is useful when you want to process the output directly in your code.

As demonstration of **`getOutput`**,
suppose that your referenced stack exports a `privateIp` output.
You want to incorporate the IP address into the name of an S3 bucket object
containing logs from that machine.

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
const infra = new pulumi.StackReference(...);
const ip = infra.getOutput("privateIp");
const logKey = ip.apply(ip => `logs/${ip}.log`);
const logFile = new aws.s3.BucketObject("log", {
    // ...
    key: logKey
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const infra: StackReference = new pulumi.StackReference(...);
const ip: Output<string> = infra.getOutput("privateIp");
const logKey: Output<string> = ip.apply(ip => `logs/${ip}.log`);
const logFile: aws.s3.BucketObject = new aws.s3.BucketObject("log", {
    // ...
    key: logKey
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
infra = StackReference(...)
ip = infra.get_output("privateIp")
log_key = ip.apply(lambda ip: f"logs/{ip}.log")
log_file = aws.s3.BucketObject("log", {
    # ...
    key: log_key
})
```

{{% /choosable %}}
{{% choosable language go %}}

```go
infra, err := pulumi.NewStackReference(ctx, ...)
if err != nil {
    return err
}
ip := infra.GetOutput("privateIp")
logKey := ip.ApplyT(func(ip string) string {
    return fmt.Sprintf("logs/%s.log", ip)
}).(StringOutput)
logFile := s3.NewBucketObject(ctx, "log", &s3.BucketObjectArgs{
    // ...
    Key: logKey,
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var infra = new StackReference(...);
var ip = infra.GetOutput("privateIp");
var logKey = ip.Apply(ip => $"logs/{ip}.log");
var logFile = new Aws.S3.BucketObject("log", new Aws.S3.BucketObjectArgs
{
    // ...
    Key = logKey,
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
StackReference infra = new StackReference(...);
Output<String> ip = infra.getOutput("privateIp");
Output<String> logKey = ip.apply(ip -> String.format("logs/%s.log", ip));
BucketObject logFile = new BucketObject("log", new BucketObjectArgs.Builder()
    .key(logKey)
    .build());
```

{{% /choosable %}}

{{< /chooser >}}

On the other hand, as an example of using **`getOutputDetails`**,
suppose that your referenced stack creates a VPC
and exports a list of public subnets as a JSON-serialized string,
and you want to add a bastion host to each subnet.
With `getOutputDetails`, this would look something like this:

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
const infra = new pulumi.StackReference(...);
const subnetsJSON = await infra.getOutputDetails("subnets");
const subnets = JSON.parse(subnetsJSON.value);
for (let i = 0; i < subnets.length; i++) {
    const subnet = subnets[i];
    const host = new aws.ec2.Instance(`bastion-${i}`, {
        // ...
        subnetId: subnet.id,
    });
    // ...
}
```

Note that your Pulumi program must export a top-level `async` function
to be able to use the `await` operator.

```javascript
export = async () => {
    // ...
}
```

See [Javascript Entrypoint](/docs/languages-sdks/javascript/#entrypoint)
for more information.

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const infra: StackReference = new pulumi.StackReference(...);
const subnetsJSON: StackReferenceOutputDetails = await infra.getOutputDetails("subnets");
const subnets = JSON.parse(subnetsJSON.value);
for (let i = 0; i < subnets.length; i++) {
    const subnet = subnets[i];
    const host = new aws.ec2.Instance(`bastion-${i}`, {
        // ...
        subnetId: subnet.id,
    });
    // ...
}
```

Note that your Pulumi program must export a top-level `async` function
to be able to use the `await` operator.

```javascript
export = async () => {
    // ...
}
```

See [Javascript Entrypoint](/docs/languages-sdks/javascript/#entrypoint)
for more information.

{{% /choosable %}}
{{% choosable language python %}}

{{% notes "info" %}}
This functionality is not currently supported in Python.
Progress is tracked on [pulumi/pulumi#12172](https://github.com/pulumi/pulumi/issues/12172)
if you need this functionality.
{{% /notes %}}

<!-- ```python -->
<!-- infra = StackReference(...) -->
<!-- subnets_json = await infra.get_output_details("subnets") -->
<!-- subnets = json.loads(subnets_json.value) -->
<!-- for i, subnet in enumerate(subnets): -->
<!--     host = aws.ec2.Instance(f"bastion-{i}", { -->
<!--         # ... -->
<!--         subnet_id: subnet["id"], -->
<!--     }) -->
<!--     # ... -->
<!-- ``` -->

{{% /choosable %}}
{{% choosable language go %}}

```go
infra, err := pulumi.NewStackReference(ctx, ...)
if err != nil {
    return err
}
subnetsJSON, err := infra.GetOutputDetails("subnets")
if err != nil {
    return err
}
var subnets []struct{ ID string `json:"id"` }
if err := json.Unmarshal([]byte(subnetsJSON.Value.(string)), &subnets); err != nil {
    return err
}

for i, subnet := range subnets {
    host, err := ec2.NewInstance(ctx, fmt.Sprintf("bastion-%d", i), &ec2.InstanceArgs{
        // ...
        SubnetId: pulumi.String(subnet.ID),
    })
    if err != nil {
        return err
    }
    // ...
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var infra = new StackReference(...);
var subnetsJSON = await infra.GetOutputDetailsAsync("subnets");
var subnets = JsonConvert.DeserializeObject<Subnet[]>((string)subnetsJSON.Value);
for (int i = 0; i < subnets.Length; i++) {
    var subnet = subnets[i];
    var host = new Aws.Ec2.Instance($"bastion-{i}", new Aws.Ec2.InstanceArgs
    {
        // ...
        SubnetId = subnet.Id,
    });
    // ...
}
```

Note that your Pulumi program must be inside an `async` function
to be able to use the `await` operator.

```csharp
return await Deployment.RunAsync(async () =>
{
    // ...
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
StackReferenceOutputDetails subnetsJSON = infra.outputDetails("subnets");
infra.outputDetailsAsync("subnets").thenAccept(subnetsJSON -> {
    Subnet[] subnets = new Gson().fromJson((String)subnetsJSON.getValue().get(), Subnet[].class);
    for (int i = 0; i < subnets.length; i++) {
        Subnet subnet = subnets[i];
        Instance host = new Instance(String.format("bastion-%d", i), new InstanceArgs.Builder()
            // ...
            .subnetId(subnet.getId())
            .build());
        // ...
    }
})
```

{{% /choosable %}}

{{< /chooser >}}

## Import and export a stack deployment

A stack can be exported to see the raw data associated with the stack. This is useful when manual changes need to be applied to the stack due to changes made in the target cloud platform that Pulumi is not aware of. The modified stack can then be imported to set the current state of the stack to the new values.

{{% notes "warning"%}}
This is a powerful capability that subverts the usual way that Pulumi manages resources and ensures immutable and repeatable infrastructure deployments. Importing an incorrect stack specification could lead to orphaning of cloud resources or the inability to make future updates to the stack. Use care when using the import and export capabilities.
{{% /notes %}}

```bash
$ pulumi stack export --file stack.json

$ pulumi stack import --file stack.json
```

## Destroy a stack

Before deleting a stack, if the stack still resources associated with it, they must first be deleted via `pulumi destroy`. This command uses the latest configuration values, rather than the ones that were last used when the program was deployed.

## Delete a stack

To delete a stack with no resources, run `pulumi stack rm`. Removing the stack will remove all stack history from pulumi.com and will delete the stack configuration file `Pulumi.<stack-name>.yaml`.

To force the deletion of a stack that still contains resources---potentially orphaning them---use `pulumi stack rm --force`.
