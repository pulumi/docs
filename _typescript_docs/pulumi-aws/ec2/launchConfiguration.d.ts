---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/launchConfiguration.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class LaunchConfiguration extends fabric.Resource {
    readonly associatePublicIpAddress?: fabric.Computed<boolean>;
    readonly ebsBlockDevice: fabric.Computed<{
        deleteOnTermination?: boolean;
        deviceName: string;
        encrypted: boolean;
        iops: number;
        snapshotId: string;
        volumeSize: number;
        volumeType: string;
    }[]>;
    readonly ebsOptimized: fabric.Computed<boolean>;
    readonly enableMonitoring?: fabric.Computed<boolean>;
    readonly ephemeralBlockDevice?: fabric.Computed<{
        deviceName: string;
        virtualName: string;
    }[]>;
    readonly iamInstanceProfile?: fabric.Computed<string>;
    readonly imageId: fabric.Computed<string>;
    readonly instanceType: fabric.Computed<string>;
    readonly keyName: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly placementTenancy?: fabric.Computed<string>;
    readonly rootBlockDevice: fabric.Computed<{
        deleteOnTermination?: boolean;
        iops: number;
        volumeSize: number;
        volumeType: string;
    }[]>;
    readonly securityGroups?: fabric.Computed<string[]>;
    readonly spotPrice?: fabric.Computed<string>;
    readonly userData?: fabric.Computed<string>;
    readonly vpcClassicLinkId?: fabric.Computed<string>;
    readonly vpcClassicLinkSecurityGroups?: fabric.Computed<string[]>;
    constructor(urnName: string, args: LaunchConfigurationArgs);
}
export interface LaunchConfigurationArgs {
    readonly associatePublicIpAddress?: fabric.MaybeComputed<boolean>;
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
    readonly enableMonitoring?: fabric.MaybeComputed<boolean>;
    readonly ephemeralBlockDevice?: fabric.MaybeComputed<{
        deviceName: fabric.MaybeComputed<string>;
        virtualName: fabric.MaybeComputed<string>;
    }>[];
    readonly iamInstanceProfile?: fabric.MaybeComputed<string>;
    readonly imageId: fabric.MaybeComputed<string>;
    readonly instanceType: fabric.MaybeComputed<string>;
    readonly keyName?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly placementTenancy?: fabric.MaybeComputed<string>;
    readonly rootBlockDevice?: fabric.MaybeComputed<{
        deleteOnTermination?: fabric.MaybeComputed<boolean>;
        iops?: fabric.MaybeComputed<number>;
        volumeSize?: fabric.MaybeComputed<number>;
        volumeType?: fabric.MaybeComputed<string>;
    }>[];
    readonly securityGroups?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly spotPrice?: fabric.MaybeComputed<string>;
    readonly userData?: fabric.MaybeComputed<string>;
    readonly vpcClassicLinkId?: fabric.MaybeComputed<string>;
    readonly vpcClassicLinkSecurityGroups?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
}
