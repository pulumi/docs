---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticloadbalancing/sslNegotiationPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SslNegotiationPolicy extends fabric.Resource {
    readonly attribute?: fabric.Computed<{
        name: string;
        value: string;
    }[]>;
    readonly lbPort: fabric.Computed<number>;
    readonly loadBalancer: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: SslNegotiationPolicyArgs);
}
export interface SslNegotiationPolicyArgs {
    readonly attribute?: fabric.MaybeComputed<{
        name: fabric.MaybeComputed<string>;
        value: fabric.MaybeComputed<string>;
    }>[];
    readonly lbPort: fabric.MaybeComputed<number>;
    readonly loadBalancer: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
}
