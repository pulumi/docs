---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/integrationResponse.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { RestApi } from "./restApi";
export declare class IntegrationResponse extends fabric.Resource {
    readonly contentHandling?: fabric.Computed<string>;
    readonly httpMethod: fabric.Computed<string>;
    readonly resourceId: fabric.Computed<string>;
    readonly responseParameters?: fabric.Computed<{
        [key: string]: string;
    }>;
    readonly responseParametersInJson?: fabric.Computed<string>;
    readonly responseTemplates?: fabric.Computed<{
        [key: string]: string;
    }>;
    readonly restApi: fabric.Computed<RestApi>;
    readonly selectionPattern?: fabric.Computed<string>;
    readonly statusCode: fabric.Computed<string>;
    constructor(urnName: string, args: IntegrationResponseArgs);
}
export interface IntegrationResponseArgs {
    readonly contentHandling?: fabric.MaybeComputed<string>;
    readonly httpMethod: fabric.MaybeComputed<string>;
    readonly resourceId: fabric.MaybeComputed<string>;
    readonly responseParameters?: fabric.MaybeComputed<{
        [key: string]: fabric.MaybeComputed<string>;
    }>;
    readonly responseParametersInJson?: fabric.MaybeComputed<string>;
    readonly responseTemplates?: fabric.MaybeComputed<{
        [key: string]: fabric.MaybeComputed<string>;
    }>;
    readonly restApi: fabric.MaybeComputed<RestApi>;
    readonly selectionPattern?: fabric.MaybeComputed<string>;
    readonly statusCode: fabric.MaybeComputed<string>;
}
