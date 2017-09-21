---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/securityGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SecurityGroup extends fabric.Resource {
    readonly description?: fabric.Computed<string>;
    readonly egress: fabric.Computed<{
        cidrBlocks?: string[];
        fromPort: number;
        ipv6CidrBlocks?: string[];
        prefixListIds?: string[];
        protocol: string;
        securityGroups?: string[];
        self?: boolean;
        toPort: number;
    }[]>;
    readonly ingress: fabric.Computed<{
        cidrBlocks?: string[];
        fromPort: number;
        ipv6CidrBlocks?: string[];
        protocol: string;
        securityGroups?: string[];
        self?: boolean;
        toPort: number;
    }[]>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly ownerId: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: SecurityGroupArgs);
}
export interface SecurityGroupArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly egress?: fabric.MaybeComputed<{
        cidrBlocks?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        fromPort: fabric.MaybeComputed<number>;
        ipv6CidrBlocks?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        prefixListIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        protocol: fabric.MaybeComputed<string>;
        securityGroups?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        self?: fabric.MaybeComputed<boolean>;
        toPort: fabric.MaybeComputed<number>;
    }>[];
    readonly ingress?: fabric.MaybeComputed<{
        cidrBlocks?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        fromPort: fabric.MaybeComputed<number>;
        ipv6CidrBlocks?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        protocol: fabric.MaybeComputed<string>;
        securityGroups?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        self?: fabric.MaybeComputed<boolean>;
        toPort: fabric.MaybeComputed<number>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly vpcId?: fabric.MaybeComputed<string>;
}
