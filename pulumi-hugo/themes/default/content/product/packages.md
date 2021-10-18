---
title: Pulumi Packages
meta_desc: Pulumi Packages give you the tools to easily build and deploy cloud infrastructure with TypeScript/JavaScript, Python, Go, and C#.

type: page
layout: product-packages

overview:
    title: Build and reuse cloud infrastructure as code
    description: |
        Pulumi Packages give you the building blocks to easily build and deploy cloud infrastructure with TypeScript/JavaScript, Python, Go, and C#. Provision resources from all of the top clouds and SaaS providers to build cloud infrastructure that meets your needs. For popular architectures like Kubernetes or serverless, use Pulumi components to get to production faster than ever.

details:
    title: A package for every cloud and architecture
    providers:
        title: Providers give you direct access to cloud resources
        description: |
            Choose from over 60 providers to build your infrastructure from scratch with cloud and SaaS integrations. Get the most comprehensive resource coverage of AWS, Azure, Google Cloud, and Kubernetes with same-day access to new features by using Pulumi Native Providers.
        ide:
            - title: index.ts
              language: typescript
              code: |
                import * as aws from "@pulumi/aws";
                import * as pulumi from "@pulumi/pulumi";

                // Get the id for the latest Amazon Linux AMI
                const ami = aws.ec2.getAmi({
                    filters: [
                        { name: "name", values: ["amzn-ami-hvm-*-x86_64-ebs"] },
                    ],
                    owners: ["137112412989"], // Amazon
                    mostRecent: true,
                }).then(result => result.id);

                // create a new security group for port 80
                const group = new aws.ec2.SecurityGroup("web-secgrp", {
                    ingress: [
                        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
                    ],
                });

                const server = new aws.ec2.Instance("web-server-www", {
                    tags: { "Name": "web-server-www" },
                    instanceType: aws.ec2.InstanceType.T2_Micro, // t2.micro is available in the AWS free tier
                    vpcSecurityGroupIds: [ group.id ], // reference the group object above
                    ami: ami,
                });

                export const publicIp = server.publicIp;
                export const publicHostName = server.publicDns;
            - title: __main__.py
              language: python
              code: |
                import pulumi
                import pulumi_aws as aws

                size = 't2.micro'

                ami = aws.ec2.get_ami(most_recent=True,
                                owners=["137112412989"],
                                filters=[aws.GetAmiFilterArgs(name="name", values=["amzn-ami-hvm-*"])])

                group = aws.ec2.SecurityGroup('web-secgrp',
                    description='Enable HTTP access',
                    ingress=[aws.ec2.SecurityGroupIngressArgs(
                        protocol='tcp',
                        from_port=80,
                        to_port=80,
                        cidr_blocks=['0.0.0.0/0'],
                    )])

                server = aws.ec2.Instance('web-server-www',
                    instance_type=size,
                    vpc_security_group_ids=[group.id],
                    ami=ami.id)

                pulumi.export('public_ip', server.public_ip)
                pulumi.export('public_dns', server.public_dns)
            - title: main.go
              language: go
              code: |
                    package main

                    import (
                        "github.com/pulumi/pulumi-aws/sdk/v4/go/aws/ec2"
                        "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
                    )

                    func main() {
                        pulumi.Run(func(ctx *pulumi.Context) error {
                            // Create a new security group for port 80.
                            group, err := ec2.NewSecurityGroup(ctx, "web-secgrp", &ec2.SecurityGroupArgs{
                                Ingress: ec2.SecurityGroupIngressArray{
                                    ec2.SecurityGroupIngressArgs{
                                        Protocol:   pulumi.String("tcp"),
                                        FromPort:   pulumi.Int(80),
                                        ToPort:     pulumi.Int(80),
                                        CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
                                    },
                                },
                            })
                            if err != nil {
                                return err
                            }

                            // Get the ID for the latest Amazon Linux AMI.
                            mostRecent := true
                            ami, err := ec2.LookupAmi(ctx, &ec2.LookupAmiArgs{
                                Filters: []ec2.GetAmiFilter{
                                    {
                                        Name:   "name",
                                        Values: []string{"amzn-ami-hvm-*-x86_64-ebs"},
                                    },
                                },
                                Owners:     []string{"137112412989"},
                                MostRecent: &mostRecent,
                            })
                            if err != nil {
                                return err
                            }

                            // Create a simple web server using the startup script for the instance.
                            srv, err := ec2.NewInstance(ctx, "web-server-www", &ec2.InstanceArgs{
                                Tags:                pulumi.StringMap{"Name": pulumi.String("web-server-www")},
                                InstanceType:        pulumi.String("t2.micro"), // t2.micro is available in the AWS free tier.
                                VpcSecurityGroupIds: pulumi.StringArray{group.ID()},
                                Ami:                 pulumi.String(ami.Id),
                            })

                            // Export the resulting server's IP address and DNS name.
                            ctx.Export("publicIp", srv.PublicIp)
                            ctx.Export("publicHostName", srv.PublicDns)
                            return nil
                        })
                    }
            - title: MyStack.cs
              language: csharp
              code: |
                using Pulumi;
                using Pulumi.Aws;
                using Pulumi.Aws.Ec2;
                using Pulumi.Aws.Ec2.Inputs;
                using Pulumi.Aws.Inputs;

                class WebServerStack : Stack
                {
                    public WebServerStack()
                    {
                        var ami = Output.Create(Pulumi.Aws.Ec2.GetAmi.InvokeAsync(new Pulumi.Aws.Ec2.GetAmiArgs
                        {
                            MostRecent = true,
                            Owners = {"137112412989"},
                            Filters = {new Pulumi.Aws.Ec2.Inputs.GetAmiFilterArgs {Name = "name", Values = {"amzn-ami-hvm-*"}}}
                        }));

                        var group = new SecurityGroup("web-secgrp", new SecurityGroupArgs
                        {
                            Description = "Enable HTTP access",
                            Ingress =
                            {
                                new SecurityGroupIngressArgs
                                {
                                    Protocol = "tcp",
                                    FromPort = 80,
                                    ToPort = 80,
                                    CidrBlocks = {"0.0.0.0/0"}
                                }
                            }
                        });

                        var server = new Instance("web-server-www", new InstanceArgs
                        {
                            InstanceType = Size,
                            VpcSecurityGroupIds = {group.Id},
                            Ami = ami.Apply(a => a.Id)
                        });

                        this.PublicIp = server.PublicIp;
                        this.PublicDns = server.PublicDns;
                    }

                    [Output] public Output<string> PublicIp { get; set; }

                    [Output] public Output<string> PublicDns { get; set; }

                    private const string Size = "t2.micro";
                }

    components:
        title: Components give you production-ready cloud architectures
        description: |
            Build production-quality cloud architectures faster and smarter by reusing component libraries. These higher-level building blocks come with best practices and sensible defaults built in so you can spend less time on configuration and more time on building applications.
        ide:
            - title: index.ts
              language: typescript
              code: |
                import * as eks from "@pulumi/eks";

                // Create an EKS cluster.
                const cluster = new eks.Cluster("cluster", {
                    instanceType: "t2.medium",
                    desiredCapacity: 2,
                    minSize: 1,
                    maxSize: 2,
                });

                // Export the cluster's kubeconfig.
                export const kubeconfig = cluster.kubeconfig;
            - title: __main__.py
              language: python
              code: |
                import pulumi
                import pulumi_eks as eks

                # Create an EKS cluster.
                cluster = eks.Cluster(
                    "cluster",
                    instance_type="t2.medium",
                    desired_capacity=2,
                    min_size=1,
                    max_size=2,
                )

                # Export the cluster's kubeconfig.
                pulumi.export("kubeconfig", cluster.kubeconfig)
            - title: main.go
              language: go
              code: |
                    package main

                    import (
                        "github.com/pulumi/pulumi-eks/sdk/go/eks/cluster"
                        "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
                    )

                    func main() {
                        pulumi.Run(func(ctx *pulumi.Context) error {
                        // Create an EKS cluster.
                        cluster, err := cluster.NewCluster(ctx, "cluster",
                            cluster.ClusterArgs{
                                InstanceType:    pulumi.String("t2.medium"),
                                DesiredCapacity: pulumi.Int(2),
                                MinSize:         pulumi.Int(1),
                                MaxSize:         pulumi.Int(2),
                            },
                        )
                        if err != nil {
                            return err
                        }

                        // Export the cluster's kubeconfig.
                        ctx.Export("kubeconfig", cluster.Kubeconfig)

                        return nil
                        })
                    }
            - title: MyStack.cs
              language: csharp
              code: |
                using System;
                using System.Threading.Tasks;
                using Pulumi;
                using Pulumi.Eks.Cluster;

                class EksStack : Stack
                {
                    public EksStack()
                    {
                        // Create an EKS cluster.
                        var cluster = new Cluster("cluster", new ClusterArgs
                        {
                            InstanceType = "t2.medium",
                            DesiredCapacity = 2,
                            MinSize = 1,
                            MaxSize = 2,
                        });

                        // Export the cluster's kubeconfig.
                        this.Kubeconfig = cluster.Kubeconfig;
                    }

                    [Output("kubeconfig")]
                    public Output<string> Kubeconfig { get; set; }
                }

                class Program
                {
                    static Task<int> Main(string[] args) => Deployment.RunAsync<EksStack>();
                }

