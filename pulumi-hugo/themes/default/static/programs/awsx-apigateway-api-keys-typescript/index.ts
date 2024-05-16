import * as aws from "@pulumi/aws";
import * as apigateway from "@pulumi/aws-apigateway";

const api = new apigateway.RestAPI("api", {
    apiKeySource: "HEADER",
    routes: [
        {
            path: "/",
            localPath: "data",
            contentType: "application/json",
            index: "index.json",
            apiKeyRequired: true,
        },
    ],
});

const key = new aws.apigateway.ApiKey("key");

const plan = new aws.apigateway.UsagePlan("plan", {
    apiStages: [
        {
            apiId: api.api.id,
            stage: api.stage.stageName,
        },
    ],
});

const planKey = new aws.apigateway.UsagePlanKey("plan-key", {
    keyId: key.id,
    keyType: "API_KEY",
    usagePlanId: plan.id,
});

export const url = api.url;
export const apiKey = key.value;
