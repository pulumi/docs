---
layout: typescript-reference
repo: pulumi-aws
subpath: cloudwatch/logDestinationPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class LogDestinationPolicy extends fabric.Resource {
    readonly accessPolicy: fabric.Computed<string>;
    readonly destinationName: fabric.Computed<string>;
    constructor(urnName: string, args: LogDestinationPolicyArgs);
}
export interface LogDestinationPolicyArgs {
    readonly accessPolicy: fabric.MaybeComputed<string>;
    readonly destinationName: fabric.MaybeComputed<string>;
}
