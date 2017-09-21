---
layout: typescript-reference
repo: pulumi-aws
subpath: ebs/volume.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Volume extends fabric.Resource {
    readonly availabilityZone: fabric.Computed<string>;
    readonly encrypted: fabric.Computed<boolean>;
    readonly iops: fabric.Computed<number>;
    readonly kmsKeyId: fabric.Computed<string>;
    readonly size: fabric.Computed<number>;
    readonly snapshotId: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly type: fabric.Computed<string>;
    constructor(urnName: string, args: VolumeArgs);
}
export interface VolumeArgs {
    readonly availabilityZone: fabric.MaybeComputed<string>;
    readonly encrypted?: fabric.MaybeComputed<boolean>;
    readonly iops?: fabric.MaybeComputed<number>;
    readonly kmsKeyId?: fabric.MaybeComputed<string>;
    readonly size?: fabric.MaybeComputed<number>;
    readonly snapshotId?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly type?: fabric.MaybeComputed<string>;
}
