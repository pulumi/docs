---
layout: typescript-reference
repo: pulumi-aws
subpath: autoscaling/lifecycleHook.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class LifecycleHook extends fabric.Resource {
    readonly autoscalingGroupName: fabric.Computed<string>;
    readonly defaultResult: fabric.Computed<string>;
    readonly heartbeatTimeout?: fabric.Computed<number>;
    readonly lifecycleTransition: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly notificationMetadata?: fabric.Computed<string>;
    readonly notificationTargetArn?: fabric.Computed<string>;
    readonly roleArn?: fabric.Computed<string>;
    constructor(urnName: string, args: LifecycleHookArgs);
}
export interface LifecycleHookArgs {
    readonly autoscalingGroupName: fabric.MaybeComputed<string>;
    readonly defaultResult?: fabric.MaybeComputed<string>;
    readonly heartbeatTimeout?: fabric.MaybeComputed<number>;
    readonly lifecycleTransition: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly notificationMetadata?: fabric.MaybeComputed<string>;
    readonly notificationTargetArn?: fabric.MaybeComputed<string>;
    readonly roleArn?: fabric.MaybeComputed<string>;
}
