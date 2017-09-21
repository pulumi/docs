---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/groupMembership.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class GroupMembership extends fabric.Resource {
    readonly group: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly users: fabric.Computed<string[]>;
    constructor(urnName: string, args: GroupMembershipArgs);
}
export interface GroupMembershipArgs {
    readonly group: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly users: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
}
