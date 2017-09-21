---
layout: typescript-reference
repo: pulumi-aws
subpath: opsworks/permission.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Permission extends fabric.Resource {
    readonly allowSsh: fabric.Computed<boolean>;
    readonly allowSudo: fabric.Computed<boolean>;
    readonly permissionId: fabric.Computed<string>;
    readonly level: fabric.Computed<string>;
    readonly stackId: fabric.Computed<string>;
    readonly userArn: fabric.Computed<string>;
    constructor(urnName: string, args: PermissionArgs);
}
export interface PermissionArgs {
    readonly allowSsh?: fabric.MaybeComputed<boolean>;
    readonly allowSudo?: fabric.MaybeComputed<boolean>;
    readonly level?: fabric.MaybeComputed<string>;
    readonly stackId?: fabric.MaybeComputed<string>;
    readonly userArn: fabric.MaybeComputed<string>;
}
