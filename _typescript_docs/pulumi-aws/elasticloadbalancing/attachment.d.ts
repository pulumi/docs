---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticloadbalancing/attachment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Attachment extends fabric.Resource {
    readonly elb: fabric.Computed<string>;
    readonly instance: fabric.Computed<string>;
    constructor(urnName: string, args: AttachmentArgs);
}
export interface AttachmentArgs {
    readonly elb: fabric.MaybeComputed<string>;
    readonly instance: fabric.MaybeComputed<string>;
}
