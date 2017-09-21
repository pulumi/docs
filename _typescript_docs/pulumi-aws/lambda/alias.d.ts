---
layout: typescript-reference
repo: pulumi-aws
subpath: lambda/alias.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Alias extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly functionName: fabric.Computed<string>;
    readonly functionVersion: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: AliasArgs);
}
export interface AliasArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly functionName: fabric.MaybeComputed<string>;
    readonly functionVersion: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
}
