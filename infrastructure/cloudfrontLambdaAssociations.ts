// Copyright 2016-2021, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import {
    CloudFrontRequest,
    CloudFrontRequestEvent,
    CloudFrontResponse,
    CloudFrontResponseEvent,
} from "aws-lambda";
import * as URLPattern from "url-pattern";
import { LambdaEdge } from "./lambdaEdge";

/**
 * Returns the Lambda function associations for the CloudFront distribution.
 * @param addSecurityHeaders If true, creates Lambda@Edge that sets security headers on
 * origin responses and adds the Lambda to the list of associated triggers.
 * @param doEdgeRedirects If true, creates a Lambda@Edge function that that conditionally
*  redirects based on the URL of the request.
 */
export function getLambdaFunctionAssociations(addSecurityHeaders: boolean, doEdgeRedirects: boolean):
    aws.types.input.cloudfront.DistributionDefaultCacheBehaviorLambdaFunctionAssociation[] {

    const associations = [];

    // Edge functions must be defined in us-east-1.
    const provider = new aws.Provider("usEast1", {
        region: aws.Region.USEast1,
    });

    if (addSecurityHeaders) {
        const securityHeadersLambda = new LambdaEdge(
            "security",
            {
                disableResourceNamePrefix: true,
                func: getSecurityHeadersLambdaCallback(),
                funcDescription: "Lambda function that sets security headers on a Cloudfront origin response.",
            },
            {
                provider,
            },
        );
        associations.push({
            includeBody: false,
            lambdaArn: securityHeadersLambda.getLambdaEdgeArn(),
            // Origin response is a type of trigger that runs the function only when CF
            // contacts the origin for a file. Thus reducing the number of times the func
            // is actually invoked.
            //
            // See the following link for all trigger events supported by CF:
            // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-cloudfront-trigger-events.html
            eventType: "origin-response",
        });
    }

    if (doEdgeRedirects) {
        const edgeRedirectsLambda = new LambdaEdge(
            "redirects",
            {
                func: getEdgeRedirectsLambdaCallback(),
                funcDescription: "Lambda function that conditionally redirects based on a path-matching expression.",
            },
            {
                provider,
            },
        );
        associations.push({
            includeBody: false,
            lambdaArn: edgeRedirectsLambda.getLambdaEdgeArn(),
            eventType: "origin-request",
        });
    }

    return associations;
}

function getSecurityHeadersLambdaCallback(): aws.lambda.Callback<CloudFrontResponseEvent, CloudFrontResponse> {
    // See the following link for an example:
    // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works-tutorial.html
    return (event, context, callback) => {

        // Get contents of response.
        const response = event.Records[0].cf.response;
        const headers = response.headers;

        // Set new headers.
        headers["x-frame-options"] = [{
            key: "X-Frame-Options",
            value: "DENY",
        }];

        // Return modified response.
        callback(null, response);
    };
}

function getEdgeRedirectsLambdaCallback():
    aws.lambda.Callback<CloudFrontRequestEvent, CloudFrontRequest | CloudFrontResponse> {
    // https://aws.amazon.com/blogs/networking-and-content-delivery/handling-redirectsedge-part1/
    return (event: CloudFrontRequestEvent, context, callback) => {
        const request = event.Records[0].cf.request;

        // Check for a redirect that matches the request URL.
        const redirect = getRedirect(request.uri);

        // If there isn't one, just return with the original request.
        if (!redirect) {
            callback(null, request);
            return;
        }

        // Return with a redirect.
        const modifiedResponse = {
            status: "301",
            statusDescription: "Moved Permanently",
            headers: {
                "location": [
                    {
                        key: "Location",
                        value: redirect,
                    },
                ],
                "cache-control": [
                    {
                        key: "Cache-Control",
                        value: "max-age=604800", /* one week in seconds */
                    },
                ],
            },
        };
        callback(null, modifiedResponse);
    };
}

function getRedirect(uri: string): string | undefined {
    return getRegistryRedirect(uri) || getSDKRedirect(uri);
}

function getRegistryRedirect(uri: string): string | undefined {
    return getCloudProvidersRedirect(uri) || getAPIDocsRedirect(uri) || getTutorialsRedirect(uri) || undefined;
}

