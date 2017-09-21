---
layout: typescript-reference
repo: pulumi-aws
subpath: opsworks/instance.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Instance extends fabric.Resource {
    readonly agentVersion?: fabric.Computed<string>;
    readonly amiId: fabric.Computed<string>;
    readonly architecture?: fabric.Computed<string>;
    readonly autoScalingType?: fabric.Computed<string>;
    readonly availabilityZone: fabric.Computed<string>;
    readonly createdAt: fabric.Computed<string>;
    readonly deleteEbs?: fabric.Computed<boolean>;
    readonly deleteEip?: fabric.Computed<boolean>;
    readonly ebsBlockDevice: fabric.Computed<{
        deleteOnTermination?: boolean;
        deviceName: string;
        iops: number;
        snapshotId: string;
        volumeSize: number;
        volumeType: string;
    }[]>;
    readonly ebsOptimized?: fabric.Computed<boolean>;
    readonly ec2InstanceId: fabric.Computed<string>;
    readonly ecsClusterArn: fabric.Computed<string>;
    readonly elasticIp: fabric.Computed<string>;
    readonly ephemeralBlockDevice: fabric.Computed<{
        deviceName: string;
        virtualName: string;
    }[]>;
    readonly hostname: fabric.Computed<string>;
    readonly instanceId: fabric.Computed<string>;
    readonly infrastructureClass: fabric.Computed<string>;
    readonly installUpdatesOnBoot?: fabric.Computed<boolean>;
    readonly instanceProfileArn: fabric.Computed<string>;
    readonly instanceType?: fabric.Computed<string>;
    readonly lastServiceErrorId: fabric.Computed<string>;
    readonly layerIds: fabric.Computed<string[]>;
    readonly os: fabric.Computed<string>;
    readonly platform: fabric.Computed<string>;
    readonly privateDns: fabric.Computed<string>;
    readonly privateIp: fabric.Computed<string>;
    readonly publicDns: fabric.Computed<string>;
    readonly publicIp: fabric.Computed<string>;
    readonly registeredBy: fabric.Computed<string>;
    readonly reportedAgentVersion: fabric.Computed<string>;
    readonly reportedOsFamily: fabric.Computed<string>;
    readonly reportedOsName: fabric.Computed<string>;
    readonly reportedOsVersion: fabric.Computed<string>;
    readonly rootBlockDevice: fabric.Computed<{
        deleteOnTermination?: boolean;
        iops: number;
        volumeSize: number;
        volumeType: string;
    }[]>;
    readonly rootDeviceType: fabric.Computed<string>;
    readonly rootDeviceVolumeId: fabric.Computed<string>;
    readonly securityGroupIds: fabric.Computed<string[]>;
    readonly sshHostDsaKeyFingerprint: fabric.Computed<string>;
    readonly sshHostRsaKeyFingerprint: fabric.Computed<string>;
    readonly sshKeyName: fabric.Computed<string>;
    readonly stackId: fabric.Computed<string>;
    readonly state?: fabric.Computed<string>;
    readonly status: fabric.Computed<string>;
    readonly subnetId: fabric.Computed<string>;
    readonly tenancy: fabric.Computed<string>;
    readonly virtualizationType: fabric.Computed<string>;
    constructor(urnName: string, args: InstanceArgs);
}
export interface InstanceArgs {
    readonly agentVersion?: fabric.MaybeComputed<string>;
    readonly amiId?: fabric.MaybeComputed<string>;
    readonly architecture?: fabric.MaybeComputed<string>;
    readonly autoScalingType?: fabric.MaybeComputed<string>;
    readonly availabilityZone?: fabric.MaybeComputed<string>;
    readonly createdAt?: fabric.MaybeComputed<string>;
    readonly deleteEbs?: fabric.MaybeComputed<boolean>;
    readonly deleteEip?: fabric.MaybeComputed<boolean>;
    readonly ebsBlockDevice?: fabric.MaybeComputed<{
        deleteOnTermination?: fabric.MaybeComputed<boolean>;
        deviceName: fabric.MaybeComputed<string>;
        iops?: fabric.MaybeComputed<number>;
        snapshotId?: fabric.MaybeComputed<string>;
        volumeSize?: fabric.MaybeComputed<number>;
        volumeType?: fabric.MaybeComputed<string>;
    }>[];
    readonly ebsOptimized?: fabric.MaybeComputed<boolean>;
    readonly ec2InstanceId?: fabric.MaybeComputed<string>;
    readonly ecsClusterArn?: fabric.MaybeComputed<string>;
    readonly elasticIp?: fabric.MaybeComputed<string>;
    readonly ephemeralBlockDevice?: fabric.MaybeComputed<{
        deviceName: fabric.MaybeComputed<string>;
        virtualName: fabric.MaybeComputed<string>;
    }>[];
    readonly hostname?: fabric.MaybeComputed<string>;
    readonly infrastructureClass?: fabric.MaybeComputed<string>;
    readonly installUpdatesOnBoot?: fabric.MaybeComputed<boolean>;
    readonly instanceProfileArn?: fabric.MaybeComputed<string>;
    readonly instanceType?: fabric.MaybeComputed<string>;
    readonly lastServiceErrorId?: fabric.MaybeComputed<string>;
    readonly layerIds: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly os?: fabric.MaybeComputed<string>;
    readonly platform?: fabric.MaybeComputed<string>;
    readonly privateDns?: fabric.MaybeComputed<string>;
    readonly privateIp?: fabric.MaybeComputed<string>;
    readonly publicDns?: fabric.MaybeComputed<string>;
    readonly publicIp?: fabric.MaybeComputed<string>;
    readonly registeredBy?: fabric.MaybeComputed<string>;
    readonly reportedAgentVersion?: fabric.MaybeComputed<string>;
    readonly reportedOsFamily?: fabric.MaybeComputed<string>;
    readonly reportedOsName?: fabric.MaybeComputed<string>;
    readonly reportedOsVersion?: fabric.MaybeComputed<string>;
    readonly rootBlockDevice?: fabric.MaybeComputed<{
        deleteOnTermination?: fabric.MaybeComputed<boolean>;
        iops?: fabric.MaybeComputed<number>;
        volumeSize?: fabric.MaybeComputed<number>;
        volumeType?: fabric.MaybeComputed<string>;
    }>[];
    readonly rootDeviceType?: fabric.MaybeComputed<string>;
    readonly rootDeviceVolumeId?: fabric.MaybeComputed<string>;
    readonly securityGroupIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly sshHostDsaKeyFingerprint?: fabric.MaybeComputed<string>;
    readonly sshHostRsaKeyFingerprint?: fabric.MaybeComputed<string>;
    readonly sshKeyName?: fabric.MaybeComputed<string>;
    readonly stackId: fabric.MaybeComputed<string>;
    readonly state?: fabric.MaybeComputed<string>;
    readonly status?: fabric.MaybeComputed<string>;
    readonly subnetId?: fabric.MaybeComputed<string>;
    readonly tenancy?: fabric.MaybeComputed<string>;
    readonly virtualizationType?: fabric.MaybeComputed<string>;
}
