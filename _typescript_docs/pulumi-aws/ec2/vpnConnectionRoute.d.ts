---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/vpnConnectionRoute.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class VpnConnectionRoute extends fabric.Resource {
    readonly destinationCidrBlock: fabric.Computed<string>;
    readonly vpnConnectionId: fabric.Computed<string>;
    constructor(urnName: string, args: VpnConnectionRouteArgs);
}
export interface VpnConnectionRouteArgs {
    readonly destinationCidrBlock: fabric.MaybeComputed<string>;
    readonly vpnConnectionId: fabric.MaybeComputed<string>;
}
