---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/networkAclRule.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class NetworkAclRule extends fabric.Resource {
    readonly cidrBlock?: fabric.Computed<string>;
    readonly egress?: fabric.Computed<boolean>;
    readonly fromPort?: fabric.Computed<number>;
    readonly icmpCode?: fabric.Computed<string>;
    readonly icmpType?: fabric.Computed<string>;
    readonly ipv6CidrBlock?: fabric.Computed<string>;
    readonly networkAclId: fabric.Computed<string>;
    readonly protocol: fabric.Computed<string>;
    readonly ruleAction: fabric.Computed<string>;
    readonly ruleNumber: fabric.Computed<number>;
    readonly toPort?: fabric.Computed<number>;
    constructor(urnName: string, args: NetworkAclRuleArgs);
}
export interface NetworkAclRuleArgs {
    readonly cidrBlock?: fabric.MaybeComputed<string>;
    readonly egress?: fabric.MaybeComputed<boolean>;
    readonly fromPort?: fabric.MaybeComputed<number>;
    readonly icmpCode?: fabric.MaybeComputed<string>;
    readonly icmpType?: fabric.MaybeComputed<string>;
    readonly ipv6CidrBlock?: fabric.MaybeComputed<string>;
    readonly networkAclId: fabric.MaybeComputed<string>;
    readonly protocol: fabric.MaybeComputed<string>;
    readonly ruleAction: fabric.MaybeComputed<string>;
    readonly ruleNumber: fabric.MaybeComputed<number>;
    readonly toPort?: fabric.MaybeComputed<number>;
}
