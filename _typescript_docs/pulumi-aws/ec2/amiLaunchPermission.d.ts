---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/amiLaunchPermission.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class AmiLaunchPermission extends fabric.Resource {
    readonly accountId: fabric.Computed<string>;
    readonly imageId: fabric.Computed<string>;
    constructor(urnName: string, args: AmiLaunchPermissionArgs);
}
export interface AmiLaunchPermissionArgs {
    readonly accountId: fabric.MaybeComputed<string>;
    readonly imageId: fabric.MaybeComputed<string>;
}
