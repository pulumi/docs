import * as apigateway from "@pulumi/aws-apigateway";

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

export const url = api.url;
