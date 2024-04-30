import * as pulumi from "@pulumi/pulumi";
import * as apigateway from "@pulumi/aws-apigateway";

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

export const url = api.url;
