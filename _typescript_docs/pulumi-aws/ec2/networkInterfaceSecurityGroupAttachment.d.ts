---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/networkInterfaceSecurityGroupAttachment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class NetworkInterfaceSecurityGroupAttachment extends fabric.Resource {
    readonly networkInterfaceId: fabric.Computed<string>;
    readonly securityGroupId: fabric.Computed<string>;
    constructor(urnName: string, args: NetworkInterfaceSecurityGroupAttachmentArgs);
}
export interface NetworkInterfaceSecurityGroupAttachmentArgs {
    readonly networkInterfaceId: fabric.MaybeComputed<string>;
    readonly securityGroupId: fabric.MaybeComputed<string>;
}
