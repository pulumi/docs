---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/methodResponse.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { RestApi } from "./restApi";
export declare class MethodResponse extends fabric.Resource {
    readonly httpMethod: fabric.Computed<string>;
    readonly resourceId: fabric.Computed<string>;
    readonly responseModels?: fabric.Computed<{
        [key: string]: string;
    }>;
    readonly responseParameters?: fabric.Computed<{
        [key: string]: boolean;
    }>;
    readonly responseParametersInJson?: fabric.Computed<string>;
    readonly restApi: fabric.Computed<RestApi>;
    readonly statusCode: fabric.Computed<string>;
    constructor(urnName: string, args: MethodResponseArgs);
}
export interface MethodResponseArgs {
    readonly httpMethod: fabric.MaybeComputed<string>;
    readonly resourceId: fabric.MaybeComputed<string>;
    readonly responseModels?: fabric.MaybeComputed<{
        [key: string]: fabric.MaybeComputed<string>;
    }>;
    readonly responseParameters?: fabric.MaybeComputed<{
        [key: string]: fabric.MaybeComputed<boolean>;
    }>;
    readonly responseParametersInJson?: fabric.MaybeComputed<string>;
    readonly restApi: fabric.MaybeComputed<RestApi>;
    readonly statusCode: fabric.MaybeComputed<string>;
}
