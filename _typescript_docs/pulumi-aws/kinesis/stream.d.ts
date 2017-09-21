---
layout: typescript-reference
repo: pulumi-aws
subpath: kinesis/stream.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Stream extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly retentionPeriod?: fabric.Computed<number>;
    readonly shardCount: fabric.Computed<number>;
    readonly shardLevelMetrics?: fabric.Computed<string[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: StreamArgs);
}
export interface StreamArgs {
    readonly arn?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly retentionPeriod?: fabric.MaybeComputed<number>;
    readonly shardCount: fabric.MaybeComputed<number>;
    readonly shardLevelMetrics?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
