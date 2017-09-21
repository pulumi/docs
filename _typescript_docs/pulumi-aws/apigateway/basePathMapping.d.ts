---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/basePathMapping.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { RestApi } from "./restApi";
export declare class BasePathMapping extends fabric.Resource {
    readonly restApi: fabric.Computed<RestApi>;
    readonly basePath?: fabric.Computed<string>;
    readonly domainName: fabric.Computed<string>;
    readonly stageName?: fabric.Computed<string>;
    constructor(urnName: string, args: BasePathMappingArgs);
}
export interface BasePathMappingArgs {
    readonly restApi: fabric.MaybeComputed<RestApi>;
    readonly basePath?: fabric.MaybeComputed<string>;
    readonly domainName: fabric.MaybeComputed<string>;
    readonly stageName?: fabric.MaybeComputed<string>;
}
