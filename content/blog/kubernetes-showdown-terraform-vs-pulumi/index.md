---
title: "Kubernetes Showdown: Terraform vs Pulumi"
authors: ["levi-blackstone"]
tags: ["Kubernetes"]
date: "2019-07-10"

 meta_image: "RELATIVE_TO_PAGE/feature.png"
 meta_description: Terraform vs Pulumi: Let’s see how Pulumi’s Kubernetes support stacks up against Terraform as we work through several examples.
---

It’s time for a showdown: [Terraform vs Pulumi]. We'll go through each of the examples from Hashicorp’s recent 
Kubernetes-focused [blog post][tf-blog-post] so you can see the difference for yourself.

## ExternalDNS Deployment

This example shows how to create a `Deployment` resource in Kubernetes, first with Terraform HCL, and then with Pulumi.

Terraform HCL
```hcl-terraform
locals {
  name = "external-dns"
}

resource "aws_route53_zone" "dev" {
  name = "dev.${var.domain}"
}

resource "kubernetes_deployment" "external_dns" {
  metadata {
    name      = local.name
    namespace = var.namespace
  }

  spec {
    selector {
      match_labels = {
        app = local.name
      }
    }

    template {
      metadata {
        labels = {
          app = local.name
        }
      }

      spec {
        container {
          name  = local.name
          image = var.image
          args = concat([
            "--source=service",
            "--source=ingress",
            "--domain-filter=${aws_route53_zone.dev.name}",
            "--provider=${var.cloud_provider}",
            "--policy=upsert-only",
            "--registry=txt",
            "--txt-owner-id=${aws_route53_zone.dev.zone_id}"
          ], var.other_provider_options)
        }

        service_account_name = local.name
      }
    }

    strategy {
      type = "Recreate"
    }
  }
}
```

Pulumi Typescript
```typescript
import * as aws from "@pulumi/aws";
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const ns = new k8s.core.v1.Namespace("example");
const zone = new aws.route53.Zone("dev", {name: config.require("zone")});

const appName = "external-dns";
const labels = {app: appName};
new k8s.apps.v1.Deployment(appName, {
    metadata: {namespace: ns.metadata.name},
    spec: {
        selector: {matchLabels: labels},
        template: {
            metadata: {labels: labels},
            spec: {
                containers: [{
                    name: appName,
                    image: config.get("image") || "registry.opensource.zalan.do/teapot/external-dns:latest",
                    args: [
                        "--source=service",
                        "--source=ingress",
                        pulumi.concat("--domain-filter=", zone.name),
                        pulumi.concat("--provider=", config.require("provider")),
                        "--policy=upsert-only",
                        "--registry=txt",
                        pulumi.concat("--txt-owner-id=", zone.zoneId)
                    ]
                }],
                serviceAccountName: appName
            },
            strategy: {type: "Recreate"}
        }
    }
});
```

There are a few important differences to highlight here:
1. Pulumi exposes the full API surface of Kubernetes. You can use any `ApiVersion` rather than only the latest version, as in the Terraform provider.
1. Pulumi [auto-names resources] by default, making it easy to avoid naming conflicts as you manage resources over time.
In this example, the `Deployment` resource will be auto-named something like `external-dns-7781rdyq`
1. Since Pulumi uses real programming languages, you can use language features like functions and classes to move away from this "assembly language" layer, and the copy-paste workflows that typically accompany it. Here's one way this could be rewritten with a helper function:

```typescript
function ExternalDNSDeployment(
  namespace?: string,
  zone?: aws.route53.zone): k8s.apps.v1.Deployment {
// ...
}

new ExternalDNSDeployment(ns.metadata.name)
```

While these examples show you how you can manage Kubernetes resources natively with Pulumi or Terraform, many teams already are already using YAML manifests for this purpose. Rather than requiring a rewrite up front, Pulumi gives you the option to use the manifest directly. This provides all the benefits of Pulumi with a minimal amount of effort to get going. Then, you can refactor this code over time without disrupting your deployed resources.

```typescript
new k8s.yaml.ConfigFile("external-dns", {file: "filepath-or-url-to-manifest"});
```

## Kubernetes DaemonSets

