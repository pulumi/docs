---
title_tag: Deploy the Stack | Kubernetes
meta_desc: This page provides an overview of how to deploy a Kubernetes project as a Pulumi Stack.
title: Deploy stack
h1: "Pulumi & Kubernetes: Deploy stack"
weight: 5
menu:
  clouds:
    parent: kubernetes-get-started
    identifier: kubernetes-deploy-stack

aliases:
- /docs/quickstart/kubernetes/deploy-stack/
- /docs/get-started/kubernetes/deploy-stack/
---

Deploy the stack:

```bash
$ pulumi up
```

This command instructs Pulumi to determine the resources needed to create the stack. A preview is shown of the changes that will be made:

```bash
Previewing update (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/diana-pulumi-corp/quickstart/dev/previews/cc72bfca-4167-4282-8482-b4fe2e0d9fad

     Type                              Name            Plan
 +   pulumi:pulumi:Stack               quickstart-dev  create
 +   └─ kubernetes:apps/v1:Deployment  app-dep         create


Outputs:
    name: "app-dep-92efcbdf"

Resources:
    + 2 to create

Do you want to perform this update?  [Use arrows to move, type to filter]
  yes
> no
  details
```

Select `yes` using the arrows and hit enter to create the resources in Kubernetes.

```bash
Do you want to perform this update? yes
Updating (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/diana-pulumi-corp/quickstart/dev/updates/1

     Type                              Name            Status
 +   pulumi:pulumi:Stack               quickstart-dev  created (3s)
 +   └─ kubernetes:apps/v1:Deployment  app-dep         created (1s)


Outputs:
    name: "app-dep-b7413dae"

Resources:
    + 2 created

Duration: 10s
```

The `name` of the deployment that we exported is shown as a [stack output](/docs/concepts/stack#outputs).

{{< console-note >}}

Next, we'll make some modifications to the program.

{{< get-started-stepper >}}
