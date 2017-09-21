---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/routeTableAssociation.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class RouteTableAssociation extends fabric.Resource {
    readonly routeTableId: fabric.Computed<string>;
    readonly subnetId: fabric.Computed<string>;
    constructor(urnName: string, args: RouteTableAssociationArgs);
}
export interface RouteTableAssociationArgs {
    readonly routeTableId: fabric.MaybeComputed<string>;
    readonly subnetId: fabric.MaybeComputed<string>;
}
