---
layout: typescript-reference
repo: pulumi-aws
subpath: waf/rule.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Rule extends fabric.Resource {
    readonly metricName: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly predicates?: fabric.Computed<{
        dataId?: string;
        negated: boolean;
        type: string;
    }[]>;
    constructor(urnName: string, args: RuleArgs);
}
export interface RuleArgs {
    readonly metricName: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly predicates?: fabric.MaybeComputed<{
        dataId?: fabric.MaybeComputed<string>;
        negated: fabric.MaybeComputed<boolean>;
        type: fabric.MaybeComputed<string>;
    }>[];
}
