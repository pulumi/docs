---
layout: typescript-reference
repo: pulumi-aws
subpath: sns/topicPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class TopicPolicy extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly policy: fabric.Computed<string>;
    constructor(urnName: string, args: TopicPolicyArgs);
}
export interface TopicPolicyArgs {
    readonly arn: fabric.MaybeComputed<string>;
    readonly policy: fabric.MaybeComputed<string>;
}
