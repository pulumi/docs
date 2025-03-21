---
title: Pulumi + AWS Summit London
meta_desc: Join Pulumi at AWS Summit London 2025 to discover how leading organizations automate AWS infrastructure as code.
meta_image: /images/aws-summit-london-meta.png
type: page
layout: aws-summit


links:
    items:
        - heading: Request a Demo
          description: See how Pulumi can help you ship infrastructure faster and manage your AWS resources at scale. Ready for a change?
          action: Talk with an Engineer
          link: https://info.pulumi.com/aws-summit-london

workshops:
    items:
      - title: Advanced Secrets Management on Kubernetes
        date: April 9, 2025
        description: Discover how to securely manage and inject secrets in Kubernetes applications with this hands-on Platform Engineering workshop.
        link: /events/advanced-secrets-management-kubernetes/
        action: Register Now
      - title: "AWS Immersion Day: AWS Infrastructure & Platform Engineering"
        date: May 7, 2025
        description: Learn best practices for platform engineering on AWS and how Pulumi simplifies infrastructure management, enhances security, and automates cloud operations.
        link: /events/aws-immersion-day-platform-engineering/
        action: Register Now

templates:
    items:
        - heading: Container Service Templates
          description: Deploy a container service on AWS with Pulumi and Amazon ECS.
          image: /templates/container-service/aws/architecture.png
          action: Try it
          link: /templates/container-service/aws
        - heading: Kubernetes Cluster on AWS
          description: Deploy a Kubernetes cluster on AWS with Pulumi and Amazon EKS.
          image: /templates/kubernetes/aws/architecture.png
          action: Try it
          link: /templates/kubernetes/aws
        - heading: Serverless Templates
          description: Deploy a serverless application on AWS with Pulumi, AWS Lambda, and Amazon API Gateway.
          image: /templates/serverless-application/aws/architecture.png
          action: Try it
          link: /templates/serverless-application/aws

knowledge:
    items:
        - link: /resources/infrastructure-as-software-best-practices/
          image: /images/video-thumbnails/infrastructure-as-software-best-practices-thumbnail.png
        - link: /resources/ci-cd-pipelines-for-kubernetes-apps-with-codefresh/
          image: /images/video-thumbnails/gitops-with-pulumi-codefresh-thumbnail.png


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
