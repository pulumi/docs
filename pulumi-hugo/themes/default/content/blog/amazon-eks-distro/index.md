---
title: "Getting Started with Amazon EKS Distro & Pulumi"
date: 2020-12-01T11:30:00-08:00
draft: false
meta_desc: Use Pulumi to provision an Amazon EKS Distro cluster.
meta_image: meta.png
authors:
    - luke-hoban
    - lee-briggs
tags:
    - kubernetes
    - eks
---

As Kubernetes grows in popularity, the number of options for Kubernetes users continues to increase. Providers of managed Kubernetes offerings will often learn lessons about operating large numbers of clusters at scale; it's increasingly common that they will contribute this knowledge back to the ecosystem, allowing those organizations who need more control and flexibility to reap the benefits.

With the announcement of the [Amazon EKS Distro](https://aws.amazon.com/blogs/opensource/introducing-amazon-eks-distro/) during AWS re:Invent, the Amazon EKS team has contributed back to the cloud-native community in a big way. In this post, we'll take a brief look at what the Amazon EKS Distro is, explore why you might choose this over current managed service offerings and finally, explore how you can get started with the Amazon EKS Distro on day 1 using Pulumi.

<!--more-->

Kubernetes is a complex, distributed system that consists of many components that operate together to create the Kubernetes experience. If you're using a managed Kubernetes service, often these components are hidden away from you as a user to reduce the operational complexity and ease the usage. The managed service provider will take care of tricky problems like upgrades and taking care of patching and compliance.

The Amazon EKS Distro is the packaging of many of the components needed to run a Kubernetes cluster distributed in an opinionated way by the Amazon EKS team. Parts of a working Kubernetes cluster like the scheduler, API server and the backing database (etcd) have been built into Docker images based on Amazon Linux. The images have backported security fixes for each Kubernetes version and are drop-in replacements for the upstream Kubernetes distribution, meaning you get all the benefits of Kubernetes, with the added support of knowing you're running a verified and supported version from the Amazon EKS team.

## Why use the Amazon EKS Distro?

If you're already a user of Amazon EKS, you're already getting all of the benefits provided by the Amazon EKS Distro. However, many users aren't utilizing the managed Kubernetes cluster provided by the Amazon EKS team, either through choice or because of external requirements. The release of the Amazon EKS Distro means that those organizations can get the benefits provided by EKS, such as secure Docker images, backported security fixes and a single upstream vendor, without having to operate with the constraints a managed service in AWS might provide.

## Provisioning an Amazon EKS Distro Cluster with Pulumi

Installing an Amazon EKS Distro cluster involves bootstrapping a Kubernetes cluster but with the images provided by the Amazon EKS team. The simplest way to provision a Kubernetes cluster is using [kops](https://kops.sigs.k8s.io/) and the Amazon EKS Distro team provides instructions on how to replace the default Kubernetes components with the Amazon EKS Distro built parts.

It's possible to get all of the benefits of provisioning a Kubernetes cluster with kops while also taking part in the Pulumi resource lifecycle. Pulumi offers support for running arbitrary commands using [dynamic providers]({{< relref "/docs/intro/concepts/resources#dynamicproviders" >}}) (available in the JavaScript, Typescript and Python SDKs) and you can register the kops commands used to create and destroy clusters as dynamic provider callbacks. Once your Kubernetes cluster has been created, you can provision Kubernetes resources using Pulumi's Kubernetes provider, using the Pulumi resource model to set dependencies on the created cluster.

### Creating an Amazon EKS Distro cluster with Pulumi

Using a Pulumi dynamic provider, you can define an Amazon EKS Distro cluster using just a few lines of code:

```typescript
import * as eksdistro from "./eksdistro";

const store = new aws.s3.Bucket("kops-state-store");
const cluster = new eksdistro.Cluster("cluster", {
  name: "luke.cluster.pulumi-demos.net",
  state: pulumi.interpolate`s3://${store.id}`,
```

Behind the scenes, we've defined a Typescript dynamic provider, which renders a kops configuration file and renders it to disk using [mustache](https://mustache.github.io/). This kops configuration file references the Amazon EKS Distro images.

This dynamic provider registers callbacks for creating, updating and deleting the cluster and also registers the created cluster's kubeconfig as a Pulumi output, which can be passed to Kubernetes resources in Pulumi.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as cp from "child_process";
import * as path from "path";
import * as fs from "fs";
import * as mustache from "mustache";
import * as tmp from "tmp";

interface ClusterProviderArgs {
    // KOPS_STATE_STORE
    state: string;
    // KOPS_CLUSTER_NAME
    name: string;
}

const clusterYamlTemplate = fs.readFileSync(path.join(__dirname, "cluster.yaml")).toString();
const authenticatorYamlTemplate = fs.readFileSync(path.join(__dirname, "aws-iam-authenticator.yaml")).toString();

const clusterprovider: pulumi.dynamic.ResourceProvider = {
    async create(inputs: ClusterProviderArgs): Promise<pulumi.dynamic.CreateResult> {
        const clusterYaml = mustache.render(clusterYamlTemplate, {
            CLUSTER_NAME: inputs.name,
            STATE_STORE: inputs.state,
        });
        console.log("kops create")
        const createOut = cp.execSync(`kops create --name ${inputs.name} --state ${inputs.state} -f -`, { input: clusterYaml });
        console.log(createOut.toString());
        console.log("kops create secret")
        const createSecretOut = cp.execSync(`kops create secret --name ${inputs.name} --state ${inputs.state} sshpublickey admin -i ~/.ssh/id_rsa.pub`);
        console.log(createSecretOut.toString());

        let outs = { ...inputs };
        try {
            const updateRes = await this.update!(inputs.name, {}, inputs);
            outs = { ...outs, ...updateRes.outs};
        } catch (err) {
            console.log(err);
        }

        return {
            id: inputs.name,
            outs,
        };
    },
    async update(id: pulumi.ID, olds: any, inputs: any): Promise<pulumi.dynamic.UpdateResult> {
        const clusterYaml = mustache.render(clusterYamlTemplate, {
            CLUSTER_NAME: inputs.name,
            STATE_STORE: inputs.state,
        });
        const authenticatorYaml = mustache.render(authenticatorYamlTemplate, {
            CLUSTER_NAME: inputs.name,
        });

        console.log("kops update cluster")
        const updateOut = cp.execSync(`kops update cluster --name ${inputs.name} --state ${inputs.state} --yes`);
        console.log(updateOut.toString());

        console.log("kops export kubecfg")
        const kubeConfigName = tmp.tmpNameSync();
        const exportKubeconfigOut = cp.execSync(`kops export kubecfg --name ${inputs.name} --state ${inputs.state} --kubeconfig ${kubeConfigName}`);
        const kubeconfig = fs.readFileSync(kubeConfigName).toString();
        console.log(exportKubeconfigOut.toString());

        // Needed to allow cluster to come available and DNS to propagate
        try {
            console.log("kops validate cluster")
            const validateOut = cp.execSync(`kops validate cluster --wait 2m --name ${inputs.name} --state ${inputs.state}`);
            console.log(validateOut.toString());

            console.log("kubectl apply -f aws-iam-authenticator.yaml");
            const authApplyOut = cp.execSync(`kubectl apply -f -`, { input: authenticatorYaml });
            console.log(authApplyOut.toString());
        } catch (err) {
            console.log(err);
        }

        return {
            outs: {
                ...inputs,
                kubeconfig,
            },
        }
    },
    async delete(id: pulumi.ID, inputs: any) {
        const clusterYaml = mustache.render(clusterYamlTemplate, {
            CLUSTER_NAME: inputs.name,
            STATE_STORE: inputs.state,
        });
        console.log("kops delete")
        const deleteOut = cp.execSync(`kops delete --name ${inputs.name} --state ${inputs.state} --yes -f -`, { input: clusterYaml });
        console.log(deleteOut.toString());
    },
}

export interface ClusterArgs {
        // KOPS_STATE_STORE
        state: pulumi.Input<string>;
        // KOPS_CLUSTER_NAME
        name: pulumi.Input<string>;
        keeper?: pulumi.Input<number>;
}

export class Cluster extends pulumi.dynamic.Resource {
    kubeconfig!: pulumi.Output<string>;
    constructor(name: string, args: ClusterArgs, opts?: pulumi.CustomResourceOptions) {
        super(clusterprovider, name, {
            ... args,
            kubeconfig: undefined,
        }, opts);
    }
}
```

Once the cluster is created, we can build a Kubernetes provider and register resources like any other Kubernetes cluster:

```typescript

const k8sProvider = new k8s.Provider("provider", { kubeconfig: cluster.kubeconfig });
const pod = new k8s.core.v1.Pod("mypod", {
    spec: {
        containers: [{ name: "echo", image: "k8s.gcr.io/echoserver:1.4" }],
    }
}, { provider: k8sProvider });
export const kubeconfig = cluster.kubeconfig;
```

The full code for defining an Amazon EKS Distro cluster using Pulumi can be found in our [examples repo](https://github.com/pulumi/examples/tree/master/aws-ts-eks-distro)

## Wrap up

The Amazon EKS Distro opens lots of avenues for users needing more flexibility and control over their Kubernetes clusters while still providing the security, compliance and reliability required to feel confident in the clusters you're building. With Pulumi, you can bootstrap Amazon EKS Distro clusters and leverage Pulumi's best-in-class Kubernetes resource management while still benefiting from the power of Pulumi's modern programming languages. Give it a try!
