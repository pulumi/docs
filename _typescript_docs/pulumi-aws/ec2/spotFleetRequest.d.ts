---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/spotFleetRequest.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SpotFleetRequest extends fabric.Resource {
    readonly allocationStrategy?: fabric.Computed<string>;
    readonly clientToken: fabric.Computed<string>;
    readonly excessCapacityTerminationPolicy?: fabric.Computed<string>;
    readonly iamFleetRole: fabric.Computed<string>;
    readonly launchSpecification: fabric.Computed<{
        ami: string;
        associatePublicIpAddress?: boolean;
        availabilityZone: string;
        ebsBlockDevice: {
            deleteOnTermination?: boolean;
            deviceName: string;
            encrypted: boolean;
            iops: number;
            snapshotId: string;
            volumeSize: number;
            volumeType: string;
        }[];
        ebsOptimized?: boolean;
        ephemeralBlockDevice: {
            deviceName: string;
            virtualName: string;
        }[];
        iamInstanceProfile?: string;
        instanceType: string;
        keyName: string;
        monitoring?: boolean;
        placementGroup: string;
        placementTenancy?: string;
        rootBlockDevice: {
            deleteOnTermination?: boolean;
            iops: number;
            volumeSize: number;
            volumeType: string;
        }[];
        spotPrice?: string;
        subnetId: string;
        userData?: string;
        vpcSecurityGroupIds: string[];
        weightedCapacity?: string;
    }[]>;
    readonly replaceUnhealthyInstances?: fabric.Computed<boolean>;
    readonly spotPrice: fabric.Computed<string>;
    readonly spotRequestState: fabric.Computed<string>;
    readonly targetCapacity: fabric.Computed<number>;
    readonly terminateInstancesWithExpiration?: fabric.Computed<boolean>;
    readonly validFrom?: fabric.Computed<string>;
    readonly validUntil?: fabric.Computed<string>;
    constructor(urnName: string, args: SpotFleetRequestArgs);
}
export interface SpotFleetRequestArgs {
    readonly allocationStrategy?: fabric.MaybeComputed<string>;
    readonly excessCapacityTerminationPolicy?: fabric.MaybeComputed<string>;
    readonly iamFleetRole: fabric.MaybeComputed<string>;
    readonly launchSpecification: fabric.MaybeComputed<{
        ami: fabric.MaybeComputed<string>;
        associatePublicIpAddress?: fabric.MaybeComputed<boolean>;
        availabilityZone?: fabric.MaybeComputed<string>;
        ebsBlockDevice?: fabric.MaybeComputed<{
            deleteOnTermination?: fabric.MaybeComputed<boolean>;
            deviceName: fabric.MaybeComputed<string>;
            encrypted?: fabric.MaybeComputed<boolean>;
            iops?: fabric.MaybeComputed<number>;
            snapshotId?: fabric.MaybeComputed<string>;
            volumeSize?: fabric.MaybeComputed<number>;
            volumeType?: fabric.MaybeComputed<string>;
        }>[];
        ebsOptimized?: fabric.MaybeComputed<boolean>;
        ephemeralBlockDevice?: fabric.MaybeComputed<{
            deviceName: fabric.MaybeComputed<string>;
            virtualName: fabric.MaybeComputed<string>;
        }>[];
        iamInstanceProfile?: fabric.MaybeComputed<string>;
        instanceType: fabric.MaybeComputed<string>;
        keyName?: fabric.MaybeComputed<string>;
        monitoring?: fabric.MaybeComputed<boolean>;
        placementGroup?: fabric.MaybeComputed<string>;
        placementTenancy?: fabric.MaybeComputed<string>;
        rootBlockDevice?: fabric.MaybeComputed<{
            deleteOnTermination?: fabric.MaybeComputed<boolean>;
            iops?: fabric.MaybeComputed<number>;
            volumeSize?: fabric.MaybeComputed<number>;
            volumeType?: fabric.MaybeComputed<string>;
        }>[];
        spotPrice?: fabric.MaybeComputed<string>;
        subnetId?: fabric.MaybeComputed<string>;
        userData?: fabric.MaybeComputed<string>;
        vpcSecurityGroupIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        weightedCapacity?: fabric.MaybeComputed<string>;
    }>[];
    readonly replaceUnhealthyInstances?: fabric.MaybeComputed<boolean>;
    readonly spotPrice: fabric.MaybeComputed<string>;
    readonly targetCapacity: fabric.MaybeComputed<number>;
    readonly terminateInstancesWithExpiration?: fabric.MaybeComputed<boolean>;
    readonly validFrom?: fabric.MaybeComputed<string>;
    readonly validUntil?: fabric.MaybeComputed<string>;
}
