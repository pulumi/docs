// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";
import * as random from "@pulumi/random";

import { pricingHandler } from "./pricing-api/handler";
import { DEFAULT_PRICING_URL } from "./pricing-api/livePricing";

// PricingApi is the server side of /api/pricing — a Lambda (fronted by a
// Function URL) that estimates a Pulumi Cloud monthly bill from usage, using the
// same formula as the /pricing/ cost calculator. Intercom's Fin calls it through
// a data connector. See pricing-api/README.md for the request contract and
// operating notes, pricing-api/handler.ts for the endpoint's behavior, and
// pricing-api/liveRates.ts for how it keeps its rates current.
//
// Same shape as SupportFormApi (supportForm.ts): the Function URL uses
// authorizationType NONE, but the handler rejects any request without the
// x-origin-verify shared secret, which only the www.pulumi.com CloudFront
// distribution injects (via getOrigin() below). That keeps all real traffic
// behind the CDN's WAF rate limiting.
export interface PricingApiArgs {
    // pricingUrl is the Markdown rendering of /pricing/ that the Lambda reads
    // its rates from. Defaults to https://www.pulumi.com/pricing.md.
    pricingUrl?: pulumi.Input<string>;
    // rateRefreshSeconds is how often a warm Lambda re-reads pricingUrl.
    // Defaults to 3600; 0 turns the refresh off and serves the rates built
    // into pricing-api/pricing.ts.
    rateRefreshSeconds?: number;
    // reservedConcurrency caps concurrent invocations; requests beyond it get
    // a 429. Defaults to 10.
    reservedConcurrency?: number;
}

export class PricingApi extends pulumi.ComponentResource {
    private readonly originSecret: random.RandomPassword;
    private readonly func: aws.lambda.CallbackFunction<any, any>;
    private readonly functionUrl: aws.lambda.FunctionUrl;

    constructor(name: string, args: PricingApiArgs = {}, opts?: pulumi.ComponentResourceOptions) {
        super("www-pulumi:infrastructure:PricingApi", name, undefined, opts);

        // The shared secret CloudFront stamps on origin requests. The handler
        // accepts a comma-separated list in its env var if a graceful
        // two-secret rotation is ever needed.
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
                    Statement: [{
                        Effect: "Allow",
                        Action: "sts:AssumeRole",
                        Principal: { Service: "lambda.amazonaws.com" },
                    }],
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
                    Statement: [{
                        Effect: "Allow",
                        Action: ["logs:CreateLogStream", "logs:PutLogEvents"],
                        Resource: "*",
                    }],
                },
            },
            { parent: this },
        );

        // Created explicitly so the logs have a bounded retention rather than
        // the forever-retention of a Lambda-created group. The function gets
        // an explicit name (unique per stack) so the group name can be derived.
        const functionName = `${name}-${pulumi.getStack()}`;
        const logGroup = new aws.cloudwatch.LogGroup(
            `${name}-logs`,
            {
                name: `/aws/lambda/${functionName}`,
                retentionInDays: 30,
            },
            { parent: this },
        );

        this.func = new aws.lambda.CallbackFunction(
            `${name}-handler`,
            {
                name: functionName,
                callback: pricingHandler,
                description: "Estimates a Pulumi Cloud monthly bill for /api/pricing on www.pulumi.com.",
                memorySize: 128,
                // Room for an hourly rate refresh (a 3-second page fetch) on top of
                // the estimate itself, which takes milliseconds.
                timeout: 10,
                reservedConcurrentExecutions: args.reservedConcurrency ?? 10,
                role,
                runtime: aws.lambda.Runtime.NodeJS22dX,
                environment: {
                    variables: {
                        PRICING_API_ORIGIN_SECRET: this.originSecret.result,
                        PRICING_URL: args.pricingUrl ?? DEFAULT_PRICING_URL,
                        PRICING_REFRESH_SECONDS: String(args.rateRefreshSeconds ?? 3600),
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
                cors: {
                    allowOrigins: ["*"],
                    allowMethods: ["GET", "POST"],
                    allowHeaders: ["content-type"],
                    maxAge: 86400,
                },
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
            originId: "pricing-api",
            // Function URLs are "https://<id>.lambda-url.<region>.on.aws/";
            // CloudFront wants just the hostname.
            domainName: this.functionUrl.functionUrl.apply(url => new URL(url).hostname),
            customOriginConfig: {
                originProtocolPolicy: "https-only",
                httpPort: 80,
                httpsPort: 443,
                originSslProtocols: ["TLSv1.2"],
            },
            customHeaders: [{
                name: "x-origin-verify",
                value: this.originSecret.result,
            }],
        };
    }

    public getFunctionName(): pulumi.Output<string> {
        return this.func.name;
    }
}
