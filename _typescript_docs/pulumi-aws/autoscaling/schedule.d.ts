---
layout: typescript-reference
repo: pulumi-aws
subpath: autoscaling/schedule.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Schedule extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly autoscalingGroupName: fabric.Computed<string>;
    readonly desiredCapacity: fabric.Computed<number>;
    readonly endTime: fabric.Computed<string>;
    readonly maxSize: fabric.Computed<number>;
    readonly minSize: fabric.Computed<number>;
    readonly recurrence: fabric.Computed<string>;
    readonly scheduledActionName: fabric.Computed<string>;
    readonly startTime: fabric.Computed<string>;
    constructor(urnName: string, args: ScheduleArgs);
}
export interface ScheduleArgs {
    readonly autoscalingGroupName: fabric.MaybeComputed<string>;
    readonly desiredCapacity?: fabric.MaybeComputed<number>;
    readonly endTime?: fabric.MaybeComputed<string>;
    readonly maxSize?: fabric.MaybeComputed<number>;
    readonly minSize?: fabric.MaybeComputed<number>;
    readonly recurrence?: fabric.MaybeComputed<string>;
    readonly scheduledActionName: fabric.MaybeComputed<string>;
    readonly startTime?: fabric.MaybeComputed<string>;
}
