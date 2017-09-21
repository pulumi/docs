---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/model.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { RestApi } from "./restApi";
export declare class Model extends fabric.Resource {
    readonly contentType: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly restApi: fabric.Computed<RestApi>;
    readonly schema?: fabric.Computed<string>;
    constructor(urnName: string, args: ModelArgs);
}
export interface ModelArgs {
    readonly contentType: fabric.MaybeComputed<string>;
    readonly description?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly restApi: fabric.MaybeComputed<RestApi>;
    readonly schema?: fabric.MaybeComputed<string>;
}
