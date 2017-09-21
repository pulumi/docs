---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/integration.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { RestApi } from "./restApi";
export declare class Integration extends fabric.Resource {
    readonly cacheKeyParameters?: fabric.Computed<string[]>;
    readonly cacheNamespace: fabric.Computed<string>;
    readonly contentHandling?: fabric.Computed<string>;
    readonly credentials?: fabric.Computed<string>;
    readonly httpMethod: fabric.Computed<string>;
    readonly integrationHttpMethod?: fabric.Computed<string>;
    readonly passthroughBehavior: fabric.Computed<string>;
    readonly requestParameters?: fabric.Computed<{
        [key: string]: string;
    }>;
    readonly requestParametersInJson?: fabric.Computed<string>;
    readonly requestTemplates?: fabric.Computed<{
        [key: string]: string;
    }>;
    readonly resourceId: fabric.Computed<string>;
    readonly restApi: fabric.Computed<RestApi>;
    readonly type: fabric.Computed<string>;
    readonly uri?: fabric.Computed<string>;
    constructor(urnName: string, args: IntegrationArgs);
}
export interface IntegrationArgs {
    readonly cacheKeyParameters?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly cacheNamespace?: fabric.MaybeComputed<string>;
    readonly contentHandling?: fabric.MaybeComputed<string>;
    readonly credentials?: fabric.MaybeComputed<string>;
    readonly httpMethod: fabric.MaybeComputed<string>;
    readonly integrationHttpMethod?: fabric.MaybeComputed<string>;
    readonly passthroughBehavior?: fabric.MaybeComputed<string>;
    readonly requestParameters?: fabric.MaybeComputed<{
        [key: string]: fabric.MaybeComputed<string>;
    }>;
    readonly requestParametersInJson?: fabric.MaybeComputed<string>;
    readonly requestTemplates?: fabric.MaybeComputed<{
        [key: string]: fabric.MaybeComputed<string>;
    }>;
    readonly resourceId: fabric.MaybeComputed<string>;
    readonly restApi: fabric.MaybeComputed<RestApi>;
    readonly type: fabric.MaybeComputed<string>;
    readonly uri?: fabric.MaybeComputed<string>;
}
