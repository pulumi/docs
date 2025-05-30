import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

const bucket = new aws.s3.BucketV2("my-bucket");

const lambdaRole = new aws.iam.Role("s3-writer-role", {
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
    managedPolicyArns: ["arn:aws:iam::aws:policy/AmazonS3FullAccess", "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess"],
});

const lambdaFunction = new aws.lambda.Function("s3-writer-lambda-function", {
    role: lambdaRole.arn,
    runtime: "python3.10",
    handler: "lambda_function.lambda_handler",
    code: new pulumi.asset.FileArchive("./s3_writer"),
    timeout: 15,
    memorySize: 128,
    environment: {
        variables: {
            BUCKET_NAME: bucket.id,
        },
    },
});

// Gives the EventBridge service permissions to invoke the Lambda function
const lambdaEvent = new aws.lambda.Permission("lambda-trigger-event", {
    action: "lambda:InvokeFunction",
    principal: "events.amazonaws.com",
    function: lambdaFunction.arn,
});

export const lambdaName = lambdaFunction.id;
export const bucketName = bucket.id;
export const lambdaArn = lambdaFunction.arn;
