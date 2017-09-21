---
layout: typescript-reference
repo: pulumi-aws
subpath: sns/topic.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { ARN } from "../index";
export declare class Topic extends fabric.Resource {
    readonly arn: fabric.Computed<ARN>;
    readonly deliveryPolicy?: fabric.Computed<string>;
    readonly displayName?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly policy: fabric.Computed<string>;
    constructor(urnName: string, args: TopicArgs);
}
export interface TopicArgs {
    readonly deliveryPolicy?: fabric.MaybeComputed<string>;
    readonly displayName?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly policy?: fabric.MaybeComputed<string>;
}
