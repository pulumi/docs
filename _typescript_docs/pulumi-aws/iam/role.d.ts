---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/role.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Role extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly assumeRolePolicy: fabric.Computed<string>;
    readonly createDate: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly forceDetachPolicies?: fabric.Computed<boolean>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly path?: fabric.Computed<string>;
    readonly uniqueId: fabric.Computed<string>;
    constructor(urnName: string, args: RoleArgs);
}
export interface RoleArgs {
    readonly assumeRolePolicy: fabric.MaybeComputed<string>;
    readonly description?: fabric.MaybeComputed<string>;
    readonly forceDetachPolicies?: fabric.MaybeComputed<boolean>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly path?: fabric.MaybeComputed<string>;
}