function getCloudProvidersRedirect(uri: string): string | undefined {
    if (uri.match(/\/docs\/intro\/cloud-providers/)) {
        return uri.replace("docs/intro/cloud-providers", "registry/packages").replace("packet", "equinix-metal").replace("setup", "installation-configuration");
    }

    if (uri.match(/\/docs\/reference\/clouds/)) {
        return uri.replace("docs/reference/clouds", "registry/packages").replace("packet", "equinix-metal").replace("setup", "installation-configuration");
    }

    return undefined;
}

function getAPIDocsRedirect(uri: string): string | undefined {  
    if (uri.match(/\/docs\/reference\/pkg\/nodejs|python|dotnet\//)) {
        return undefined;
    }

    const apiDocsPage = uri.match(/\/docs\/reference\/pkg\/([^\/]+)/);
    if (apiDocsPage) {
        const packageName = apiDocsPage[1];

        return uri.replace("docs/reference/pkg", "registry/packages").replace(packageName, `${packageName}/api-docs`);
    }

    return undefined;
}

function getTutorialsRedirect(uri: string): string | undefined {
    const tutorialsPage = uri.match(/\/docs\/(?:reference\/)?tutorials([^\/]+)/);
    if (tutorialsPage) {
        const packageName = tutorialsPage[1];

        return uri.replace("docs/tutorials", "registry/packages").replace("docs/reference/tutorials", "registry/packages").replace(packageName, `${packageName}/how-to-guides`);
    }

    return undefined;
}

// getSDKRedirect conditionally redirects based on whether the request URL points
// to an SDK doc that we no longer host.
function getSDKRedirect(uri: string): string | undefined {

    // Redirect docs requests for azure-nextgen to azure-native, matching with or without
    // a trailing slash.
    if (uri.match(/\/docs\/reference\/pkg\/azure-nextgen$|azure-nextgen\//)) {
        return uri.replace("azure-nextgen", "azure-native");
    }

    // Return early if the request doesn't match the prefixes we care about.
    if (!uri.match(/\/docs\/reference\/pkg\/nodejs|python|dotnet\//)) {
        return undefined;
    }
    return nodeSDKRedirect(uri) || pythonSDKRedirect(uri) || dotnetSDKRedirect(uri) || undefined;
}

function nodeSDKRedirect(uri: string): string | undefined {
    const pattern = new URLPattern("/docs/reference/pkg/nodejs/pulumi/:provider(/:service)(*)");
    const match = pattern.match(uri);
    const exceptions = [
        "pulumi",
        "cloud",
        "policy",
        "awsx",
        "kubernetesx",
        "terraform",
    ];

    if (match && match.provider && !exceptions.includes(match.provider)) {
        if (match.service && !match.service.match(/types|config/)) {
            return `/docs/reference/pkg/${match.provider}/${match.service}/?language=nodejs`;
        }
        return `/docs/reference/pkg/${match.provider}/?language=nodejs`;
    }

    return undefined;
}

function pythonSDKRedirect(uri: string): string | undefined {
    const pattern = new URLPattern("/docs/reference/pkg/python/pulumi_(:provider)(/:service)(*)");
    const match = pattern.match(uri);
    const exceptions = [
        "pulumi",
        "policy",
        "terraform",
    ];

    if (match && match.provider && !exceptions.includes(match.provider)) {
        if (match.service) {
            return `/docs/reference/pkg/${match.provider}/${match.service}/?language=python`;
        }
        return `/docs/reference/pkg/${match.provider}/?language=python`;
    }

    return undefined;
}

function dotnetSDKRedirect(uri: string): string | undefined {
    const pattern = new URLPattern(
        "/docs/reference/pkg/dotnet/Pulumi.:provider/Pulumi.:providerRepeated(.:service)(.*).html"
    );
    const match = pattern.match(uri);
    const exceptions = [
        "Automation",
        "FSharp",
    ];

    if (match && match.provider && !exceptions.includes(match.provider)) {
        if (match.service && !match.service.match(/Types|Config/)) {
            // tslint:disable-next-line:max-line-length
            return `/docs/reference/pkg/${match.provider.toLowerCase()}/${match.service.toLowerCase()}/?language=csharp`;
        }
        return `/docs/reference/pkg/${match.provider.toLowerCase()}/?language=csharp`;

    }

    return undefined;
}
