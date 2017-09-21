---
layout: typescript-reference
repo: pulumi-aws
subpath: cfg/deliveryChannel.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class DeliveryChannel extends fabric.Resource {
    readonly name: fabric.Computed<string>;
    readonly s3BucketName: fabric.Computed<string>;
    readonly s3KeyPrefix?: fabric.Computed<string>;
    readonly snapshotDeliveryProperties?: fabric.Computed<{
        deliveryFrequency?: string;
    }[]>;
    readonly snsTopicArn?: fabric.Computed<string>;
    constructor(urnName: string, args: DeliveryChannelArgs);
}
export interface DeliveryChannelArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly s3BucketName: fabric.MaybeComputed<string>;
    readonly s3KeyPrefix?: fabric.MaybeComputed<string>;
    readonly snapshotDeliveryProperties?: fabric.MaybeComputed<{
        deliveryFrequency?: fabric.MaybeComputed<string>;
    }>[];
    readonly snsTopicArn?: fabric.MaybeComputed<string>;
}
