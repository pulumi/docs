import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

const stackRef = // TO-DO

const lambdaArn = // TO-DO

const schedulerRole = new aws.iam.Role("scheduler-role", {
    assumeRolePolicy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
            Action: "sts:AssumeRole",
            Effect: "Allow",
            Principal: {
                Service: "scheduler.amazonaws.com",
            },
        }],
    }),
    inlinePolicies: [
        {
            name: "my_inline_policy",
            policy: JSON.stringify({
                Version: "2012-10-17",
                Statement: [{
                    Action: ["lambda:*"],
                    Effect: "Allow",
                    Resource: "*",
                }],
            }),
        }
    ],
});

const scheduler = // TO-DO