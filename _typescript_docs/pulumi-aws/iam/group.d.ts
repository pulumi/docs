---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/group.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Group extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly path?: fabric.Computed<string>;
    readonly uniqueId: fabric.Computed<string>;
    constructor(urnName: string, args: GroupArgs);
}
export interface GroupArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly path?: fabric.MaybeComputed<string>;
}
