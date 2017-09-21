---
layout: typescript-reference
repo: pulumi-aws
subpath: appautoscaling/target.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Target extends fabric.Resource {
    readonly maxCapacity: fabric.Computed<number>;
    readonly minCapacity: fabric.Computed<number>;
    readonly resourceId: fabric.Computed<string>;
    readonly roleArn: fabric.Computed<string>;
    readonly scalableDimension: fabric.Computed<string>;
    readonly serviceNamespace: fabric.Computed<string>;
    constructor(urnName: string, args: TargetArgs);
}
export interface TargetArgs {
    readonly maxCapacity: fabric.MaybeComputed<number>;
    readonly minCapacity: fabric.MaybeComputed<number>;
    readonly resourceId: fabric.MaybeComputed<string>;
    readonly roleArn: fabric.MaybeComputed<string>;
    readonly scalableDimension: fabric.MaybeComputed<string>;
    readonly serviceNamespace: fabric.MaybeComputed<string>;
}
