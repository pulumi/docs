---
title_tag: Destroy the Stack | Kubernetes
meta_desc: This page provides an overview of how to destroy a Pulumi stack of a Kubernetes project.
title: Destroy stack
h1: "Pulumi & Kubernetes: Destroy stack"
block_external_search_index: true
---

Now that we've seen how to deploy changes to our program, let's clean up and tear down the resources that are part of our stack.

To destroy resources, run the following:

```bash
$ pulumi destroy
```

You'll be prompted to make sure you really want to delete these resources.

```
Previewing destroy (dev):

     Type                           Name            Plan
 -   pulumi:pulumi:Stack            quickstart-dev  delete
 -   ├─ kubernetes:core:Service     nginx           delete
 -   └─ kubernetes:apps:Deployment  nginx           delete

Outputs:
  - ip: "10.105.234.140"

Resources:
    - 3 to delete

Do you want to perform this destroy? yes
Destroying (dev):

     Type                           Name            Status
 -   pulumi:pulumi:Stack            quickstart-dev  deleted
 -   ├─ kubernetes:core:Service     nginx           deleted
 -   └─ kubernetes:apps:Deployment  nginx           deleted

Outputs:
  - ip: "10.105.234.140"

Resources:
    - 3 deleted

Duration: 1s
```

To delete the stack itself, run [`pulumi stack rm`](/docs/cli/commands/pulumi_stack_rm). Note that this removes the stack
entirely from the Pulumi Cloud, along with all of its update history.

Next, we'll look at some next steps.

<div class="mt-6">
    <a data-track="previous-step" class="btn btn-secondary" href="/docs/clouds/kubernetes/get-started/deploy-changes-b/">&larr; Previous Step</a>
    <a data-track="next-step" class="btn" href="/docs/clouds/kubernetes/get-started/next-steps/">Next Steps &rarr;</a>
</div>
