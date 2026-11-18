---
title_tag: Pulumi Delivery stacks and jobs
meta_desc: Use Stacks to update existing stacks and Job to run commands in each stage of a Pulumi Delivery pipeline, and configure the runners they use.
title: Stacks and jobs
h1: Stacks and jobs
menu:
  delivery:
    name: Stacks and jobs
    parent: delivery-concepts
    weight: 30
aliases: []
---

Stacks and jobs do the work inside a stage. A `Stacks` resource updates existing stacks, and a `Job` runs a command, such as a shell script.

Both belong to a `stage`. A `Job`, and each entry in a `Stacks` resource, also specifies a `source` repository and a `directory` in that repository. Pulumi Delivery checks out the commit the run pinned for that source before it updates a stack or runs a job.

## Stacks

A `Stacks` resource updates one or more existing stacks. Each entry in `stacks` runs `pulumi up` non-interactively on a target stack:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const services = new delivery.Stacks("services", {
    stage: dev,
    stacks: {
        api: { stack: "shop-api/dev", source: repo, directory: "api" },
        worker: { stack: "shop-worker/dev", source: repo, directory: "worker", timeout: 1800 },
    },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
services = delivery.Stacks(
    "services",
    stage=dev,
    stacks={
        "api": {"stack": "shop-api/dev", "source": repo, "directory": "api"},
        "worker": {"stack": "shop-worker/dev", "source": repo, "directory": "worker", "timeout": 1800},
    },
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
services, err := delivery.NewStacks(ctx, "services", &delivery.StacksArgs{
	Stage: dev,
	Stacks: delivery.StacksEntryMap{
		"api":    delivery.StacksEntryArgs{Stack: pulumi.String("shop-api/dev"), Source: repo, Directory: pulumi.String("api")},
		"worker": delivery.StacksEntryArgs{Stack: pulumi.String("shop-worker/dev"), Source: repo, Directory: pulumi.String("worker"), Timeout: pulumi.Int(1800)},
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var services = new Stacks("services", new StacksArgs
{
    Stage = dev,
    Stacks =
    {
        ["api"] = new StacksEntryArgs { Stack = "shop-api/dev", Source = repo, Directory = "api" },
        ["worker"] = new StacksEntryArgs { Stack = "shop-worker/dev", Source = repo, Directory = "worker", Timeout = 1800 },
    },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var services = new Stacks("services", StacksArgs.builder()
    .stage(dev)
    .stacks(Map.of(
        "api", StacksEntryArgs.builder().stack("shop-api/dev").source(repo).directory("api").build(),
        "worker", StacksEntryArgs.builder().stack("shop-worker/dev").source(repo).directory("worker").timeout(1800).build()))
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  services:
    type: delivery:Stacks
    properties:
      stage: ${dev}
      stacks:
        api:
          stack: shop-api/dev
          source: ${repo}
          directory: api
        worker:
          stack: shop-worker/dev
          source: ${repo}
          directory: worker
          timeout: 1800
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_stacks" "services" {
  stage = delivery_stage.dev
  stacks = {
    api = {
      stack     = "shop-api/dev"
      source    = delivery_git_hub_source.repo
      directory = "api"
    }
    worker = {
      stack     = "shop-worker/dev"
      source    = delivery_git_hub_source.repo
      directory = "worker"
      timeout   = 1800
    }
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

Delivery doesn't create target stacks. Create each one before the first run, or the run fails. A target must be an ordinary stack in the pipeline's organization.

Each entry can set `config`, a map of plain-string values. Before the update, Delivery sets these keys on the target stack, overriding the same keys in the stack's config file for that update only. Nothing is committed to your repository. `config` can't hold secrets, so set secrets and cloud credentials in the target stack's config file instead, for example by importing a [Pulumi ESC (Environments, Secrets, and Configuration) environment](/docs/esc/), or pass them in `environment`. See [Cloud credentials](/docs/delivery/guides/cloud-credentials/).

By default, the stacks in a `Stacks` resource are updated concurrently. To control the order, create dependencies between them with stack outputs and stack references. A stack that depends on another stack's outputs waits until that stack's update completes before it starts.

For example, put a `network` stack and an `app` stack that reads it in the same `Stacks` resource. When the `app` program reads `network` through a stack reference, the read waits for `network`'s update to finish and returns its new outputs:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const network = new pulumi.StackReference("acme/shop-network/dev");
const subnetId = network.getOutput("subnetId");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
network = pulumi.StackReference("acme/shop-network/dev")
subnet_id = network.get_output("subnetId")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
network, err := pulumi.NewStackReference(ctx, "acme/shop-network/dev", nil)
if err != nil {
	return err
}
subnetId := network.GetOutput(pulumi.String("subnetId"))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var network = new StackReference("acme/shop-network/dev");
var subnetId = network.GetOutput("subnetId");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var network = new StackReference("acme/shop-network/dev");
var subnetId = network.output("subnetId");
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  network:
    type: pulumi:pulumi:StackReference
    properties:
      name: acme/shop-network/dev

variables:
  subnetId: ${network.outputs["subnetId"]}
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "pulumi_stack_reference" "network" {
  name = "acme/shop-network/dev"
}

locals {
  subnet_id = pulumi_stack_reference.network.outputs["subnetId"]
}
```

{{% /choosable %}}

{{< /chooser >}}

If stacks in one `Stacks` resource reference each other in a cycle, the read fails with an error that names the stacks in the cycle.

Similarly, resources that depend on a `Stacks` resource, for example through its outputs, aren't updated until every stack in it has finished updating. Retrying a failed entry reruns every entry.

The `outputs` property contains the collected outputs of each member stack, keyed by name. If any stack's outputs include a secret, the entire `outputs` map is tracked as a secret.

## Jobs

A `Job` runs a command with `sh -c` in `directory`:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
new delivery.Job("smoke", {
    stage: dev,
    source: repo,
    directory: "delivery",
    command: "sh smoke.sh",
    environment: { ENDPOINT: services.outputs.apply(o => String(o["api"]["endpoint"])) },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
delivery.Job(
    "smoke",
    stage=dev,
    source=repo,
    directory="delivery",
    command="sh smoke.sh",
    environment={"ENDPOINT": services.outputs.apply(lambda o: str(o["api"]["endpoint"]))},
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
_, err = delivery.NewJob(ctx, "smoke", &delivery.JobArgs{
	Stage:     dev,
	Source:    repo,
	Directory: pulumi.String("delivery"),
	Command:   pulumi.String("sh smoke.sh"),
	Environment: pulumi.StringMap{
		"ENDPOINT": services.Outputs.ApplyT(func(o map[string]map[string]interface{}) string {
			return fmt.Sprint(o["api"]["endpoint"])
		}).(pulumi.StringOutput),
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
new Job("smoke", new JobArgs
{
    Stage = dev,
    Source = repo,
    Directory = "delivery",
    Command = "sh smoke.sh",
    Environment = { ["ENDPOINT"] = services.Outputs.Apply(o => o["api"]["endpoint"].ToString()!) },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
new Job("smoke", JobArgs.builder()
    .stage(dev)
    .source(repo)
    .directory("delivery")
    .command("sh smoke.sh")
    .environment(services.outputs().applyValue(o -> Map.of(
        "ENDPOINT", String.valueOf(o.get("api").get("endpoint")))))
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  smoke:
    type: delivery:Job
    properties:
      stage: ${dev}
      source: ${repo}
      directory: delivery
      command: sh smoke.sh
      environment:
        ENDPOINT: ${services.outputs["api"]["endpoint"]}
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_job" "smoke" {
  stage     = delivery_stage.dev
  source    = delivery_git_hub_source.repo
  directory = "delivery"
  command   = "sh smoke.sh"
  environment = {
    ENDPOINT = delivery_stacks.services.outputs["api"]["endpoint"]
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

A job that exits with a non-zero code fails, and so does its stage. A job gets a temporary `PULUMI_ACCESS_TOKEN` that acts as the [pipeline's identity](/docs/delivery/concepts/identity/#credentials-in-stack-updates-and-jobs), which it uses to upload its outputs.

### Job outputs

To publish outputs, the command writes a JSON object to the file named by `DELIVERY_OUTPUTS`. Each key becomes one output, and the file can be at most 1 MiB. To mark an output secret, write it as `{"value": ..., "secret": true}`. An output is also secret if it contains the value of a secret environment variable. If one output is secret, the whole `outputs` map is secret.

A resource outside Delivery that uses a job's output waits for the job to finish.

## Runner settings

`Job` and each `Stacks` entry accept the same runner settings.

`image` sets the container image the stack update or job runs in. The default is the official Pulumi image. Images can be pinned to control the Pulumi CLI or language versions, as in `pulumi/pulumi-nodejs:3.272.0`. Custom images require `bash`, `curl`, `gzip`, and the Pulumi CLI on the `PATH`. For a private registry, set `image.credentials` with a `username` and a secret `password`.

`environment` sets environment variables for the stack update or job, such as cloud credentials. Unlike `config`, it accepts secret values, and they stay secret.

`timeout` sets the maximum run time. On a `Stacks` entry, it's a number of seconds, and the default is 7200 (2 hours). See [Limits](/docs/delivery/limits/) for the allowed range.

<!-- TODO(launch): The provider schema types a Job's `timeout` as a Go duration string (such as `30m`) and says it isn't applied in the private preview. Confirm its behavior for the public preview and document it here. -->

`preRunCommands` is a list of bash commands that run in the project directory before the main command. For a `Stacks` entry, they run after `pulumi install` and before `pulumi up`. For a job, they run before the job's command. Each command runs separately, so environment changes don't carry over between them.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
new delivery.Job("smoke", {
    stage: prod,
    source: repo,
    directory: "delivery",
    command: "./scripts/smoke.sh",
    image: { reference: "pulumi/pulumi-nodejs:3.272.0" },
    preRunCommands: ["npm run build"],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
delivery.Job(
    "smoke",
    stage=prod,
    source=repo,
    directory="delivery",
    command="./scripts/smoke.sh",
    image={"reference": "pulumi/pulumi-nodejs:3.272.0"},
    pre_run_commands=["npm run build"],
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
_, err = delivery.NewJob(ctx, "smoke", &delivery.JobArgs{
	Stage:          prod,
	Source:         repo,
	Directory:      pulumi.String("delivery"),
	Command:        pulumi.String("./scripts/smoke.sh"),
	Image:          delivery.ImageArgs{Reference: pulumi.String("pulumi/pulumi-nodejs:3.272.0")},
	PreRunCommands: pulumi.StringArray{pulumi.String("npm run build")},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
new Job("smoke", new JobArgs
{
    Stage = prod,
    Source = repo,
    Directory = "delivery",
    Command = "./scripts/smoke.sh",
    Image = new ImageArgs { Reference = "pulumi/pulumi-nodejs:3.272.0" },
    PreRunCommands = { "npm run build" },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
new Job("smoke", JobArgs.builder()
    .stage(prod)
    .source(repo)
    .directory("delivery")
    .command("./scripts/smoke.sh")
    .image(ImageArgs.builder().reference("pulumi/pulumi-nodejs:3.272.0").build())
    .preRunCommands("npm run build")
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  smoke:
    type: delivery:Job
    properties:
      stage: ${prod}
      source: ${repo}
      directory: delivery
      command: ./scripts/smoke.sh
      image:
        reference: pulumi/pulumi-nodejs:3.272.0
      preRunCommands:
        - npm run build
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_job" "smoke" {
  stage     = delivery_stage.prod
  source    = delivery_git_hub_source.repo
  directory = "delivery"
  command   = "./scripts/smoke.sh"
  image = {
    reference = "pulumi/pulumi-nodejs:3.272.0"
  }
  pre_run_commands = ["npm run build"]
}
```

{{% /choosable %}}

{{< /chooser >}}

## Environment variables

Jobs and `Stacks` updates see which run they belong to as environment variables:

| Variable | Value |
| --- | --- |
| `DELIVERY_RUN` | The run number. |
| `DELIVERY_RELEASE` | The release number. |
| `DELIVERY_STAGE` | The stage. |
| `DELIVERY_COMMIT` | The commit of the source the stack update or job checked out. |
| `DELIVERY_PIPELINE` | The pipeline stack, as `org/project/stack`. |
| `DELIVERY_STACK` | The target stack of a `Stacks` update, as `org/project/stack`. Not set for jobs. |
| `DELIVERY_OUTPUTS` | The file a job writes its outputs to. |

`PULUMI_ACCESS_TOKEN`, `PULUMI_BACKEND_URL`, and every name that starts with `DELIVERY_` are reserved.

## Rules for writing stacks and jobs

The provider and the service enforce these rules:

- A stack update or job can use outputs from its own stage or an earlier stage, but not a later one. [Registration](/docs/delivery/concepts/#pipeline-program) rejects a dependency on a later stage, because it could never start.
- Ordinary code decides which stages, stacks, and jobs a run has. You can use `if`, loops, and `.apply` on their outputs.
- A non-Delivery resource must use a stack update's or job's output to wait for it. `dependsOn` orders only Delivery resources.
- The provider rejects error hooks on stacks and jobs.
- `pulumi.getStack()` returns the run stack's name, which changes on every run. It should not be used for deriving resource names.

## Next steps

- Give each stage [cloud credentials](/docs/delivery/guides/cloud-credentials/).
- See common setups in [Pipeline patterns](/docs/delivery/guides/pipeline-patterns/).
- Run a custom agent in a stage with an [`Agent`](/docs/delivery/concepts/agents/).
