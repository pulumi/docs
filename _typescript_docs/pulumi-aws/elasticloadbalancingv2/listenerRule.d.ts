---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticloadbalancingv2/listenerRule.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ListenerRule extends fabric.Resource {
    readonly action: fabric.Computed<{
        targetGroupArn: string;
        type: string;
    }[]>;
    readonly arn: fabric.Computed<string>;
    readonly condition: fabric.Computed<{
        field?: string;
        values?: string[];
    }[]>;
    readonly listenerArn: fabric.Computed<string>;
    readonly priority: fabric.Computed<number>;
    constructor(urnName: string, args: ListenerRuleArgs);
}
export interface ListenerRuleArgs {
    readonly action: fabric.MaybeComputed<{
        targetGroupArn: fabric.MaybeComputed<string>;
        type: fabric.MaybeComputed<string>;
    }>[];
    readonly condition: fabric.MaybeComputed<{
        field?: fabric.MaybeComputed<string>;
        values?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    }>[];
    readonly listenerArn: fabric.MaybeComputed<string>;
    readonly priority: fabric.MaybeComputed<number>;
}
