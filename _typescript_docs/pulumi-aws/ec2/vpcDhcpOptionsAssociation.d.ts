---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/vpcDhcpOptionsAssociation.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class VpcDhcpOptionsAssociation extends fabric.Resource {
    readonly dhcpOptionsId: fabric.Computed<string>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: VpcDhcpOptionsAssociationArgs);
}
export interface VpcDhcpOptionsAssociationArgs {
    readonly dhcpOptionsId: fabric.MaybeComputed<string>;
    readonly vpcId: fabric.MaybeComputed<string>;
}
