---
layout: typescript-reference
repo: pulumi-aws
subpath: ses/receiptFilter.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ReceiptFilter extends fabric.Resource {
    readonly cidr: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly policy: fabric.Computed<string>;
    constructor(urnName: string, args: ReceiptFilterArgs);
}
export interface ReceiptFilterArgs {
    readonly cidr: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly policy: fabric.MaybeComputed<string>;
}
