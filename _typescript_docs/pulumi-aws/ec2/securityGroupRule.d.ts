---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/securityGroupRule.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SecurityGroupRule extends fabric.Resource {
    readonly cidrBlocks?: fabric.Computed<string[]>;
    readonly fromPort: fabric.Computed<number>;
    readonly ipv6CidrBlocks?: fabric.Computed<string[]>;
    readonly prefixListIds?: fabric.Computed<string[]>;
    readonly protocol: fabric.Computed<string>;
    readonly securityGroupId: fabric.Computed<string>;
    readonly self?: fabric.Computed<boolean>;
    readonly sourceSecurityGroupId: fabric.Computed<string>;
    readonly toPort: fabric.Computed<number>;
    readonly type: fabric.Computed<string>;
    constructor(urnName: string, args: SecurityGroupRuleArgs);
}
export interface SecurityGroupRuleArgs {
    readonly cidrBlocks?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly fromPort: fabric.MaybeComputed<number>;
    readonly ipv6CidrBlocks?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly prefixListIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly protocol: fabric.MaybeComputed<string>;
    readonly securityGroupId: fabric.MaybeComputed<string>;
    readonly self?: fabric.MaybeComputed<boolean>;
    readonly sourceSecurityGroupId?: fabric.MaybeComputed<string>;
    readonly toPort: fabric.MaybeComputed<number>;
    readonly type: fabric.MaybeComputed<string>;
}
