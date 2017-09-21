---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/subnet.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Subnet extends fabric.Resource {
    readonly assignIpv6AddressOnCreation?: fabric.Computed<boolean>;
    readonly availabilityZone: fabric.Computed<string>;
    readonly cidrBlock: fabric.Computed<string>;
    readonly ipv6CidrBlock: fabric.Computed<string>;
    readonly ipv6CidrBlockAssociationId: fabric.Computed<string>;
    readonly mapPublicIpOnLaunch?: fabric.Computed<boolean>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: SubnetArgs);
}
export interface SubnetArgs {
    readonly assignIpv6AddressOnCreation?: fabric.MaybeComputed<boolean>;
    readonly availabilityZone?: fabric.MaybeComputed<string>;
    readonly cidrBlock: fabric.MaybeComputed<string>;
    readonly ipv6CidrBlock?: fabric.MaybeComputed<string>;
    readonly mapPublicIpOnLaunch?: fabric.MaybeComputed<boolean>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.MaybeComputed<string>;
}
