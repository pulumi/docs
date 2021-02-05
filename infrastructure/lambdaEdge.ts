// Copyright 2016-2021, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";
import { createComputedPropertyName } from "typescript";

export interface LambdaEdgeArgs {
    func: aws.lambda.Callback<any, any>;
    funcDescription: string;
}

export class LambdaEdge extends pulumi.ComponentResource {
    private args: LambdaEdgeArgs;

    private name: string;
    private callbackName: string;
    private role: aws.iam.Role;
    private lambdaEdgeFunc: aws.lambda.CallbackFunction<any, any>;

    constructor(name: string, callbackName: string, args: LambdaEdgeArgs, opts: pulumi.ComponentResourceOptions) {
        super("www-pulumi:infrastructure:LambdaEdge", name, undefined, opts);

        this.name = name;
        this.callbackName = callbackName;
        this.args = args;

        this.createIam();
        this.createLambdaFunction();
        super.registerOutputs({});
    }

    public getLambdaEdgeArn(): pulumi.Output<string> {
        return pulumi.interpolate `${this.lambdaEdgeFunc.arn}:${this.lambdaEdgeFunc.version}`;
    }

    private createIam() {
        this.role = new aws.iam.Role(`${this.name}-lambdaEdgeRole`,
            {
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
            },
        );

        const rolePolicy = new aws.iam.RolePolicy(`${this.name}-lambdaCloudWatchPolicy`,
            {
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
            },
            {
                parent: this,
            },
        );
    }

    private createLambdaFunction() {
        this.lambdaEdgeFunc = new aws.lambda.CallbackFunction(this.callbackName,
            {
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
            },
            {
                parent: this,
            },
        );

        // Grant permissions on the above Lambda function to the Lambda@Edge service.
        const perm = new aws.lambda.Permission(`${this.name}-getFuncPermission`,
            {
                action: "lambda:GetFunction",
                principal: "edgelambda.amazonaws.com",
                function: this.lambdaEdgeFunc,
            },
            {
                parent: this,
            },
        );
    }
}
