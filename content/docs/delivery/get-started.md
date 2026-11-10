---
title_tag: Get started with Pulumi Delivery
meta_desc: Build and register your first Pulumi Delivery pipeline, with a dev stage that updates a stack and runs a smoke test and a prod stage behind an approval gate.
title: Get started
h1: Get started with Pulumi Delivery
menu:
  delivery:
    name: Get started
    parent: delivery-home
    identifier: delivery-get-started
    weight: 5
aliases: []
---

<!-- TODO(launch): Add `pulumi_cloud_feature: delivery` to the front matter once pulumi/marketing-web adds a hidden `delivery` feature (min_edition: essentials) and its sync PR updates data/pulumi_editions.yaml. Then drop the hand-written edition sentence. -->

<!-- TODO(launch): Coordinate with MA-866 (Delivery quickstart). Validate every step against the GA build on 2026-11-18 and replace placeholder output with real console screenshots. -->

In this guide, you'll build a pipeline with two stages. The `dev` stage updates a stack and runs a smoke check against it. The `prod` stage waits for an approval, then updates a second stack. By the end, every push to `main` starts a run that promotes the release from `dev` to `prod`.

{{% notes type="info" %}}
Pulumi Delivery is in public preview. Behavior, the SDK, and the REST API routes under `/api/preview/` can change before general availability.
{{% /notes %}}

## Before you begin

You'll need:

- A Pulumi Cloud organization on the Essentials, Pro, or Enterprise edition. Approval gates need the Pro or Enterprise edition, and the `manual()` gate works on every edition that includes Delivery.
- Pulumi CLI v3.272.0 or later, running on Linux or macOS.
- The Pulumi Cloud backend. Delivery doesn't work with a DIY backend or self-hosted Pulumi Cloud.
- A [version control integration](/docs/integrations/version-control/) that can read the repository you'll deploy from. Delivery works with GitHub, GitLab, Bitbucket, and Azure DevOps.

<!-- TODO(launch): Confirm edition availability with the final pricing decision (DLV-453) and with pulumi/marketing-web, which owns edition availability. -->

## Lay out the repository

This guide uses one GitHub repository, `acme/shop`, on the `main` branch. The pipeline program and the project it deploys live side by side:

```text
delivery/        the pipeline program
  Pulumi.yaml
  package.json
  index.ts
  smoke.sh
infra/           the project of the target stacks
  Pulumi.yaml
```

Replace `acme/shop` with your own repository as you go.

## Create the target stacks

Delivery updates stacks that already exist. It doesn't create them. The `infra` project in this guide declares one config value and one output:

```yaml
name: shop-infra
runtime: yaml
config:
  environment:
    type: string
outputs:
  endpoint: https://${environment}.shop.example.com
```

Create a stack for each environment:

```bash
cd infra
pulumi stack init acme/shop-infra/dev
pulumi stack init acme/shop-infra/prod
```

## Write the pipeline program

The pipeline program is an ordinary Pulumi project. In `delivery/Pulumi.yaml`, name the project:

```yaml
name: shop-delivery
runtime: nodejs
```

Then add the Delivery SDK from the `delivery` directory:

```bash
pulumi package add delivery
```

The command writes a `packages` entry to `Pulumi.yaml`. Keep that entry, because the hosted runner reads it to install the SDK for each run.

Now declare the pipeline in `delivery/index.ts`:

```typescript
import * as delivery from "@pulumi/delivery";

const app = new delivery.GitHubSource("app", {
    repository: "acme/shop",
    branch: "main",
    trigger: true,
});

const pipeline = new delivery.Pipeline("shop", {
    program: { source: app, directory: "delivery" },
});

const dev = new delivery.Stage("dev", { pipeline });
const prod = new delivery.Stage("prod", {
    pipeline,
    from: [dev],
    when: delivery.approval({ approvers: ["<your-colleague>"] }),
});

const devStacks = new delivery.Stacks("dev", {
    stage: dev,
    stacks: {
        app: {
            stack: "shop-infra/dev",
            source: app,
            directory: "infra",
            config: { environment: "dev" },
        },
    },
});

new delivery.Job("smoke", {
    stage: dev,
    source: app,
    directory: "delivery",
    command: "sh smoke.sh",
    environment: {
        ENDPOINT: devStacks.outputs.apply(outputs => String(outputs["app"]["endpoint"])),
    },
});

new delivery.Stacks("prod", {
    stage: prod,
    stacks: {
        app: {
            stack: "shop-infra/prod",
            source: app,
            directory: "infra",
            config: { environment: "prod" },
        },
    },
});
```

Replace `<your-colleague>` with the Pulumi username of whoever approves `prod`. It can be you.

<!-- TODO(launch): Add a language chooser with Python, Go, C#, and Java versions. The SDK ships all five languages; examples live in static/programs/. -->

The smoke test in `delivery/smoke.sh` checks the `dev` endpoint and records what it checked as a job output:

```bash
set -eu
echo "Checking $ENDPOINT"
echo "{\"checked\": \"$ENDPOINT\"}" > "$DELIVERY_OUTPUTS"
```

## Register the pipeline

A run checks out the pipeline program from the repository, so commit and push before you register:

```bash
cd delivery
npm install
pulumi stack init acme/shop-delivery/main
git add -A && git commit -m "Add the delivery pipeline" && git push
pulumi up
```

`pulumi up` on the pipeline stack registers the pipeline. It finishes with exit code 10, which is expected: the stages and steps are waiting for a run. The last line tells you whether a run is starting:

- "Registered. A run starts for commit abc1234 when this update finishes." You're done.
- "No run starts because commit abc1234 is not the head of branch main." Push your commit, or pull the latest and register again.
- "No run starts because the checkout has uncommitted changes." Commit and push to start a run.
- "No run starts because the update has no git commit." Run `pulumi up` from a Git checkout.

## Watch the run

In the Pulumi Cloud console, navigate to **Delivery** and select the run. The `dev` stage updates `acme/shop-infra/dev` and runs the smoke job, then the `prod` stage waits at its approval gate. Once the approver approves, `prod` updates `acme/shop-infra/prod`.

<!-- TODO(launch): Screenshot of the pipeline visualization with prod waiting at its gate. Confirm console navigation labels. -->

From now on, every push to `main` starts a new run. You can also start one from **Run pipeline** in the console, or through the REST API:

```bash
curl -X POST \
    -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"key": "first-run"}' \
    https://api.pulumi.com/api/preview/stacks/acme/shop-delivery/main/delivery/dispatch
```

The optional `key` makes the request idempotent: a second dispatch with the same key returns the first run.

## Next steps

- Learn how [pipelines, runs, and releases](/docs/delivery/concepts/) fit together.
- Give each stage [cloud credentials through Pulumi ESC](/docs/delivery/guides/cloud-credentials/).
- Add more environments with the [pipeline patterns](/docs/delivery/guides/pipeline-patterns/) guide.
