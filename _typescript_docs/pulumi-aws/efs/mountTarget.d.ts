---
layout: typescript-reference
repo: pulumi-aws
subpath: efs/mountTarget.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class MountTarget extends fabric.Resource {
    readonly dnsName: fabric.Computed<string>;
    readonly fileSystemId: fabric.Computed<string>;
    readonly ipAddress: fabric.Computed<string>;
    readonly networkInterfaceId: fabric.Computed<string>;
    readonly securityGroups: fabric.Computed<string[]>;
    readonly subnetId: fabric.Computed<string>;
    constructor(urnName: string, args: MountTargetArgs);
}
export interface MountTargetArgs {
    readonly fileSystemId: fabric.MaybeComputed<string>;
    readonly ipAddress?: fabric.MaybeComputed<string>;
    readonly securityGroups?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly subnetId: fabric.MaybeComputed<string>;
}
