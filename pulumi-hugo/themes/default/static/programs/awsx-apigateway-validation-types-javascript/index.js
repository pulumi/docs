"use strict";
const apigateway = require("@pulumi/aws-apigateway");

const api = new apigateway.RestAPI("api", {
    requestValidator: apigateway.RequestValidator.PARAMS_ONLY,
    routes: [
        {
            path: "/search",
            method: apigateway.Method.GET,
            target: {
                type: "http_proxy",
                uri: "https://www.example.com/",
            },
            requestValidator: apigateway.RequestValidator.ALL,
            requiredParameters: [
                {
                    name: "q",
                    in: "query",
                },
            ],
        },
    ],
});

exports.url = api.url;