This example shows off the new `dynamic` syntax in Terraform `0.12`. While it's an improvement over the very verbose pre-`0.12` syntax, it's not what k8s users are used to seeing.

```hcl-terraform
env_variables = {
  "HOST" : "elasticsearch-logging",
  "PORT" : var.port,
  "SCHEME" : "http",
  "USER" : var.user,
  "PASSWORD" : var.password
}

dynamic "env" {
  for_each = local.env_variables
  content {
    name  = "FLUENT_ELASTICSEARCH_${env.key}"
    value = env.value
  }
}
```

```typescript
env: {
    FLUENT_ELASTICSEARCH_HOST: "elasticsearch-logging",
    FLUENT_ELASTICSEARCH_PORT: config.get("port") || 9200,
    FLUENT_ELASTICSEARCH_SCHEME: "http",
    FLUENT_ELASTICSEARCH_USER: config.get("user") || "elastic",
    FLUENT_ELASTICSEARCH_PASSWORD: config.getSecret("password") || new random.RandomString(
        "es-password", {length: 16, special: true})
}
```

Here we see a few advantages of using a real language rather than a domain specific language like HCL to manage k8s resources:

1. No special syntax is required. Declaring environment variables is clear and concise. The schema is generated directly from the Kubernetes API spec, so it doesn't require any mental translation.
1. It's easy to mix in bits of conditional logic like we see for the password field. If a secret value is not present in the stack configuration, Pulumi will automatically generate one.

## Managing Helm Charts via Pulumi

In this final example, we see the difference between the Helm providers in Terraform and Pulumi.

```hcl-terraform
provider "helm" {
  version        = "~> 0.9"
  install_tiller = true
}

resource "helm_release" "consul" {
  name      = var.name
  chart     = "${path.module}/consul-helm"
  namespace = var.namespace

  set {
    name  = "server.replicas"
    value = var.replicas
  }

  set {
    name  = "server.bootstrapExpect"
    value = var.replicas
  }

  set {
    name  = "server.connect"
    value = true
  }

  provisioner "local-exec" {
    command = "helm test ${var.name}"
  }
}
```

```typescript
new k8s.helm.v2.Chart("consul", {
    path: "consul-helm", // local copy of chart repo
    namespace: config.get("namespace") || "default",
    values: {
        server: {
            replicas: config.get("replicas") || 3,
            bootstrapExpect: config.get("bootstrapExpect") || 3,
            connect: config.get("connect") || true,
        }
    }
});
```

![consul-demo](./consul-demo.gif)

The differences here are substantial:

1. Pulumi's Helm support does not require Tiller.
1. Pulumi provides a rich preview and status updates as the resources from the chart are deployed.
1. Pulumi's Helm SDK includes a [transformations parameter] that can be used to customize the Helm deployment without
 requiring changes to the actual chart.

## Learn more

If you’d like to learn about Pulumi and how to manage your infrastructure and Kubernetes through code, [click here to get started today][quickstart]. Pulumi is open source and free to use.

As always, you can check out our code on [GitHub], follow us on [Twitter], subscribe to our [YouTube channel], or join our [Community Slack] channel if you have any questions, need support, or just want to say hello.

If you’d like to chat with our team, or get hands-on assistance with migrating your existing configuration code (including Terraform HCL programs) to Pulumi, [please don’t hesitate to drop us a line][contact].

[Terraform vs Pulumi]: https://www.pulumi.com/docs/reference/vs/terraform/
[tf-blog-post]: https://www.hashicorp.com/blog/using-the-kubernetes-and-helm-providers-with-terraform-0-12
[auto-names resources]: https://pulumi.io/reference/programming-model/#autonaming
[transformations parameter]: https://pulumi.io/reference/pkg/nodejs/pulumi/kubernetes/helm/v2/#ChartOpts-transformations
[quickstart]: https://pulumi.io/quickstart
[GitHub]: https://github.com/pulumi
[Twitter]: https://twitter.com/pulumicorp
[YouTube channel]: https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw
[Community Slack]: https://slack.pulumi.io/
[contact]: https://www.pulumi.com/contact/

Meta description:
Terraform vs Pulumi: Let’s see how Pulumi’s Kubernetes support stacks up against Terraform as we work through several examples.
