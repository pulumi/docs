---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/eip.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Eip extends fabric.Resource {
    readonly allocationId: fabric.Computed<string>;
    readonly associateWithPrivateIp?: fabric.Computed<string>;
    readonly associationId: fabric.Computed<string>;
    readonly domain: fabric.Computed<string>;
    readonly instance: fabric.Computed<string>;
    readonly networkInterface: fabric.Computed<string>;
    readonly privateIp: fabric.Computed<string>;
    readonly publicIp: fabric.Computed<string>;
    readonly vpc: fabric.Computed<boolean>;
    constructor(urnName: string, args: EipArgs);
}
export interface EipArgs {
    readonly associateWithPrivateIp?: fabric.MaybeComputed<string>;
    readonly instance?: fabric.MaybeComputed<string>;
    readonly networkInterface?: fabric.MaybeComputed<string>;
    readonly vpc?: fabric.MaybeComputed<boolean>;
}
