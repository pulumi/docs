"use strict";
const aws = require("@pulumi/aws");
const apigateway = require("@pulumi/aws-apigateway");

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

exports.url = api.url;
