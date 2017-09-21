---
layout: typescript-reference
repo: pulumi-aws
subpath: cloudwatch/metricAlarm.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { Topic } from "../sns/topic";
export declare class MetricAlarm extends fabric.Resource {
    readonly actionsEnabled?: fabric.Computed<boolean>;
    readonly alarmActions?: fabric.Computed<Topic[]>;
    readonly alarmDescription?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly comparisonOperator: fabric.Computed<string>;
    readonly dimensions?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly evaluateLowSampleCountPercentiles: fabric.Computed<string>;
    readonly evaluationPeriods: fabric.Computed<number>;
    readonly extendedStatistic?: fabric.Computed<string>;
    readonly insufficientDataActions?: fabric.Computed<Topic[]>;
    readonly metricName: fabric.Computed<string>;
    readonly namespace: fabric.Computed<string>;
    readonly okActions?: fabric.Computed<Topic[]>;
    readonly period: fabric.Computed<number>;
    readonly statistic?: fabric.Computed<string>;
    readonly threshold: fabric.Computed<number>;
    readonly treatMissingData?: fabric.Computed<string>;
    readonly unit?: fabric.Computed<string>;
    constructor(urnName: string, args: MetricAlarmArgs);
}
export interface MetricAlarmArgs {
    readonly actionsEnabled?: fabric.MaybeComputed<boolean>;
    readonly alarmActions?: fabric.MaybeComputed<fabric.MaybeComputed<Topic>>[];
    readonly alarmDescription?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly comparisonOperator: fabric.MaybeComputed<string>;
    readonly dimensions?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly evaluateLowSampleCountPercentiles?: fabric.MaybeComputed<string>;
    readonly evaluationPeriods: fabric.MaybeComputed<number>;
    readonly extendedStatistic?: fabric.MaybeComputed<string>;
    readonly insufficientDataActions?: fabric.MaybeComputed<fabric.MaybeComputed<Topic>>[];
    readonly metricName: fabric.MaybeComputed<string>;
    readonly namespace: fabric.MaybeComputed<string>;
    readonly okActions?: fabric.MaybeComputed<fabric.MaybeComputed<Topic>>[];
    readonly period: fabric.MaybeComputed<number>;
    readonly statistic?: fabric.MaybeComputed<string>;
    readonly threshold: fabric.MaybeComputed<number>;
    readonly treatMissingData?: fabric.MaybeComputed<string>;
    readonly unit?: fabric.MaybeComputed<string>;
}
