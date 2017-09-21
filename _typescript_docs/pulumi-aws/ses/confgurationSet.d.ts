---
layout: typescript-reference
repo: pulumi-aws
subpath: ses/confgurationSet.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ConfgurationSet extends fabric.Resource {
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: ConfgurationSetArgs);
}
export interface ConfgurationSetArgs {
    readonly name?: fabric.MaybeComputed<string>;
}
