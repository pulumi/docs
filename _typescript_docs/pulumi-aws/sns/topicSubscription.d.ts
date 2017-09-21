---
layout: typescript-reference
repo: pulumi-aws
subpath: sns/topicSubscription.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { Topic } from "./topic";
export declare class TopicSubscription extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly confirmationTimeoutInMinutes?: fabric.Computed<number>;
    readonly deliveryPolicy?: fabric.Computed<string>;
    readonly endpoint: fabric.Computed<string>;
    readonly endpointAutoConfirms?: fabric.Computed<boolean>;
    readonly protocol: fabric.Computed<string>;
    readonly rawMessageDelivery?: fabric.Computed<boolean>;
    readonly topic: fabric.Computed<Topic>;
    constructor(urnName: string, args: TopicSubscriptionArgs);
}
export interface TopicSubscriptionArgs {
    readonly confirmationTimeoutInMinutes?: fabric.MaybeComputed<number>;
    readonly deliveryPolicy?: fabric.MaybeComputed<string>;
    readonly endpoint: fabric.MaybeComputed<string>;
    readonly endpointAutoConfirms?: fabric.MaybeComputed<boolean>;
    readonly protocol: fabric.MaybeComputed<string>;
    readonly rawMessageDelivery?: fabric.MaybeComputed<boolean>;
    readonly topic: fabric.MaybeComputed<Topic>;
}
