---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/volumeAttachment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class VolumeAttachment extends fabric.Resource {
    readonly deviceName: fabric.Computed<string>;
    readonly forceDetach: fabric.Computed<boolean>;
    readonly instanceId: fabric.Computed<string>;
    readonly skipDestroy: fabric.Computed<boolean>;
    readonly volumeId: fabric.Computed<string>;
    constructor(urnName: string, args: VolumeAttachmentArgs);
}
export interface VolumeAttachmentArgs {
    readonly deviceName: fabric.MaybeComputed<string>;
    readonly forceDetach?: fabric.MaybeComputed<boolean>;
    readonly instanceId: fabric.MaybeComputed<string>;
    readonly skipDestroy?: fabric.MaybeComputed<boolean>;
    readonly volumeId: fabric.MaybeComputed<string>;
}
