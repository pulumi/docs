// Copyright 2016-2021, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

export interface LambdaEdgeArgs {
    func: aws.lambda.Callback<any, any>;
    funcDescription: string;
}

export class LambdaEdge extends pulumi.ComponentResource {
    private args: LambdaEdgeArgs;

    private role: aws.iam.Role;
    private lambdaEdgeFunc: aws.lambda.CallbackFunction<any, any>;

    constructor(name: string, args: LambdaEdgeArgs, opts: pulumi.ComponentResourceOptions) {
        super("www-pulumi:infrastructure:LambdaEdge", name, undefined, opts);

        const defaultRegion = aws.config.region;
        if (defaultRegion !== aws.Region.USEast1 && !opts.providers && !opts.provider) {
            throw new Error("Lambda@Edge must be deployed in us-east-1. You must pass a custom provider option.");
        }

        this.args = args;

        this.createIam();
        this.createLambdaFunction();
        super.registerOutputs({});
    }

    public getLambdaEdgeArn(): pulumi.Output<string> {
        return pulumi.interpolate `${this.lambdaEdgeFunc.arn}:${this.lambdaEdgeFunc.version}`;
    }

    private createIam() {
        this.role = new aws.iam.Role("lambdaEdgeRole", {
            assumeRolePolicy: {
                Statement: [{
                    Effect: "Allow",
                    Action: "sts:AssumeRole",
                    Principal: {
                        Service: [
                            "lambda.amazonaws.com",
                            "edgelambda.amazonaws.com",
                        ],
                    },
                }],
                Version: "2012-10-17",
            },
        },
        {
            parent: this,
            // The items in the policy's Service list are returned by AWS in an unreliable order,
            // so we ignore any diffs to this property as a whole.
            ignoreChanges: [ "assumeRolePolicy" ]
        });

        const rolePolicy = new aws.iam.RolePolicy("lambdaCloudWatchPolicy", {
            role: this.role,
            policy: {
                Version: "2012-10-17",
                Statement: [
                    {
                    Action: [
                        "logs:CreateLogStream",
                        "logs:PutLogEvents",
                        "logs:CreateLogGroup",
                    ],
                    Effect: "Allow",
                    Resource: "*",
                    },
                ],
            },
        // tslint:disable-next-line:align
        }, { parent: this });
    }

    private createLambdaFunction() {
        this.lambdaEdgeFunc = new aws.lambda.CallbackFunction("lambdaEdge", {
            callback: this.args.func,
            description: this.args.funcDescription,
            // Minimum is 128MB.
            memorySize: 128,
            publish: true,
            role: this.role,
            runtime: "nodejs12.x",
            // Note that Lambda@Edge functions have a different max timeout of 30 seconds
            // than the regular Lambda functions.
            timeout: 5,
        // tslint:disable-next-line:align
        }, { parent: this });

        // Grant permissions on the above Lambda function to the Lambda@Edge service.
        const perm = new aws.lambda.Permission("getFuncPermission", {
            action: "lambda:GetFunction",
            principal: "edgelambda.amazonaws.com",
            function: this.lambdaEdgeFunc,
        // tslint:disable-next-line:align
        }, { parent: this });
    }
}
