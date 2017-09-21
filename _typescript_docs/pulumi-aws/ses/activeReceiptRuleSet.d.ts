---
layout: typescript-reference
repo: pulumi-aws
subpath: ses/activeReceiptRuleSet.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ActiveReceiptRuleSet extends fabric.Resource {
    readonly ruleSetName: fabric.Computed<string>;
    constructor(urnName: string, args: ActiveReceiptRuleSetArgs);
}
export interface ActiveReceiptRuleSetArgs {
    readonly ruleSetName: fabric.MaybeComputed<string>;
}
