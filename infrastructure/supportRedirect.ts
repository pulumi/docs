// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

// SupportRedirect issues a permanent redirect from a retired hostname to the support-request form at /support/new/.
// It exists for the Zendesk-to-Intercom migration: support.pulumi.com is a CNAME to Zendesk's help center today, and
// once the help center retires, the hostname and years of deep links (support.pulumi.com/hc/...) still need to land
// somewhere useful.
//
// It is a dedicated CloudFront distribution, rather than an extra alias on the website distribution, so no host-based
// branching has to thread through the website's per-behavior function and Lambda@Edge associations. A CloudFront
// Function answers every request at viewer-request time, so the origin (required by CloudFront) is never contacted.
//
// DNS is not managed here: the pulumi.com hosted zone belongs to the pulumi-service repo, which CNAMEs the hostname
// to this distribution's domain name — the supportRedirectDistributionDomain stack output.
export interface SupportRedirectArgs {
    // domain is the hostname to redirect from, e.g. support.pulumi.com.
    domain: pulumi.Input<string>;
    // targetUrl is the fully-qualified URL every request is redirected to.
    targetUrl: string;
    // certificateArn is an ACM certificate (us-east-1) covering `domain` — the *.pulumi.com wildcard in production.
    certificateArn: pulumi.Input<string>;
}

export class SupportRedirect extends pulumi.ComponentResource {
    private readonly distribution: aws.cloudfront.Distribution;

    constructor(name: string, args: SupportRedirectArgs, opts?: pulumi.ComponentResourceOptions) {
        super("www-pulumi:infrastructure:SupportRedirect", name, undefined, opts);

        const redirectFunction = new aws.cloudfront.Function(
            `${name}-function`,
            {
                runtime: "cloudfront-js-2.0",
                comment: `Redirects all requests to ${args.targetUrl}`,
                publish: true,
                code: `function handler(event) {
    return {
        statusCode: 301,
        statusDescription: "Moved Permanently",
        headers: {
            "location": { value: "${args.targetUrl}" },
            "cache-control": { value: "max-age=604800" },
        },
    };
}`,
            },
            { parent: this },
        );

        this.distribution = new aws.cloudfront.Distribution(
            `${name}-distribution`,
            {
                enabled: true,
                comment: pulumi.interpolate`Redirects ${args.domain} to ${args.targetUrl}`,
                aliases: [args.domain],
                // The cheapest price class is plenty: the only content served is a redirect.
                priceClass: "PriceClass_100",
                isIpv6Enabled: true,

                // CloudFront requires an origin, but the redirect function answers every request, so it never
                // receives traffic.
                origins: [
                    {
                        originId: "unused-placeholder",
                        domainName: "www.pulumi.com",
                        customOriginConfig: {
                            originProtocolPolicy: "https-only",
                            httpPort: 80,
                            httpsPort: 443,
                            originSslProtocols: ["TLSv1.2"],
                        },
                    },
                ],

                defaultCacheBehavior: {
                    targetOriginId: "unused-placeholder",
                    // allow-all so plain-HTTP requests get one 301 to the HTTPS target, not an https:// hop first.
                    viewerProtocolPolicy: "allow-all",
                    // CloudFront enforces allowedMethods before the viewer-request function runs, and this is its
                    // only POST-capable set — anything narrower 403s non-GET requests instead of redirecting them.
                    allowedMethods: ["GET", "HEAD", "OPTIONS", "PUT", "POST", "PATCH", "DELETE"],
                    cachedMethods: ["GET", "HEAD"],
                    // AWS-managed CachingDisabled policy — the function generates every response.
                    cachePolicyId: "4135ea2d-6df8-44a3-b632-99711092ca9d",
                    functionAssociations: [
                        {
                            eventType: "viewer-request",
                            functionArn: redirectFunction.arn,
                        },
                    ],
                },

                restrictions: {
                    geoRestriction: {
                        restrictionType: "none",
                    },
                },

                viewerCertificate: {
                    acmCertificateArn: args.certificateArn,
                    sslSupportMethod: "sni-only",
                    minimumProtocolVersion: "TLSv1.2_2021",
                },
            },
            // protect: the pulumi-service repo's CNAME depends on this distribution's generated domain name, which an
            // accidental delete/replace would silently regenerate.
            { parent: this, protect: true },
        );

        super.registerOutputs({});
    }

    public getDistributionDomainName(): pulumi.Output<string> {
        return this.distribution.domainName;
    }
}
