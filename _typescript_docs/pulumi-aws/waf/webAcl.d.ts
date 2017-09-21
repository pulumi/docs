---
layout: typescript-reference
repo: pulumi-aws
subpath: waf/webAcl.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class WebAcl extends fabric.Resource {
    readonly defaultAction: fabric.Computed<{
        type: string;
    }[]>;
    readonly metricName: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly rules?: fabric.Computed<{
        action: {
            type: string;
        }[];
        priority: number;
        ruleId: string;
    }[]>;
    constructor(urnName: string, args: WebAclArgs);
}
export interface WebAclArgs {
    readonly defaultAction: fabric.MaybeComputed<{
        type: fabric.MaybeComputed<string>;
    }>[];
    readonly metricName: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly rules?: fabric.MaybeComputed<{
        action: fabric.MaybeComputed<{
            type: fabric.MaybeComputed<string>;
        }>[];
        priority: fabric.MaybeComputed<number>;
        ruleId: fabric.MaybeComputed<string>;
    }>[];
}
