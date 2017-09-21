---
layout: typescript-reference
repo: pulumi-aws
subpath: ebs/snapshot.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Snapshot extends fabric.Resource {
    readonly dataEncryptionKeyId: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly encrypted: fabric.Computed<boolean>;
    readonly kmsKeyId: fabric.Computed<string>;
    readonly ownerAlias: fabric.Computed<string>;
    readonly ownerId: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly volumeId: fabric.Computed<string>;
    readonly volumeSize: fabric.Computed<number>;
    constructor(urnName: string, args: SnapshotArgs);
}
export interface SnapshotArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly volumeId: fabric.MaybeComputed<string>;
}
