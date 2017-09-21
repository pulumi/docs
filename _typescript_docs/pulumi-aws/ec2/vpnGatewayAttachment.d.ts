---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/vpnGatewayAttachment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class VpnGatewayAttachment extends fabric.Resource {
    readonly vpcId: fabric.Computed<string>;
    readonly vpnGatewayId: fabric.Computed<string>;
    constructor(urnName: string, args: VpnGatewayAttachmentArgs);
}
export interface VpnGatewayAttachmentArgs {
    readonly vpcId: fabric.MaybeComputed<string>;
    readonly vpnGatewayId: fabric.MaybeComputed<string>;
}
