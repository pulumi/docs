---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/user.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class User extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly forceDestroy?: fabric.Computed<boolean>;
    readonly name: fabric.Computed<string>;
    readonly path?: fabric.Computed<string>;
    readonly uniqueId: fabric.Computed<string>;
    constructor(urnName: string, args: UserArgs);
}
export interface UserArgs {
    readonly forceDestroy?: fabric.MaybeComputed<boolean>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly path?: fabric.MaybeComputed<string>;
}
