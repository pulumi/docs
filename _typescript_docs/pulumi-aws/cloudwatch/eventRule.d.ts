---
layout: typescript-reference
repo: pulumi-aws
subpath: cloudwatch/eventRule.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class EventRule extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly eventPattern?: fabric.Computed<string>;
    readonly isEnabled?: fabric.Computed<boolean>;
    readonly name: fabric.Computed<string>;
    readonly roleArn?: fabric.Computed<string>;
    readonly scheduleExpression?: fabric.Computed<string>;
    constructor(urnName: string, args: EventRuleArgs);
}
export interface EventRuleArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly eventPattern?: fabric.MaybeComputed<string>;
    readonly isEnabled?: fabric.MaybeComputed<boolean>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly roleArn?: fabric.MaybeComputed<string>;
    readonly scheduleExpression?: fabric.MaybeComputed<string>;
}
