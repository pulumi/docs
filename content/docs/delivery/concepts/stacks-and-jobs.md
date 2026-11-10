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

Stacks and jobs do the work inside a stage. A `Stacks` resource updates existing stacks, and a `Job` runs a command, such as a smoke test.

Both name their `stage`, a `source` to check out, and a `directory` in that source. Delivery checks out the source at the run's locked commit before it updates a stack or runs a job.

## Stacks

A `Stacks` resource updates one or more existing stacks. Each entry in `stacks` runs `pulumi up` on one target stack:

```typescript
const services = new delivery.Stacks("services", {
    stage: dev,
    stacks: {
        api: { stack: "shop-api/dev", source: repo, directory: "api" },
        worker: { stack: "shop-worker/dev", source: repo, directory: "worker", timeout: 1800 },
    },
});
```

Create each target stack before the first run. A target must be an ordinary stack in the pipeline's organization; a pipeline stack or run stack can't be a target.

Each entry can set `config`, a map of plain-string values that Delivery writes to the target stack before the update. `config` can't hold secrets, and registration rejects one that does. Keep secrets in the target stack's own config file or in an [ESC environment](/docs/delivery/guides/cloud-credentials/).

The entries in one `Stacks` resource run together, and each can read the others' new outputs through stack references. The group is one unit for dependencies and retries: anything that uses one entry's output waits for the whole group, and retrying a failed entry reruns every entry. See [Stacks that deploy together](/docs/delivery/guides/pipeline-patterns/#stacks-that-deploy-together).

The `outputs` property holds each entry's stack outputs, keyed by entry name. If any entry's outputs are secret, the whole map is secret.

## Jobs

A `Job` runs a command with `sh -c` in `directory`:

```typescript
new delivery.Job("smoke", {
    stage: dev,
    source: repo,
    directory: "delivery",
    command: "sh smoke.sh",
    environment: { ENDPOINT: services.outputs.apply(o => String(o["api"]["endpoint"])) },
});
```

A job that exits with a non-zero code fails, and so does its stage. A job doesn't get a Pulumi access token.

### Job outputs

To publish outputs, the command writes a JSON object to the file named by `DELIVERY_OUTPUTS`. Each key becomes one output, and the file can be at most 1 MiB. To mark an output secret, write it as `{"value": ..., "secret": true}`. An output is also secret if it contains the value of a secret environment variable. If one output is secret, the whole `outputs` map is secret.

A resource outside Delivery that uses a job's output waits for the job to finish.

## Runner settings

`Job` and each `Stacks` entry accept the same runner settings.

`image` sets the container image the stack update or job runs in. The default is the Pulumi image. Pin it to control the Pulumi CLI or language versions, as in `pulumi/pulumi-nodejs:3.272.0`. A custom image needs `bash`, `curl`, `gzip`, and the Pulumi CLI on `PATH`. For a private registry, set `image.credentials` with a `username` and a secret `password`.

`preRunCommands` is a list of bash commands that run in the project directory after dependencies are installed and before the Pulumi command or job command. Each command runs separately, so environment changes don't carry over between them.

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

Stack updates and jobs run on Pulumi-managed runners. Leave `runtime` unset, and don't use the `WorkflowsRuntime` resource.

## Environment variables

Jobs and `Stacks` updates see the identity of the run as environment variables:

| Variable | Value |
| --- | --- |
| `DELIVERY_RUN` | The run number. |
| `DELIVERY_RELEASE` | The release number. |
| `DELIVERY_STAGE` | The stage. |
| `DELIVERY_COMMIT` | The commit of the source the stack update or job checked out. |
| `DELIVERY_PIPELINE` | The pipeline stack. |
| `DELIVERY_STACK` | The target stack of a `Stacks` update. |
| `DELIVERY_OUTPUTS` | The file a job writes its outputs to. |

`PULUMI_ACCESS_TOKEN`, `PULUMI_BACKEND_URL`, and every name that starts with `DELIVERY_` are reserved. Don't set them in `environment`.

These variables aren't set when you run `pulumi up` by hand, so give them a fallback, as in `process.env.DELIVERY_RUN ?? "manual"`. A tag or setting that uses them changes on every release.

## Rules for writing stacks and jobs

- A program has one `Pipeline`.
- A stage reads only the outputs of its own stacks and jobs, its sources, and pipeline sources. Don't pass an output from one stage into a stack update or job in a later stage.
- Ordinary code decides which stages, stacks, and jobs a run has. You can use `if`, loops, and `.apply` on their outputs.
- A non-Delivery resource must use a stack update's or job's output to wait for it. `dependsOn` orders only Delivery resources.
- The provider rejects error hooks on stacks and jobs.
- `pulumi.getStack()` returns the run stack's name, which changes on every run. Don't derive resource names from it.
