---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/requestValidator.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { RestApi } from "./restApi";
export declare class RequestValidator extends fabric.Resource {
    readonly name: fabric.Computed<string>;
    readonly restApi: fabric.Computed<RestApi>;
    readonly validateRequestBody?: fabric.Computed<boolean>;
    readonly validateRequestParameters?: fabric.Computed<boolean>;
    constructor(urnName: string, args: RequestValidatorArgs);
}
export interface RequestValidatorArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly restApi: fabric.MaybeComputed<RestApi>;
    readonly validateRequestBody?: fabric.MaybeComputed<boolean>;
    readonly validateRequestParameters?: fabric.MaybeComputed<boolean>;
}
