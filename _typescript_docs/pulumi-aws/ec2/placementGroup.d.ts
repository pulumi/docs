---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/placementGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class PlacementGroup extends fabric.Resource {
    readonly name: fabric.Computed<string>;
    readonly strategy: fabric.Computed<string>;
    constructor(urnName: string, args: PlacementGroupArgs);
}
export interface PlacementGroupArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly strategy: fabric.MaybeComputed<string>;
}
