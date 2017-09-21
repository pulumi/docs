---
layout: typescript-reference
repo: pulumi-aws
subpath: cloudwatch/logStream.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class LogStream extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly logGroupName: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: LogStreamArgs);
}
export interface LogStreamArgs {
    readonly logGroupName: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
}
