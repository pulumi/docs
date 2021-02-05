import * as aws from "@pulumi/aws";
import * as URLPattern from "url-pattern";
import { CloudFrontRequestEvent } from "aws-lambda";
import { LambdaEdge } from "./lambdaEdge";

export function getEdgeRedirectAssociations():
    aws.types.input.cloudfront.DistributionDefaultCacheBehaviorLambdaFunctionAssociation[] {
    // https://aws.amazon.com/blogs/networking-and-content-delivery/handling-redirectsedge-part1/

    const lambdaEdge = new LambdaEdge(
        "redirects", {
            func: (event: CloudFrontRequestEvent, context, callback) => {

                // Get contents of response.
                const request = event.Records[0].cf.request;

                const redirect = getRedirect(request.uri);
                if (redirect) {
                    const modifiedResponse = {
                        status: "301",
                        statusDescription: 'Moved Permanently',
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
                                    value: "max-age=3600",
                                },
                            ],
                        },
                    };

                    // Use a modified response.
                    callback(null, modifiedResponse);

                } else {

                    // Use the original request.
                    callback(null, request)
                }
            },
            funcDescription: "Lambda function that conditionally redirects based on a path-matching expression.",
        },
        {}
    );

    return [
        {
            includeBody: false,
            lambdaArn: lambdaEdge.getLambdaEdgeArn(),
            eventType: "origin-request",
        }
    ];
}

function getRedirect(uri: string): string | undefined {
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
        "eks",
        "kubernetesx",
        "terraform",
    ];

    if (match && match.provider && !exceptions.includes(match.provider)) {
        if (match.service) {
            return `/docs/reference/pkg/${match.provider}/${match.service}/?language=nodejs`;
        }
        return `/docs/reference/pkg/${match.provider}/?language=nodejs`;
    }

    return undefined;
};

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
};

function dotnetSDKRedirect(uri: string): string | undefined {
    const pattern = new URLPattern("/docs/reference/pkg/dotnet/Pulumi.(:provider)/Pulumi.(:providerAgain)(.(:service)).html");
    const match = pattern.match(uri);

    if (match && match.provider) {
        if (match.service) {
            return `/docs/reference/pkg/${match.provider.toLowerCase()}/${match.service.toLowerCase()}/?language=csharp`;
        }
        return `/docs/reference/pkg/${match.provider.toLowerCase()}/?language=csharp`;

    // If the URI matches /dotnet/anything-else, we'll just direct you to the GitHub repo.
    } else if (uri.startsWith("/docs/reference/pkg/dotnet/")) {
        return "https://github.com/pulumi/pulumi/tree/master/sdk/dotnet";
    }

    return undefined;
};
