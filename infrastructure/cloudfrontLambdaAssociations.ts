// Copyright 2016-2021, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import { LambdaEdge } from "./lambdaEdge";
import {CloudFrontResponse, CloudFrontResponseEvent} from "aws-lambda";

/**
 * Returns the lambda function associations for the cloudfront distribution.
 * @param addSecurityHeaders If true, will create a Lambda@Edge that sets security headers on
 * origin responses and adds the lambda to the list of associated triggers.
 */
export function getLambdaFunctionAssociations(addSecurityHeaders: boolean):
    aws.types.input.cloudfront.DistributionDefaultCacheBehaviorLambdaFunctionAssociation[] | undefined {
    if (!addSecurityHeaders) {
        // We only need to setup one lambda function right now, so if that's not requested
        // simply return.
        return;
    }

    const provider = new aws.Provider("usEast1", {
        region: aws.Region.USEast1,
    });
    const lambdaEdge = new LambdaEdge("security", {
        func: getSecurityHeadersLambdaCallback(),
        funcDescription: "Lambda function that sets security headers on a Cloudfront origin response.",
    // tslint:disable-next-line:align
    }, { provider });

    return [{
        includeBody: false,
        lambdaArn: lambdaEdge.getLambdaEdgeArn(),
        // Origin response is a type of trigger that runs the function only when CF
        // contacts the origin for a file. Thus reducing the number of times the func
        // is actually reduced.
        //
        // See the following link for all trigger events supported by CF:
        // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-cloudfront-trigger-events.html
        eventType: "origin-response",
    }];
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
