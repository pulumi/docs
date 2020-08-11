---
title: "Introducing crd2pulumi: Typed CustomResources for Kubernetes"
date: 2020-08-12
draft: true
meta_desc: Generate Kubernetes CustomResource types in TypeScript, Python, C#, and Go.
meta_image: crd.png
authors:
    - levi-blackstone
    - albert-zhong
tags:
    - Kubernetes
---

[CustomResource]s in Kubernetes allow users to extend the API with their types. These types are defined using
[CustomResourceDefinition]s (CRDs), which include an OpenAPI schema. This extensibility is very useful but comes at the
cost of very complex YAML definitions. Our new [crd2pulumi] tool takes the pain out of managing CustomResources by
generating types in the Pulumi-supported language of your choice!

<!--more-->

Pulumi already supports the management of CRDs and their associated CustomResources using the [apiextensions package].
However, these SDK resources are untyped since every schema is, well, custom. While this is fine for simple CRDs, it
quickly becomes complicated for real-world CRDs like [cert-manager] or [Istio]. These CRDs contain thousands of lines of
complex YAML schemas, making it difficult to write CustomResources that adhere to those specs. Programming languages
offer a better path forward. Instead of wrangling error-prone YAML definitions, using types in a programming language
lets you use IDE type checking and autocomplete features!

## Getting Started with crd2pulumi

Let's test `crd2pulumi` on the example [CronTab CRD] specified in the Kubernetes Documentation.

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

Create a file called `crd.yaml` with this definition and then run `crd2pulumi` for your language of choice.

{{% notes type="info" %}}
crd2pulumi supports TypeScript and Go today, and Python and .NET is coming soon.
{{% /notes %}}

By default, this creates the folder `crontabs/` in the same directory as the YAML file. Now you can instantiate a
Pulumi project and import the generated code. In this example, we register the CronTab CRD and then create a CronTab
CustomResource.

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```
$ crd2pulumi nodejs crd.yaml
```

```typescript
import * as crontabs from "./crontabs"
import * as pulumi from "@pulumi/pulumi"

// Register the CronTab CRD.
const cronTabDefinition = new crontabs.CronTabDefinition("my-crontab-definition");

// Instantiate a CronTab resource.
const myCronTab = new crontabs.v1.CronTab("my-new-cron-object",
{
	metadata: {
    	name: "my-new-cron-object",
	},
	spec: {
    	cronSpec: "* * * * */5",
    	image: "my-awesome-cron-image",
        replicas: 3,
	}
});
```

{{% /choosable %}}

{{% choosable language python %}}

*Coming soon!*

{{% /choosable %}}

{{% choosable language csharp %}}

*Coming soon!*

{{% /choosable %}}

{{% choosable language go %}}

```
$ crd2pulumi go crd.yaml
```

```go
package main

import (
	v1 "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/yaml"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        // Register the CronTab CRD.
		_, err := yaml.NewConfigFile(ctx, "my-crontab-definition",
			&yaml.ConfigFileArgs{
				File: "crontabdefinition.yaml",
			},
		)
		if err != nil {
			return err
		}
        // Instantiate a CronTab resource.
		_, err = NewCronTab(ctx, "my-new-cron-object", &CronTabArgs{
			Metadata: &v1.ObjectMetaArgs{
				Name: pulumi.String("my-new-cron-object"),
			},
			Spec: CronTabSpecArgs{
				CronSpec: pulumi.String("* * * * */5"),
				Image:    pulumi.String("my-awesome-cron-image"),
                Replicas: pulumi.IntPtr(3),
			},
		})
		if err != nil {
			return err
		}
		return nil
	})
}
```

{{% /choosable %}}

{{< /chooser >}}

As you can see, the `v1.CronTab` object is strongly-typed. So if you try to set replicas to a string or add an
unsupported argument, your IDE will immediately warn you!

![IDE Usage](ide.gif)

## Cert Manager Example

Now let's examine a [real-world cert-manager example]. In this case, the CRD is over 1200 lines
of YAML, but `crd2pulumi` generates a nice interface so that we don't have to worry about it. Here's
what it looks like to create a `Certificate` CustomResource using our new types.

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}
```ts
import * as certificates from "./certificates"

// Register the Certificate CRD.
new certificates.CertificateDefinition("certificate");

// Instantiate a Certificate resource.
new certificates.v1beta1.Certificate("example-cert", {
    metadata: {
        name: "example-com",
    },
    spec: {
        secretName: "example-com-tls",
        duration: "2160h",
        renewBefore: "360h",
        commonName: "example.com",
        dnsNames: [
            "example.com",
            "www.example.com",
        ],
        issuerRef: {
            name: "ca-issuer",
            kind: "Issuer",
        }
    }
});
```

{{% /choosable %}}

{{% choosable language python %}}

*Coming soon!*

{{% /choosable %}}

{{% choosable language csharp %}}

*Coming soon!*

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/yaml"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

        // Register the Certificate CRD.
		_, err := yaml.NewConfigFile(ctx, "my-certificate-definition",
			&yaml.ConfigFileArgs{
				File: "certificate.yaml",
			},
		)
		if err != nil {
			return err
		}

        // Instantiate a Certificate resource.
		_, err = NewCertificate(ctx, "example-cert", &CertificateArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("example-com"),
			},
			Spec: CertificateSpecArgs{
				SecretName:  pulumi.String("example-com-tls"),
				Duration:    pulumi.String("2160h"),
				RenewBefore: pulumi.String("360h"),
				CommonName:  pulumi.String("example.com"),
				DnsNames: pulumi.StringArray{
					pulumi.String("example.com"),
					pulumi.String("www.example.com"),
				},
				IssuerRef: CertificateSpecIssuerRefArgs{
					Name: pulumi.String("ca-issuer"),
					Kind: pulumi.String("Issuer"),
				},
			},
		})
		if err != nil {
			return err
		}

		return nil
	})
}
```

{{% /choosable %}}

{{< /chooser >}}

Kubernetes can be complex, but Pulumi gives you the tools you need to manage it successfully. With Pulumi superpowers
at your fingertips, you can stop worrying about YAML indentation, and get back to solving the problems you care about!

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
[apiextensions package]: {{< relref "/docs/reference/pkg/kubernetes/apiextensions" >}}
[crd2pulumi]: https://github.com/pulumi/pulumi-kubernetes/tree/master/provider/cmd/crd2pulumi
[cert-manager]: https://github.com/jetstack/cert-manager/tree/master/deploy/crds
[CronTab CRD]: https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#create-a-customresourcedefinition
[CustomResource]: {{< relref "/docs/reference/pkg/kubernetes/apiextensions/customresource" >}}
[CustomResourceDefinition]: {{< relref "docs/reference/pkg/kubernetes/apiextensions/v1/customresourcedefinition" >}}
[Istio]: https://github.com/istio/istio/tree/0321da58ca86fc786fb03a68afd29d082477e4f2/manifests/charts/base/crds
[real-world cert-manager example]: https://docs.cert-manager.io/en/release-0.7/tasks/issuing-certificates/index.html#creating-certificate-resources
<!-- markdownlint-enable url -->
