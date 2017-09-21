---
layout: typescript-reference
repo: pulumi-aws
subpath: redshift/securityGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SecurityGroup extends fabric.Resource {
    readonly description?: fabric.Computed<string>;
    readonly ingress: fabric.Computed<{
        cidr?: string;
        securityGroupName: string;
        securityGroupOwnerId: string;
    }[]>;
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: SecurityGroupArgs);
}
export interface SecurityGroupArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly ingress: fabric.MaybeComputed<{
        cidr?: fabric.MaybeComputed<string>;
        securityGroupName?: fabric.MaybeComputed<string>;
        securityGroupOwnerId?: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
}
