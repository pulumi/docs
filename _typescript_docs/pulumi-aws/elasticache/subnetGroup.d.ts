---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticache/subnetGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SubnetGroup extends fabric.Resource {
    readonly description?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly subnetIds: fabric.Computed<string[]>;
    constructor(urnName: string, args: SubnetGroupArgs);
}
export interface SubnetGroupArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly subnetIds: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
}
