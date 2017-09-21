---
layout: typescript-reference
repo: pulumi-aws
subpath: rds/instance.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Instance extends fabric.Resource {
    readonly address: fabric.Computed<string>;
    readonly allocatedStorage: fabric.Computed<number>;
    readonly allowMajorVersionUpgrade?: fabric.Computed<boolean>;
    readonly applyImmediately: fabric.Computed<boolean>;
    readonly arn: fabric.Computed<string>;
    readonly autoMinorVersionUpgrade?: fabric.Computed<boolean>;
    readonly availabilityZone: fabric.Computed<string>;
    readonly backupRetentionPeriod: fabric.Computed<number>;
    readonly backupWindow: fabric.Computed<string>;
    readonly characterSetName: fabric.Computed<string>;
    readonly copyTagsToSnapshot?: fabric.Computed<boolean>;
    readonly dbSubnetGroupName: fabric.Computed<string>;
    readonly endpoint: fabric.Computed<string>;
    readonly engine: fabric.Computed<string>;
    readonly engineVersion: fabric.Computed<string>;
    readonly finalSnapshotIdentifier?: fabric.Computed<string>;
    readonly hostedZoneId: fabric.Computed<string>;
    readonly iamDatabaseAuthenticationEnabled?: fabric.Computed<boolean>;
    readonly identifier: fabric.Computed<string>;
    readonly identifierPrefix: fabric.Computed<string>;
    readonly instanceClass: fabric.Computed<string>;
    readonly iops?: fabric.Computed<number>;
    readonly kmsKeyId: fabric.Computed<string>;
    readonly licenseModel: fabric.Computed<string>;
    readonly maintenanceWindow: fabric.Computed<string>;
    readonly monitoringInterval?: fabric.Computed<number>;
    readonly monitoringRoleArn: fabric.Computed<string>;
    readonly multiAz: fabric.Computed<boolean>;
    readonly name: fabric.Computed<string>;
    readonly optionGroupName: fabric.Computed<string>;
    readonly parameterGroupName: fabric.Computed<string>;
    readonly password?: fabric.Computed<string>;
    readonly port: fabric.Computed<number>;
    readonly publiclyAccessible?: fabric.Computed<boolean>;
    readonly replicas: fabric.Computed<string[]>;
    readonly replicateSourceDb?: fabric.Computed<string>;
    readonly resourceId: fabric.Computed<string>;
    readonly securityGroupNames?: fabric.Computed<string[]>;
    readonly skipFinalSnapshot?: fabric.Computed<boolean>;
    readonly snapshotIdentifier?: fabric.Computed<string>;
    readonly status: fabric.Computed<string>;
    readonly storageEncrypted?: fabric.Computed<boolean>;
    readonly storageType: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly timezone: fabric.Computed<string>;
    readonly username: fabric.Computed<string>;
    readonly vpcSecurityGroupIds: fabric.Computed<string[]>;
    constructor(urnName: string, args: InstanceArgs);
}
export interface InstanceArgs {
    readonly allocatedStorage?: fabric.MaybeComputed<number>;
    readonly allowMajorVersionUpgrade?: fabric.MaybeComputed<boolean>;
    readonly applyImmediately?: fabric.MaybeComputed<boolean>;
    readonly autoMinorVersionUpgrade?: fabric.MaybeComputed<boolean>;
    readonly availabilityZone?: fabric.MaybeComputed<string>;
    readonly backupRetentionPeriod?: fabric.MaybeComputed<number>;
    readonly backupWindow?: fabric.MaybeComputed<string>;
    readonly characterSetName?: fabric.MaybeComputed<string>;
    readonly copyTagsToSnapshot?: fabric.MaybeComputed<boolean>;
    readonly dbSubnetGroupName?: fabric.MaybeComputed<string>;
    readonly engine?: fabric.MaybeComputed<string>;
    readonly engineVersion?: fabric.MaybeComputed<string>;
    readonly finalSnapshotIdentifier?: fabric.MaybeComputed<string>;
    readonly iamDatabaseAuthenticationEnabled?: fabric.MaybeComputed<boolean>;
    readonly identifier?: fabric.MaybeComputed<string>;
    readonly identifierPrefix?: fabric.MaybeComputed<string>;
    readonly instanceClass: fabric.MaybeComputed<string>;
    readonly iops?: fabric.MaybeComputed<number>;
    readonly kmsKeyId?: fabric.MaybeComputed<string>;
    readonly licenseModel?: fabric.MaybeComputed<string>;
    readonly maintenanceWindow?: fabric.MaybeComputed<string>;
    readonly monitoringInterval?: fabric.MaybeComputed<number>;
    readonly monitoringRoleArn?: fabric.MaybeComputed<string>;
    readonly multiAz?: fabric.MaybeComputed<boolean>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly optionGroupName?: fabric.MaybeComputed<string>;
    readonly parameterGroupName?: fabric.MaybeComputed<string>;
    readonly password?: fabric.MaybeComputed<string>;
    readonly port?: fabric.MaybeComputed<number>;
    readonly publiclyAccessible?: fabric.MaybeComputed<boolean>;
    readonly replicateSourceDb?: fabric.MaybeComputed<string>;
    readonly securityGroupNames?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly skipFinalSnapshot?: fabric.MaybeComputed<boolean>;
    readonly snapshotIdentifier?: fabric.MaybeComputed<string>;
    readonly storageEncrypted?: fabric.MaybeComputed<boolean>;
    readonly storageType?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly timezone?: fabric.MaybeComputed<string>;
    readonly username?: fabric.MaybeComputed<string>;
    readonly vpcSecurityGroupIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
}
