---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/method.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { RestApi } from "./restApi";
export declare class Method extends fabric.Resource {
    readonly apiKeyRequired?: fabric.Computed<boolean>;
    readonly authorization: fabric.Computed<string>;
    readonly authorizerId?: fabric.Computed<string>;
    readonly httpMethod: fabric.Computed<string>;
    readonly requestModels?: fabric.Computed<{
        [key: string]: string;
    }>;
    readonly requestParameters?: fabric.Computed<{
        [key: string]: boolean;
    }>;
    readonly requestParametersInJson?: fabric.Computed<string>;
    readonly requestValidatorId?: fabric.Computed<string>;
    readonly resourceId: fabric.Computed<string>;
    readonly restApi: fabric.Computed<RestApi>;
    constructor(urnName: string, args: MethodArgs);
}
export interface MethodArgs {
    readonly apiKeyRequired?: fabric.MaybeComputed<boolean>;
    readonly authorization: fabric.MaybeComputed<string>;
    readonly authorizerId?: fabric.MaybeComputed<string>;
    readonly httpMethod: fabric.MaybeComputed<string>;
    readonly requestModels?: fabric.MaybeComputed<{
        [key: string]: fabric.MaybeComputed<string>;
    }>;
    readonly requestParameters?: fabric.MaybeComputed<{
        [key: string]: fabric.MaybeComputed<boolean>;
    }>;
    readonly requestParametersInJson?: fabric.MaybeComputed<string>;
    readonly requestValidatorId?: fabric.MaybeComputed<string>;
    readonly resourceId: fabric.MaybeComputed<string>;
    readonly restApi: fabric.MaybeComputed<RestApi>;
}
