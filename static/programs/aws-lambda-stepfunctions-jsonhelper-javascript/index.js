"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");
const awsNative = require("@pulumi/aws-native");

const lambdaRole = new aws.iam.Role("lambda-role", {
    assumeRolePolicy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [
            {
                Action: "sts:AssumeRole",
                Effect: "Allow",
                Principal: {
                    Service: "lambda.amazonaws.com",
                },
            },
        ],
    }),
    managedPolicyArns: [aws.iam.ManagedPolicy.AWSLambdaBasicExecutionRole],
});

const sfnRole = new aws.iam.Role("sfn-role", {
    assumeRolePolicy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [
            {
                Action: "sts:AssumeRole",
                Effect: "Allow",
                Principal: {
                    Service: "states.amazonaws.com",
                },
            },
        ],
    }),
    managedPolicyArns: ["arn:aws:iam::aws:policy/AWSLambda_FullAccess"],
});

const helloFunction = new aws.lambda.Function("hello-function", {
    runtime: aws.lambda.Runtime.Python3d9,
    handler: "handler.handler",
    role: lambdaRole.arn,
    code: new pulumi.asset.AssetArchive({
        ".": new pulumi.asset.FileArchive("./function"),
    }),
});

const stateMachine = new awsNative.stepfunctions.StateMachine("stateMachine", {
    roleArn: sfnRole.arn,
    stateMachineType: "EXPRESS",
    definitionString: pulumi.jsonStringify({
        // converts JSON into string
        Comment: "A Hello World example of the Amazon States Language using two AWS Lambda Functions",
        StartAt: "Hello",
        States: {
            Hello: {
                Type: "Task",
                Resource: helloFunction.arn, // unwraps Pulumi resource Output
                End: true,
            },
        },
    }),
});
