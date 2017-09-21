---
layout: typescript-reference
repo: pulumi-aws
subpath: cloudwatch/logGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class LogGroup extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly retentionInDays?: fabric.Computed<number>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: LogGroupArgs);
}
export interface LogGroupArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly retentionInDays?: fabric.MaybeComputed<number>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
