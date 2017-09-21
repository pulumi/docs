---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/defaultVpc.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class DefaultVpc extends fabric.Resource {
    readonly assignGeneratedIpv6CidrBlock: fabric.Computed<boolean>;
    readonly cidrBlock: fabric.Computed<string>;
    readonly defaultNetworkAclId: fabric.Computed<string>;
    readonly defaultRouteTableId: fabric.Computed<string>;
    readonly defaultSecurityGroupId: fabric.Computed<string>;
    readonly dhcpOptionsId: fabric.Computed<string>;
    readonly enableClassiclink: fabric.Computed<boolean>;
    readonly enableClassiclinkDnsSupport: fabric.Computed<boolean>;
    readonly enableDnsHostnames: fabric.Computed<boolean>;
    readonly enableDnsSupport?: fabric.Computed<boolean>;
    readonly instanceTenancy: fabric.Computed<string>;
    readonly ipv6AssociationId: fabric.Computed<string>;
    readonly ipv6CidrBlock: fabric.Computed<string>;
    readonly mainRouteTableId: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: DefaultVpcArgs);
}
export interface DefaultVpcArgs {
    readonly enableClassiclink?: fabric.MaybeComputed<boolean>;
    readonly enableClassiclinkDnsSupport?: fabric.MaybeComputed<boolean>;
    readonly enableDnsHostnames?: fabric.MaybeComputed<boolean>;
    readonly enableDnsSupport?: fabric.MaybeComputed<boolean>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
