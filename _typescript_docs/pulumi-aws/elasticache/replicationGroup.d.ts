---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticache/replicationGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ReplicationGroup extends fabric.Resource {
    readonly applyImmediately: fabric.Computed<boolean>;
    readonly autoMinorVersionUpgrade?: fabric.Computed<boolean>;
    readonly automaticFailoverEnabled?: fabric.Computed<boolean>;
    readonly availabilityZones?: fabric.Computed<string[]>;
    readonly clusterMode?: fabric.Computed<{
        numNodeGroups: number;
        replicasPerNodeGroup: number;
    }[]>;
    readonly configurationEndpointAddress: fabric.Computed<string>;
    readonly engine?: fabric.Computed<string>;
    readonly engineVersion: fabric.Computed<string>;
    readonly maintenanceWindow: fabric.Computed<string>;
    readonly nodeType: fabric.Computed<string>;
    readonly notificationTopicArn?: fabric.Computed<string>;
    readonly numberCacheClusters: fabric.Computed<number>;
    readonly parameterGroupName: fabric.Computed<string>;
    readonly port: fabric.Computed<number>;
    readonly primaryEndpointAddress: fabric.Computed<string>;
    readonly replicationGroupDescription: fabric.Computed<string>;
    readonly replicationGroupId: fabric.Computed<string>;
    readonly securityGroupIds: fabric.Computed<string[]>;
    readonly securityGroupNames: fabric.Computed<string[]>;
    readonly snapshotArns?: fabric.Computed<string[]>;
    readonly snapshotName?: fabric.Computed<string>;
    readonly snapshotRetentionLimit?: fabric.Computed<number>;
    readonly snapshotWindow: fabric.Computed<string>;
    readonly subnetGroupName: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: ReplicationGroupArgs);
}
export interface ReplicationGroupArgs {
    readonly applyImmediately?: fabric.MaybeComputed<boolean>;
    readonly autoMinorVersionUpgrade?: fabric.MaybeComputed<boolean>;
    readonly automaticFailoverEnabled?: fabric.MaybeComputed<boolean>;
    readonly availabilityZones?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly clusterMode?: fabric.MaybeComputed<{
        numNodeGroups: fabric.MaybeComputed<number>;
        replicasPerNodeGroup: fabric.MaybeComputed<number>;
    }>[];
    readonly engine?: fabric.MaybeComputed<string>;
    readonly engineVersion?: fabric.MaybeComputed<string>;
    readonly maintenanceWindow?: fabric.MaybeComputed<string>;
    readonly nodeType: fabric.MaybeComputed<string>;
    readonly notificationTopicArn?: fabric.MaybeComputed<string>;
    readonly numberCacheClusters?: fabric.MaybeComputed<number>;
    readonly parameterGroupName?: fabric.MaybeComputed<string>;
    readonly port: fabric.MaybeComputed<number>;
    readonly replicationGroupDescription: fabric.MaybeComputed<string>;
    readonly replicationGroupId: fabric.MaybeComputed<string>;
    readonly securityGroupIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly securityGroupNames?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly snapshotArns?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly snapshotName?: fabric.MaybeComputed<string>;
    readonly snapshotRetentionLimit?: fabric.MaybeComputed<number>;
    readonly snapshotWindow?: fabric.MaybeComputed<string>;
    readonly subnetGroupName?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
