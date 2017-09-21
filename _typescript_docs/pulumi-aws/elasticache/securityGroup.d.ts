---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticache/securityGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SecurityGroup extends fabric.Resource {
    readonly description?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly securityGroupNames: fabric.Computed<string[]>;
    constructor(urnName: string, args: SecurityGroupArgs);
}
export interface SecurityGroupArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly securityGroupNames: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
}
