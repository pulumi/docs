// Copyright 2016-2021, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

export interface LambdaEdgeArgs {
    func: aws.lambda.Callback<any, any>;
    funcDescription: string;

    /**
     * Setting this to `true` will not add the `name` arg of this
     * component as a prefix for the resources it creates.
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

        // You might be wondering why the resources created in this component can't always have the prefix
        // based on the `name` of the component resource. The answer has to do with restrictions AWS places
        // on deleting Lambda@Edge replicated functions (namely that they don't let you do it).
        // At update-time, if Pulumi determines that a Lambda@Edge function needs to be deleted,
        // (for example, when it's renamed), our create-before-delete functionality does the right thing,
        // creating the replacement function and the CloudFront association, but fails on attempting to delete
        // the previously associated function because of a bug in the AWS provider. So to safeguard against
        // these failures, we opt to have the component accept these names explicitly.
        // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-delete-replicas.html
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
