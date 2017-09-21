---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/deployment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { RestApi } from "./restApi";
export declare class Deployment extends fabric.Resource {
    readonly createdDate: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly executionArn: fabric.Computed<string>;
    readonly invokeUrl: fabric.Computed<string>;
    readonly restApi: fabric.Computed<RestApi>;
    readonly stageDescription?: fabric.Computed<string>;
    readonly stageName: fabric.Computed<string>;
    readonly variables?: fabric.Computed<{
        [key: string]: string;
    }>;
    constructor(urnName: string, args: DeploymentArgs);
}
export interface DeploymentArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly restApi: fabric.MaybeComputed<RestApi>;
    readonly stageDescription?: fabric.MaybeComputed<string>;
    readonly stageName: fabric.MaybeComputed<string>;
    readonly variables?: fabric.MaybeComputed<{
        [key: string]: fabric.MaybeComputed<string>;
    }>;
}
