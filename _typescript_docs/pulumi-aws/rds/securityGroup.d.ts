---
layout: typescript-reference
repo: pulumi-aws
subpath: rds/securityGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SecurityGroup extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly ingress: fabric.Computed<{
        cidr?: string;
        securityGroupId: string;
        securityGroupName: string;
        securityGroupOwnerId: string;
    }[]>;
    readonly name: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: SecurityGroupArgs);
}
export interface SecurityGroupArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly ingress: fabric.MaybeComputed<{
        cidr?: fabric.MaybeComputed<string>;
        securityGroupId?: fabric.MaybeComputed<string>;
        securityGroupName?: fabric.MaybeComputed<string>;
        securityGroupOwnerId?: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
