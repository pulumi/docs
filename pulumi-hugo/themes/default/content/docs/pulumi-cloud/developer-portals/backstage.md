---
title: Pulumi Backstage Plugin
title_tag: Get started with the Pulumi Backstage Plugin
h1: Building Developer Portals with Pulumi and Backstage
meta_desc: Learn how to get the Pulumi Backstage Plugin up and running!
menu:
  pulumicloud:
    weight: 3
    parent: developer-portals
---

We’ve seen many developer portal technologies rapidly growing in popularity over the last few years.  In particular, we’ve seen Pulumi users adopting [Backstage](https://backstage.io/) and as a result we built the [Pulumi Backstage Plugin](blog/pulumi-backstage-plugin/) to address the needs of organizations using Backstage and Pulumi together.

![Pulumi Backstage Plugin Activity screenshot](pulumi_backstage_plugin_activity.png)

The new Pulumi tab gives you direct access to all Pulumi stack activity associated with your backstage projects that include Pulumi stacks.

The Pulumi Backstage Plugin supports two new scaffolding actions, `pulumi:new` and `pulumi:up` which can be used to template out new Pulumi projects and to trigger updates to Pulumi stacks, fully integrated into the Backstage scaffolding system.

```yaml
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: kubernetes-template
  title: Kubernetes Cluster
  description: |
    A template for creating a new Kubernetes Cluster.
  tags:
    - pulumi
    - kubernetes
spec:
  steps:
    - id: pulumi-new-component
      name: Cookie cut the component Pulumi project
      action: pulumi:new
      input:
        name: "${{ parameters.component_id }}-infrastructure"
        description: ${{ parameters.description | dump }}
        organization: ediri
        stack: ${{ parameters.stack }}
        template: "https://github.com/my-silly-organisation/microservice-civo/tree/main/infrastructure-${{ parameters.cloud }}-${{ parameters.language }}"
        config:
          "node:node_count": "${{ parameters.nodeCount }}"
        folder: .
```

Checkout the [Pulumi Backstage Plugin](https://github.com/pulumi/pulumi-backstage-plugin) in the [Backstage Plugin directory](https://backstage.io/plugins/) or the [Roadie Pulumi Backstage Plugin guide](https://roadie.io/backstage/plugins/pulumi/).
