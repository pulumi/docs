// Copyright 2016-2021, Pulumi Corporation.  All rights reserved.

import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import {
    CloudFrontRequest,
    CloudFrontRequestEvent,
    CloudFrontResponse,
    CloudFrontResponseEvent,
} from "aws-lambda";
import * as URLPattern from "url-pattern";
import { LambdaEdge } from "./lambdaEdge";
import { getResources } from "@pulumi/aws/resourcegroupstaggingapi/getResources";

// Edge functions must be defined in us-east-1.
const usEast1Provider = new aws.Provider("usEast1", {
    region: aws.Region.USEast1,
});

export function getEdgeRedirectAssociation(): aws.types.input.cloudfront.DistributionDefaultCacheBehaviorLambdaFunctionAssociation {
    const edgeRedirectsLambda = new LambdaEdge("redirects", {
        func: getEdgeRedirectsLambdaCallback(),
        funcDescription: "Lambda function that conditionally redirects based on a path-matching expression.",
    }, { provider: usEast1Provider });

    return {
        includeBody: false,
        lambdaArn: edgeRedirectsLambda.getLambdaEdgeArn(),
        eventType: "origin-request",
    };
}

export function getAIAnswersRewriteAssociation(): aws.types.input.cloudfront.DistributionDefaultCacheBehaviorLambdaFunctionAssociation {
    const aiAnswersRewritesLambda = new LambdaEdge("answers-rewrites", {
        func: getAIAnswersRewritesLambdaCallback(),
        funcDescription: "Lambda function that rewrites HTTP 404s from Pulumi AI Answers as 410s.",
    }, { provider: usEast1Provider });

     return {
        includeBody: false,
        lambdaArn: aiAnswersRewritesLambda.getLambdaEdgeArn(),
        eventType: "origin-response",
    };
}

