---
layout: typescript-reference
repo: pulumi-aws
subpath: rds/clusterParameterGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ClusterParameterGroup extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly family: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix: fabric.Computed<string>;
    readonly parameter?: fabric.Computed<{
        applyMethod?: string;
        name: string;
        value: string;
    }[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: ClusterParameterGroupArgs);
}
export interface ClusterParameterGroupArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly family: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly parameter?: fabric.MaybeComputed<{
        applyMethod?: fabric.MaybeComputed<string>;
        name: fabric.MaybeComputed<string>;
        value: fabric.MaybeComputed<string>;
    }>[];
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
