---
title: Cloud Infrastructure as Code for Google Cloud
layout: template-page
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
              "github.com/pulumi/pulumi-gcp/sdk/v10/go/gcp/storage"
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
        description: Deliver infrastructure from hundreds of cloud and SaaS providers. Pulumi's SDKs provide a complete and consistent interface that offers full access to clouds and abstracts complexity.
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
      [Pulumi components](/docs/iac/concepts/components/) let you define Google Cloud best practices once and reuse them everywhere. Wrap a Cloud Run service, its IAM bindings, and your organization's defaults in a single component, then share it as a package that teammates can consume in the language of their choice, regardless of the language you authored it in.

      Follow the [component authoring guide](/docs/iac/guides/building-extending/components/build-a-component/) to build and publish your own.
    cta_text: Build a component
    cta_link: /docs/iac/guides/building-extending/components/build-a-component/
    code_title: index.ts
    code_snippets:
      - language: typescript
        label: TypeScript
        title: index.ts
        code: |
          import * as pulumi from "@pulumi/pulumi";
          import * as gcp from "@pulumi/gcp";

          interface PublicServiceArgs {
              location: pulumi.Input<string>;
              image: pulumi.Input<string>;
          }

          // A reusable component: a Cloud Run service that anyone can invoke.
          class PublicService extends pulumi.ComponentResource {
              public readonly url: pulumi.Output<string>;

              constructor(name: string, args: PublicServiceArgs, opts?: pulumi.ComponentResourceOptions) {
                  super("acme:gcp:PublicService", name, {}, opts);

                  const service = new gcp.cloudrunv2.Service(name, {
                      location: args.location,
                      template: { containers: [{ image: args.image }] },
                      deletionProtection: false,
                  }, { parent: this });

                  new gcp.cloudrunv2.ServiceIamMember(`${name}-invoker`, {
                      name: service.name,
                      location: service.location,
                      role: "roles/run.invoker",
                      member: "allUsers",
                  }, { parent: this });

                  this.url = service.uri;
                  this.registerOutputs({ url: this.url });
              }
          }

          const hello = new PublicService("hello", {
              location: "us-central1",
              image: "us-docker.pkg.dev/cloudrun/container/hello",
          });

          export const url = hello.url;
      - language: python
        label: Python
        title: __main__.py
        code: |
          import pulumi
          import pulumi_gcp as gcp


          class PublicService(pulumi.ComponentResource):
              """A reusable component: a Cloud Run service that anyone can invoke."""

              def __init__(self, name, location, image, opts=None):
                  super().__init__("acme:gcp:PublicService", name, {}, opts)

                  service = gcp.cloudrunv2.Service(
                      name,
                      location=location,
                      template={"containers": [{"image": image}]},
                      deletion_protection=False,
                      opts=pulumi.ResourceOptions(parent=self),
                  )

                  gcp.cloudrunv2.ServiceIamMember(
                      f"{name}-invoker",
                      name=service.name,
                      location=service.location,
                      role="roles/run.invoker",
                      member="allUsers",
                      opts=pulumi.ResourceOptions(parent=self),
                  )

                  self.url = service.uri
                  self.register_outputs({"url": self.url})


          hello = PublicService(
              "hello",
              location="us-central1",
              image="us-docker.pkg.dev/cloudrun/container/hello",
          )

          pulumi.export("url", hello.url)
      - language: go
        label: Go
        title: main.go
        code: |
          package main

          import (
              "github.com/pulumi/pulumi-gcp/sdk/v10/go/gcp/cloudrunv2"
              "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
          )

          // PublicService is a reusable component: a Cloud Run service that anyone can invoke.
          type PublicService struct {
              pulumi.ResourceState
              Url pulumi.StringOutput
          }

          func NewPublicService(ctx *pulumi.Context, name, location, image string, opts ...pulumi.ResourceOption) (*PublicService, error) {
              c := &PublicService{}
              if err := ctx.RegisterComponentResource("acme:gcp:PublicService", name, c, opts...); err != nil {
                  return nil, err
              }

              service, err := cloudrunv2.NewService(ctx, name, &cloudrunv2.ServiceArgs{
                  Location: pulumi.String(location),
                  Template: &cloudrunv2.ServiceTemplateArgs{
                      Containers: cloudrunv2.ServiceTemplateContainerArray{
                          &cloudrunv2.ServiceTemplateContainerArgs{Image: pulumi.String(image)},
                      },
                  },
                  DeletionProtection: pulumi.Bool(false),
              }, pulumi.Parent(c))
              if err != nil {
                  return nil, err
              }

              _, err = cloudrunv2.NewServiceIamMember(ctx, name+"-invoker", &cloudrunv2.ServiceIamMemberArgs{
                  Name:     service.Name,
                  Location: service.Location,
                  Role:     pulumi.String("roles/run.invoker"),
                  Member:   pulumi.String("allUsers"),
              }, pulumi.Parent(c))
              if err != nil {
                  return nil, err
              }

              c.Url = service.Uri
              return c, ctx.RegisterResourceOutputs(c, pulumi.Map{"url": c.Url})
          }

          func main() {
              pulumi.Run(func(ctx *pulumi.Context) error {
                  hello, err := NewPublicService(ctx, "hello", "us-central1", "us-docker.pkg.dev/cloudrun/container/hello")
                  if err != nil {
                      return err
                  }
                  ctx.Export("url", hello.Url)
                  return nil
              })
          }
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
              "github.com/pulumi/pulumi-gcp/sdk/v10/go/gcp/container"
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
        cta_primary_link: /request-a-demo/
      - title: Get started with Pulumi and Google Cloud
        description: Deploy your first Google Cloud project in minutes. Follow our quickstart guide, or talk to our team about your specific needs.
        cta_primary_text: Get started
        cta_primary_link: /docs/iac/clouds/gcp/
    anchor: get-started
    highlight_first_card: true
---
