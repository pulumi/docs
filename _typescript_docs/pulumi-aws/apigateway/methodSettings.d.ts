---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/methodSettings.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { RestApi } from "./restApi";
export declare class MethodSettings extends fabric.Resource {
    readonly methodPath: fabric.Computed<string>;
    readonly restApi: fabric.Computed<RestApi>;
    readonly settings: fabric.Computed<{
        cacheDataEncrypted?: boolean;
        cacheTtlInSeconds?: number;
        cachingEnabled?: boolean;
        dataTraceEnabled?: boolean;
        loggingLevel?: string;
        metricsEnabled?: boolean;
        requireAuthorizationForCacheControl?: boolean;
        throttlingBurstLimit?: number;
        throttlingRateLimit?: number;
        unauthorizedCacheControlHeaderStrategy?: string;
    }[]>;
    readonly stageName: fabric.Computed<string>;
    constructor(urnName: string, args: MethodSettingsArgs);
}
export interface MethodSettingsArgs {
    readonly methodPath: fabric.MaybeComputed<string>;
    readonly restApi: fabric.MaybeComputed<RestApi>;
    readonly settings: fabric.MaybeComputed<{
        cacheDataEncrypted?: fabric.MaybeComputed<boolean>;
        cacheTtlInSeconds?: fabric.MaybeComputed<number>;
        cachingEnabled?: fabric.MaybeComputed<boolean>;
        dataTraceEnabled?: fabric.MaybeComputed<boolean>;
        loggingLevel?: fabric.MaybeComputed<string>;
        metricsEnabled?: fabric.MaybeComputed<boolean>;
        requireAuthorizationForCacheControl?: fabric.MaybeComputed<boolean>;
        throttlingBurstLimit?: fabric.MaybeComputed<number>;
        throttlingRateLimit?: fabric.MaybeComputed<number>;
        unauthorizedCacheControlHeaderStrategy?: fabric.MaybeComputed<string>;
    }>[];
    readonly stageName: fabric.MaybeComputed<string>;
}
