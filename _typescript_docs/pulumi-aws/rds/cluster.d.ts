---
layout: typescript-reference
repo: pulumi-aws
subpath: rds/cluster.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Cluster extends fabric.Resource {
    readonly applyImmediately: fabric.Computed<boolean>;
    readonly availabilityZones: fabric.Computed<string[]>;
    readonly backupRetentionPeriod?: fabric.Computed<number>;
    readonly clusterIdentifier: fabric.Computed<string>;
    readonly clusterIdentifierPrefix: fabric.Computed<string>;
    readonly clusterMembers: fabric.Computed<string[]>;
    readonly clusterResourceId: fabric.Computed<string>;
    readonly databaseName: fabric.Computed<string>;
    readonly dbClusterParameterGroupName: fabric.Computed<string>;
    readonly dbSubnetGroupName: fabric.Computed<string>;
    readonly endpoint: fabric.Computed<string>;
    readonly engine: fabric.Computed<string>;
    readonly finalSnapshotIdentifier?: fabric.Computed<string>;
    readonly iamDatabaseAuthenticationEnabled?: fabric.Computed<boolean>;
    readonly kmsKeyId: fabric.Computed<string>;
    readonly masterPassword?: fabric.Computed<string>;
    readonly masterUsername: fabric.Computed<string>;
    readonly port: fabric.Computed<number>;
    readonly preferredBackupWindow: fabric.Computed<string>;
    readonly preferredMaintenanceWindow: fabric.Computed<string>;
    readonly readerEndpoint: fabric.Computed<string>;
    readonly replicationSourceIdentifier?: fabric.Computed<string>;
    readonly skipFinalSnapshot?: fabric.Computed<boolean>;
    readonly snapshotIdentifier?: fabric.Computed<string>;
    readonly storageEncrypted?: fabric.Computed<boolean>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcSecurityGroupIds: fabric.Computed<string[]>;
    constructor(urnName: string, args: ClusterArgs);
}
export interface ClusterArgs {
    readonly applyImmediately?: fabric.MaybeComputed<boolean>;
    readonly availabilityZones?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly backupRetentionPeriod?: fabric.MaybeComputed<number>;
    readonly clusterIdentifier?: fabric.MaybeComputed<string>;
    readonly clusterIdentifierPrefix?: fabric.MaybeComputed<string>;
    readonly clusterMembers?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly databaseName?: fabric.MaybeComputed<string>;
    readonly dbClusterParameterGroupName?: fabric.MaybeComputed<string>;
    readonly dbSubnetGroupName?: fabric.MaybeComputed<string>;
    readonly finalSnapshotIdentifier?: fabric.MaybeComputed<string>;
    readonly iamDatabaseAuthenticationEnabled?: fabric.MaybeComputed<boolean>;
    readonly kmsKeyId?: fabric.MaybeComputed<string>;
    readonly masterPassword?: fabric.MaybeComputed<string>;
    readonly masterUsername?: fabric.MaybeComputed<string>;
    readonly port?: fabric.MaybeComputed<number>;
    readonly preferredBackupWindow?: fabric.MaybeComputed<string>;
    readonly preferredMaintenanceWindow?: fabric.MaybeComputed<string>;
    readonly replicationSourceIdentifier?: fabric.MaybeComputed<string>;
    readonly skipFinalSnapshot?: fabric.MaybeComputed<boolean>;
    readonly snapshotIdentifier?: fabric.MaybeComputed<string>;
    readonly storageEncrypted?: fabric.MaybeComputed<boolean>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly vpcSecurityGroupIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
}
