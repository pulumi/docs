---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/instance.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { InstanceType } from "./instanceType";
export declare class Instance extends fabric.Resource {
    readonly ami: fabric.Computed<string>;
    readonly associatePublicIpAddress: fabric.Computed<boolean>;
    readonly availabilityZone: fabric.Computed<string>;
    readonly disableApiTermination?: fabric.Computed<boolean>;
    readonly ebsBlockDevice: fabric.Computed<{
        deleteOnTermination?: boolean;
        deviceName: string;
        encrypted: boolean;
        iops: number;
        snapshotId: string;
        volumeSize: number;
        volumeType: string;
    }[]>;
    readonly ebsOptimized?: fabric.Computed<boolean>;
    readonly ephemeralBlockDevice: fabric.Computed<{
        deviceName: string;
        noDevice?: boolean;
        virtualName?: string;
    }[]>;
    readonly iamInstanceProfile?: fabric.Computed<string>;
    readonly instanceInitiatedShutdownBehavior?: fabric.Computed<string>;
    readonly instanceState: fabric.Computed<string>;
    readonly instanceType: fabric.Computed<InstanceType>;
    readonly ipv6AddressCount: fabric.Computed<number>;
    readonly ipv6Addresses: fabric.Computed<string[]>;
    readonly keyName: fabric.Computed<string>;
    readonly monitoring?: fabric.Computed<boolean>;
    readonly networkInterface: fabric.Computed<{
        deleteOnTermination?: boolean;
        deviceIndex: number;
        networkInterfaceId: string;
    }[]>;
    readonly networkInterfaceId: fabric.Computed<string>;
    readonly placementGroup: fabric.Computed<string>;
    readonly primaryNetworkInterfaceId: fabric.Computed<string>;
    readonly privateDns: fabric.Computed<string>;
    readonly privateIp: fabric.Computed<string>;
    readonly publicDns: fabric.Computed<string>;
    readonly publicIp: fabric.Computed<string>;
    readonly rootBlockDevice: fabric.Computed<{
        deleteOnTermination?: boolean;
        iops: number;
        volumeSize: number;
        volumeType: string;
    }[]>;
    readonly securityGroups: fabric.Computed<string[]>;
    readonly sourceDestCheck?: fabric.Computed<boolean>;
    readonly subnetId: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly tenancy: fabric.Computed<string>;
    readonly userData?: fabric.Computed<string>;
    readonly volumeTags: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcSecurityGroupIds: fabric.Computed<string[]>;
    constructor(urnName: string, args: InstanceArgs);
}
export interface InstanceArgs {
    readonly ami: fabric.MaybeComputed<string>;
    readonly associatePublicIpAddress?: fabric.MaybeComputed<boolean>;
    readonly availabilityZone?: fabric.MaybeComputed<string>;
    readonly disableApiTermination?: fabric.MaybeComputed<boolean>;
    readonly ebsBlockDevice?: fabric.MaybeComputed<{
        deleteOnTermination?: fabric.MaybeComputed<boolean>;
        deviceName: fabric.MaybeComputed<string>;
        encrypted?: fabric.MaybeComputed<boolean>;
        iops?: fabric.MaybeComputed<number>;
        snapshotId?: fabric.MaybeComputed<string>;
        volumeSize?: fabric.MaybeComputed<number>;
        volumeType?: fabric.MaybeComputed<string>;
    }>[];
    readonly ebsOptimized?: fabric.MaybeComputed<boolean>;
    readonly ephemeralBlockDevice?: fabric.MaybeComputed<{
        deviceName: fabric.MaybeComputed<string>;
        noDevice?: fabric.MaybeComputed<boolean>;
        virtualName?: fabric.MaybeComputed<string>;
    }>[];
    readonly iamInstanceProfile?: fabric.MaybeComputed<string>;
    readonly instanceInitiatedShutdownBehavior?: fabric.MaybeComputed<string>;
    readonly instanceType: fabric.MaybeComputed<InstanceType>;
    readonly ipv6AddressCount?: fabric.MaybeComputed<number>;
    readonly ipv6Addresses?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly keyName?: fabric.MaybeComputed<string>;
    readonly monitoring?: fabric.MaybeComputed<boolean>;
    readonly networkInterface?: fabric.MaybeComputed<{
        deleteOnTermination?: fabric.MaybeComputed<boolean>;
        deviceIndex: fabric.MaybeComputed<number>;
        networkInterfaceId: fabric.MaybeComputed<string>;
    }>[];
    readonly placementGroup?: fabric.MaybeComputed<string>;
    readonly privateIp?: fabric.MaybeComputed<string>;
    readonly rootBlockDevice?: fabric.MaybeComputed<{
        deleteOnTermination?: fabric.MaybeComputed<boolean>;
        iops?: fabric.MaybeComputed<number>;
        volumeSize?: fabric.MaybeComputed<number>;
        volumeType?: fabric.MaybeComputed<string>;
    }>[];
    readonly securityGroups?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly sourceDestCheck?: fabric.MaybeComputed<boolean>;
    readonly subnetId?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly tenancy?: fabric.MaybeComputed<string>;
    readonly userData?: fabric.MaybeComputed<string>;
    readonly volumeTags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly vpcSecurityGroupIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
}
