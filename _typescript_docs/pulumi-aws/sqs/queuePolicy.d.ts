---
layout: typescript-reference
repo: pulumi-aws
subpath: sqs/queuePolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class QueuePolicy extends fabric.Resource {
    readonly policy: fabric.Computed<string>;
    readonly queueUrl: fabric.Computed<string>;
    constructor(urnName: string, args: QueuePolicyArgs);
}
export interface QueuePolicyArgs {
    readonly policy: fabric.MaybeComputed<string>;
    readonly queueUrl: fabric.MaybeComputed<string>;
}
