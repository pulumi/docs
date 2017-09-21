---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticloadbalancingv2/targetGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class TargetGroup extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly arnSuffix: fabric.Computed<string>;
    readonly deregistrationDelay?: fabric.Computed<number>;
    readonly healthCheck: fabric.Computed<{
        healthyThreshold?: number;
        interval?: number;
        matcher?: string;
        path?: string;
        port?: string;
        protocol?: string;
        timeout?: number;
        unhealthyThreshold?: number;
    }[]>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly port: fabric.Computed<number>;
    readonly protocol: fabric.Computed<string>;
    readonly stickiness: fabric.Computed<{
        cookieDuration?: number;
        enabled?: boolean;
        type: string;
    }[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: TargetGroupArgs);
}
export interface TargetGroupArgs {
    readonly deregistrationDelay?: fabric.MaybeComputed<number>;
    readonly healthCheck?: fabric.MaybeComputed<{
        healthyThreshold?: fabric.MaybeComputed<number>;
        interval?: fabric.MaybeComputed<number>;
        matcher?: fabric.MaybeComputed<string>;
        path?: fabric.MaybeComputed<string>;
        port?: fabric.MaybeComputed<string>;
        protocol?: fabric.MaybeComputed<string>;
        timeout?: fabric.MaybeComputed<number>;
        unhealthyThreshold?: fabric.MaybeComputed<number>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly port: fabric.MaybeComputed<number>;
    readonly protocol: fabric.MaybeComputed<string>;
    readonly stickiness?: fabric.MaybeComputed<{
        cookieDuration?: fabric.MaybeComputed<number>;
        enabled?: fabric.MaybeComputed<boolean>;
        type: fabric.MaybeComputed<string>;
    }>[];
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.MaybeComputed<string>;
}
