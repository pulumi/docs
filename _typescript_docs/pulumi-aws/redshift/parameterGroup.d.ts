---
layout: typescript-reference
repo: pulumi-aws
subpath: redshift/parameterGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ParameterGroup extends fabric.Resource {
    readonly description?: fabric.Computed<string>;
    readonly family: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly parameter?: fabric.Computed<{
        name: string;
        value: string;
    }[]>;
    constructor(urnName: string, args: ParameterGroupArgs);
}
export interface ParameterGroupArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly family: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly parameter?: fabric.MaybeComputed<{
        name: fabric.MaybeComputed<string>;
        value: fabric.MaybeComputed<string>;
    }>[];
}
