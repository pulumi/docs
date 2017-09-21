---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/vpnGateway.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class VpnGateway extends fabric.Resource {
    readonly availabilityZone?: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: VpnGatewayArgs);
}
export interface VpnGatewayArgs {
    readonly availabilityZone?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly vpcId?: fabric.MaybeComputed<string>;
}
