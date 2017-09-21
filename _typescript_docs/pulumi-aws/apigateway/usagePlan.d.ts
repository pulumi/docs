---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/usagePlan.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class UsagePlan extends fabric.Resource {
    readonly apiStages?: fabric.Computed<{
        apiId: string;
        stage: string;
    }[]>;
    readonly description?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly productCode?: fabric.Computed<string>;
    readonly quotaSettings?: fabric.Computed<{
        limit: number;
        offset?: number;
        period: string;
    }[]>;
    readonly throttleSettings?: fabric.Computed<{
        burstLimit?: number;
        rateLimit?: number;
    }[]>;
    constructor(urnName: string, args: UsagePlanArgs);
}
export interface UsagePlanArgs {
    readonly apiStages?: fabric.MaybeComputed<{
        apiId: fabric.MaybeComputed<string>;
        stage: fabric.MaybeComputed<string>;
    }>[];
    readonly description?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly productCode?: fabric.MaybeComputed<string>;
    readonly quotaSettings?: fabric.MaybeComputed<{
        limit: fabric.MaybeComputed<number>;
        offset?: fabric.MaybeComputed<number>;
        period: fabric.MaybeComputed<string>;
    }>[];
    readonly throttleSettings?: fabric.MaybeComputed<{
        burstLimit?: fabric.MaybeComputed<number>;
        rateLimit?: fabric.MaybeComputed<number>;
    }>[];
}
