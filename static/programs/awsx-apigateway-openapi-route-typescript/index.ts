const apigateway = require("@pulumi/aws-apigateway");

const api = new apigateway.RestAPI("api", {
    routes: [
        {
            path: "/",
            method: "GET",
            data: {
                "x-amazon-apigateway-integration": {
                    httpMethod: "GET",
                    passthroughBehavior: "when_no_match",
                    type: "http_proxy",
                    uri: "https://httpbin.org/uuid",
                },
            },
        },
    ],
});

exports.url = api.url;
