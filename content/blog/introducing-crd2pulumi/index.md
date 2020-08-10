---
title: "Introducing crd2pulumi: Typing for CustomResources"
date: 2020-08-12
draft: true
meta_desc: Generate Kubernetes CustomResource types in TypeScript, Python, C#, and Go.
meta_image: meta.png
authors:
    - levi-blackstone
    - albert-zhong
tags:
    - Kubernetes
---

We're proud to introduce crd2pulumi, a CLI tool that generates strongly-typed CustomResources based on a Kubernetes CRD.
CustomResourceDefinitions allow you to extend the Kubernetes API by defining your schemas for custom objects.
Pulumi lets you create a [CustomResourceDefinition] (CRD) and associated [CustomResource]s, but previously there was no
strong-typing for these objects since every schema was, well, custom. This can be a massive headache for popular CRDs
such as [cert-manager] or [Istio], which contain thousands of lines of complex YAML schemas. By generating
strongly-typed versions of CustomResources, crd2pulumi makes filling out their arguments more convenient because it
lets you leverage existing IDE type checking and autocomplete features.

Currently, this tool only generates strongly-typed CustomResources for TypeScript and Go, but support for Python
and .NET is coming soon.

## Example usage

Let's test crd2pulumi on the example [CronTab CRD] specified in the Kubernetes Documentation.

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  # name must match the spec fields below, and be in the form: <plural>.<group>
  name: crontabs.stable.example.com
spec:
  # group name to use for REST API: /apis/<group>/<version>
  group: stable.example.com
  # list of versions supported by this CustomResourceDefinition
  versions:
	- name: v1
  	# Each version can be enabled/disabled by Served flag.
  	served: true
  	# One and only one version must be marked as the storage version.
  	storage: true
  	schema:
    	openAPIV3Schema:
      	type: object
      	properties:
        	spec:
          	type: object
          	properties:
            	cronSpec:
              	type: string
            	image:
              	type: string
            	replicas:
              	type: integer
  # either Namespaced or Cluster
  scope: Namespaced
  names:
	# plural name to be used in the URL: /apis/<group>/<version>/<plural>
	plural: crontabs
	# singular name to be used as an alias on the CLI and for display
	singular: crontab
	# kind is normally the CamelCased singular type. Your resource manifests use this.
	kind: CronTab
	# shortNames allow shorter string to match your resource on the CLI
	shortNames:
	- ct
```

Download this YAML file as `resourcedefinition.yaml` and run the command:

```bash
$ crd2pulumi nodejs resourcedefinition.yaml
```

By default, this creates the folder `crontabs/` in the same directory as the YAML
file. That folder contains two useful classes: `v1.CronTab` and `CronTabDefinition`. Now you can instantiate a Pulumi project and import the generated code as `crontabs`. In this example, we provisioned the CronTab CRD and created an instance of it.

```typescript
import * as crontabs from "./crontabs"
import * as pulumi from "@pulumi/pulumi"

const cronTabDefinition = new crontabs.CronTabDefinition("my-crontab-definition")

const myCronTab = new crontabs.v1.CronTab("my-new-cron-object",
{
	metadata: {
    	name: "my-new-cron-object",
	},
	spec: {
    	cronSpec: "* * * * */5",
    	image: "my-awesome-cron-image",
	}
})

export const urn = myCronTab.urn;
```

As you can see, the `v1.CronTab` object is strongly-typed. So if you try to set
`cronSpec` to a non-string or add an extra field, your IDE should immediately tell you. Also, the `CronTabDefinition` class lets you create the CRD with a single line, whereas previously you would manually write out the entire `resourcedefinition.yaml` schema as a `k8s.apiextensions.v1.CustomResourceDefinition` object.

Now let's run the program and perform the update.

```bash
$ pulumi up
```

```bash
Previewing update (dev):
 	Type                                                     	Name               	Plan
 	pulumi:pulumi:Stack                                      	examples-dev
 +   ├─ kubernetes:stable.example.com:CronTab                 	my-new-cron-object 	create
 +   └─ kubernetes:apiextensions.k8s.io:CustomResourceDefinition  my-crontab-definition  create

Resources:
	+ 2 to create
	1 unchanged

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details
```

```bash
Do you want to perform this update? yes
Updating (dev):
 	Type                                                     	Name               	Status
 	pulumi:pulumi:Stack                                      	examples-dev
 +   ├─ kubernetes:stable.example.com:CronTab                 	my-new-cron-object 	created
 +   └─ kubernetes:apiextensions.k8s.io:CustomResourceDefinition  my-crontab-definition  created

Outputs:
	urn: "urn:pulumi:dev::examples::kubernetes:stable.example.com/v1:CronTab::my-new-cron-object"

Resources:
	+ 2 created
	1 unchanged

Duration: 17s

Permalink: https://app.pulumi.com/albert-zhong/examples/dev/updates/4
```

It looks like both the CronTab definition and instance were both created! Finally, let's verify that they were created
by manually viewing the raw YAML data:

```bash
$ kubectl get ct -o yaml
```

```bash
- apiVersion: stable.example.com/v1
  kind: CronTab
  metadata:
	annotations:
  	kubectl.kubernetes.io/last-applied-configuration: |
    	{"apiVersion":"stable.example.com/v1","kind":"CronTab","metadata":{"labels":{"app.kubernetes.io/managed-by":"pulumi"},"name":"my-new-cron-object"},"spec":{"cronSpec":"* * * * */5","image":"my-awesome-cron-image"}}
	creationTimestamp: "2020-08-10T09:50:38Z"
	generation: 1
	labels:
  	app.kubernetes.io/managed-by: pulumi
	name: my-new-cron-object
	namespace: default
	resourceVersion: "1658962"
	selfLink: /apis/stable.example.com/v1/namespaces/default/crontabs/my-new-cron-object
	uid: 5e2c56a2-7332-49cf-b0fc-211a0892c3d5
  spec:
	cronSpec: '* * * * */5'
	image: my-awesome-cron-image
kind: List
metadata:
  resourceVersion: ""
  selfLink: ""
```

## Learn More

If you'd like to learn about Pulumi and how to manage your
infrastructure and Kubernetes through code, [get started today]({{< relref "/docs/get-started" >}}). Pulumi is open
source and free to use.

For further examples on how to use Pulumi to create Kubernetes
clusters, or deploy workloads to a cluster, check out the rest of the
[Kubernetes tutorials]({{< relref "/docs/tutorials/kubernetes" >}}).

As always, you can check out our code on
[GitHub](https://github.com/pulumi), follow us on
[Twitter](https://twitter.com/pulumicorp), subscribe to our [YouTube
channel](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw), or
join our [Community Slack](https://slack.pulumi.com/) channel if you have
any questions, need support, or just want to say hello.

<!-- markdownlint-disable url -->
[cert-manager]: https://github.com/jetstack/cert-manager/tree/master/deploy/crds
[CronTab CRD]: https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#create-a-customresourcedefinition
[CustomResource]: {{< ref "/docs/reference/pkg/kubernetes/apiextensions/customresource" >}}
[CustomResourceDefinition]: {{< ref "docs/reference/pkg/kubernetes/apiextensions/v1/customresourcedefinition" >}}
[Istio]: https://github.com/istio/istio/tree/0321da58ca86fc786fb03a68afd29d082477e4f2/manifests/charts/base/crds
<!-- markdownlint-enable url -->
