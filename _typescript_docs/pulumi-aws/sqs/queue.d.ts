---
layout: typescript-reference
repo: pulumi-aws
subpath: sqs/queue.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Queue extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly contentBasedDeduplication?: fabric.Computed<boolean>;
    readonly delaySeconds?: fabric.Computed<number>;
    readonly fifoQueue?: fabric.Computed<boolean>;
    readonly kmsDataKeyReusePeriodSeconds: fabric.Computed<number>;
    readonly kmsMasterKeyId?: fabric.Computed<string>;
    readonly maxMessageSize?: fabric.Computed<number>;
    readonly messageRetentionSeconds?: fabric.Computed<number>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly policy: fabric.Computed<string>;
    readonly receiveWaitTimeSeconds?: fabric.Computed<number>;
    readonly redrivePolicy?: fabric.Computed<string>;
    readonly visibilityTimeoutSeconds?: fabric.Computed<number>;
    constructor(urnName: string, args: QueueArgs);
}
export interface QueueArgs {
    readonly contentBasedDeduplication?: fabric.MaybeComputed<boolean>;
    readonly delaySeconds?: fabric.MaybeComputed<number>;
    readonly fifoQueue?: fabric.MaybeComputed<boolean>;
    readonly kmsDataKeyReusePeriodSeconds?: fabric.MaybeComputed<number>;
    readonly kmsMasterKeyId?: fabric.MaybeComputed<string>;
    readonly maxMessageSize?: fabric.MaybeComputed<number>;
    readonly messageRetentionSeconds?: fabric.MaybeComputed<number>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly policy?: fabric.MaybeComputed<string>;
    readonly receiveWaitTimeSeconds?: fabric.MaybeComputed<number>;
    readonly redrivePolicy?: fabric.MaybeComputed<string>;
    readonly visibilityTimeoutSeconds?: fabric.MaybeComputed<number>;
}
