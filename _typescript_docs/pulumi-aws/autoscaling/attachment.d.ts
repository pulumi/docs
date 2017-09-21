---
layout: typescript-reference
repo: pulumi-aws
subpath: autoscaling/attachment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Attachment extends fabric.Resource {
    readonly albTargetGroupArn?: fabric.Computed<string>;
    readonly autoscalingGroupName: fabric.Computed<string>;
    readonly elb?: fabric.Computed<string>;
    constructor(urnName: string, args: AttachmentArgs);
}
export interface AttachmentArgs {
    readonly albTargetGroupArn?: fabric.MaybeComputed<string>;
    readonly autoscalingGroupName: fabric.MaybeComputed<string>;
    readonly elb?: fabric.MaybeComputed<string>;
}
