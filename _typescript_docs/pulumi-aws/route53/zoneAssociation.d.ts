---
layout: typescript-reference
repo: pulumi-aws
subpath: route53/zoneAssociation.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ZoneAssociation extends fabric.Resource {
    readonly vpcId: fabric.Computed<string>;
    readonly vpcRegion: fabric.Computed<string>;
    readonly zoneId: fabric.Computed<string>;
    constructor(urnName: string, args: ZoneAssociationArgs);
}
export interface ZoneAssociationArgs {
    readonly vpcId: fabric.MaybeComputed<string>;
    readonly vpcRegion?: fabric.MaybeComputed<string>;
    readonly zoneId: fabric.MaybeComputed<string>;
}
