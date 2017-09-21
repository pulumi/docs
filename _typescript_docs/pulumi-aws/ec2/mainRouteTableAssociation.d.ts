---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/mainRouteTableAssociation.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class MainRouteTableAssociation extends fabric.Resource {
    readonly originalRouteTableId: fabric.Computed<string>;
    readonly routeTableId: fabric.Computed<string>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: MainRouteTableAssociationArgs);
}
export interface MainRouteTableAssociationArgs {
    readonly routeTableId: fabric.MaybeComputed<string>;
    readonly vpcId: fabric.MaybeComputed<string>;
}
