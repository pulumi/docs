---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/response.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Response extends fabric.Resource {
    readonly responseParameters?: fabric.Computed<{
        [key: string]: string;
    }>;
    readonly responseTemplates?: fabric.Computed<{
        [key: string]: string;
    }>;
    readonly responseType: fabric.Computed<string>;
    readonly restApiId: fabric.Computed<string>;
    readonly statusCode?: fabric.Computed<string>;
    constructor(urnName: string, args: ResponseArgs);
}
export interface ResponseArgs {
    readonly responseParameters?: fabric.MaybeComputed<{
        [key: string]: fabric.MaybeComputed<string>;
    }>;
    readonly responseTemplates?: fabric.MaybeComputed<{
        [key: string]: fabric.MaybeComputed<string>;
    }>;
    readonly responseType: fabric.MaybeComputed<string>;
    readonly restApiId: fabric.MaybeComputed<string>;
    readonly statusCode?: fabric.MaybeComputed<string>;
}
