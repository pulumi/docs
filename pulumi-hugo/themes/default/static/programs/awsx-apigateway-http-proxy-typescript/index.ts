import * as apigateway from "@pulumi/aws-apigateway";

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

export const url = api.url;
