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

    private callbackName: string;
    private roleName: string;
    private rolePolicyName: string;
    private permissionName: string;

    private role: aws.iam.Role;
    private lambdaEdgeFunc: aws.lambda.CallbackFunction<any, any>;

    constructor(name: string, callbackName: string, roleName: string, rolePolicyName: string, permissionName: string, args: LambdaEdgeArgs, opts: pulumi.ComponentResourceOptions) {
        super("www-pulumi:infrastructure:LambdaEdge", name, undefined, opts);

        // You might be wondering why these names need to be passed in when they could easily have
        // been created dynamically based on the `name` of the component resource. The answer has to do
        // with restrictions AWS places on deleting Lambda@Edge replicated functions (namely that they don't
        // let you do it). At update-time, if Pulumi determines that a Lambda@Edge function needs to be
        // deleted, (for example, when it's renamed), our create-before-delete functionality does the right thing,
        // creating the replacement function and the CloudFront association, but fails on attempting to delete the
        // previously associated function because of a bug in the AWS provider. So to safeguard against these
        // failures, we opt to have the component accept these names explicitly.
        // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-delete-replicas.html

        this.callbackName = callbackName;
        this.roleName = roleName;
        this.rolePolicyName = rolePolicyName;
        this.permissionName = permissionName;

        this.args = args;

        this.createIam();
        this.createLambdaFunction();
        super.registerOutputs({});
    }

    public getLambdaEdgeArn(): pulumi.Output<string> {
        return pulumi.interpolate `${this.lambdaEdgeFunc.arn}:${this.lambdaEdgeFunc.version}`;
    }

    private createIam() {
        this.role = new aws.iam.Role(this.roleName,
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

        const rolePolicy = new aws.iam.RolePolicy(this.rolePolicyName,
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
        const perm = new aws.lambda.Permission(this.permissionName,
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
