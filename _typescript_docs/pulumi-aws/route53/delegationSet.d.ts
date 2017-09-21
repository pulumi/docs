---
layout: typescript-reference
repo: pulumi-aws
subpath: route53/delegationSet.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class DelegationSet extends fabric.Resource {
    readonly nameServers: fabric.Computed<string[]>;
    readonly referenceName?: fabric.Computed<string>;
    constructor(urnName: string, args: DelegationSetArgs);
}
export interface DelegationSetArgs {
    readonly referenceName?: fabric.MaybeComputed<string>;
}
