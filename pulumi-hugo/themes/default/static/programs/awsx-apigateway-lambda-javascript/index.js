"use strict";
const aws = require("@pulumi/aws");
const apigateway = require("@pulumi/aws-apigateway");

// A Lambda function to invoke.
const handler = new aws.lambda.CallbackFunction("handler", {
    callback: async (event, context) => {
        return {
            statusCode: 200,
            body: JSON.stringify({
                message: "Hello from API Gateway!",
            }),
        };
    },
});

// A REST API to route requests to the Lambda function.
const api = new apigateway.RestAPI("api", {
    routes: [
        {
            path: "/",
            method: "GET",
            eventHandler: handler,
        },
    ],
});

// The URL at which the REST API will be served.
exports.url = api.url;
