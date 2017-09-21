---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/eipAssociation.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class EipAssociation extends fabric.Resource {
    readonly allocationId: fabric.Computed<string>;
    readonly allowReassociation?: fabric.Computed<boolean>;
    readonly instanceId: fabric.Computed<string>;
    readonly networkInterfaceId: fabric.Computed<string>;
    readonly privateIpAddress: fabric.Computed<string>;
    readonly publicIp: fabric.Computed<string>;
    constructor(urnName: string, args: EipAssociationArgs);
}
export interface EipAssociationArgs {
    readonly allocationId?: fabric.MaybeComputed<string>;
    readonly allowReassociation?: fabric.MaybeComputed<boolean>;
    readonly instanceId?: fabric.MaybeComputed<string>;
    readonly networkInterfaceId?: fabric.MaybeComputed<string>;
    readonly privateIpAddress?: fabric.MaybeComputed<string>;
    readonly publicIp?: fabric.MaybeComputed<string>;
}
