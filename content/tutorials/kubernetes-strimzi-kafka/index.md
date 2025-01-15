---
title_tag: Deploying Kafka on Kubernetes using Strimzi and Pulumi
allow_long_title: true
title: Deploying Kafka on Kubernetes using Strimzi and Pulumi
layout: single
description: |
  Learn how to deploy a Kafka cluster on Kubernetes using Strimzi and Pulumi.
meta_desc: Learn how to deploy a Kafka cluster on Kubernetes using Strimzi and Pulumi.
meta_image: meta.png
weight: 999
summary: |
  In this guide, we will use [Pulumi](https://www.pulumi.com/) to provision the [Strimzi Kafka Operator](https://strimzi.io/) on a Kubernetes cluster. We’ll then create a Kafka cluster using Custom Resources provided by Strimzi.
youll_learn:
- How to use Pulumi to manage your Kubernetes resources
- How to use Strimzi to deploy a Kafka cluster on Kubernetes
estimated_time: 10
collections_weight: 2
prereqs:
- "A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)"
- "The [Pulumi CLI](/docs/install/)"
- "A Kubernetes cluster (for example, [kind](https://kind.sigs.k8s.io/))"
- "[kubectl](https://kubernetes.io/releases/download/#kubectl)"
- "[helm](https://helm.sh/docs/intro/install/)"
collections:
- kubernetes
---

## What is Strimzi?

[Strimzi](https://strimzi.io/) is an open-source project that provides a way to run an Apache Kafka cluster on
Kubernetes. It provides operators and custom resources to deploy and manage Kafka clusters on Kubernetes.

It is a CNCF project and is widely used in the Kubernetes community to deploy Kafka clusters as it makes it very easy
handle the lifecycle of Kafka clusters. Before Strimzi, deploying Kafka on Kubernetes was a complex task with many
manual steps. From creating topics to managing brokers, everything was a manual task.

## Project Setup

Initialize a new Pulumi project in an empty directory. We’ll use TypeScript for this example:

```bash
mkdir pulumi-strimzi
cd pulumi-strimzi
# Choose your favorite Pulumi supported language
pulumi new kubernetes-<your-programming-language>
```

This will create a new Pulumi project with the necessary files to deploy resources on Kubernetes. As we are using
pre-built templates, we don’t need to write the boilerplate code to bootstrap the project.

## Install Strimzi

To install Strimzi, we need to add the Strimzi Helm repository and install the Strimzi Kafka Operator:

Replace the content of created Pulumi program with the following code:

{{< chooser language "typescript,python,go,csharp,yaml" />}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="helm-kubernetes-part-one" language="typescript" from="1" to="45" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="helm-kubernetes-part-one" language="python" from="1" to="47" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="helm-kubernetes-part-one" language="go" from="1" to="66" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="helm-kubernetes-part-one" language="csharp" from="1" to="59" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="helm-kubernetes-part-one" language="yaml" from="1" to="53" >}}
```

{{% /choosable %}}

## Create a Kafka Cluster

Once the Strimzi operator is installed, we can create a Kafka cluster by defining a Kafka Custom Resource. Strimzi provides a CRD that we will rely on.

Add this after your Helm chart code:

{{< chooser language "typescript,python,go,csharp,yaml" />}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="helm-kubernetes-part-one" language="typescript" from="1" to="45" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="helm-kubernetes-part-one" language="python" from="1" to="47" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="helm-kubernetes-part-one" language="go" from="1" to="66" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="helm-kubernetes-part-one" language="csharp" from="1" to="59" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="helm-kubernetes-part-one" language="yaml" from="1" to="53" >}}
```

{{% /choosable %}}

Background:

* We create a dedicated namespace called `kafka` (optional, but often recommended).
* We define a `Kafka` custom resource that:
* Uses `apiVersion: kafka.strimzi.io/v1beta2`.
* Creates a 3-node Kafka broker
* Sets up both plaintext (plain) and TLS listeners (tls).
* Includes the Entity Operator, which manages users and topics.

## Creating a Kafka User (Optional)

Strimzi also provides a `KafkaUser` CRD to manage Kafka users. Here’s an example of how you might create one for your cluster:

{{< chooser language "typescript,python,go,csharp,yaml" />}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="helm-kubernetes-part-one" language="typescript" from="1" to="45" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="helm-kubernetes-part-one" language="python" from="1" to="47" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="helm-kubernetes-part-one" language="go" from="1" to="66" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="helm-kubernetes-part-one" language="csharp" from="1" to="59" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="helm-kubernetes-part-one" language="yaml" from="1" to="53" >}}
```

{{% /choosable %}}

## Deploying the Kafka Cluster

Now run the `pulumi up` command to preview and deploy the resources you’ve just defined in your project.

```bash
pulumi up
Please choose a stack, or create a new one: dev
Previewing update (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/dirien/helm/dev/previews/88cf6d4c-d4a4-401f-9b25-cedd50146545

     Type                              Name               Plan
 +   pulumi:pulumi:Stack               helm-dev           create
 +   ├─ kubernetes:core/v1:Namespace   ingressns          create
 +   └─ kubernetes:helm.sh/v3:Release  ingresscontroller  create

Outputs:
    name: "ingresscontroller-7e4b854f"

Resources:
    + 3 to create

Do you want to perform this update? yes
Updating (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/dirien/helm/dev/updates/1

     Type                              Name               Status
 +   pulumi:pulumi:Stack               helm-dev           created (15s)
 +   ├─ kubernetes:core/v1:Namespace   ingressns          created (0.32s)
 +   └─ kubernetes:helm.sh/v3:Release  ingresscontroller  created (7s)

Outputs:
    name: "ingresscontroller-b5455c41"

Resources:
    + 3 created

Duration: 17s
```

Pulumi will:

* Install the Strimzi Kafka Operator via Helm.
* Create a namespace called kafka.
* Create a Kafka cluster.
* Optionally create a Kafka user.

After confirming, Pulumi will provision your Kafka stack. You can then verify the resources with kubectl:

```bash 
kubectl get pods -n kafka
kubectl get kafka -n kafka
kubectl get kafkauser -n kafka
```

## Housekeeping

Before moving on, tear down the resources that are part of your stack to avoid incurring any charges.

1. Run `pulumi destroy` to tear down all resources. You'll be prompted to make sure you really want to delete these resources. A destroy operation may take some time, since Pulumi waits for the resources to finish shutting down before it considers the destroy operation to be complete.
2. To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Service.

## Next steps

In this tutorial, you learned how to install Helm on Kubernetes using the Kubernetes provider from Pulumi and the `Release` resource.

- Learn more about Pulumi and Kubernetes in the [Kubernetes documentation](/docs/iac/clouds/kubernetes/).
- Learn more about the `Release` resource in the [Pulumi Kubernetes API documentation](/registry/packages/kubernetes/api-docs/helm/v3/release/).
- Try the out the `Chart` [tutorial](/tutorials/kubernetes-helm-part-two) to learn how to install Helm charts on Kubernetes using the `Chart` resource.
- Or give the tutorial about [Creating Resources on Kubernetes](/tutorials/creating-resources-kubernetes/) a try.
