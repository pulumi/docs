import * as aws from "@pulumi/aws";
import * as apigateway from "@pulumi/aws-apigateway";

const authorizer = new aws.lambda.CallbackFunction("authorizer", {
    callback: async (event: any, context) => {
        const effect = event.headers.Authorization === "token a-good-token" ? "Allow" : "Deny";

        return {
            principalId: "my-user",
            policyDocument: {
                Version: "2012-10-17",
                Statement: [
                    {
                        Action: "execute-api:Invoke",
                        Effect: effect,
                        Resource: event.methodArn,
                    },
                ],
            },
        };
    },
});

const api = new apigateway.RestAPI("api", {
    routes: [
        {
            path: "/",
            method: "GET",
            localPath: "www",
            authorizers: [
                {
                    authType: "custom",
                    parameterName: "Authorization",
                    type: "request",
                    identitySource: ["method.request.header.Authorization"],
                    handler: authorizer,
                },
            ],
        },
    ],
});

export const url = api.url;
