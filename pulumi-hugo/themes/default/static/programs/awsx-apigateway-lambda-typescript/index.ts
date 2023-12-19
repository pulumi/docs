import * as aws from "@pulumi/aws";
import * as apigateway from "@pulumi/aws-apigateway";

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
export const url = api.url;
