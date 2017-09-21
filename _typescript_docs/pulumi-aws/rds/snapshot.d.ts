---
layout: typescript-reference
repo: pulumi-aws
subpath: rds/snapshot.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Snapshot extends fabric.Resource {
    readonly allocatedStorage: fabric.Computed<number>;
    readonly availabilityZone: fabric.Computed<string>;
    readonly dbInstanceIdentifier: fabric.Computed<string>;
    readonly dbSnapshotArn: fabric.Computed<string>;
    readonly dbSnapshotIdentifier: fabric.Computed<string>;
    readonly encrypted: fabric.Computed<boolean>;
    readonly engine: fabric.Computed<string>;
    readonly engineVersion: fabric.Computed<string>;
    readonly iops: fabric.Computed<number>;
    readonly kmsKeyId: fabric.Computed<string>;
    readonly licenseModel: fabric.Computed<string>;
    readonly optionGroupName: fabric.Computed<string>;
    readonly port: fabric.Computed<number>;
    readonly snapshotType: fabric.Computed<string>;
    readonly sourceDbSnapshotIdentifier: fabric.Computed<string>;
    readonly sourceRegion: fabric.Computed<string>;
    readonly status: fabric.Computed<string>;
    readonly storageType: fabric.Computed<string>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: SnapshotArgs);
}
export interface SnapshotArgs {
    readonly dbInstanceIdentifier: fabric.MaybeComputed<string>;
    readonly dbSnapshotIdentifier: fabric.MaybeComputed<string>;
}
