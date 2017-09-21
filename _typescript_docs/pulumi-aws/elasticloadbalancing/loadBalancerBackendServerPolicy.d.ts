---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticloadbalancing/loadBalancerBackendServerPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class LoadBalancerBackendServerPolicy extends fabric.Resource {
    readonly instancePort: fabric.Computed<number>;
    readonly loadBalancerName: fabric.Computed<string>;
    readonly policyNames?: fabric.Computed<string[]>;
    constructor(urnName: string, args: LoadBalancerBackendServerPolicyArgs);
}
export interface LoadBalancerBackendServerPolicyArgs {
    readonly instancePort: fabric.MaybeComputed<number>;
    readonly loadBalancerName: fabric.MaybeComputed<string>;
    readonly policyNames?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
}
