---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticloadbalancing/listenerPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ListenerPolicy extends fabric.Resource {
    readonly loadBalancerName: fabric.Computed<string>;
    readonly loadBalancerPort: fabric.Computed<number>;
    readonly policyNames?: fabric.Computed<string[]>;
    constructor(urnName: string, args: ListenerPolicyArgs);
}
export interface ListenerPolicyArgs {
    readonly loadBalancerName: fabric.MaybeComputed<string>;
    readonly loadBalancerPort: fabric.MaybeComputed<number>;
    readonly policyNames?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
}
