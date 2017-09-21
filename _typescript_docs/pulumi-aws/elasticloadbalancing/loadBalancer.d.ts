---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticloadbalancing/loadBalancer.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class LoadBalancer extends fabric.Resource {
    readonly accessLogs?: fabric.Computed<{
        bucket: string;
        bucketPrefix?: string;
        enabled?: boolean;
        interval?: number;
    }[]>;
    readonly availabilityZones: fabric.Computed<string[]>;
    readonly connectionDraining?: fabric.Computed<boolean>;
    readonly connectionDrainingTimeout?: fabric.Computed<number>;
    readonly crossZoneLoadBalancing?: fabric.Computed<boolean>;
    readonly dnsName: fabric.Computed<string>;
    readonly healthCheck: fabric.Computed<{
        healthyThreshold: number;
        interval: number;
        target: string;
        timeout: number;
        unhealthyThreshold: number;
    }[]>;
    readonly idleTimeout?: fabric.Computed<number>;
    readonly instances: fabric.Computed<string[]>;
    readonly internal: fabric.Computed<boolean>;
    readonly listener: fabric.Computed<{
        instancePort: number;
        instanceProtocol: string;
        lbPort: number;
        lbProtocol: string;
        sslCertificateId?: string;
    }[]>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly securityGroups: fabric.Computed<string[]>;
    readonly sourceSecurityGroup: fabric.Computed<string>;
    readonly sourceSecurityGroupId: fabric.Computed<string>;
    readonly subnets: fabric.Computed<string[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly zoneId: fabric.Computed<string>;
    constructor(urnName: string, args: LoadBalancerArgs);
}
export interface LoadBalancerArgs {
    readonly accessLogs?: fabric.MaybeComputed<{
        bucket: fabric.MaybeComputed<string>;
        bucketPrefix?: fabric.MaybeComputed<string>;
        enabled?: fabric.MaybeComputed<boolean>;
        interval?: fabric.MaybeComputed<number>;
    }>[];
    readonly availabilityZones?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly connectionDraining?: fabric.MaybeComputed<boolean>;
    readonly connectionDrainingTimeout?: fabric.MaybeComputed<number>;
    readonly crossZoneLoadBalancing?: fabric.MaybeComputed<boolean>;
    readonly healthCheck?: fabric.MaybeComputed<{
        healthyThreshold: fabric.MaybeComputed<number>;
        interval: fabric.MaybeComputed<number>;
        target: fabric.MaybeComputed<string>;
        timeout: fabric.MaybeComputed<number>;
        unhealthyThreshold: fabric.MaybeComputed<number>;
    }>[];
    readonly idleTimeout?: fabric.MaybeComputed<number>;
    readonly instances?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly internal?: fabric.MaybeComputed<boolean>;
    readonly listener: fabric.MaybeComputed<{
        instancePort: fabric.MaybeComputed<number>;
        instanceProtocol: fabric.MaybeComputed<string>;
        lbPort: fabric.MaybeComputed<number>;
        lbProtocol: fabric.MaybeComputed<string>;
        sslCertificateId?: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly securityGroups?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly sourceSecurityGroup?: fabric.MaybeComputed<string>;
    readonly subnets?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
