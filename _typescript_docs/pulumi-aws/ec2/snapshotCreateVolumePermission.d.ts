---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/snapshotCreateVolumePermission.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SnapshotCreateVolumePermission extends fabric.Resource {
    readonly accountId: fabric.Computed<string>;
    readonly snapshotId: fabric.Computed<string>;
    constructor(urnName: string, args: SnapshotCreateVolumePermissionArgs);
}
export interface SnapshotCreateVolumePermissionArgs {
    readonly accountId: fabric.MaybeComputed<string>;
    readonly snapshotId: fabric.MaybeComputed<string>;
}
