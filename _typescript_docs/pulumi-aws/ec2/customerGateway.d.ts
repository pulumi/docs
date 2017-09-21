---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/customerGateway.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class CustomerGateway extends fabric.Resource {
    readonly bgpAsn: fabric.Computed<number>;
    readonly ipAddress: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly type: fabric.Computed<string>;
    constructor(urnName: string, args: CustomerGatewayArgs);
}
export interface CustomerGatewayArgs {
    readonly bgpAsn: fabric.MaybeComputed<number>;
    readonly ipAddress: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly type: fabric.MaybeComputed<string>;
}
