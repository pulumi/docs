---
title_tag: Deploy the Stack | Kubernetes
meta_desc: This page provides an overview of how to deploy a Kubernetes project as a Pulumi Stack.
title: Deploy stack
h1: "Pulumi & Kubernetes: Deploy stack"
block_external_search_index: true
---

### Configure Kubernetes

<a href="/registry/packages/kubernetes/installation-configuration" target="_blank">Configure Kubernetes</a> so the Pulumi CLI can connect to a Kubernetes cluster. If you have previously configured the <a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">kubectl CLI</a>, `kubectl`, Pulumi will respect and use your configuration settings.  Depending on the approach you choose, you may need to apply some of the configuation after creating your project and stack in the next step.

### Deployt stack

Let's go ahead and deploy the stack:

```bash
$ pulumi up
```

This command instructs Pulumi to determine the resources needed to create the stack. First, a preview is shown of the changes that will be made:

```
Previewing update (dev):

     Type                           Name            Plan
 +   pulumi:pulumi:Stack            quickstart-dev  create
 +   └─ kubernetes:apps:Deployment  nginx           create

Resources:
    + 2 to create

Do you want to perform this update?
  yes
> no
  details
```

Choosing `yes` will create resources in Kubernetes.

```
Do you want to perform this update? yes
Updating (dev):

     Type                           Name            Status
 +   pulumi:pulumi:Stack            quickstart-dev  created
 +   └─ kubernetes:apps:Deployment  nginx           created

Outputs:
    name: "nginx-xw231xdt"

Resources:
    + 2 created

Duration: 11s
```

The name of the deployment that we exported is shown as a [stack output](/docs/concepts/stack#outputs).

{{< console-note >}}

Next, we'll make some modifications to the program.

<div class="mt-6">
    <a data-track="previous-step" class="btn btn-secondary" href="/docs/clouds/kubernetes/get-started/review-project-b/">&larr; Previous Step</a>
    <a data-track="next-step" class="btn" href="/docs/clouds/kubernetes/get-started/modify-program-b/">Modify Program &rarr;</a>
</div>
