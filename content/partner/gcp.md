---
title: Cloud Infrastructure as Code for Google Cloud
layout: product-page
type: page
url: /gcp

meta_desc: Infrastructure as code on Google Cloud with Pulumi for huge productivity gains and a unified programming model for developers and operators.

sections:
  - type: hero
    layout: split
    title: Cloud engineering on Google Cloud
    description: |
      Pulumi's [infrastructure as code](/what-is/what-is-infrastructure-as-code/) SDK helps create, deploy, and manage Google Cloud Platform containers, serverless functions, and infrastructure using real programming languages.
    cta_primary_text: Get started
    cta_primary_link: /docs/iac/clouds/gcp/
    cta_secondary_text: Try Pulumi Cloud
    cta_secondary_link: https://app.pulumi.com/signup
    code_title: index.ts
    code_snippets:
      - language: typescript
        label: TypeScript
        title: index.ts
        code: |
          import * as pulumi from "@pulumi/pulumi";
          import * as gcp from "@pulumi/gcp";

          const bucket = new gcp.storage.Bucket("bucket", {
              location: "US",
          });

          export const bucketName = bucket.url;
      - language: python
        label: Python
        title: __main__.py
        code: |
          import pulumi
          import pulumi_gcp as gcp

          bucket = gcp.storage.Bucket("static-site",
              location="US")

          pulumi.export('bucket_name',  bucket.url)
      - language: go
        label: Go
        title: main.go
        code: |
          package main

          import (
              "github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/storage"
              "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
          )

          func main() {
              pulumi.Run(func(ctx *pulumi.Context) error {
                  bucket, err := storage.NewBucket(ctx, "my-bucket", &storage.BucketArgs{
                      Location: pulumi.String("US"),
                  })
                  if err != nil {
                      return err
                  }

                  ctx.Export("bucketName", bucket.Url)
                  return nil
              })
          }
      - language: csharp
        label: C#
        title: MyStack.cs
        code: |
          using Pulumi;
          using Pulumi.Gcp.Storage;

          class MyStack : Stack
          {
              public MyStack()
              {
                  var bucket = new Bucket("my-bucket");

                  // Export the DNS name of the bucket
                  this.BucketName = bucket.Url;
              }

              [Output]
              public Output<string> BucketName { get; set; }
          }
      - language: yaml
        label: YAML
        title: Pulumi.yaml
        code: |
          name: gcp-bucket
          runtime: yaml
          description: A simple Pulumi program.
          resources:
            bucket:
              type: gcp:storage:Bucket
              properties:
                location: "US"
          outputs:
            bucketName: ${bucket.url}
    anchor: hero

  - type: section_header
    align: left
    title: The benefits of using Pulumi
    cards_cols: 2
    cards:
      - icon: terminal-window
        title: Tame cloud complexity
        description: Deliver infrastructure from 50+ cloud and SaaS providers. Pulumi's SDKs provide a complete and consistent interface that offers full access to clouds and abstracts complexity.
      - icon: cloud-arrow-down
        title: Bring the cloud closer to application development
        description: Build reusable cloud infrastructure and infrastructure platforms that empower developers to build modern cloud applications faster and with less overhead.
      - icon: arrows-left-right
        title: Use engineering practices with infrastructure
        description: Replace inefficient, manual infrastructure processes with automation. Test and deliver infrastructure through CI/CD workflows or automate deployments with code at runtime.
      - icon: lightning
        title: Foster collaboration and innovate faster
        description: Unite infrastructure teams, developers, and security teams around shared languages and tools so that everyone can ship products quickly and reliably.
    anchor: benefits

  - type: section_header_with_code
    flip: true
    title: Reduce your complexity with shared packages
    description: |
      Pulumi Packages enable you to define cloud infrastructure once and then consume that package in any supported Pulumi language. You can easily reduce boilerplate code, define best practices, and allow teammates to use your package in the language of their choice, regardless of the language you authored the package with.

      [Pulumi Registry](/registry/) is the central location where you can find all of the Pulumi Packages you can use.
    cta_text: Browse the registry
    cta_link: /registry/
    code_title: cloudrun.ts
    code_snippets:
      - language: typescript
        label: TypeScript
        title: cloudrun.ts
        code: |
          import * as pulumi from "@pulumi/pulumi";
          import * as cloudrun from "@pulumi/gcp-global-cloudrun";

          const conf = new pulumi.Config()
          const project = conf.require("project")

          const deployment = new cloudrun.Deployment("my-sample-deployment", {
              projectId: project,
              imageName: "gcr.io/ahmetb-public/zoneprinter",
              serviceName: "demo-service-ts"
          });

          export const ip = deployment.ipAddress;
      - language: python
        label: Python
        title: __main__.py
        code: |
          import pulumi
          import pulumi_gcp_global_cloudrun as cloudrun

          config = pulumi.Config()
          project = config.require("project")

          deployment = cloudrun.Deployment("my-sample-deployment",
                                          project_id=project,
                                          image_name="gcr.io/ahmetb-public/zoneprinter",
                                          service_name="demo-service-py")

          pulumi.export('ip', deployment.ip_address)
      - language: go
        label: Go
        title: main.go
        code: |
          package main

          import (
            "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
            "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
            cloudrun "github.com/pulumi/pulumi-gcp-global-cloudrun/sdk/go/gcp"
          )

          func main() {
            pulumi.Run(func(ctx *pulumi.Context) error {
              c := config.New(ctx, "")
              project := c.Require("project")

              deployment, err := cloudrun.NewDeployment(ctx, "demo-deployment-go", &cloudrun.DeploymentArgs{
                ImageName:   pulumi.String("gcr.io/ahmetb-public/zoneprinter"),
                ServiceName: "demo-service-ts",
                ProjectId:   project,
              })
              if err != nil {
                return err
              }

              ctx.Export("ip", deployment.IpAddress)

              return nil
            })
          }
      - language: yaml
        label: YAML
        title: Pulumi.yaml
        code: |
          name: gcp-cloud-run
          runtime: yaml
          description: A simple Pulumi program.
          configuration:
            project:
              type: String
              default: "project"
          resources:
            deployment:
              type: gcp-global-cloudrun:index:Deployment
              properties:
                imageName: "gcr.io/ahmetb-public/zoneprinter"
                serviceName: "demo-service-yaml"
                projectId: ${project}
          outputs:
            ip: ${deployment.ipAddress}
    anchor: packages

  - type: section_header_with_code
    title: Create your own GKE cluster
    description: |
      Pulumi supports programming against Kubernetes — Minikube, custom on-premises, or cloud-hosted custom clusters or in managed clusters such as Google GKE. This code defines a GKE cluster with configurable settings that could be packaged in a module and then used to deploy an app to the cluster.
    cta_text: Learn more about GKE with Pulumi
    cta_link: /docs/iac/clouds/kubernetes/
    code_title: gke.ts
    code_snippets:
      - language: typescript
        label: TypeScript
        title: gke.ts
        code: |
          import * as gcp from "@pulumi/gcp";
          import * as k8s from "@pulumi/kubernetes";
          import * as pulumi from "@pulumi/pulumi";

          const name = "demo";

          const engineVersion = gcp.container.getEngineVersions().then(v => v.latestMasterVersion);

          const cluster = new gcp.container.Cluster(name, {
              initialNodeCount: 2,
              minMasterVersion: engineVersion,
              nodeVersion: engineVersion,
              nodeConfig: {
                  machineType: "n1-standard-1",
                  oauthScopes: [
                      "https://www.googleapis.com/auth/compute",
                      "https://www.googleapis.com/auth/devstorage.read_only",
                      "https://www.googleapis.com/auth/logging.write",
                      "https://www.googleapis.com/auth/monitoring",
                  ],
              },
          });

          export const clusterName = cluster.name;
      - language: python
        label: Python
        title: __main__.py
        code: |
          import pulumi
          import pulumi_gcp as gcp

          engine_version = gcp.container.get_engine_versions().latest_master_version

          cluster = gcp.container.Cluster("demo",
              initial_node_count=2,
              min_master_version=engine_version,
              node_version=engine_version,
              node_config=gcp.container.ClusterNodeConfigArgs(
                  machine_type="n1-standard-1",
                  oauth_scopes=[
                      "https://www.googleapis.com/auth/compute",
                      "https://www.googleapis.com/auth/devstorage.read_only",
                      "https://www.googleapis.com/auth/logging.write",
                      "https://www.googleapis.com/auth/monitoring",
                  ],
              ))

          pulumi.export("cluster_name", cluster.name)
      - language: go
        label: Go
        title: main.go
        code: |
          package main

          import (
              "github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/container"
              "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
          )

          func main() {
              pulumi.Run(func(ctx *pulumi.Context) error {
                  engineVersions, err := container.GetEngineVersions(ctx, nil, nil)
                  if err != nil {
                      return err
                  }
                  cluster, err := container.NewCluster(ctx, "demo", &container.ClusterArgs{
                      InitialNodeCount: pulumi.Int(2),
                      MinMasterVersion: pulumi.String(engineVersions.LatestMasterVersion),
                      NodeVersion:      pulumi.String(engineVersions.LatestMasterVersion),
                      NodeConfig: &container.ClusterNodeConfigArgs{
                          MachineType: pulumi.String("n1-standard-1"),
                          OauthScopes: pulumi.StringArray{
                              pulumi.String("https://www.googleapis.com/auth/compute"),
                              pulumi.String("https://www.googleapis.com/auth/devstorage.read_only"),
                              pulumi.String("https://www.googleapis.com/auth/logging.write"),
                              pulumi.String("https://www.googleapis.com/auth/monitoring"),
                          },
                      },
                  })
                  if err != nil {
                      return err
                  }
                  ctx.Export("clusterName", cluster.Name)
                  return nil
              })
          }
    anchor: gke

  - type: two_column
    columns:
      - title: Need help with Google Cloud?
        description: Learn how top engineering teams are using Pulumi's SDK to create, deploy, and manage Google Cloud resources.
        cta_primary_text: Request a demo
        cta_primary_link: /contact/?form=request-a-demo
      - title: Get started with Pulumi and Google Cloud
        description: Deploy your first Google Cloud project in minutes. Follow our quickstart guide, or talk to our team about your specific needs.
        cta_primary_text: Get started
        cta_primary_link: /docs/iac/clouds/gcp/
    anchor: get-started
    highlight_first_card: true
---
