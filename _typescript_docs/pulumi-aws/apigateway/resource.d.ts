---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/resource.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { RestApi } from "./restApi";
export declare class Resource extends fabric.Resource {
    readonly parentId: fabric.Computed<string>;
    readonly path: fabric.Computed<string>;
    readonly pathPart: fabric.Computed<string>;
    readonly restApi: fabric.Computed<RestApi>;
    constructor(urnName: string, args: ResourceArgs);
}
export interface ResourceArgs {
    readonly parentId: fabric.MaybeComputed<string>;
    readonly pathPart: fabric.MaybeComputed<string>;
    readonly restApi: fabric.MaybeComputed<RestApi>;
}
