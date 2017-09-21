---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/rolePolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class RolePolicy extends fabric.Resource {
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly policy: fabric.Computed<string>;
    readonly role: fabric.Computed<string>;
    constructor(urnName: string, args: RolePolicyArgs);
}
export interface RolePolicyArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly policy: fabric.MaybeComputed<string>;
    readonly role: fabric.MaybeComputed<string>;
}
