---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/internetGateway.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class InternetGateway extends fabric.Resource {
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcId?: fabric.Computed<string>;
    constructor(urnName: string, args: InternetGatewayArgs);
}
export interface InternetGatewayArgs {
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly vpcId?: fabric.MaybeComputed<string>;
}
