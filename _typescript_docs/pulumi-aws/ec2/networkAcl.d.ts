---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/networkAcl.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class NetworkAcl extends fabric.Resource {
    readonly egress: fabric.Computed<{
        action: string;
        cidrBlock?: string;
        fromPort: number;
        icmpCode?: number;
        icmpType?: number;
        ipv6CidrBlock?: string;
        protocol: string;
        ruleNo: number;
        toPort: number;
    }[]>;
    readonly ingress: fabric.Computed<{
        action: string;
        cidrBlock?: string;
        fromPort: number;
        icmpCode?: number;
        icmpType?: number;
        ipv6CidrBlock?: string;
        protocol: string;
        ruleNo: number;
        toPort: number;
    }[]>;
    readonly subnetId?: fabric.Computed<string>;
    readonly subnetIds: fabric.Computed<string[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: NetworkAclArgs);
}
export interface NetworkAclArgs {
    readonly egress?: fabric.MaybeComputed<{
        action: fabric.MaybeComputed<string>;
        cidrBlock?: fabric.MaybeComputed<string>;
        fromPort: fabric.MaybeComputed<number>;
        icmpCode?: fabric.MaybeComputed<number>;
        icmpType?: fabric.MaybeComputed<number>;
        ipv6CidrBlock?: fabric.MaybeComputed<string>;
        protocol: fabric.MaybeComputed<string>;
        ruleNo: fabric.MaybeComputed<number>;
        toPort: fabric.MaybeComputed<number>;
    }>[];
    readonly ingress?: fabric.MaybeComputed<{
        action: fabric.MaybeComputed<string>;
        cidrBlock?: fabric.MaybeComputed<string>;
        fromPort: fabric.MaybeComputed<number>;
        icmpCode?: fabric.MaybeComputed<number>;
        icmpType?: fabric.MaybeComputed<number>;
        ipv6CidrBlock?: fabric.MaybeComputed<string>;
        protocol: fabric.MaybeComputed<string>;
        ruleNo: fabric.MaybeComputed<number>;
        toPort: fabric.MaybeComputed<number>;
    }>[];
    readonly subnetId?: fabric.MaybeComputed<string>;
    readonly subnetIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.MaybeComputed<string>;
}
