---
layout: typescript-reference
repo: pulumi-aws
subpath: autoscaling/policy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Policy extends fabric.Resource {
    readonly adjustmentType: fabric.Computed<string>;
    readonly arn: fabric.Computed<string>;
    readonly autoscalingGroupName: fabric.Computed<string>;
    readonly cooldown?: fabric.Computed<number>;
    readonly estimatedInstanceWarmup?: fabric.Computed<number>;
    readonly metricAggregationType: fabric.Computed<string>;
    readonly minAdjustmentMagnitude?: fabric.Computed<number>;
    readonly minAdjustmentStep?: fabric.Computed<number>;
    readonly name: fabric.Computed<string>;
    readonly policyType?: fabric.Computed<string>;
    readonly scalingAdjustment?: fabric.Computed<number>;
    readonly stepAdjustment?: fabric.Computed<{
        metricIntervalLowerBound?: string;
        metricIntervalUpperBound?: string;
        scalingAdjustment: number;
    }[]>;
    constructor(urnName: string, args: PolicyArgs);
}
export interface PolicyArgs {
    readonly adjustmentType: fabric.MaybeComputed<string>;
    readonly autoscalingGroupName: fabric.MaybeComputed<string>;
    readonly cooldown?: fabric.MaybeComputed<number>;
    readonly estimatedInstanceWarmup?: fabric.MaybeComputed<number>;
    readonly metricAggregationType?: fabric.MaybeComputed<string>;
    readonly minAdjustmentMagnitude?: fabric.MaybeComputed<number>;
    readonly minAdjustmentStep?: fabric.MaybeComputed<number>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly policyType?: fabric.MaybeComputed<string>;
    readonly scalingAdjustment?: fabric.MaybeComputed<number>;
    readonly stepAdjustment?: fabric.MaybeComputed<{
        metricIntervalLowerBound?: fabric.MaybeComputed<string>;
        metricIntervalUpperBound?: fabric.MaybeComputed<string>;
        scalingAdjustment: fabric.MaybeComputed<number>;
    }>[];
}
