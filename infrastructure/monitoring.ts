import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as archive from "@pulumi/archive";

// const canaryLambda = new aws.lambda.Function("canary_lambda", {
//     architectures: ["x86_64"],
//     ephemeralStorage: {
//         size: 1024,
//     },
//     handler: "index.handler",
//     layers: [
//         "arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:54",
//         "arn:aws:lambda:us-west-2:571684982431:layer:cwsyn-canary-www-test-c27a0ebd-3def-42f1-ab9d-79cdb0d1deee:1",
//     ],
//     loggingConfig: {
//         logFormat: "Text",
//         logGroup: "/aws/lambda/cwsyn-canary-www-test-c27a0ebd-3def-42f1-ab9d-79cdb0d1deee",
//     },
//     memorySize: 1000,
//     name: "cwsyn-canary-www-test-c27a0ebd-3def-42f1-ab9d-79cdb0d1deee",
//     packageType: "Zip",
//     role: "arn:aws:iam::571684982431:role/service-role/CloudWatchSyntheticsRole-canary-www-test-bce-3e90df84ffa9",
//     runtime: "nodejs20.x",
//     sourceCodeHash: "GaX/iLc52waUvJjB3IVXEdqf55EnIhzrx+Zaiu/3aRg=",
//     timeout: 300,
//     tracingConfig: {
//         mode: "PassThrough",
//     },
// });

// const lambda = archive.getFile({
//     type: "zip",
//     sourceFile: "canaryLambda/index.js",
//     outputPath: "lambda_function_payload.zip",
// });

const canaryPolicy = new aws.iam.Policy("canary-policy", {
    name: "CanaryPolicyWWWTest",
    path: "/service-role/",
    policy: {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:PutObject",
                    "s3:GetObject"
                ],
                "Resource": [
                    "arn:aws:s3:::monitoting-www-test*"
                ]
            },
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetBucketLocation"
                ],
                "Resource": [
                    "arn:aws:s3:::monitoting-www-test*"
                ]
            },
            {
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                    "logs:CreateLogGroup"
                ],
                "Resource": [
                    "arn:aws:logs:us-west-2:571684982431:log-group:/aws/lambda/cwsyn-canary-www-test-*"
                ]
            },
            {
                "Effect": "Allow",
                "Action": [
                    "s3:ListAllMyBuckets",
                    "xray:PutTraceSegments"
                ],
                "Resource": [
                    "*"
                ]
            },
            {
                "Effect": "Allow",
                "Resource": "*",
                "Action": "cloudwatch:PutMetricData",
                "Condition": {
                    "StringEquals": {
                        "cloudwatch:namespace": "CloudWatchSynthetics"
                    }
                }
            }
        ]
    },
});

const canaryExecutionRole = new aws.iam.Role("canary-execution-role", {
    assumeRolePolicy: {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    },
    managedPolicyArns: canaryPolicy.arn.apply(arn => [arn] ),
    name: "canary-execution-role",
    path: "/service-role/",
});


const canaryLambda = new aws.lambda.Function("canary_lambda", {
    code: new pulumi.asset.FileArchive("lambda_function_payload.zip"),
    name: "canary-www-test-lambda",
    architectures: ["x86_64"],
    ephemeralStorage: {
        size: 1024,
    },
    handler: "index.handler",
    // sourceCodeHash: lambda.then(lambda => lambda.outputBase64sha256),
    role: canaryExecutionRole.arn,
    runtime: "nodejs20.x",
    environment: {
        variables: {
            foo: "bar",
        },
    },
    timeout: 300,
    memorySize: 1000,
    tracingConfig: {
        mode: "PassThrough",
    },
    loggingConfig: {
        logFormat: "Text",
        logGroup: "/aws/lambda/cwsyn-canary-www-test-c27a0ebd-3def-42f1-ab9d-79cdb0d1deee",
    },
});

const canaryWWWTest = new aws.synthetics.Canary("canary-www-test", {
    artifactS3Location: "s3://monitoting-www-test/",
    executionRoleArn: canaryExecutionRole.arn,
    handler: "index.handler",
    name: "canary-www-test",
    runConfig: {
        memoryInMb: 1024,
        timeoutInSeconds: 300,
    },
    runtimeVersion: "syn-nodejs-puppeteer-9.0",
    schedule: {
        expression: "rate(5 minutes)",
    },
    tags: {
        blueprint: "heartbeat",
    },
    zipFile: "canaryLambda1.zip",
    // s3Bucket: "monitoting-www-test",
    // s3Key: "index.js"
});

export const canary = canaryWWWTest;