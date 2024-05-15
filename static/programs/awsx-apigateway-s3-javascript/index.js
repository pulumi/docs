"use strict";
const apigateway = require("@pulumi/aws-apigateway");

const api = new apigateway.RestAPI("api", {
    routes: [
        {
            path: "/",
            localPath: "www",
        },
    ],
});

exports.url = api.url;
