---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/natGateway.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class NatGateway extends fabric.Resource {
    readonly allocationId: fabric.Computed<string>;
    readonly networkInterfaceId: fabric.Computed<string>;
    readonly privateIp: fabric.Computed<string>;
    readonly publicIp: fabric.Computed<string>;
    readonly subnetId: fabric.Computed<string>;
    constructor(urnName: string, args: NatGatewayArgs);
}
export interface NatGatewayArgs {
    readonly allocationId: fabric.MaybeComputed<string>;
    readonly networkInterfaceId?: fabric.MaybeComputed<string>;
    readonly privateIp?: fabric.MaybeComputed<string>;
    readonly publicIp?: fabric.MaybeComputed<string>;
    readonly subnetId: fabric.MaybeComputed<string>;
}
