---
title_tag: Pulumi Delivery pipeline patterns
meta_desc: Common patterns for Pulumi Delivery pipelines, including per-environment helper functions, smoke tests after each deploy, and stacks that deploy together.
title: Pipeline patterns
h1: Pipeline patterns
menu:
  delivery:
    name: Pipeline patterns
    parent: delivery-guides
    weight: 20
aliases: []
---

The examples on this page assume the `delivery` import, a source named `repo`, and a `pipeline`, as in [Get started](/docs/delivery/get-started/).

## One stage per environment from a helper function

When your environments differ by only a few values, write a function that adds one environment's members to a stage, and call it for each stage:

```typescript
function deploy(stage: delivery.Stage, name: string, region: string) {
    const app = new delivery.Stacks(name, {
        stage,
        stacks: { app: { stack: `shop-app/${name}`, source: repo, directory: "app" } },
    });
    new delivery.Job(`smoke-${name}`, {
        stage,
        source: repo,
        directory: "delivery",
        command: "sh smoke.sh",
        environment: {
            ENDPOINT: app.outputs.apply(o => String(o["app"]["endpoint"])),
            EXPECTED_REGION: region,
        },
    });
}

const dev = new delivery.Stage("dev", { pipeline });
deploy(dev, "dev", "eu-central-1");
const staging = new delivery.Stage("staging", { pipeline, from: [dev] });
deploy(staging, "staging", "eu-west-1");
const prod = new delivery.Stage("prod", { pipeline, from: [staging], when: delivery.approval() });
deploy(prod, "prod", "us-west-2");
```

Resource names must be unique, so build them from the environment name. The region itself comes from each target stack's config file (`aws:region` in `Pulumi.<stack>.yaml`); the `region` argument here only tells the smoke test what to expect.

## Smoke test after each deploy

Put a `Job` in the same stage as the `Stacks` member it tests, so it can read that member's outputs. A job can't read outputs from an earlier stage. This script retries, because a new deployment can take a few seconds to answer:

```bash
set -eu
for attempt in 1 2 3 4 5; do
    if curl -fsS "$ENDPOINT/health" > /dev/null; then
        echo "{\"checked\": \"$ENDPOINT\"}" > "$DELIVERY_OUTPUTS"
        exit 0
    fi
    sleep 10
done
echo "Smoke test failed for $ENDPOINT" >&2
exit 1
```

`curl -fsS` makes an HTTP error return a non-zero exit code. When the job fails, its stage fails and later stages don't start. Fix the problem and [retry the run](/docs/delivery/operations/runs-and-stages/#retry-a-failed-run).

## Stacks that deploy together

When stacks depend on each other and should update in the same step, put them in one `Stacks` group:

```typescript
new delivery.Stacks("platform", {
    stage: dev,
    stacks: {
        network: { stack: "shop-network/dev", source: repo, directory: "network" },
        app: { stack: "shop-app/dev", source: repo, directory: "app" },
    },
});
```

The `app` program reads the network's new outputs with a [stack reference](/docs/iac/concepts/stacks/#stackreferences):

```typescript
const network = new pulumi.StackReference("acme/shop-network/dev");
const subnetId = network.getOutput("subnetId");
```

Keep groups small. A group is one unit for retries, and each entry uses one slot of your organization's concurrency limit, so a group larger than that limit can block itself. Put stacks that don't share a step in separate groups.

<!-- TODO(launch): Confirm whether entries in a group run in parallel or in dependency order, and say so explicitly. -->
