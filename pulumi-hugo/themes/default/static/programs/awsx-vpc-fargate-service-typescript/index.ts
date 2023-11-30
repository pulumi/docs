import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const vpc = new awsx.ec2.Vpc("vpc");

const securityGroup = new aws.ec2.SecurityGroup("securityGroup", {
    vpcId: vpc.vpcId,
    egress: [
        {
            fromPort: 0,
            toPort: 0,
            protocol: "-1",
            cidrBlocks: ["0.0.0.0/0"],
            ipv6CidrBlocks: ["::/0"],
        },
    ],
});

const cluster = new aws.ecs.Cluster("cluster", {});

const service = new awsx.ecs.FargateService("service", {
    cluster: cluster.arn,
    networkConfiguration: {
        subnets: vpc.privateSubnetIds,
        securityGroups: [securityGroup.id],
    },
    desiredCount: 2,
    taskDefinitionArgs: {
        container: {
            name: "my-service",
            image: "nginx:latest",
            cpu: 128,
            memory: 512,
            essential: true,
        },
    },
});
