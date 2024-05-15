import * as aws from "@pulumi/aws";
import * as apigateway from "@pulumi/aws-apigateway";

const userPool = new aws.cognito.UserPool("user-pool");

const api = new apigateway.RestAPI("api", {
    routes: [
        {
            path: "/",
            localPath: "www",
            authorizers: [
                {
                    parameterName: "Authorization",
                    identitySource: ["method.request.header.Authorization"],
                    providerARNs: [userPool.arn],
                },
            ],
        },
    ],
});

export const url = api.url;
