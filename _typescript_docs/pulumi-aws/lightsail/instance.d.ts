---
layout: typescript-reference
repo: pulumi-aws
subpath: lightsail/instance.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Instance extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly availabilityZone: fabric.Computed<string>;
    readonly blueprintId: fabric.Computed<string>;
    readonly bundleId: fabric.Computed<string>;
    readonly cpuCount: fabric.Computed<number>;
    readonly createdAt: fabric.Computed<string>;
    readonly ipv6Address: fabric.Computed<string>;
    readonly isStaticIp: fabric.Computed<boolean>;
    readonly keyPairName?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly privateIpAddress: fabric.Computed<string>;
    readonly publicIpAddress: fabric.Computed<string>;
    readonly ramSize: fabric.Computed<number>;
    readonly userData?: fabric.Computed<string>;
    readonly username: fabric.Computed<string>;
    constructor(urnName: string, args: InstanceArgs);
}
export interface InstanceArgs {
    readonly availabilityZone: fabric.MaybeComputed<string>;
    readonly blueprintId: fabric.MaybeComputed<string>;
    readonly bundleId: fabric.MaybeComputed<string>;
    readonly keyPairName?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly userData?: fabric.MaybeComputed<string>;
}
