---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticloadbalancingv2/loadBalancer.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class LoadBalancer extends fabric.Resource {
    readonly accessLogs?: fabric.Computed<{
        bucket: string;
        enabled?: boolean;
        prefix?: string;
    }[]>;
    readonly arn: fabric.Computed<string>;
    readonly arnSuffix: fabric.Computed<string>;
    readonly dnsName: fabric.Computed<string>;
    readonly enableDeletionProtection?: fabric.Computed<boolean>;
    readonly idleTimeout?: fabric.Computed<number>;
    readonly internal: fabric.Computed<boolean>;
    readonly ipAddressType: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly securityGroups: fabric.Computed<string[]>;
    readonly subnets: fabric.Computed<string[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.Computed<string>;
    readonly zoneId: fabric.Computed<string>;
    constructor(urnName: string, args: LoadBalancerArgs);
}
export interface LoadBalancerArgs {
    readonly accessLogs?: fabric.MaybeComputed<{
        bucket: fabric.MaybeComputed<string>;
        enabled?: fabric.MaybeComputed<boolean>;
        prefix?: fabric.MaybeComputed<string>;
    }>[];
    readonly enableDeletionProtection?: fabric.MaybeComputed<boolean>;
    readonly idleTimeout?: fabric.MaybeComputed<number>;
    readonly internal?: fabric.MaybeComputed<boolean>;
    readonly ipAddressType?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly securityGroups?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly subnets: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
