---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/groupPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class GroupPolicy extends fabric.Resource {
    readonly group: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly policy: fabric.Computed<string>;
    constructor(urnName: string, args: GroupPolicyArgs);
}
export interface GroupPolicyArgs {
    readonly group: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly policy: fabric.MaybeComputed<string>;
}
