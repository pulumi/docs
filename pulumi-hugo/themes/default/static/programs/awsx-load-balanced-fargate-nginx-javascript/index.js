"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

const lb = new awsx.lb.ApplicationLoadBalancer("lb");
const cluster = new aws.ecs.Cluster("cluster");

const service = new awsx.ecs.FargateService("service", {
    cluster: cluster.arn,
    assignPublicIp: true,
    desiredCount: 2,
    taskDefinitionArgs: {
        container: {
            name: "my-service",
            image: "nginx:latest",
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
