---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/vpnGatewayRoutePropagation.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class VpnGatewayRoutePropagation extends fabric.Resource {
    readonly routeTableId: fabric.Computed<string>;
    readonly vpnGatewayId: fabric.Computed<string>;
    constructor(urnName: string, args: VpnGatewayRoutePropagationArgs);
}
export interface VpnGatewayRoutePropagationArgs {
    readonly routeTableId: fabric.MaybeComputed<string>;
    readonly vpnGatewayId: fabric.MaybeComputed<string>;
}
