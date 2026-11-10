---
title_tag: Pulumi Delivery stages and gates
meta_desc: Order promotion between environments with Pulumi Delivery stages, and hold a release at a gate until someone approves it or continues it.
title: Stages and gates
h1: Stages and gates
menu:
  delivery:
    name: Stages and gates
    parent: delivery-concepts
    weight: 20
aliases: []
---

Stages give a pipeline its shape. Each stage is usually one environment, and its `from` list says which stages a release must pass through first. A gate, set in `when`, holds the release at the entrance to a stage until a rule passes.

## Order stages with `from`

A stage with no `from` is an entry stage. Every other stage lists its upstream stages:

```typescript
const dev = new delivery.Stage("dev", { pipeline });
const staging = new delivery.Stage("staging", { pipeline, from: [dev] });
const prod = new delivery.Stage("prod", { pipeline, from: [staging] });
```

A stage with several upstream stages waits until the same release has converged in all of them. Stage names must be unique within a pipeline.

A stage deploys one run at a time. When a newer run reaches a stage while an older run is still waiting for it, or waiting at its gate, the newer run replaces the older one. A run the stage has already admitted keeps the stage until it finishes.

{{% notes type="warning" %}}
Delivery doesn't detect cycles between stages. A run in a cycle waits until you cancel it.
{{% /notes %}}

## Gates

A gate is a rule in a stage's `when` property. The release can't enter the stage until the rule passes.

### Manual gates

`manual()` waits until someone continues the gate. It's available on every edition that includes Delivery. Use `description` to tell that person what to check first:

```typescript
const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.manual({ description: "Check the staging dashboards first." }),
});
```

Continue a manual gate from the run page in the Pulumi Cloud console, or with the REST API. See [Continue a gate from another system](#continue-a-gate-from-another-system).

### Approval gates

<!-- TODO(launch): Replace the next sentence with the pulumi-cloud shortcode for "delivery-approvals" once pulumi/marketing-web adds a hidden `delivery-approvals` feature (min_edition: pro). -->

Approval gates are available in the Pro and Enterprise editions.

`approval()` waits until enough eligible people approve. It takes `approvers`, a list of Pulumi usernames or team names, and `count`, the number of approvals required (one by default).

```typescript
const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.approval({ approvers: ["platform-leads"], count: 2 }),
});
```

Anyone eligible can approve, including the person who started the run or pushed the commit. With no `approvers`, anyone with update permission on the organization can approve. A name that matches no user or team keeps the gate waiting, so double-check spelling.

An approval gate shows the approver a preview of the stack updates the stage will make. The preview can be partial, and "Not available" doesn't mean "no changes".

Use `approval()` when specific people must sign off or you need more than one approval. Otherwise, `manual()` is enough.

### Combine rules

`allOf()` passes when every child rule passes, and `anyOf()` passes when any one does. You can nest them up to three levels deep. Build a combined rule with the `Output` form of each function, because `rules` doesn't accept the promise a plain rule function returns:

```typescript
const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.allOfOutput({
        rules: [
            delivery.approvalOutput({ approvers: ["your-colleague"] }),
            delivery.manualOutput({ name: "dashboards", description: "Check the dashboards first." }),
        ],
    }),
});
```

Every rule takes an optional `name`. Names must be unique within a gate, and `manual()` defaults to `manual`.

### HTTP gates

The SDK includes an `http()` rule that polls a URL until a JMESPath expression is true. It isn't available during public preview, and registration rejects a stage that uses it.

<!-- TODO(launch): Confirm http() status at GA. If it's still unavailable, consider removing this section and listing it only under known limitations. -->

## Continue a gate from another system

Any credential with write access to the pipeline stack can continue a manual gate. To do it from another system, such as a deployment hook:

1. Read the run with `GET /api/preview/stacks/<org>/<project>/<stack>/delivery/runs/<run number>`.
1. In `stages`, find the stage. If `stages[].gate.status` is `open`, note `stages[].gate.id`.
1. Send `POST .../delivery/runs/<run number>/gates/<gate id>/continue` with a JSON body.

```bash
curl -X POST \
    -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{}' \
    https://api.pulumi.com/api/preview/stacks/acme/shop-delivery/main/delivery/runs/<run-number>/gates/<gate-id>/continue
```

The body is required; a request without one gets a 400 response. A gate with one manual rule takes an empty object. A gate with several needs the rule's name, as in `{"condition": "dashboards"}`. A 409 response saying the gate isn't open means someone already continued it.

An approval rule in `stages[].gate.conditions` carries a `changeRequestId`. Approve it with `POST /api/change-requests/<org>/<change-request-id>/approve` and an empty JSON body. Approving needs a user token; see [Permissions](/docs/delivery/operations/permissions/).

To pass the run number to the other system, write it into a resource the stack updates anyway. For an Amazon ECS blue/green deployment, the lifecycle hook's `hookDetails` works well:

```typescript
hookDetails: JSON.stringify({
    run: process.env.DELIVERY_RUN,
    release: process.env.DELIVERY_RELEASE,
    commit: process.env.DELIVERY_COMMIT,
}),
```

Don't write the run number into a Lambda function's environment variables. That changes the function on every run.
