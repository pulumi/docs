---
layout: typescript-reference
repo: pulumi-aws
subpath: ses/receiptRuleSet.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ReceiptRuleSet extends fabric.Resource {
    readonly ruleSetName: fabric.Computed<string>;
    constructor(urnName: string, args: ReceiptRuleSetArgs);
}
export interface ReceiptRuleSetArgs {
    readonly ruleSetName: fabric.MaybeComputed<string>;
}
