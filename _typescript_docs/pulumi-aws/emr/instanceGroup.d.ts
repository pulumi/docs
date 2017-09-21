---
layout: typescript-reference
repo: pulumi-aws
subpath: emr/instanceGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class InstanceGroup extends fabric.Resource {
    readonly clusterId: fabric.Computed<string>;
    readonly ebsConfig?: fabric.Computed<{
        iops?: number;
        size: number;
        type: string;
        volumesPerInstance?: number;
    }[]>;
    readonly ebsOptimized?: fabric.Computed<boolean>;
    readonly instanceCount?: fabric.Computed<number>;
    readonly instanceType: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly runningInstanceCount: fabric.Computed<number>;
    readonly status: fabric.Computed<string>;
    constructor(urnName: string, args: InstanceGroupArgs);
}
export interface InstanceGroupArgs {
    readonly clusterId: fabric.MaybeComputed<string>;
    readonly ebsConfig?: fabric.MaybeComputed<{
        iops?: fabric.MaybeComputed<number>;
        size: fabric.MaybeComputed<number>;
        type: fabric.MaybeComputed<string>;
        volumesPerInstance?: fabric.MaybeComputed<number>;
    }>[];
    readonly ebsOptimized?: fabric.MaybeComputed<boolean>;
    readonly instanceCount?: fabric.MaybeComputed<number>;
    readonly instanceType: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
}
