// Copyright 2016-2021, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

export interface LambdaEdgeArgs {
    func: aws.lambda.Callback<any, any>;
    funcDescription: string;

    /**
     * Set this to `true` if you do not want the component resources
     * to have a prefix of the component name.
     *
     * This was added to support backwards compatibility with resources
     * that were created prior to having the default naming strategy use
     * this component's name as prefix for all resources. Any changes in names,
     * after the fact will cause a replacement of all the resources,
     * which will subsequently fail because a Lambda@Edge function cannot be
     * deleted during a replacement.
     *
     * Lambda@Edge functions are automatically deleted by AWS when the
     * last CloudFront Distribution association to it is removed.
     */
    disableResourceNamePrefix?: boolean;
}

export class LambdaEdge extends pulumi.ComponentResource {
    private args: LambdaEdgeArgs;

    private readonly resourceNamesPrefix: string;

    private role: aws.iam.Role;
    private lambdaEdgeFunc: aws.lambda.CallbackFunction<any, any>;

    constructor(name: string, args: LambdaEdgeArgs, opts: pulumi.ComponentResourceOptions) {
        super("www-pulumi:infrastructure:LambdaEdge", name, undefined, opts);

        const defaultRegion = aws.config.region;
        if (defaultRegion !== aws.Region.USEast1 && !opts.providers && !opts.provider) {
            throw new Error("Lambda@Edge must be deployed in us-east-1.");
        }

        if (!args.disableResourceNamePrefix) {
            this.resourceNamesPrefix = `${name}-`;
        } else {
            this.resourceNamesPrefix = "";
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
        this.role = new aws.iam.Role(
            `${this.resourceNamesPrefix}lambdaEdgeRole`,
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

        const rolePolicy = new aws.iam.RolePolicy(
            `${this.resourceNamesPrefix}lambdaCloudWatchPolicy`,
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
        this.lambdaEdgeFunc = new aws.lambda.CallbackFunction(
            `${this.resourceNamesPrefix}lambdaEdge`,
            {
                callback: this.args.func,
                description: this.args.funcDescription,
                // Minimum is 128MB.
                memorySize: 128,
                publish: true,
                role: this.role,
                runtime: aws.lambda.Runtime.NodeJS18dX,
                // Note that Lambda@Edge functions have a different max timeout of 30 seconds
                // than the regular Lambda functions.
                timeout: 5,
            },
            {
                parent: this,
            },
        );

        // Grant permissions on the above Lambda function to the Lambda@Edge service.
        const perm = new aws.lambda.Permission(
            `${this.resourceNamesPrefix}getFuncPermission`,
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
