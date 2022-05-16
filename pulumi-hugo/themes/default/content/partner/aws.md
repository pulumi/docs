---
title: Universal Infrastructure as Code for AWS
layout: aws
url: /aws

meta_desc: Build, deploy & manage infrastructure as code on AWS with TypeScript, Python, Go, C#, Java & YAML. Use existing software engineering tools & practices.

hero:
    title: Cloud Engineering for AWS
    description: |
        Pulumi’s [infrastructure as code](/what-is/what-is-infrastructure-as-code/)
        SDK enables you to build, deploy, and manage your AWS infrastructure faster
        and with more confidence, using modern programming languages and software engineering
        practices. Leverage the full expressivity of general-purpose languages ([TypeScript/JavaScript](/docs/intro/languages/javascript/),
        [Python](/docs/intro/languages/python/), [Go](/docs/intro/languages/go/), [C#](/docs/intro/languages/dotnet/), [Java](/docs/intro/languages/java/))
        or use markup languages (e.g., [YAML](/docs/intro/languages/yaml/), CUE) to build any cloud architecture including containers, serverless, and server-based.

awsx:
    yaml: |
        name: aws-eks
        runtime: yaml
        description: An EKS cluster
        resources:
            cluster:
                type: eks:Cluster
                properties:
                    instanceType: "t2.medium"
                    desiredCapacity: 2
                    minSize: 1
                    maxSize: 2
        outputs:
            kubeconfig: ${cluster.kubeconfig}
    java: |
        package com.pulumi.example.eks;

        import com.pulumi.Context;
        import com.pulumi.Exports;
        import com.pulumi.Pulumi;
        import com.pulumi.core.Output;
        import com.pulumi.eks.Cluster;
        import com.pulumi.eks.ClusterArgs;

        import java.util.stream.Collectors;

        public class App {
            public static void main(String[] args) {
                Pulumi.run(App::stack);
            }

            private static Exports stack(Context ctx) {
                var cluster = new Cluster("my-cluster", ClusterArgs.builder()
                        .instanceType("t2.micro")
                        .desiredCapacity(2)
                        .minSize(1)
                        .maxSize(2)
                        .build());

                ctx.export("kubeconfig", cluster.kubeconfig());
                return ctx.exports();
            }
        }
    csharp: |
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
    go: |
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
    py: |
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
    ts: |
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

contact_us_form:
    section_id: contact-us
    hubspot_form_id: 8a0e0f30-b43e-468e-98cc-6b5d481e8660
    headline: Need help with cloud-native infrastructure as code on AWS?
    quote:
        title: Learn how top engineering teams are using Pulumi's SDK to create, deploy, and manage AWS resources.
        name: Josh Imhoff
        name_title: Site Reliability Engineer, Cockroach Labs
        content: |
            We are building a distributed-database-as-a-service product that runs on Kubernetes clusters across
            multiple public clouds including GCP, AWS and others. Pulumi's declarative model, the support for real
            programming languages, and the uniform workflow on any cloud make our SRE team much more efficient.
---
