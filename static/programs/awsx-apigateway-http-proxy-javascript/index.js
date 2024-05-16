"use strict";
const apigateway = require("@pulumi/aws-apigateway");

const api = new apigateway.RestAPI("api", {
    routes: [
        {
            path: "/",
            target: {
                type: "http_proxy",
                uri: "https://www.example.com/",
            },
        },
    ],
});

exports.url = api.url;
