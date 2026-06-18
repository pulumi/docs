---
title_tag: Install Self-Hosted Pulumi Cloud
meta_desc: Install self-hosted Pulumi Cloud on your platform — evaluate in minutes with Docker Compose, or deploy to production on AWS, Azure, Google Cloud, or Kubernetes.
title: Install
h1: Install Self-Hosted Pulumi Cloud
meta_image: /images/docs/meta-images/docs-meta.png
weight: 1
menu:
  administration:
    name: Install
    parent: administration-self-hosting
    weight: 0
    identifier: administration-self-hosting-install
aliases:
  - /self-hosted/install/
---

Run the full Pulumi Cloud platform in your own cloud account or data center. Start with the all-in-one Docker Compose stack to evaluate in about ten minutes, then choose a production deployment for your platform.

{{% notes "info" %}}
You can evaluate self-hosted Pulumi Cloud yourself — the Docker Compose stack below runs on your own machine in about ten minutes. You'll need an evaluation license key; [get one here](/product/self-hosted/#self-hosted-trial). For production, self-hosted Pulumi Cloud is available with the [Business Critical edition](/pricing/).
{{% /notes %}}

## Choose your platform

{{< chooser cloud "docker,kubernetes,aws,azure,gcp" >}}

{{% choosable cloud docker %}}

The all-in-one Docker Compose stack runs the API, Console, database, and search on a single host — the fastest way to try self-hosted Pulumi Cloud.

```bash
git clone https://github.com/pulumi/pulumi-self-hosted-installers.git
cd pulumi-self-hosted-installers/quickstart-docker-compose
export PULUMI_LICENSE_KEY=<your-license-key>
./scripts/run-ee.sh -f ./all-in-one/docker-compose.yml
```

Then open the Console at [http://localhost:3000](http://localhost:3000), create the first account, and run `pulumi login http://localhost:8080`.

See the [Docker Compose quickstart](/docs/administration/self-hosting/deployment-options/quickstart-docker-compose/) for prerequisites, first login, verification, and teardown.

{{% /choosable %}}

{{% choosable cloud kubernetes %}}

Deploy to your own Kubernetes cluster with MySQL and S3-compatible object storage. This is the most flexible production option and works in any environment, including air-gapped networks.

See [Bring your own infrastructure](/docs/administration/self-hosting/deployment-options/byo-infra-hosted/) for the Kubernetes deployment guide.

{{% /choosable %}}

{{% choosable cloud aws %}}

Deploy a production system on AWS. Two managed options are available:

- [Amazon EKS](/docs/administration/self-hosting/deployment-options/eks-hosted/) — Kubernetes-based, with RDS Aurora, S3, and CloudWatch.
- [Amazon ECS](/docs/administration/self-hosting/deployment-options/ecs-hosted/) — ECS and Fargate, with RDS Aurora, S3, and an Application Load Balancer.

{{% /choosable %}}

{{% choosable cloud azure %}}

Deploy a production system on [Azure Kubernetes Service](/docs/administration/self-hosting/deployment-options/aks-hosted/) with Azure Database for MySQL and Azure Blob Storage.

{{% /choosable %}}

{{% choosable cloud gcp %}}

Deploy a production system on [Google Kubernetes Engine](/docs/administration/self-hosting/deployment-options/gke-hosted/) with Cloud SQL for MySQL and Cloud Storage.

{{% /choosable %}}

{{< /chooser >}}

## Before you go to production

The deployment guides stand up a working system. Before you run production workloads, review the [Operations guide](/docs/administration/self-hosting/operations/) for high availability, backup and recovery, monitoring, sizing, and security hardening, and the [Network requirements](/docs/administration/self-hosting/network/) for ingress, egress, and air-gapped configurations.

## Next steps

- [Docker Compose quickstart](/docs/administration/self-hosting/deployment-options/quickstart-docker-compose/)
- [All deployment options](/docs/administration/self-hosting/deployment-options/)
- [Components and configuration](/docs/administration/self-hosting/components/)
- [Operations guide](/docs/administration/self-hosting/operations/)
