"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

const repo = new awsx.ecr.Repository("repo", {
    forceDelete: true,
});

const image = new awsx.ecr.Image("image", {
    repositoryUrl: repo.url,
    context: "./app",
    platform: "linux/amd64",
});

const cluster = new aws.ecs.Cluster("cluster");

const lb = new awsx.lb.ApplicationLoadBalancer("lb");

const service = new awsx.ecs.FargateService("service", {
    cluster: cluster.arn,
    assignPublicIp: true,
    taskDefinitionArgs: {
        container: {
            name: "my-service",
            image: image.imageUri,
            cpu: 128,
            memory: 512,
            essential: true,
            portMappings: [
                {
                    containerPort: 80,
                    targetGroup: lb.defaultTargetGroup,
                },
            ],
        },
    },
});

exports.url = pulumi.interpolate`http://${lb.loadBalancer.dnsName}`;
