---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/apiKey.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { RestApi } from "./restApi";
export declare class ApiKey extends fabric.Resource {
    readonly createdDate: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly enabled?: fabric.Computed<boolean>;
    readonly lastUpdatedDate: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly stageKey?: fabric.Computed<{
        restApi: RestApi;
        stageName: string;
    }[]>;
    readonly value: fabric.Computed<string>;
    constructor(urnName: string, args: ApiKeyArgs);
}
export interface ApiKeyArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly enabled?: fabric.MaybeComputed<boolean>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly stageKey?: fabric.MaybeComputed<{
        restApi: fabric.MaybeComputed<RestApi>;
        stageName: fabric.MaybeComputed<string>;
    }>[];
    readonly value?: fabric.MaybeComputed<string>;
}