benefits:
    title: Benefits
    items:
        - title: Use your favorite languages
          icon: code
          icon_color: salmon
          description: |
            Start building infrastructure just by installing a Go module or a NuGet, npm, or Python package. Create your own packages in every language by authoring in just one language.

        - title: Get started faster
          icon: rocketship
          icon_color: violet
          description: |
            Find everything you need in each package to start building cloud infrastructure and applications, including SDKs, how-to guides, and API references with hundreds of examples.

        - title: Build faster and smarter
          icon: guage
          icon_color: purple
          description: |
            Don’t reinvent the wheel. Use or create infrastructure abstractions that encapsulate cloud architectures and best practices with Pulumi components in your favorite languages.

        - title: Share and track infrastructure code
          icon: collab
          icon_color: blue
          description: |
            Distribute your infrastructure code through package managers and artifactories. Share and reuse code with versioning, dependency management, and auditing.

case_studies:
    title: Case Studies
    items:
        - company: lemonade
          name: Igor Shapiro
          name_title: Principal Engineer at Lemonade
          link: /case-studies/lemonade
          quote: |
            Pulumi supercharged our infrastructure team by helping us create reusable building blocks that developers can leverage... This empowered our developer teams to self-provision resources and ship new capabilities faster without having to wait for the infrastructure team to deploy new resources on their behalf.

        - company: skai
          name: Danny Zalkind
          name_title: DevOps Group Manager at Skai
          link: /blog/kenshoo-migrates-to-aws-with-pulumi
          quote: |
            A key benefit of Pulumi is that it allows us to modularize our cloud infrastructure as reusable Python components that enable our developer teams to build faster and more independently.

        - company: panther-labs
          name: Austin Byers
          name_title: Principal Platform Engineer at Panther Labs
          link: /case-studies/panther-labs
          quote: |
            Our developers needed a robust platform for managing our complex infrastructure, and it needed to be fast, modular, and testable. We now have more reliable releases and a significantly better developer experience as a result of adopting Pulumi.

get_started:
    title: Getting started

    browse:
        title: Browse all Packages in the Registry
        cta_text: Go to the registry
        description: View the API docs and examples of all the supported providers and components in the Pulumi ecosystem.

    publish:
        title: Build Your Own Packages
        cta_text: Read the docs
        description: Learn how to get started building and publishing your own Pulumi Packages.
---
