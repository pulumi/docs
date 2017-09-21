---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/userPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class UserPolicy extends fabric.Resource {
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly policy: fabric.Computed<string>;
    readonly user: fabric.Computed<string>;
    constructor(urnName: string, args: UserPolicyArgs);
}
export interface UserPolicyArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly policy: fabric.MaybeComputed<string>;
    readonly user: fabric.MaybeComputed<string>;
}
