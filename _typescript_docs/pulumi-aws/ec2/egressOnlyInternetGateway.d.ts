---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/egressOnlyInternetGateway.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class EgressOnlyInternetGateway extends fabric.Resource {
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: EgressOnlyInternetGatewayArgs);
}
export interface EgressOnlyInternetGatewayArgs {
    readonly vpcId: fabric.MaybeComputed<string>;
}
