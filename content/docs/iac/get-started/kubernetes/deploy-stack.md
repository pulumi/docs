---
title_tag: Deploy the Stack | Kubernetes
title: Deploy the stack
h1: "Deploy the stack"
meta_desc: Learn how to deploy your stack to a Kubernetes project in this guide.
weight: 6
menu:
    iac:
        name: Deploy the stack
        identifier: kubernetes-get-started.deploy-stack
        parent: kubernetes-get-started
        weight: 6
aliases:
    - /docs/quickstart/kubernetes/deploy-stack/
---

Now deploy the stack with `pulumi up`:

```bash
$ pulumi up
```

This command first shows you a preview of the changes to be made:

```
Previewing update (dev):

     Type                              Name            Plan
 +   pulumi:pulumi:Stack               quickstart-dev  create
 +   └─ kubernetes:apps/v1:Deployment  nginx           create

Resources:
    + 2 to create

Do you want to perform this update?
> yes
  no
  details
```

Choosing `yes` proceeds with an update, which creates the resources in your cluster:

```
Updating (dev):

     Type                              Name            Status
 +   pulumi:pulumi:Stack               quickstart-dev  created (3s)
 +   └─ kubernetes:apps/v1:Deployment  nginx           created (2s)

Outputs:
    name: "nginx-bec13562"

Resources:
    + 2 created

Duration: 4s
```

The update completes when all resources are created. The deployment finishes in just a few seconds.

{{< auto-naming-note resource="deployment" suffix="bec13562" >}}

{{% notes type="warning" %}}
If you get `configured Kubernetes cluster is unreachable` or `unable to load schema information from the API server`, verify your cluster access with `kubectl cluster-info` and `kubectl auth can-i get pods`. If those fail, revisit the [Configure access](/docs/iac/get-started/kubernetes/configure/) step.
{{% /notes %}}

Notice the deployment's name was emitted as a [stack output](/docs/iac/concepts/stacks/#outputs). You can retrieve the output's value with `pulumi stack output`:

```bash
$ pulumi stack output name
```

Next, you'll expose the deployment with a service.

{{< get-started-stepper >}}
