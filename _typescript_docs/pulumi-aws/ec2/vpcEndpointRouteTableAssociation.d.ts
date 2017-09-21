---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/vpcEndpointRouteTableAssociation.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class VpcEndpointRouteTableAssociation extends fabric.Resource {
    readonly routeTableId: fabric.Computed<string>;
    readonly vpcEndpointId: fabric.Computed<string>;
    constructor(urnName: string, args: VpcEndpointRouteTableAssociationArgs);
}
export interface VpcEndpointRouteTableAssociationArgs {
    readonly routeTableId: fabric.MaybeComputed<string>;
    readonly vpcEndpointId: fabric.MaybeComputed<string>;
}
