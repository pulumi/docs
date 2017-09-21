---
layout: typescript-reference
repo: pulumi-aws
subpath: cloudwatch/logDestination.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class LogDestination extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly roleArn: fabric.Computed<string>;
    readonly targetArn: fabric.Computed<string>;
    constructor(urnName: string, args: LogDestinationArgs);
}
export interface LogDestinationArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly roleArn: fabric.MaybeComputed<string>;
    readonly targetArn: fabric.MaybeComputed<string>;
}
