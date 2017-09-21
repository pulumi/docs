---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/amiFromInstance.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class AmiFromInstance extends fabric.Resource {
    readonly architecture: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly ebsBlockDevice: fabric.Computed<{
        deleteOnTermination: boolean;
        deviceName: string;
        encrypted: boolean;
        iops: number;
        snapshotId: string;
        volumeSize: number;
        volumeType: string;
    }[]>;
    readonly ephemeralBlockDevice: fabric.Computed<{
        deviceName: string;
        virtualName: string;
    }[]>;
    readonly amiId: fabric.Computed<string>;
    readonly imageLocation: fabric.Computed<string>;
    readonly kernelId: fabric.Computed<string>;
    readonly manageEbsSnapshots: fabric.Computed<boolean>;
    readonly name: fabric.Computed<string>;
    readonly ramdiskId: fabric.Computed<string>;
    readonly rootDeviceName: fabric.Computed<string>;
    readonly snapshotWithoutReboot?: fabric.Computed<boolean>;
    readonly sourceInstanceId: fabric.Computed<string>;
    readonly sriovNetSupport: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly virtualizationType: fabric.Computed<string>;
    constructor(urnName: string, args: AmiFromInstanceArgs);
}
export interface AmiFromInstanceArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly ebsBlockDevice?: fabric.MaybeComputed<{
        deleteOnTermination?: fabric.MaybeComputed<boolean>;
        deviceName?: fabric.MaybeComputed<string>;
        encrypted?: fabric.MaybeComputed<boolean>;
        iops?: fabric.MaybeComputed<number>;
        snapshotId?: fabric.MaybeComputed<string>;
        volumeSize?: fabric.MaybeComputed<number>;
        volumeType?: fabric.MaybeComputed<string>;
    }>[];
    readonly ephemeralBlockDevice?: fabric.MaybeComputed<{
        deviceName?: fabric.MaybeComputed<string>;
        virtualName?: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly snapshotWithoutReboot?: fabric.MaybeComputed<boolean>;
    readonly sourceInstanceId: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
