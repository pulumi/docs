---
title: "Multicloud with Kubernetes and Pulumi"
date: 2022-06-09T11:40:47-07:00
meta_desc: "Learn how to customize the multi-cloud developer experience with Kubernetes and Pulumi, using TypeScript"
meta_image: showcase-image.png
authors:
    - guinevere-saenger
tags:
    - kubernetes
    - packages
    - cloud-engineering
    - typescript
---

In this article we'll show you how to use Pulumi Components and the Pulumi Automation API to make golden path
decisions which will both support your customers on multiple different clouds, and enable infrastructure teams and
frontend service teams to more easily own their respective parts of your codebase.

<!--more-->

Let's say you provide a hosted service for your customers. You would like to offer customizable Kubernetes cluster
provisioning, on multiple different clouds, as well as your product service itself.

There's a lot of configuration fine-tuning and manual repetition that is required when bringing up Kubernetes clusters
on different clouds.

This article is a written summary of our [KubeCrash live demo](https://www.youtube.com/watch?v=co6ByyRh0_I).
Please find the [repository with the full version of the code here.](https://github.com/pulumi/demo-kubecrash-2022)

## Part One: Create a component

A [Component Resource](https://www.pulumi.com/docs/intro/concepts/resources/components/) is an abstraction on top of
other Pulumi packages, often combining a few different providers into something that fits your infrastructure needs
precisely.

### Prerequisites

In our example, we are using three separate clouds, one of these being a local KinD cluster.

- [Nodejs](https://nodejs.org/en/download/)
- [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/)
- Have the Pulumi Registry documentation handy for some Pulumi providers:
    - [Pulumi Civo Provider](https://www.pulumi.com/registry/packages/civo/)
    - [Pulumi Linode Provider](https://www.pulumi.com/registry/packages/linode/)
    - [Pulumi Kubernetes Provider](https://www.pulumi.com/registry/packages/kubernetes/)
    - [Pulumi KinD Provider](https://github.com/frezbo/pulumi-provider-kind) (Kubernetes-in-Docker)
      _Note: As this is a community package, follow installation instructions from the README. This provider only supports
      Go and Nodejs._

Gather access tokens for Linode and Civo, if using, and set them in the environment or as
[secrets](https://www.pulumi.com/docs/intro/concepts/secrets/#using-configuration-and-secrets-in-code).

### Start by writing the code for each cloud

The below code, when run against `pulumi up`, will create a single cloud stack with three separate Kubernetes clusters.
The Stack output will be the cluster's name and kubeconfig.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as civo from '@pulumi/civo';
import * as linode from "@pulumi/linode";
import * as kind from "@pulumi/kind";


//Civo

// Create a firewall
const fw = new civo.Firewall("guin-fw", {
  region: "nyc1",
  createDefaultRules: true,
});

const civoCluster = new civo.KubernetesCluster("guin-civo-demo", {
  name: "guin-demo",
  region: "nyc1",
  firewallId: fw.id,
  pools: {
  nodeCount: 3,
  size: "g4s.kube.xsmall",
  }
});

export const clusterNameCivo = civoCluster.name
export const kcCivo = civoCluster.kubeconfig

//Linode

const linodeCluster = new linode.LkeCluster("guin-linode-demo", {
  k8sVersion: "1.22",
  label: "guin-demo",
  pools: [{
    count: 2,
    type: "g6-standard-2",
  }],
  region: "us-central",
  tags: ["guin-demo"],
});

export const clusterLabelLinode = linodeCluster.label
export const kcLinode = linodeCluster.kubeconfig

// Kind

const kindCluster = new kind.cluster.Cluster(
  'guin-kind',
  {
    name: pulumi.interpolate`guin-kind`,
    nodes: [
      {
        role: kind.node.RoleType.ControlPlane,
        extraPortMappings: [
          {
            containerPort: args.nodePort,
            hostPort: args.nodePort,
          },
        ],
      },
      {
        role: kind.node.RoleType.Worker,
      },
    ],
  },
)

export const clusterNameKind = kindCluster.name
export const kcKind = kindCluster.kubeconfig
```

We could stop here, export the kubeconfigs to a file, and start interacting with our clusters via `kubectl`.
But that would require our cluster operators to be deeply familiar with each cloud provider's Kubernetes implementation.
Let's see if we can do better.

### Create a custom component for the Kubernetes cluster

Our goal today is to bring up a "generic" Kubernetes cluster that fits a single use case for multiple clouds.
To do so, we create a default implementation as a wrapper around each cloud provider.
We implement the following features:

1. Choice of cloud
2. Cluster Naming
3. Kubeconfig Output for later use

The Pulumi SDK allows us to wrap resources into a `ComponentResource`, which in our Typescript example means we create
a new class that extends `pulumi.ComponentResource`.

```typescript
export class ShinyCluster extends pulumi.ComponentResource {
    constructor(
      name: string,
      args: {},
      opts: {},
    ) {
    # ...
    }
}
```

Because we like all things shiny, we'll call it a ShinyCluster, and pass `pkg:index:ShinyCluster` as the unique
resource name.

We'll also register the name and kubeconfig for each ShinyCluster as Outputs:

```typescript
import { Output } from '@pulumi/pulumi'; // add this to dependencies

#...

export class ShinyCluster extends pulumi.ComponentResource {
    constructor(
      name: string,
      args: {},
      opts: {},
    ) {
        super('pkg:index:ShinyCluster', name, {}, opts);
    }
    name: Output<string>;
    kubeConfig: Output<string>;
}
```

Write the implementation for each cloud provider:

```typescript
export class ShinyCluster extends pulumi.ComponentResource {
    constructor(
      name: string,
      args: {
        cloud: 'linode' | 'civo' | 'kind';
        nodePort?: number; // this is a KinD-specific add-on so we can connect to our workload
      },
        opts: {},
    ) {
        super('pkg:index:ShinyCluster', name, {}, opts);
    switch (args.cloud) {
      case 'linode':
        const linodeCluster = new linode.LkeCluster(
          'my-cluster',
          {
            label: 'guin-linode',
            k8sVersion: '1.22',
            pools: [
              {
                count: 2,
                type: 'g6-standard-2',
              },
            ],
            region: 'us-central',
            tags: ['guin'],
          },
          { parent: this },
        );
        this.name = linodeCluster.label;
        this.kubeConfig = linodeCluster.kubeconfig.apply((x) =>
          Buffer.from(x, 'base64').toString(),
        );
        break;
      case 'civo':
        const fw = new civo.Firewall(
          'guin-fw',
          {
            name: 'guin-civo',
            region: 'nyc1',
            createDefaultRules: true,
          },
          { parent: this },
        );

        const civoCluster = new civo.KubernetesCluster(
          'guin-civo',
          {
            region: 'nyc1',
            name: 'guin-civo',
            firewallId: fw.id,
            pools: {
              nodeCount: 3,
              size: 'g4s.kube.xsmall',
            },
          },
          { parent: this },
        );
        this.name = civoCluster.name;
        this.kubeConfig = civoCluster.kubeconfig;
        break;
      case 'kind':
        const kindCluster = new kind.cluster.Cluster(
          'guin-kind',
          {
            name: 'guin-kind',
            nodes: [
              {
                role: kind.node.RoleType.ControlPlane,
                extraPortMappings: [
                  {
                    containerPort: args.nodePort,
                    hostPort: args.nodePort,
                  },
                ],
              },
              {
                role: kind.node.RoleType.Worker,
              },
            ],
          },
          { parent: this },
        );
        this.name = kindCluster.name;
        this.kubeConfig = kindCluster.kubeconfig;
    }
  }
    name: Output<string>;
    kubeConfig: Output<string>;
}
```

We are now ready to use our component.

Read in the configuration from the config file and create a cluster:

```typescript
const config = new pulumi.Config();

const shinyCluster = new ShinyCluster(
  'guin',
  {
    cloud: config.require('cloud'),
    nodePort: config.getNumber('nodePort'),
  },
  {},
);

export const shinyName = shinyCluster.name;
export const shinyConfig = pulumi.secret(shinyCluster.kubeConfig);
```

In our terminal, we can now create a stack called `dev`, set the necessary inputs in the Pulumi config, and run `pulumi up`:

```bash
$ pulumi stack init dev
Created stack 'dev'
$ pulumi config set shinycluster:cloud civo
$ pulumi up
Previewing update (dev)

View Live: https://app.pulumi.com/guinevere/shinycluster/dev/previews/cf968a89-dadc-461f-badd-b062601c18b4

     Type                 Name              Plan
 +   pulumi:pulumi:Stack  shinycluster-dev  create
```

At this point, we have created a Pulumi Component Resource that we can use to scaffold Kubernetes
infrastructure.

## Side Quest: Ship an app!

The purpose of this demo is not focused on the details of deploying a web app on Kubernetes with Pulumi, so we won't
go into too much detail here.
We created a [shinyapp folder](https://github.com/pulumi/demo-kubecrash-2022/tree/main/shinyapp) to hold a Pulumi program (written in yaml!)
We could now follow the [Kubernetes provider configuration steps](https://www.pulumi.com/registry/packages/kubernetes/installation-configuration/#configuration)
to set up and deploy our `shinyapp` to each of our clusters.

But if we have multiple Kubernetes backends, and would like to deploy our `shinyapp` to each of them, this would get
tedious soon. Here is where we automate deploying our frontend as well.

## Part 2: Leverage the Automation API

The [Pulumi Automation API](https://www.pulumi.com/docs/guides/automation-api/) allows us to run Pulumi commands
without using the CLI manually.

Let's review our basic project file structure first, for context.
We place both our `shinycluster` backend and `shinyapp` frontend Pulumi projects in their own folders, to separate
concerns, and for visual clarity.

```
.
├── shinyapp
│   ├── Main.yaml           # our web app, declared in yaml
│   └── Pulumi.yaml         # Pulumi project config for `shinyapp`, with yaml runtime
├── shinycluster
│   ├── index.ts            # our showcased Pulumi Component Resource for a Kubernetes cluster
│   └── Pulumi.yaml         # Pulumi project config for `shinycluster`, with nodejs (Typescript) runtime
```

The neat thing here is that both our Kubernetes clusters and our application service are in their own contained folder,
and in fact each can be deployed independently using Pulumi.
Let's go ahead and implement the functionality that allows us to automate it all by adding the following files to the
root of the project:

```
├── Pulumi.yaml             # Pulumi project config for the entire demo
├── index.ts                # Input and output logic for our frontend and backend stacks
├── outputFormatter.ts      # Prettify output
├── runPulumiProject.ts     # Our specific automation implementation, using Automation API
└── stackModule.ts          # Wrapper logic to show which types are expected by each part of our project
```

_Not shown: dependency and package files._

### The Stack Module

First, we define a generic Pulumi stack, with variable working directories and outputs, as expected by the automation API.

```typescript
// stackModule.ts
import * as pulumi from '@pulumi/pulumi';

export type Unwrapped<T> = NonNullable<pulumi.Unwrap<Awaited<T>>>;

export type OutputMap<T> = {
  [K in keyof T]: {
    value: T[K];
    secret: boolean;
  };
};

export type StackModule<T> = {
  workDir: string;
  projectName: string;
  stack(): Promise<T>;
};

type StackOutputs<T> = T extends StackModule<infer O> ? O : never;

/**
 * The type of the outputs, as returned by the automation API as an "OutputMap".
 */
export type StackOutputMap<T> = OutputMap<Unwrapped<StackOutputs<T>>>;

/**
 * The type of the outputs, as if executed and run in a Pulumi program:
 */
export type StackOutputValues<T> = Unwrapped<StackOutputs<T>>;

/**
 * The type of a function that gets values by name from the outputs of a stack.
 *
 * See `stackOutputConfig`.
 */
export type StackOutputGetter<T> = <
  K extends keyof StackOutputValues<T> & string,
>(
  key: K,
) => StackOutputValues<T>[K];
```

### Wrap the Automation API

We have a few functionalities that we can expand on and implement in just the way we like, so we put them in a file
called `runPulumiProject.ts`.

```typescript
// runPulumiProject.ts
import {
  ConfigMap,
  LocalProgramArgs,
  LocalWorkspace,
  OpMap,
  PreviewResult,
  Stack,
  UpResult
} from '@pulumi/pulumi/automation';
```

For the purposes of this demo repo, we added a formatter as well, but it's not necessary for the functionality:

```typescript
import chalk from 'chalk';
import { Formatter } from './outputFormatter';
```

And we import the output mappings we abstracted away in the stack module, above.

```typescript
import { OutputMap, Unwrapped } from './stackModule';
```

We can now decide how we want to implement our automation options.

Let's define the options we'd like this program to be able to run with. We need:

1. Directory name
2. Project name
3. Stack name
4. Pulumi operation to run
5. Extra configuration (so we can pass in that kubeconfig)
6. The formatter
7. Stack outputs

```typescript
// runPulumiProject.ts
interface PulumiRunOptions {
    dir: string;
    project: string;
    stackName: string;
    operation: 'up' | 'preview' | 'destroy';
    additionalConfig: ConfigMap;
    formatter: Formatter;
}
interface PulumiRunResult<T> {
    stack: Stack;
    projectName: string;
    outputs: OutputMap<Unwrapped<T>>;
}
```

In this example, the pulumi commands we automate are:

1. Preview
2. Up
3. Destroy

```typescript
export async function runPulumiProject<T extends object>({
  dir, project, stackName, operation, additionalConfig, formatter,
}: PulumiRunOptions): Promise<PulumiRunResult<T> | undefined> {
  const localProgramArgs: LocalProgramArgs = {
    stackName,
    workDir: dir,
  };
  const stack = await LocalWorkspace.createOrSelectStack(localProgramArgs, {});

  formatter(`Spinning up stack ${project}/${stackName}`);
  await stack.setAllConfig({
    ...additionalConfig,
  });

  formatter('Refreshing');
  await stack.refresh();

  let result: UpResult | PreviewResult;
  let status: string = 'succeeded';
  let outputs: OutputMap<Unwrapped<T>>;
  let summaryMessage: string | undefined;
  let operations: OpMap;
  switch (operation) {
    case 'preview':
      formatter('Previewing');

      const previewResult = await stack.preview({ onOutput: formatter });
      operations = previewResult.changeSummary;
      outputs = (await stack.outputs()) as OutputMap<Unwrapped<T>>;
      break;
    case 'up':
      formatter('Deploying');

      const upResult = await stack.up({ onOutput: formatter });
      operations = upResult.summary.resourceChanges;
      status = upResult.summary.result;
      summaryMessage = upResult.summary.message;
      outputs = upResult.outputs as OutputMap<Unwrapped<T>>;
      break;
    case 'destroy':
      formatter('Destroying');

      const destroyResult = await stack.destroy({ onOutput: formatter });
      operations = destroyResult.summary.resourceChanges;
      status = destroyResult.summary.result;
      summaryMessage = destroyResult.summary.message;
      break;
  }

  if (status !== 'succeeded') {
    formatter(result.stderr);
    formatter(summaryMessage);
    throw new Error();
  }

  if (operations) {
    formatter('Succeeded! Resource summary:');
    const fmtNum = (num?: number) => `${num}`.padStart(3);
    if (operations?.create) {
      formatter(`${fmtNum(operations?.create)} ${chalk.green('created')}`);
    }
    if (operations?.replace) {
      formatter(`${fmtNum(operations?.replace)} ${chalk.magenta('replaced')}`);
    }
    if (operations?.update) {
      formatter(`${fmtNum(operations?.update)} ${chalk.yellow('updated')}`);
    }
    if (operations?.same) {
      formatter(`${fmtNum(operations?.same)} ${chalk.bold('unchanged')}`);
    }
  }

  return {
    stack,
    projectName: project,
    outputs: outputs as OutputMap<Unwrapped<T>>,
  };
}
```

In addition, this code gives us the ability to take a stack's Output and apply it to another stack, which is what we
will do next, in our top-level `index.js` file.

### Putting it all together

```typescript
// index.js
import { chooseColor, outputFormatter } from './outputFormatter';
import { runPulumiProject } from './runPulumiProject';

interface ClusterOutputs {
    shinyName: string;
    shinyConfig: string;
}
```

`ClusterOutputs` defines the information we need to pass on the kubeconfig to our Kubernetes web app,
and the cluster name to associate each frontend stack with its backend Kubernetes cluster.

Here, we're deploying our `shinyapp` to a local KinD cluster, but we have the ability to add any cluster to this list:

```typescript
const clusters = [
    {name: 'kind-local', cloud: 'kind', nodePort: 32001},
];
```

First, we wait for our clusters to be created (note the `operation: 'up'` being passed):

```typescript
await Promise.allSettled(
    clusters.map(async (clusterDefinition) => {
      let theme = chooseColor();

      const serviceType = clusterDefinition.nodePort ? 'NodePort' : 'LoadBalancer';
      const serviceNodePort = `${clusterDefinition.nodePort ?? 0}`;
      const cluster = await runPulumiProject<ClusterOutputs>({
        dir: './shinycluster',
        project: 'shinycluster',
        stackName: clusterDefinition.name,
        operation: 'up',
        additionalConfig: {
          cloud: { value: clusterDefinition.cloud },
          nodePort: { value: serviceNodePort },
        },
        formatter: outputFormatter(`cluster   ${clusterDefinition.name}`, theme)
      });
    // here we will call runPulumiProject, this time on the web app
    }),
  );
```

And then deploy our web app:

```typescript
runPulumiProject({
    dir: './shinyapp',
    project: 'shinyapp',
    stackName: clusterDefinition.name,
    operation: 'up',
    additionalConfig: {
        kubeconfig: cluster.outputs.shinyConfig,
        serviceType: { value: serviceType },
        serviceNodePort: { value: serviceNodePort },
    },
    formatter: outputFormatter(`app       ${clusterDefinition.name}`, theme)
});
```

Putting it all together:

```typescript
// index.js
import { chooseColor, outputFormatter } from './outputFormatter';
import { runPulumiProject } from './runPulumiProject';

interface ClusterOutputs {
  shinyName: string;
  shinyConfig: string;
}

async function main() {
  const clusters = [
    { name: 'kind-local', cloud: 'kind', nodePort: 32001 },
  ];

  await Promise.allSettled(
    clusters.map(async (clusterDefinition) => {
      let theme = chooseColor();

      const serviceType = clusterDefinition.nodePort ? 'NodePort' : 'LoadBalancer';
      const serviceNodePort = `${clusterDefinition.nodePort ?? 0}`;
      const cluster = await runPulumiProject<ClusterOutputs>({
        dir: './shinycluster',
        project: 'shinycluster',
        stackName: clusterDefinition.name,
        operation: 'up',
        additionalConfig: {
          cloud: { value: clusterDefinition.cloud },
          nodePort: { value: serviceNodePort },
        },
        formatter: outputFormatter(`cluster   ${clusterDefinition.name}`, theme)
      });

      runPulumiProject({
        dir: './shinyapp',
        project: 'shinyapp',
        stackName: clusterDefinition.name,
        operation: 'up',
        additionalConfig: {
          kubeconfig: cluster.outputs.shinyConfig,
          serviceType: { value: serviceType },
          serviceNodePort: { value: serviceNodePort },
        },
        formatter: outputFormatter(`app       ${clusterDefinition.name}`, theme)
      });
    }),
  );
}

main();

```

### Run the program

All that is left to do is run our top-level program:

```bash
$ ts-node ./index.js
```

Once that's done running, go visit your webapp appear on localhost with the specified port:

```bash
$ curl localhost:32002
<!DOCTYPE html>
<html>

<head>
  <meta http-equiv="Content-Type" content="text/html" charset="utf-8">
</head>

<body>
  <h1>Made with love by Pulumi!</h1>
</body>

</html>
```

## Summary

1. We chose some cloud providers  for bringing up Kubernetes clusters
2. We created a ShinyCluster custom resource that abstracts away any cloud provider implementation details, giving us
   a small set of defaults we care about
3. We programmatically deployed infrastructure using the Automation API
4. We deployed an app to this infrastructure, also using Automation API.

We hope you have gotten a little bit of inspiration from our whirlwind tour through these Pulumi features.
Happy coding!
