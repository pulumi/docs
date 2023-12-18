import * as apigateway from "@pulumi/aws-apigateway";

const api = new apigateway.RestAPI("api", {
    routes: [
        {
            path: "/",
            localPath: "www",
        },
    ],
});

export const url = api.url;
