---
title: Universal Infrastructure as Code for AWS with Pulumi
layout: aws

meta_title: Well-Architected Infrastructure as Code for AWS
meta_desc: Programming the AWS cloud with Pulumi for huge productivity gains, and a unified programming model for Devs and DevOps.

vpc:
    ts: |
        import * as awsx from "@pulumi/awsx";

        const vpc = new awsx.vpc.Vpc('my-vpc', {});

        export const vpcId = vpc.id;
        export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
        export const vpcPublicSubnetIds = vpc.publicSubnetIds;
    py: |
        import pulumi
        import pulumi_awsx as awsx

        vpc = pulumi_awsx.vpc.Vpc("my-vpc")

        pulumi.export("vpcId", vpc.id)
        pulumi.export("vpcPrivateSubnetIds", vpc.privateSubnetIds)
        pulumi.export("publicSubnetIds", vpc.publicSubnetIds)
    go: |
        package main

        import (
            "github.com/pulumi/pulumi-awsx/sdk/go/awsx/vpc"
            "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
        )

        func main() {
            pulumi.Run(func(ctx *pulumi.Context) error {
                vpc, err := vpc.Vpc(ctx, "my-vpc", nil)
                if err != nil {
                    return err
                }

                ctx.Export("vpcId", vpc.ID)
                ctx.Export("vpcPrivateSubnetIds", vpc.PrivateSubnetIDs)
                ctx.Export("vpcPublicSubnetIds", vpc.PublicSubnetIDs)
                return nil
            })
        }
    csharp: |
        using Pulumi;
        using Awsx = Pulumi.Awsx;

        class MyStack : Stack
        {
            public MyStack()
            {
                var vpc = Awsx.Vpc.Vpc("my-vpc", new Awsx.Vpc.VpcArgs());

                this.VpcId = vpc.id;
                this.VpcPrivateSubnetIds = vpc.privateSubnetIds;
                this.VpcPublicSubnetIds = vpc.publicSubnetIds;
            }

            [Output]
            public Output<string> VpcId { get; set; }

            [Output]
            public Output<string> VpcPrivateSubnetIds { get; set; }

            [Output]
            public Output<string> VpcPublicSubnetIds { get; set; }
        }
    java: |
        package com.pulumi.example.infra;

        import com.pulumi.Context;
        import com.pulumi.Exports;
        import com.pulumi.Pulumi;
        import com.pulumi.awsx.vpc.Vpc;
        import com.pulumi.awsx.vpc.VpcArgs;

        public class Main {

            public static void main(String[] args) {
                Pulumi.run(Main::stack);
            }

            private static Exports stack(Context ctx) {
                var vpc = new Vpc("my-vpc, VpcArgs.builder().build());

                ctx.export("vpcId", vpc.id);
                ctx.export("vpcPrivateSubnetIds", vpc.privateSubnetIds);
                ctx.export("vpcPublicSubnetIds", vpc.publicSubnetIds);
                return ctx.exports();
            }
        }
    yaml: |
        name: awsx-vpc
        runtime: yaml
        description: A simple Pulumi program.
        resources:
            vpc:
                type: awsx:vpc:Vpc
        outputs:
            vpcId: ${vpc.id}
            vpcPrivateSubnetIds: ${vpc.privateSubnetIds}
            vpcPublicSubnetIds: ${vpc.publicSubnetIds}

architectures:
    ts: |
        import * as awsx from "@pulumi/awsx";

        // Spin up two instances of NGINX on port 80.
        const lb = new awsx.lb.ApplicationListener("nginx", { port: 80 });
        const nginx = new awsx.ecs.FargateService("nginx", {
            taskDefinitionArgs: {
                containers: {
                    nginx: {
                        image: "nginx",
                        memory: 128,
                        portMappings: [ lb ],
                    },
                },
            },
            desiredCount: 2,
        });

        // Export the service's URL so that it's easy to access.
        export const url = lb.endpoint.hostname;
    py: |
        import pulumi
        import pulumi_awsx as awsx

        // Spin up two instances of NGINX on port 80.
        lb = awsx.lb.ApplicationListener("nginx", port=80)
        nginx = awsx.ecs.FargateService("nginx",
        	desired_count=2,
            task_definition_args=[awsx.ecs.FargateServiceTaskDefinitionArgs(
                containers: json.dumps({
                    "nginx": {
                        "image": "nginx",
                        "memory": 128,
                        "portMappings": [ lb ],
                    },
                }),
            )],
        )

        pulumi.export("url", lb.endpoint.hostname)
    go: |
        package main

        import (
            "github.com/pulumi/pulumi-awsx/sdk/go/awsx/ecs"
            "github.com/pulumi/pulumi-awsx/sdk/go/awsx/lb"
            "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
        )

        func main() {
            pulumi.Run(func(ctx *pulumi.Context) error {
               lb, err := lb.NewApplicationListener(ctx, "nginx", &lb.ApplicationListenerArgs{
                   Port: pulumi.Int(80),
               })
               if err != nil {
                   return err
               }

               nginx, err := ecs.NewFargateService(ctx, "nginx", &ecs.FargateServiceArgs{
                   DesiredCount: pulumi.Int(2),
                   TaskDefinitionArgs: &ecs.TaskDefinitionArgs{
                       Containers: map[string]TaskDefinitionContainerDefinitionArgs{
                           "nginx": {
                               Image: "nginx",
                               Memory: 128,
                               PortMappings: [ lb ],
                           },
                       },
                   },
               })
               if err != nil {
                   return err
               }

               ctx.Export("url", lb.Endpoint.Hostname)
               return nil
            })
        }
    csharp: |
        using Pulumi;
        using Awsx = Pulumi.Awsx;

        class MyStack : Stack
        {
            public MyStack()
            {
                var lb = new Awsx.Lb.ApplicationListener("nginx", new Awsx.Lb.ApplicationListenerArgs
                {
                    Port = 80,
                });

                var nginx = new Awsx.Ecs.FargateService("nginx", new Awsx.Ecs.FargateServiceArgs
                {
                    DesiredCount = 2,
                    TaskDefinitionArgs = new Awsx.Ecs.TaskDefinitionArgs
                    {
                        Containers = new Dictionary<string, Awsx.Ecs.TaskDefinitionContainerDefinitionArgs>
                        {
                            {
                                "nginx",
                                new Awsx.Ecs.TaskDefinitionContainerDefinitionArgs
                                {
                                    Image = "nginx",
                                    Memory = 128,
                                    PortMappings = { lb },
                                }
                            }
                        }
                    },
                });

                this.Url = lb.endpoint.hostname;
            }

            [Output]
            public Output<string> Url { get; set; }
        }
    java: |
        package com.pulumi.example.infra;

        import com.pulumi.Context;
        import com.pulumi.Exports;
        import com.pulumi.Pulumi;
        import com.pulumi.awsx.lb.ApplicationListener;
        import com.pulumi.awsx.lb.ApplicationListenerArgs;
        import com.pulumi.awsx.ecs.FargateService;
        import com.pulumi.awsx.ecs.FargateServiceArgs;
        import com.pulumi.awsx.ecs.TaskDefinitionArgs;
        import com.pulumi.awsx.ecs.TaskDefinitionContainerDefinitionArgs;
        import java.util.HashMap;

        public class Main {

            public static void main(String[] args) {
                Pulumi.run(Main::stack);
            }

            private static Exports stack(Context ctx) {
                var lb = new ApplicationListener("nginx", ApplicationListenerArgs.builder()
                            .port(80)
                            .build());

                var nginx = new FargateService("nginx", FargateServiceArgs.builder()
                            .desiredCount(2)
                            .taskDefinitionArgs(TaskDefinitionArgs.builder()
                                        .containers(new HashMap<String, TaskDefinitionContainerDefinitionArgs>(){
                                            {
                                                put("nginx", TaskDefinitionContainerDefinitionArgs.builder()
                                                    .image("")
                                                    .memory(128)
                                                    .portMappings(new ApplicationListener[]{lb})
                                                    .build()),
                                            }
                                        })
                                        .build())
                            .build());

                ctx.export("url", lb.endpoint.hostname);
                return ctx.exports();
            }
        }
    yaml: |
      name: awsx-fargate-service
      runtime: yaml
      description: A simple Pulumi program.
      resources:
        lb:
            type: awsx:lb:ApplicationListener
            properties:
                port: 80
        nginx:
            type: awsx:ecs:FargateService
            properties:
                desiredCount: 2
                taskDefinitionArgs:
                    containers:
                        nginx:
                            image: "nginx"
                            memory: 128
                            portMappings: [ ${lb} ]
      outputs:
        url: ${lb.endpoint.hostname}

---
