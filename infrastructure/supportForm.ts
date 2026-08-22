// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";
import * as random from "@pulumi/random";

import { supportFormHandler } from "./support-form/handler";

// SupportFormApi is the server side of the support-request form at
// /support/new/ — a Lambda (fronted by a Function URL) that validates
// submissions and, for now, stubs the Intercom integration by writing accepted
// entries to CloudWatch Logs. See support-form/handler.ts for the endpoint's
// behavior and support-form/validation.ts for the payload contract.
//
// The Function URL uses authorizationType NONE, so it is technically publicly
// invokable — but the handler rejects any request that doesn't carry the
// x-origin-verify shared secret, which only the www.pulumi.com CloudFront
// distribution injects (via getOrigin() below). That keeps all real traffic
// behind the CDN's WAF rate limiting. If we ever need to seal the URL
// cryptographically, the upgrade path is authorizationType AWS_IAM plus a
// CloudFront Origin Access Control — which requires the browser to send
// x-amz-content-sha256 on every POST, so it needs frontend changes too.
export class SupportFormApi extends pulumi.ComponentResource {
    private readonly originSecret: random.RandomPassword;
    private readonly func: aws.lambda.CallbackFunction<any, any>;
    private readonly functionUrl: aws.lambda.FunctionUrl;

    constructor(name: string, opts?: pulumi.ComponentResourceOptions) {
        super("www-pulumi:infrastructure:SupportFormApi", name, undefined, opts);

        // The shared secret CloudFront stamps on origin requests. Rotating it
        // (pulumi up with a taint/replace of this resource) briefly races
        // CloudFront config propagation; the handler accepts a comma-separated
        // list in its env var if a graceful two-secret rotation is ever needed.
        this.originSecret = new random.RandomPassword(
            `${name}-origin-secret`,
            {
                length: 32,
                special: false,
            },
            { parent: this },
        );

        const role = new aws.iam.Role(
            `${name}-role`,
            {
                assumeRolePolicy: {
                    Version: "2012-10-17",
                    Statement: [
                        {
                            Effect: "Allow",
                            Action: "sts:AssumeRole",
                            Principal: {
                                Service: "lambda.amazonaws.com",
                            },
                        },
                    ],
                },
            },
            { parent: this },
        );

        const rolePolicy = new aws.iam.RolePolicy(
            `${name}-cloudwatch-policy`,
            {
                role,
                policy: {
                    Version: "2012-10-17",
                    Statement: [
                        {
                            Effect: "Allow",
                            Action: [
                                "logs:CreateLogStream",
                                "logs:PutLogEvents",
                            ],
                            Resource: "*",
                        },
                    ],
                },
            },
            { parent: this },
        );

        // Accepted submissions contain contact details (PII), so the log group
        // is created explicitly with a bounded retention rather than letting
        // Lambda auto-create one that keeps logs forever. The function gets an
        // explicit name (unique per stack) so the group name can be derived.
        const functionName = `${name}-${pulumi.getStack()}`;
        const logGroup = new aws.cloudwatch.LogGroup(
            `${name}-logs`,
            {
                name: `/aws/lambda/${functionName}`,
                retentionInDays: 90,
            },
            { parent: this },
        );

        this.func = new aws.lambda.CallbackFunction(
            `${name}-handler`,
            {
                name: functionName,
                callback: supportFormHandler,
                description: "Validates support-request form submissions from www.pulumi.com/support/new/.",
                memorySize: 256,
                timeout: 10,
                role,
                runtime: aws.lambda.Runtime.NodeJS22dX,
                environment: {
                    variables: {
                        SUPPORT_FORM_ORIGIN_SECRET: this.originSecret.result,
                    },
                },
            },
            { parent: this, dependsOn: [logGroup, rolePolicy] },
        );

        this.functionUrl = new aws.lambda.FunctionUrl(
            `${name}-url`,
            {
                functionName: this.func.name,
                authorizationType: "NONE",
            },
            { parent: this },
        );

        const invokePermission = new aws.lambda.Permission(
            `${name}-invoke-url-permission`,
            {
                action: "lambda:InvokeFunctionUrl",
                function: this.func,
                principal: "*",
                functionUrlAuthType: "NONE",
            },
            { parent: this },
        );

        super.registerOutputs({});
    }

    // getOrigin returns the CloudFront origin for the Function URL, stamping
    // the shared secret the handler requires on every origin request.
    public getOrigin(): aws.types.input.cloudfront.DistributionOrigin {
        return {
            originId: "support-form-api",
            // Function URLs are "https://<id>.lambda-url.<region>.on.aws/";
            // CloudFront wants just the hostname.
            domainName: this.functionUrl.functionUrl.apply(url => new URL(url).hostname),
            customOriginConfig: {
                originProtocolPolicy: "https-only",
                httpPort: 80,
                httpsPort: 443,
                originSslProtocols: ["TLSv1.2"],
            },
            customHeaders: [
                {
                    name: "x-origin-verify",
                    value: this.originSecret.result,
                },
            ],
        };
    }

    public getFunctionName(): pulumi.Output<string> {
        return this.func.name;
    }
}
