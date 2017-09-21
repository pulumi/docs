---
layout: typescript-reference
repo: pulumi-aws
subpath: rds/clusterInstance.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ClusterInstance extends fabric.Resource {
    readonly applyImmediately: fabric.Computed<boolean>;
    readonly autoMinorVersionUpgrade?: fabric.Computed<boolean>;
    readonly clusterIdentifier: fabric.Computed<string>;
    readonly dbParameterGroupName: fabric.Computed<string>;
    readonly dbSubnetGroupName: fabric.Computed<string>;
    readonly dbiResourceId: fabric.Computed<string>;
    readonly endpoint: fabric.Computed<string>;
    readonly identifier: fabric.Computed<string>;
    readonly identifierPrefix: fabric.Computed<string>;
    readonly instanceClass: fabric.Computed<string>;
    readonly kmsKeyId: fabric.Computed<string>;
    readonly monitoringInterval?: fabric.Computed<number>;
    readonly monitoringRoleArn: fabric.Computed<string>;
    readonly port: fabric.Computed<number>;
    readonly preferredBackupWindow: fabric.Computed<string>;
    readonly preferredMaintenanceWindow: fabric.Computed<string>;
    readonly promotionTier?: fabric.Computed<number>;
    readonly publiclyAccessible?: fabric.Computed<boolean>;
    readonly storageEncrypted: fabric.Computed<boolean>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly writer: fabric.Computed<boolean>;
    constructor(urnName: string, args: ClusterInstanceArgs);
}
export interface ClusterInstanceArgs {
    readonly applyImmediately?: fabric.MaybeComputed<boolean>;
    readonly autoMinorVersionUpgrade?: fabric.MaybeComputed<boolean>;
    readonly clusterIdentifier: fabric.MaybeComputed<string>;
    readonly dbParameterGroupName?: fabric.MaybeComputed<string>;
    readonly dbSubnetGroupName?: fabric.MaybeComputed<string>;
    readonly identifier?: fabric.MaybeComputed<string>;
    readonly identifierPrefix?: fabric.MaybeComputed<string>;
    readonly instanceClass: fabric.MaybeComputed<string>;
    readonly monitoringInterval?: fabric.MaybeComputed<number>;
    readonly monitoringRoleArn?: fabric.MaybeComputed<string>;
    readonly preferredBackupWindow?: fabric.MaybeComputed<string>;
    readonly preferredMaintenanceWindow?: fabric.MaybeComputed<string>;
    readonly promotionTier?: fabric.MaybeComputed<number>;
    readonly publiclyAccessible?: fabric.MaybeComputed<boolean>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
