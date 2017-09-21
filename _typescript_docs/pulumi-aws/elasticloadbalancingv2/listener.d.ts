---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticloadbalancingv2/listener.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Listener extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly certificateArn?: fabric.Computed<string>;
    readonly defaultAction: fabric.Computed<{
        targetGroupArn: string;
        type: string;
    }[]>;
    readonly loadBalancerArn: fabric.Computed<string>;
    readonly port: fabric.Computed<number>;
    readonly protocol?: fabric.Computed<string>;
    readonly sslPolicy: fabric.Computed<string>;
    constructor(urnName: string, args: ListenerArgs);
}
export interface ListenerArgs {
    readonly certificateArn?: fabric.MaybeComputed<string>;
    readonly defaultAction: fabric.MaybeComputed<{
        targetGroupArn: fabric.MaybeComputed<string>;
        type: fabric.MaybeComputed<string>;
    }>[];
    readonly loadBalancerArn: fabric.MaybeComputed<string>;
    readonly port: fabric.MaybeComputed<number>;
    readonly protocol?: fabric.MaybeComputed<string>;
    readonly sslPolicy?: fabric.MaybeComputed<string>;
}
