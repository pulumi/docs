---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/instanceProfile.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { Role } from "./role";
export declare class InstanceProfile extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly createDate: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly path?: fabric.Computed<string>;
    readonly role: fabric.Computed<Role>;
    readonly roles: fabric.Computed<Role[]>;
    readonly uniqueId: fabric.Computed<string>;
    constructor(urnName: string, args: InstanceProfileArgs);
}
export interface InstanceProfileArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly path?: fabric.MaybeComputed<string>;
    readonly role?: fabric.MaybeComputed<Role>;
    readonly roles?: fabric.MaybeComputed<fabric.MaybeComputed<Role>>[];
}