function getEdgeRedirectsLambdaCallback(): aws.lambda.Callback<CloudFrontRequestEvent, CloudFrontRequest | CloudFrontResponse> {
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

function getAIAnswersRewritesLambdaCallback(): aws.lambda.Callback<CloudFrontRequestEvent, CloudFrontRequest | CloudFrontResponse> {
    return (event: CloudFrontResponseEvent, context, callback) => {
        const request = event.Records[0].cf.request;
        const response = event.Records[0].cf.response;

        // When requests for an AI Answers page return 404, either the page doesn't exist or we've explicitly unpublished it.
        // For the latter case, it'd be great if the AI App could 410 (Gone), but unfortunately Next.js doesn't support this.
        // So we use this function to rewrite the responses for these pages on the way out.
        // https://github.com/vercel/next.js/discussions/53225
        if (request.uri.match(/\/ai\/answers\//) && response.status === "404") {
            callback(null, {
                ...response,
                status: "410",
                statusDescription: "Gone",
            });
        }

        callback(null, response);
        return;
    };
}

function getRedirect(uri: string): string | undefined {
    return getRegistryRedirect(uri) || getSDKRedirect(uri) || getResourcesRedirect(uri);
}

function getRegistryRedirect(uri: string): string | undefined {
    return getCloudProvidersRedirect(uri) || getAPIDocsRedirect(uri) || getTutorialsRedirect(uri) || undefined;
}

function getCloudProvidersRedirect(uri: string): string | undefined {

    if (uri.includes("/docs/intro/cloud-providers/azure-classic")) {
        return uri.replace("docs/intro/cloud-providers", "registry/packages")
            .replace("azure-classic", "azure")
            .replace("setup", "installation-configuration");
    }
    if (uri.includes("/docs/intro/cloud-providers/azure")) {
        return uri.replace("docs/intro/cloud-providers", "registry/packages")
            .replace("azure", "azure-native")
            .replace("setup", "installation-configuration");
    }
    if (uri.match(/\/docs\/intro\/cloud-providers/)) {
        return uri.replace("docs/intro/cloud-providers", "registry/packages")
            .replace("packet", "equinix-metal")
            .replace("setup", "installation-configuration");
    }

    if (uri.match(/\/docs\/reference\/clouds/)) {
        return uri.replace("docs/reference/clouds", "registry/packages")
            .replace("packet", "equinix-metal")
            .replace("setup", "installation-configuration");
    }

    return undefined;
}

function getAPIDocsRedirect(uri: string): string | undefined {
    console.log(`getAPIDocsRedirect uri: '${uri}'`);
    console.log(uri.match(/\/docs\/reference\/pkg\/nodejs|python|dotnet|java\//));
    console.log(uri.match(/\/docs\/reference\/pkg\/(nodejs|python|dotnet|java)\//));

    if (uri.match(/\/docs\/reference\/pkg\/nodejs|python|dotnet|java\//)) {
        return undefined;
    }

    const apiDocsPage = uri.match(/\/docs\/reference\/pkg\/([^\/]+)/);
    if (apiDocsPage) {
        const packageName = apiDocsPage[1];

        return uri.replace("docs/reference/pkg", "registry/packages")
            .replace(packageName, `${packageName}/api-docs`);
    }

    return undefined;
}

function getTutorialsRedirect(uri: string): string | undefined {
    const tutorialsPage = uri.match(/\/docs\/(?:reference\/)?tutorials\/([^\/]+)/);

    if (tutorialsPage) {
        const packageName = tutorialsPage[1];

        const isAWSNativeGuide = AWS_NATIVE_TUTORIALS.some((awsNativeGuide) => uri.includes(awsNativeGuide))
        if (isAWSNativeGuide) {
            return uri.replace("docs/tutorials/aws", "registry/packages/aws-native/how-to-guides")
                .replace("docs/reference/tutorials/aws", "registry/packages/aws-native/how-to-guides");
        }

        const isAzureNativeGuide = AZURE_NATIVE_TUTORIALS.some((azureNativeGuide) => uri.includes(azureNativeGuide))
        if (isAzureNativeGuide) {
            return uri.replace("docs/tutorials/azure", "registry/packages/azure-native/how-to-guides")
                .replace("docs/reference/tutorials/azure", "registry/packages/azure-native/how-to-guides");
        }

        return uri.replace("docs/tutorials", "registry/packages")
            .replace("docs/reference/tutorials", "registry/packages")
            .replace("aws-stackreference-architecture", "aws-ts-stackreference-architecture")
            .replace("aws-pern-voting-app", "aws-ts-pern-voting-app")
            .replace("aws-django-voting-app", "aws-py-django-voting-app")
            .replace(packageName, `${packageName}/how-to-guides`);
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

// redirect /resources/* to /events/* following workshop+event URL rename to capture orphaned links
function getResourcesRedirect(uri: string): string | undefined {
    if (uri.startsWith("/resources/")) {
        return uri.replace("/resources/", "/events/");
    }

    return undefined;
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
        "esc-sdk",
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
        "esc_sdk",
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

// These are how-to guides that have the improper package because our template-creating script was not parsing classic-azure or aws-native correctly
const AZURE_NATIVE_TUTORIALS = [
    "azure-cs-aks-cosmos-helm",
    "azure-cs-credential-rotation-one-set",
    "azure-cs-appservice-docker",
    "azure-go-appservice-docker",
    "azure-py-appservice-docker",
    "azure-ts-appservice-docker",
    "azure-cs-appservice",
    "azure-py-appservice",
    "azure-ts-appservice",
    "azure-cs-aci",
    "azure-go-aci",
    "azure-py-aci",
    "azure-ts-aci",
    "azure-cs-cosmosdb-logicapp",
    "azure-py-cosmosdb-logicapp",
    "azure-ts-cosmosdb-logicapp",
    "azure-ts-functions-many",
    "azure-cs-functions",
    "azure-cs-aks-helm",
    "azure-go-aks-helm",
    "azure-py-aks-helm",
    "azure-ts-aks-helm",
    "azure-cs-aks",
    "azure-go-aks",
    "azure-py-aks",
    "azure-ts-aks",
    "azure-cs-synapse",
    "azure-py-synapse",
    "azure-ts-synapse",
    "azure-py-virtual-data-center",
    "azure-cs-call-azure-api",
    "azure-go-call-azure-sdk",
    "azure-py-call-azure-sdk",
    "azure-ts-call-azure-sdk",
    "azure-cs-net5-aks-webapp",
    "azure-ts-webapp-privateendpoint-vnet-injection",
    "azure-ts-functions",
    "azure-py-minecraft-server",
    "azure-cs-aks-multicluster",
    "azure-go-aks-multicluster",
    "azure-py-aks-multicluster",
    "azure-ts-aks-multicluster",
    "azure-cs-static-website",
    "azure-go-static-website",
    "azure-py-static-website",
    "azure-ts-static-website",
    "azure-py-webserver",
    "azure-ts-webserver",
];
const AWS_NATIVE_TUTORIALS = [
    "aws-native-ts-stepfunctions",
    "aws-native-ts-ecs",
    "aws-native-ts-s3-folder",
];
