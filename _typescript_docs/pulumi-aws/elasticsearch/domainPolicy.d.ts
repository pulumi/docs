---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticsearch/domainPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class DomainPolicy extends fabric.Resource {
    readonly accessPolicies: fabric.Computed<string>;
    readonly domainName: fabric.Computed<string>;
    constructor(urnName: string, args: DomainPolicyArgs);
}
export interface DomainPolicyArgs {
    readonly accessPolicies: fabric.MaybeComputed<string>;
    readonly domainName: fabric.MaybeComputed<string>;
}
