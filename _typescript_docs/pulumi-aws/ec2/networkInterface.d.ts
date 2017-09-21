---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/networkInterface.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class NetworkInterface extends fabric.Resource {
    readonly attachment: fabric.Computed<{
        attachmentId: string;
        deviceIndex: number;
        instance: string;
    }[]>;
    readonly description?: fabric.Computed<string>;
    readonly privateIp: fabric.Computed<string>;
    readonly privateIps: fabric.Computed<string[]>;
    readonly privateIpsCount: fabric.Computed<number>;
    readonly securityGroups: fabric.Computed<string[]>;
    readonly sourceDestCheck?: fabric.Computed<boolean>;
    readonly subnetId: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: NetworkInterfaceArgs);
}
export interface NetworkInterfaceArgs {
    readonly attachment?: fabric.MaybeComputed<{
        attachmentId?: fabric.MaybeComputed<string>;
        deviceIndex: fabric.MaybeComputed<number>;
        instance: fabric.MaybeComputed<string>;
    }>[];
    readonly description?: fabric.MaybeComputed<string>;
    readonly privateIp?: fabric.MaybeComputed<string>;
    readonly privateIps?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly privateIpsCount?: fabric.MaybeComputed<number>;
    readonly securityGroups?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly sourceDestCheck?: fabric.MaybeComputed<boolean>;
    readonly subnetId: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
