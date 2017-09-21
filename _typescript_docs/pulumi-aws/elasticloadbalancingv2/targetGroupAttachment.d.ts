---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticloadbalancingv2/targetGroupAttachment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class TargetGroupAttachment extends fabric.Resource {
    readonly port?: fabric.Computed<number>;
    readonly targetGroupArn: fabric.Computed<string>;
    readonly targetId: fabric.Computed<string>;
    constructor(urnName: string, args: TargetGroupAttachmentArgs);
}
export interface TargetGroupAttachmentArgs {
    readonly port?: fabric.MaybeComputed<number>;
    readonly targetGroupArn: fabric.MaybeComputed<string>;
    readonly targetId: fabric.MaybeComputed<string>;
}
