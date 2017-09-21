---
layout: typescript-reference
repo: pulumi-aws
subpath: cloudwatch/logMetricFilter.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class LogMetricFilter extends fabric.Resource {
    readonly logGroupName: fabric.Computed<string>;
    readonly metricTransformation: fabric.Computed<{
        name: string;
        namespace: string;
        value: string;
    }[]>;
    readonly name: fabric.Computed<string>;
    readonly pattern: fabric.Computed<string>;
    constructor(urnName: string, args: LogMetricFilterArgs);
}
export interface LogMetricFilterArgs {
    readonly logGroupName: fabric.MaybeComputed<string>;
    readonly metricTransformation: fabric.MaybeComputed<{
        name: fabric.MaybeComputed<string>;
        namespace: fabric.MaybeComputed<string>;
        value: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly pattern: fabric.MaybeComputed<string>;
}
