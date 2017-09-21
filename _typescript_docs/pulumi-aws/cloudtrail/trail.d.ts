---
layout: typescript-reference
repo: pulumi-aws
subpath: cloudtrail/trail.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Trail extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly cloudWatchLogsGroupArn?: fabric.Computed<string>;
    readonly cloudWatchLogsRoleArn?: fabric.Computed<string>;
    readonly enableLogFileValidation?: fabric.Computed<boolean>;
    readonly enableLogging?: fabric.Computed<boolean>;
    readonly homeRegion: fabric.Computed<string>;
    readonly includeGlobalServiceEvents?: fabric.Computed<boolean>;
    readonly isMultiRegionTrail?: fabric.Computed<boolean>;
    readonly kmsKeyId?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly s3BucketName: fabric.Computed<string>;
    readonly s3KeyPrefix?: fabric.Computed<string>;
    readonly snsTopicName?: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: TrailArgs);
}
export interface TrailArgs {
    readonly cloudWatchLogsGroupArn?: fabric.MaybeComputed<string>;
    readonly cloudWatchLogsRoleArn?: fabric.MaybeComputed<string>;
    readonly enableLogFileValidation?: fabric.MaybeComputed<boolean>;
    readonly enableLogging?: fabric.MaybeComputed<boolean>;
    readonly includeGlobalServiceEvents?: fabric.MaybeComputed<boolean>;
    readonly isMultiRegionTrail?: fabric.MaybeComputed<boolean>;
    readonly kmsKeyId?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly s3BucketName: fabric.MaybeComputed<string>;
    readonly s3KeyPrefix?: fabric.MaybeComputed<string>;
    readonly snsTopicName?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
