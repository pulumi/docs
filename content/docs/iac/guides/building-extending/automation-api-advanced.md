---
title_tag: "Advanced Automation API Patterns"
meta_desc: "Advanced Pulumi Automation API patterns for cross-stack teardown ordering, multi-stack orchestration, error handling, and workspace lifecycle management."
title: Advanced Automation API
h1: Advanced Automation API Patterns
menu:
    iac:
        identifier: advanced-automation-api
        name: Advanced Patterns
        parent: iac-guides-building-extending
        weight: 17
---

Once you've built a first Automation API program by following [Using Automation API](/docs/iac/guides/building-extending/automation-api/), you'll often need to go further: coordinate multiple stacks instead of one, tear resources down safely and in the right order, recover from failures gracefully, and manage the workspaces that back them. This guide covers those patterns with runnable TypeScript and Python examples. For terminology used throughout---`Workspace`, `Stack`, inline versus local programs---see [Automation API concepts](/docs/iac/concepts/automation-api/).

## Prerequisites

The examples below assume the same setup as the getting-started guide: the [Pulumi CLI](/docs/install/) on your `PATH` (or [installed programmatically](/docs/iac/guides/building-extending/automation-api/#install-the-cli-programmatically)), the Node.js or Python runtime for your chosen language, and a [Pulumi access token](/docs/administration/concepts/access-tokens/) or another configured [state backend](/docs/iac/concepts/state-and-backends/).

Some examples below orchestrate multiple Pulumi projects from a single Automation API program. Each project---`network` and `app` in the examples---is an ordinary Pulumi project directory with its own `Pulumi.yaml`, deployed as a [local program](/docs/iac/concepts/automation-api/#local-programs) rather than an inline one. That's a deliberate choice for these scenarios: an orchestrator managing multiple independently developed projects typically doesn't own their program code, so it drives them by path instead of importing their logic as a function.

## Cross-stack teardown ordering

When one stack's program reads another stack's outputs through a [`StackReference`](/docs/iac/concepts/stacks/#stackreferences), the two stacks become coupled: the dependent stack's resources may need values---a VPC ID, a subnet, a security group---that only exist while the referenced stack's resources still exist. Automation API doesn't infer this coupling for you, so destroying stacks in the wrong order can fail mid-destroy or, worse, leave orphaned resources behind.

The examples below use `selectStack`/`select_stack` and `createOrSelectStack`/`create_or_select_stack` directly; see [Create, select, and create-or-select](#create-select-and-create-or-select) later in this guide for how those functions differ and when to reach for each.

Consider an `app` stack that reads networking details from a `network` stack:

{{< chooser language "typescript,python" >}}

{{% choosable language "typescript" %}}

```typescript
// app/index.ts -- an ordinary Pulumi program, not an Automation API program.
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const config = new pulumi.Config();
const networkStackName = config.require("networkStackName");

const network = new pulumi.StackReference(networkStackName);
const vpcId = network.getOutput("vpcId");
const subnetIds = network.getOutput("subnetIds");

const server = new aws.ec2.Instance("app-server", {
    ami: "ami-0c55b159cbfafe1f0",
    instanceType: "t3.micro",
    subnetId: subnetIds.apply((ids: string[]) => ids[0]),
});

export const serverId = server.id;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# app/__main__.py -- an ordinary Pulumi program, not an Automation API program.
import pulumi
import pulumi_aws as aws

config = pulumi.Config()
network_stack_name = config.require("network_stack_name")

network = pulumi.StackReference(network_stack_name)
vpc_id = network.get_output("vpc_id")
subnet_ids = network.get_output("subnet_ids")

server = aws.ec2.Instance("app-server",
    ami="ami-0c55b159cbfafe1f0",
    instance_type="t3.micro",
    subnet_id=subnet_ids.apply(lambda ids: ids[0]))

pulumi.export("server_id", server.id)
```

{{% /choosable %}}

{{< /chooser >}}

Because `app` depends on `network`'s outputs, you must always destroy `app` before `network`---the reverse of the order you deployed them in. An orchestrator program can encode that rule directly instead of relying on whoever runs it to remember it:

{{< chooser language "typescript,python" >}}

{{% choosable language "typescript" %}}

```typescript
import { LocalWorkspace } from "@pulumi/pulumi/automation";

async function selectStack(workDir: string, stackName: string) {
    return LocalWorkspace.selectStack({ stackName, workDir });
}

async function teardownEnvironment(envName: string) {
    const appStack = await selectStack("./app", `app-${envName}`);
    const networkStack = await selectStack("./network", `network-${envName}`);

    // Destroy the dependent stack first. If network's resources disappear
    // while app still references them, the app destroy can fail partway
    // through, leaving some of its resources behind.
    console.info(`Destroying app-${envName}...`);
    await appStack.destroy({ onOutput: console.info });

    console.info(`Destroying network-${envName}...`);
    await networkStack.destroy({ onOutput: console.info });
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
from pulumi import automation as auto


def select_stack(work_dir: str, stack_name: str) -> auto.Stack:
    return auto.select_stack(stack_name=stack_name, work_dir=work_dir)


def teardown_environment(env_name: str) -> None:
    app_stack = select_stack("./app", f"app-{env_name}")
    network_stack = select_stack("./network", f"network-{env_name}")

    # Destroy the dependent stack first. If network's resources disappear
    # while app still references them, the app destroy can fail partway
    # through, leaving some of its resources behind.
    print(f"Destroying app-{env_name}...")
    app_stack.destroy(on_output=print)

    print(f"Destroying network-{env_name}...")
    network_stack.destroy(on_output=print)
```

{{% /choosable %}}

{{< /chooser >}}

For a scenario with more than two stacks, build the same reverse-order list you used to deploy them and iterate over it: `[app, cache, network]` at teardown time for a `[network, cache, app]` deployment order, destroying each stack in turn before moving to the next.

## Multi-stack orchestration

Automation API is well suited to deploying the same program across many environments---development, staging, production---or many regions, without hand-writing a stack for each one. Represent each target as data, then loop over it, creating or selecting the corresponding stack, and applying its own configuration:

{{< chooser language "typescript,python" >}}

{{% choosable language "typescript" %}}

```typescript
import { LocalWorkspace, UpResult } from "@pulumi/pulumi/automation";

interface EnvironmentConfig {
    stackName: string;
    awsRegion: string;
}

const environments: EnvironmentConfig[] = [
    { stackName: "dev", awsRegion: "us-west-2" },
    { stackName: "staging", awsRegion: "us-east-1" },
    { stackName: "production", awsRegion: "us-east-1" },
];

async function deployAll(): Promise<void> {
    for (const env of environments) {
        const stack = await LocalWorkspace.createOrSelectStack({
            stackName: env.stackName,
            workDir: "./webapp",
        });

        await stack.setConfig("aws:region", { value: env.awsRegion });

        console.info(`Updating stack ${env.stackName}...`);
        const result: UpResult = await stack.up({ onOutput: console.info });

        const changes = result.summary.resourceChanges ?? {};
        console.info(
            `Stack ${env.stackName} updated: ${changes.same ?? 0} unchanged, ` +
            `${changes.create ?? 0} created, ${changes.update ?? 0} updated.`,
        );
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
from pulumi import automation as auto

environments = [
    {"stack_name": "dev", "aws_region": "us-west-2"},
    {"stack_name": "staging", "aws_region": "us-east-1"},
    {"stack_name": "production", "aws_region": "us-east-1"},
]


def deploy_all() -> None:
    for env in environments:
        stack = auto.create_or_select_stack(
            stack_name=env["stack_name"],
            work_dir="./webapp",
        )

        stack.set_config("aws:region", auto.ConfigValue(value=env["aws_region"]))

        print(f"Updating stack {env['stack_name']}...")
        result = stack.up(on_output=print)

        changes = result.summary.resource_changes or {}
        print(
            f"Stack {env['stack_name']} updated: {changes.get('same', 0)} unchanged, "
            f"{changes.get('create', 0)} created, {changes.get('update', 0)} updated."
        )
```

{{% /choosable %}}

{{< /chooser >}}

### CI/CD integration pattern

A common way to run this kind of program in a pipeline is to promote sequentially: deploy to `dev`, and only proceed to `staging` and `production` if it succeeds. Wrap each stack's `up` in error handling (see the next section) and stop the loop---rather than continuing to the next environment---the first time a deployment fails, so a broken change never reaches production. See [Continuous delivery](/docs/iac/operations/continuous-delivery/) for how to wire an Automation API program like this one into your CI/CD system.

## Error handling and observability

Automation API surfaces failures as exceptions rather than nonzero exit codes, and it gives you structured results instead of text you'd otherwise have to parse from CLI output. Both make an orchestrator program considerably easier to operate than a script that shells out to `pulumi`.

### Streaming output

The `onOutput` (`on_output`) callback you've seen throughout this guide receives the same incremental output a user watching `pulumi up` in a terminal would see. Pass any function that accepts a string---writing it to your own structured logger instead of `stdout` is often more useful in a service context than in a script:

{{< chooser language "typescript,python" >}}

{{% choosable language "typescript" %}}

```typescript
const result = await stack.up({
    onOutput: (chunk: string) => logger.info("pulumi", { output: chunk.trimEnd() }),
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
result = stack.up(on_output=lambda chunk: logger.info("pulumi", extra={"output": chunk.rstrip()}))
```

{{% /choosable %}}

{{< /chooser >}}

### Reading structured results

`up`, `destroy`, `preview`, and `refresh` all return a result object with a `summary` describing the update---its resulting [permalink](/docs/iac/guides/basics/how-pulumi-works/) URL, per-resource-operation counts, and duration---plus, for `up`, the stack's `outputs`. Use these instead of scraping console text to drive decisions in your program:

{{< chooser language "typescript,python" >}}

{{% choosable language "typescript" %}}

```typescript
const result = await stack.up({ onOutput: console.info });

if (result.summary.result !== "succeeded") {
    throw new Error(`Update did not succeed: ${result.summary.result}`);
}

console.info(`Website URL: ${result.outputs.websiteUrl.value}`);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
result = stack.up(on_output=print)

if result.summary.result != "succeeded":
    raise RuntimeError(f"Update did not succeed: {result.summary.result}")

print(f"Website URL: {result.outputs['website_url'].value}")
```

{{% /choosable %}}

{{< /chooser >}}

### Catching engine errors

Failed updates raise a language-native exception rather than only returning a failed summary. Catch it around each stack operation so one failing stack doesn't take down an orchestrator managing many others:

{{< chooser language "typescript,python" >}}

{{% choosable language "typescript" %}}

```typescript
import { CommandError } from "@pulumi/pulumi/automation";

try {
    await stack.up({ onOutput: console.info });
} catch (err) {
    if (err instanceof CommandError) {
        console.error(`Update failed for stack ${env.stackName}: ${err.message}`);
        // Record the failure, alert, or stop promoting to later environments,
        // depending on how your orchestrator should react.
    } else {
        throw err;
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
from pulumi.automation import CommandError

try:
    stack.up(on_output=print)
except CommandError as err:
    print(f"Update failed for stack {env['stack_name']}: {err}")
    # Record the failure, alert, or stop promoting to later environments,
    # depending on how your orchestrator should react.
```

{{% /choosable %}}

{{< /chooser >}}

For transient failures---a provider's API rate-limiting you, a momentary network blip---wrap the call in your own retry loop with backoff rather than retrying blindly; a `CommandError` from a genuine configuration or program error will fail again immediately and shouldn't be retried the same way.

## Workspace lifecycle management

Every `Stack` operates against a `Workspace`, and how you construct that workspace determines where Pulumi looks for your program, your project settings, and your stack configuration.

### Choosing how to associate a program

Automation API gives you three ways to associate a stack with a program, and the convenience functions (`createStack`, `selectStack`, `createOrSelectStack`) all accept either shape:

- **Local program** (`workDir`/`work_dir`): points at an existing project directory with its own `Pulumi.yaml`, exactly like a program you'd run with the CLI. Use this when the program already exists as a standalone project---the orchestration examples earlier in this guide use this style because they drive existing `network` and `app` projects.
- **Inline program** (`program`): a function defined in the same process as your Automation API code, with no `Pulumi.yaml` of its own. Use this when the Automation API program *is* the deployment tool---for example, a small CLI or service that both defines and deploys the infrastructure with no separate project to maintain. See [Using Automation API](/docs/iac/guides/building-extending/automation-api/#define-your-pulumi-program) for an inline example.
- **Remote program** (`RemoteWorkspace`): runs a program from a remote Git repository through [Pulumi Deployments](/docs/deployments/concepts/) rather than on the machine executing your Automation API code.

### Create, select, and create-or-select

The three convenience functions differ only in what they assume about the stack's existence: `createStack` fails if the stack already exists, `selectStack` fails if it doesn't, and `createOrSelectStack` does whichever is needed. Prefer `createOrSelectStack` for idempotent orchestrators that may run against a mix of new and existing environments---most of the examples in this guide use it for that reason. Reach for `createStack` or `selectStack` directly when you want the corresponding failure mode: `createStack` to guarantee you never silently reuse an existing stack's state, `selectStack` (as in the teardown example above) to guarantee you never accidentally create one that shouldn't exist yet.

Once you have a `Stack`, the same Automation API can also manage which [Pulumi ESC environments](/docs/esc/concepts/environments/) it imports, adding, listing, and removing them programmatically instead of editing `Pulumi.<stack>.yaml` by hand. See [Automation API for ESC](/docs/esc/integrations/automation-api/) for the supported methods and per-language examples.

### Reusing workspaces across stacks

Creating a new `Workspace` for every stack works, but it's wasteful when you're operating on many stacks that share the same program: each `LocalWorkspace` you construct re-reads `Pulumi.yaml` and re-resolves the CLI. When you already have a `Stack` object, reuse its `workspace` property to select a sibling stack in the same project instead of building a new workspace from scratch:

{{< chooser language "typescript,python" >}}

{{% choosable language "typescript" %}}

```typescript
import { LocalWorkspace, Stack } from "@pulumi/pulumi/automation";

const devStack = await LocalWorkspace.createOrSelectStack({
    stackName: "dev",
    workDir: "./webapp",
});

// Reuse the same workspace---and therefore the same Pulumi.yaml and
// CLI resolution---to operate on a sibling stack in the same project.
const stagingStack = await Stack.select("staging", devStack.workspace);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
from pulumi.automation import Stack
from pulumi import automation as auto

dev_stack = auto.create_or_select_stack(stack_name="dev", work_dir="./webapp")

# Reuse the same workspace---and therefore the same Pulumi.yaml and
# CLI resolution---to operate on a sibling stack in the same project.
staging_stack = Stack.select("staging", dev_stack.workspace)
```

{{% /choosable %}}

{{< /chooser >}}

### Cleaning up workspace and stack state

Automation API's `Workspace` methods for removing state mirror the CLI commands they drive, and it's worth being precise about which one you want:

- **`stack.destroy()`** tears down the stack's deployed resources but leaves the stack itself---and its history---registered with your state backend. Use this for routine teardown, including the ordering pattern described earlier in this guide.
- **`workspace.removeStack(stackName)`** (`remove_stack`) deletes the stack's registration and configuration entirely. Run this only after the stack's resources are already destroyed---removing a stack that still has resources orphans them, since nothing is tracking them anymore.

{{< chooser language "typescript,python" >}}

{{% choosable language "typescript" %}}

```typescript
await stack.destroy({ onOutput: console.info });
await stack.workspace.removeStack(stackName);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
stack.destroy(on_output=print)
stack.workspace.remove_stack(stack_name)
```

{{% /choosable %}}

{{< /chooser >}}

For temporary environments---per-branch preview environments or integration test stacks, for example---pair these two calls so every stack you create programmatically is also fully cleaned up programmatically, rather than accumulating stale stacks in your state backend.

## Next steps

- Review [Automation API concepts](/docs/iac/concepts/automation-api/) for the underlying `Workspace`, `Stack`, and program model these patterns build on.
- See [Using Automation API](/docs/iac/guides/building-extending/automation-api/) if you haven't yet built a first Automation API program.
- Explore the [`automation-api-examples` repository](https://github.com/pulumi/automation-api-examples) for complete, runnable programs in every supported language.
