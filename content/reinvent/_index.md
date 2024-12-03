---
title: Pulumi + AWS re:Invent 2024
meta_desc: "Visit Pulumi at booth 370 to book 1:1s, join workshops, and transform your cloud strategy. AWS re:Invent 2024 | December 2–6, 2024"
meta_image: /images/reinvent/reinvent-meta-24.png
type: page
layout: reinvent
aliases:
  - aws-reinvent-2021

exhibition_data:
    name: "AWS re:Invent 2024"
    description: "Visit Pulumi at booth #370 to book 1:1s, join workshops, and transform your cloud strategy."
    start_date: "2024-12-02"
    end_date: "2024-12-06"
    location:
        name: "The Venetian Convention and Expo Center"
        address:
            street: "3355 S Las Vegas Blvd"
            locality: "Las Vegas"
            region: "NV"
            postal_code: "89109"
            country: "US"
    organizer:
        name: "Amazon Web Services"
        url: https://reinvent.awsevents.com/
    booth: "370"

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

---
