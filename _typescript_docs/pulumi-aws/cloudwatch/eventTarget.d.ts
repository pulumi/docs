---
layout: typescript-reference
repo: pulumi-aws
subpath: cloudwatch/eventTarget.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class EventTarget extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly ecsTarget?: fabric.Computed<{
        taskCount?: number;
        taskDefinitionArn: string;
    }[]>;
    readonly input?: fabric.Computed<string>;
    readonly inputPath?: fabric.Computed<string>;
    readonly roleArn?: fabric.Computed<string>;
    readonly rule: fabric.Computed<string>;
    readonly runCommandTargets?: fabric.Computed<{
        key: string;
        values: string[];
    }[]>;
    readonly targetId: fabric.Computed<string>;
    constructor(urnName: string, args: EventTargetArgs);
}
export interface EventTargetArgs {
    readonly arn: fabric.MaybeComputed<string>;
    readonly ecsTarget?: fabric.MaybeComputed<{
        taskCount?: fabric.MaybeComputed<number>;
        taskDefinitionArn: fabric.MaybeComputed<string>;
    }>[];
    readonly input?: fabric.MaybeComputed<string>;
    readonly inputPath?: fabric.MaybeComputed<string>;
    readonly roleArn?: fabric.MaybeComputed<string>;
    readonly rule: fabric.MaybeComputed<string>;
    readonly runCommandTargets?: fabric.MaybeComputed<{
        key: fabric.MaybeComputed<string>;
        values: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    }>[];
    readonly targetId?: fabric.MaybeComputed<string>;
}
