"use strict";
const pulumi = require("@pulumi/pulumi");
const apigateway = require("@pulumi/aws-apigateway");

const api = new apigateway.RestAPI("api", {
    swaggerString: JSON.stringify({
        "swagger": "2.0",
        "info": {
            title: "example",
            version: "1.0",
        },
        "paths": {
            "/": {
                get: {
                    "x-amazon-apigateway-integration": {
                        httpMethod: "GET",
                        passthroughBehavior: "when_no_match",
                        type: "http_proxy",
                        uri: "https://httpbin.org/uuid",
                    },
                },
            },
        },
        "x-amazon-apigateway-binary-media-types": ["*/*"],
    }),
});

exports.url = api.url;
