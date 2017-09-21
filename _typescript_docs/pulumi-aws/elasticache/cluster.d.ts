---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticache/cluster.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Cluster extends fabric.Resource {
    readonly applyImmediately: fabric.Computed<boolean>;
    readonly availabilityZone: fabric.Computed<string>;
    readonly availabilityZones?: fabric.Computed<string[]>;
    readonly azMode: fabric.Computed<string>;
    readonly cacheNodes: fabric.Computed<{
        address: string;
        availabilityZone: string;
        id: string;
        port: number;
    }[]>;
    readonly clusterAddress: fabric.Computed<string>;
    readonly clusterId: fabric.Computed<string>;
    readonly configurationEndpoint: fabric.Computed<string>;
    readonly engine: fabric.Computed<string>;
    readonly engineVersion: fabric.Computed<string>;
    readonly maintenanceWindow: fabric.Computed<string>;
    readonly nodeType: fabric.Computed<string>;
    readonly notificationTopicArn?: fabric.Computed<string>;
    readonly numCacheNodes: fabric.Computed<number>;
    readonly parameterGroupName: fabric.Computed<string>;
    readonly port: fabric.Computed<number>;
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
    constructor(urnName: string, args: ClusterArgs);
}
export interface ClusterArgs {
    readonly applyImmediately?: fabric.MaybeComputed<boolean>;
    readonly availabilityZone?: fabric.MaybeComputed<string>;
    readonly availabilityZones?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly azMode?: fabric.MaybeComputed<string>;
    readonly clusterId: fabric.MaybeComputed<string>;
    readonly engine: fabric.MaybeComputed<string>;
    readonly engineVersion?: fabric.MaybeComputed<string>;
    readonly maintenanceWindow?: fabric.MaybeComputed<string>;
    readonly nodeType: fabric.MaybeComputed<string>;
    readonly notificationTopicArn?: fabric.MaybeComputed<string>;
    readonly numCacheNodes: fabric.MaybeComputed<number>;
    readonly parameterGroupName?: fabric.MaybeComputed<string>;
    readonly port: fabric.MaybeComputed<number>;
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
