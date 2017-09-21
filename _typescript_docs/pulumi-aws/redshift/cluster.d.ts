---
layout: typescript-reference
repo: pulumi-aws
subpath: redshift/cluster.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Cluster extends fabric.Resource {
    readonly allowVersionUpgrade?: fabric.Computed<boolean>;
    readonly automatedSnapshotRetentionPeriod?: fabric.Computed<number>;
    readonly availabilityZone: fabric.Computed<string>;
    readonly bucketName: fabric.Computed<string>;
    readonly clusterIdentifier: fabric.Computed<string>;
    readonly clusterParameterGroupName: fabric.Computed<string>;
    readonly clusterPublicKey: fabric.Computed<string>;
    readonly clusterRevisionNumber: fabric.Computed<string>;
    readonly clusterSecurityGroups: fabric.Computed<string[]>;
    readonly clusterSubnetGroupName: fabric.Computed<string>;
    readonly clusterType: fabric.Computed<string>;
    readonly clusterVersion?: fabric.Computed<string>;
    readonly databaseName: fabric.Computed<string>;
    readonly elasticIp?: fabric.Computed<string>;
    readonly enableLogging?: fabric.Computed<boolean>;
    readonly encrypted: fabric.Computed<boolean>;
    readonly endpoint: fabric.Computed<string>;
    readonly enhancedVpcRouting: fabric.Computed<boolean>;
    readonly finalSnapshotIdentifier?: fabric.Computed<string>;
    readonly iamRoles: fabric.Computed<string[]>;
    readonly kmsKeyId: fabric.Computed<string>;
    readonly masterPassword?: fabric.Computed<string>;
    readonly masterUsername?: fabric.Computed<string>;
    readonly nodeType: fabric.Computed<string>;
    readonly numberOfNodes?: fabric.Computed<number>;
    readonly ownerAccount?: fabric.Computed<string>;
    readonly port?: fabric.Computed<number>;
    readonly preferredMaintenanceWindow: fabric.Computed<string>;
    readonly publiclyAccessible?: fabric.Computed<boolean>;
    readonly s3KeyPrefix: fabric.Computed<string>;
    readonly skipFinalSnapshot?: fabric.Computed<boolean>;
    readonly snapshotClusterIdentifier?: fabric.Computed<string>;
    readonly snapshotIdentifier?: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcSecurityGroupIds: fabric.Computed<string[]>;
    constructor(urnName: string, args: ClusterArgs);
}
export interface ClusterArgs {
    readonly allowVersionUpgrade?: fabric.MaybeComputed<boolean>;
    readonly automatedSnapshotRetentionPeriod?: fabric.MaybeComputed<number>;
    readonly availabilityZone?: fabric.MaybeComputed<string>;
    readonly bucketName?: fabric.MaybeComputed<string>;
    readonly clusterIdentifier: fabric.MaybeComputed<string>;
    readonly clusterParameterGroupName?: fabric.MaybeComputed<string>;
    readonly clusterPublicKey?: fabric.MaybeComputed<string>;
    readonly clusterRevisionNumber?: fabric.MaybeComputed<string>;
    readonly clusterSecurityGroups?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly clusterSubnetGroupName?: fabric.MaybeComputed<string>;
    readonly clusterType?: fabric.MaybeComputed<string>;
    readonly clusterVersion?: fabric.MaybeComputed<string>;
    readonly databaseName?: fabric.MaybeComputed<string>;
    readonly elasticIp?: fabric.MaybeComputed<string>;
    readonly enableLogging?: fabric.MaybeComputed<boolean>;
    readonly encrypted?: fabric.MaybeComputed<boolean>;
    readonly endpoint?: fabric.MaybeComputed<string>;
    readonly enhancedVpcRouting?: fabric.MaybeComputed<boolean>;
    readonly finalSnapshotIdentifier?: fabric.MaybeComputed<string>;
    readonly iamRoles?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly kmsKeyId?: fabric.MaybeComputed<string>;
    readonly masterPassword?: fabric.MaybeComputed<string>;
    readonly masterUsername?: fabric.MaybeComputed<string>;
    readonly nodeType: fabric.MaybeComputed<string>;
    readonly numberOfNodes?: fabric.MaybeComputed<number>;
    readonly ownerAccount?: fabric.MaybeComputed<string>;
    readonly port?: fabric.MaybeComputed<number>;
    readonly preferredMaintenanceWindow?: fabric.MaybeComputed<string>;
    readonly publiclyAccessible?: fabric.MaybeComputed<boolean>;
    readonly s3KeyPrefix?: fabric.MaybeComputed<string>;
    readonly skipFinalSnapshot?: fabric.MaybeComputed<boolean>;
    readonly snapshotClusterIdentifier?: fabric.MaybeComputed<string>;
    readonly snapshotIdentifier?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly vpcSecurityGroupIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
}
