---
layout: typescript-reference
repo: pulumi-aws
subpath: kms/alias.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Alias extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly targetKeyId: fabric.Computed<string>;
    constructor(urnName: string, args: AliasArgs);
}
export interface AliasArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly targetKeyId: fabric.MaybeComputed<string>;
}
