---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticloadbalancing/loadBalancerPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class LoadBalancerPolicy extends fabric.Resource {
    readonly loadBalancerName: fabric.Computed<string>;
    readonly policyAttribute?: fabric.Computed<{
        name?: string;
        value?: string;
    }[]>;
    readonly policyName: fabric.Computed<string>;
    readonly policyTypeName: fabric.Computed<string>;
    constructor(urnName: string, args: LoadBalancerPolicyArgs);
}
export interface LoadBalancerPolicyArgs {
    readonly loadBalancerName: fabric.MaybeComputed<string>;
    readonly policyAttribute?: fabric.MaybeComputed<{
        name?: fabric.MaybeComputed<string>;
        value?: fabric.MaybeComputed<string>;
    }>[];
    readonly policyName: fabric.MaybeComputed<string>;
    readonly policyTypeName: fabric.MaybeComputed<string>;
}
