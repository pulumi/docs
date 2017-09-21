---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/proxyProtocolPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ProxyProtocolPolicy extends fabric.Resource {
    readonly instancePorts: fabric.Computed<string[]>;
    readonly loadBalancer: fabric.Computed<string>;
    constructor(urnName: string, args: ProxyProtocolPolicyArgs);
}
export interface ProxyProtocolPolicyArgs {
    readonly instancePorts: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly loadBalancer: fabric.MaybeComputed<string>;
}
