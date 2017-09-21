---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/networkInterfaceAttachment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class NetworkInterfaceAttachment extends fabric.Resource {
    readonly attachmentId: fabric.Computed<string>;
    readonly deviceIndex: fabric.Computed<number>;
    readonly instanceId: fabric.Computed<string>;
    readonly networkInterfaceId: fabric.Computed<string>;
    readonly status: fabric.Computed<string>;
    constructor(urnName: string, args: NetworkInterfaceAttachmentArgs);
}
export interface NetworkInterfaceAttachmentArgs {
    readonly deviceIndex: fabric.MaybeComputed<number>;
    readonly instanceId: fabric.MaybeComputed<string>;
    readonly networkInterfaceId: fabric.MaybeComputed<string>;
}
