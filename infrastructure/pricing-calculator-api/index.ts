// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.
//
// Pricing calculator API — a Lambda behind a Function URL that returns the same
// monthly estimate as the /pricing/ cost calculator, so it can be called from
// scripts and other services. See src/handler.ts for the request shape and
// src/pricing.ts for the formula and rates.
//
// This is its own stack, separate from the www.pulumi.com stack in
// infrastructure/index.ts, so it can be deployed and torn down without touching
// the site. That stack serves it at /api/pricing when its pricingApiStack config
// names this stack, reading the `url` output below; use that address for anything
// long-lived (such as an Intercom Fin data connector), since the Function URL
// changes if the Lambda is ever replaced. The Function URL is public (authorizationType NONE); the handler
// has no secrets or side effects, and reserved concurrency caps what a flood of
// requests can cost.
//
// Before declaring anything, the program reads the rates from the live pricing
// page (src/livePricing.ts) and compares them with src/pricing.ts. What happens
// on a difference depends on pricingCheck:
//
//     update  (default) deploy with the live rates and warn with the diff, so
//             the deployed API corrects itself; src/pricing.ts is left alone
//     error   stop the deploy
//     warn    deploy with src/pricing.ts and warn
//     off     don't fetch the page; deploy with src/pricing.ts
//
// update and error also stop the deploy if the page can't be read or parsed,
// rather than quietly falling back to rates that may be stale. The rates
// chosen reach the Lambda as JSON in its PRICING_RATES environment variable,
// so a price change shows up as a diff on the function in `pulumi preview`.
//
//     pricingUrl  defaults to https://www.pulumi.com/pricing.md
//
//     yarn install && pulumi stack select testing && pulumi up
//     curl "$(pulumi stack output url)?edition=essentials&iac_resources=1000"

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

import { pricingHandler } from "./src/handler";
import { comparePricing, DEFAULT_PRICING_URL, fetchLivePricing, LivePricing, toRates } from "./src/livePricing";
import { DEFAULT_RATES, PricingRates } from "./src/pricing";

const config = new pulumi.Config();
const reservedConcurrency = config.getNumber("reservedConcurrency") ?? 10;
const pricingCheck = config.get("pricingCheck") || "update";
const pricingUrl = config.get("pricingUrl") || DEFAULT_PRICING_URL;

const name = "pricing-calculator-api";

interface ResolvedRates {
    rates: PricingRates;
    source: "live" | "built-in";
}

const lines = (items: string[]): string => `\n  ${items.join("\n  ")}`;

async function resolveRates(): Promise<ResolvedRates> {
    const builtIn: ResolvedRates = { rates: DEFAULT_RATES, source: "built-in" };
    if (pricingCheck === "off") {
        return builtIn;
    }
    if (!["update", "error", "warn"].includes(pricingCheck)) {
        throw new pulumi.RunError(
            `pricingCheck must be update, error, warn, or off, not ${JSON.stringify(pricingCheck)}`);
    }

    let live: LivePricing;
    try {
        live = await fetchLivePricing(pricingUrl);
    } catch (err) {
        const reason = `couldn't read ${pricingUrl}: ${err instanceof Error ? err.message : err}`;
        if (pricingCheck === "warn") {
            pulumi.log.warn(`${reason}. Deploying with src/pricing.ts.`);
            return builtIn;
        }
        throw new pulumi.RunError(`${reason}\nSet pricingCheck to warn or off to deploy with src/pricing.ts.`);
    }

    const diff = comparePricing(live);

    if (pricingCheck === "update") {
        const result = toRates(live);
        if (!result.ok) {
            throw new pulumi.RunError(`couldn't read every rate from ${pricingUrl}:${lines(result.problems)}\n` +
                "The page's format may have changed; update src/livePricing.ts, " +
                "or set pricingCheck to warn or off to deploy with src/pricing.ts.");
        }
        if (diff.length > 0) {
            pulumi.log.warn(`Deploying with the rates from ${pricingUrl}, which differ from src/pricing.ts:` +
                `${lines(diff)}\nUpdate src/pricing.ts to match.`);
        } else {
            pulumi.log.info(`src/pricing.ts matches ${pricingUrl}`);
        }
        return { rates: result.rates, source: "live" };
    }

    if (diff.length === 0) {
        pulumi.log.info(`src/pricing.ts matches ${pricingUrl}`);
        return builtIn;
    }
    const message = `src/pricing.ts doesn't match ${pricingUrl}:${lines(diff)}`;
    if (pricingCheck === "warn") {
        pulumi.log.warn(`${message}\nDeploying with src/pricing.ts.`);
        return builtIn;
    }
    throw new pulumi.RunError(`${message}\n` +
        "Update src/pricing.ts, or set pricingCheck to update to deploy with the live rates.");
}

export = async () => {
    const { rates, source } = await resolveRates();

    const role = new aws.iam.Role(`${name}-role`, {
        assumeRolePolicy: {
            Version: "2012-10-17",
            Statement: [{
                Effect: "Allow",
                Action: "sts:AssumeRole",
                Principal: { Service: "lambda.amazonaws.com" },
            }],
        },
    });

    const rolePolicy = new aws.iam.RolePolicy(`${name}-cloudwatch-policy`, {
        role,
        policy: {
            Version: "2012-10-17",
            Statement: [{
                Effect: "Allow",
                Action: ["logs:CreateLogStream", "logs:PutLogEvents"],
                Resource: "*",
            }],
        },
    });

    // Created explicitly so the logs have a bounded retention rather than the
    // forever-retention of a Lambda-created group.
    const functionName = `${name}-${pulumi.getStack()}`;
    const logGroup = new aws.cloudwatch.LogGroup(`${name}-logs`, {
        name: `/aws/lambda/${functionName}`,
        retentionInDays: 30,
    });

    const func = new aws.lambda.CallbackFunction(
        `${name}-handler`,
        {
            name: functionName,
            callback: pricingHandler,
            description: "Estimates a Pulumi Cloud monthly bill from usage, using the /pricing/ calculator's formula.",
            memorySize: 128,
            timeout: 5,
            reservedConcurrentExecutions: reservedConcurrency,
            role,
            runtime: aws.lambda.Runtime.NodeJS22dX,
            environment: {
                variables: {
                    PRICING_RATES: JSON.stringify(rates),
                },
            },
        },
        { dependsOn: [logGroup, rolePolicy] },
    );

    const functionUrl = new aws.lambda.FunctionUrl(`${name}-url`, {
        functionName: func.name,
        authorizationType: "NONE",
        cors: {
            allowOrigins: ["*"],
            allowMethods: ["GET", "POST"],
            allowHeaders: ["content-type"],
            maxAge: 86400,
        },
    });

    const invokePermission = new aws.lambda.Permission(`${name}-invoke-url-permission`, {
        action: "lambda:InvokeFunctionUrl",
        function: func,
        principal: "*",
        functionUrlAuthType: "NONE",
    });

    return {
        url: functionUrl.functionUrl,
        lambdaFunctionName: func.name,
        ratesSource: source,
    };
};
