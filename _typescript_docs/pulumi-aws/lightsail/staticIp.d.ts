---
layout: typescript-reference
repo: pulumi-aws
subpath: lightsail/staticIp.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class StaticIp extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly ipAddress: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly supportCode: fabric.Computed<string>;
    constructor(urnName: string, args: StaticIpArgs);
}
export interface StaticIpArgs {
    readonly name?: fabric.MaybeComputed<string>;
}
