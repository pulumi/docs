import * as aws from "@pulumi/aws";
import * as awsnative from "@pulumi/aws-native";
import * as awsx from "@pulumi/awsx";

// AWSx provides a VPC with well-architected defaults: subnets, route
// tables, NAT gateways, and an internet gateway, all pre-configured.
const vpc = new awsx.ec2.Vpc("main", {
    natGateways: { strategy: "Single" },
});

// The AWS provider manages the majority of resources.
const bucket = new aws.s3.Bucket("app-data");

// The AWS Cloud Control provider is used for a resource available
// through Cloud Control but not yet in the classic AWS provider.
const slo = new awsnative.applicationsignals.ServiceLevelObjective("api-slo", {
    name: "api-availability-slo",
    sli: {
        sliMetric: {
            metricType: "AVAILABILITY",
            operationName: "GET /api",
            keyAttributes: {
                Type: "Service",
                Name: "my-service",
                Environment: "production",
            },
        },
        comparisonOperator: "GreaterThanOrEqualTo",
        metricThreshold: 99,
    },
    goal: {
        attainmentGoal: 99,
        warningThreshold: 99.5,
        interval: {
            rollingInterval: { durationUnit: "DAY", duration: 30 },
        },
    },
});

export const vpcId = vpc.vpcId;
export const bucketName = bucket.bucket;
export const sloArn = slo.arn;