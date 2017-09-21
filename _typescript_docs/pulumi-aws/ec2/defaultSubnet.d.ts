---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/defaultSubnet.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class DefaultSubnet extends fabric.Resource {
    readonly assignIpv6AddressOnCreation: fabric.Computed<boolean>;
    readonly availabilityZone: fabric.Computed<string>;
    readonly cidrBlock: fabric.Computed<string>;
    readonly ipv6CidrBlock: fabric.Computed<string>;
    readonly ipv6CidrBlockAssociationId: fabric.Computed<string>;
    readonly mapPublicIpOnLaunch: fabric.Computed<boolean>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: DefaultSubnetArgs);
}
export interface DefaultSubnetArgs {
    readonly availabilityZone: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
