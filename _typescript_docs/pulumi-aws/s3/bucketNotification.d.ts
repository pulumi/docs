---
layout: typescript-reference
repo: pulumi-aws
subpath: s3/bucketNotification.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class BucketNotification extends fabric.Resource {
    readonly bucket: fabric.Computed<string>;
    readonly lambdaFunction?: fabric.Computed<{
        events: string[];
        filterPrefix?: string;
        filterSuffix?: string;
        id: string;
        lambdaFunctionArn?: string;
    }[]>;
    readonly queue?: fabric.Computed<{
        events: string[];
        filterPrefix?: string;
        filterSuffix?: string;
        id: string;
        queueArn: string;
    }[]>;
    readonly topic?: fabric.Computed<{
        events: string[];
        filterPrefix?: string;
        filterSuffix?: string;
        id: string;
        topicArn: string;
    }[]>;
    constructor(urnName: string, args: BucketNotificationArgs);
}
export interface BucketNotificationArgs {
    readonly bucket: fabric.MaybeComputed<string>;
    readonly lambdaFunction?: fabric.MaybeComputed<{
        events: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        filterPrefix?: fabric.MaybeComputed<string>;
        filterSuffix?: fabric.MaybeComputed<string>;
        id?: fabric.MaybeComputed<string>;
        lambdaFunctionArn?: fabric.MaybeComputed<string>;
    }>[];
    readonly queue?: fabric.MaybeComputed<{
        events: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        filterPrefix?: fabric.MaybeComputed<string>;
        filterSuffix?: fabric.MaybeComputed<string>;
        id?: fabric.MaybeComputed<string>;
        queueArn: fabric.MaybeComputed<string>;
    }>[];
    readonly topic?: fabric.MaybeComputed<{
        events: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        filterPrefix?: fabric.MaybeComputed<string>;
        filterSuffix?: fabric.MaybeComputed<string>;
        id?: fabric.MaybeComputed<string>;
        topicArn: fabric.MaybeComputed<string>;
    }>[];
}
