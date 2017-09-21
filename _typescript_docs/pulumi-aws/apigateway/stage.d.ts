---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/stage.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { Deployment } from "./deployment";
import { RestApi } from "./restApi";
export declare class Stage extends fabric.Resource {
    readonly cacheClusterEnabled?: fabric.Computed<boolean>;
    readonly cacheClusterSize?: fabric.Computed<string>;
    readonly clientCertificateId?: fabric.Computed<string>;
    readonly deployment: fabric.Computed<Deployment>;
    readonly description?: fabric.Computed<string>;
    readonly documentationVersion?: fabric.Computed<string>;
    readonly restApi: fabric.Computed<RestApi>;
    readonly stageName: fabric.Computed<string>;
    readonly variables?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: StageArgs);
}
export interface StageArgs {
    readonly cacheClusterEnabled?: fabric.MaybeComputed<boolean>;
    readonly cacheClusterSize?: fabric.MaybeComputed<string>;
    readonly clientCertificateId?: fabric.MaybeComputed<string>;
    readonly deployment: fabric.MaybeComputed<Deployment>;
    readonly description?: fabric.MaybeComputed<string>;
    readonly documentationVersion?: fabric.MaybeComputed<string>;
    readonly restApi: fabric.MaybeComputed<RestApi>;
    readonly stageName: fabric.MaybeComputed<string>;
    readonly variables?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
