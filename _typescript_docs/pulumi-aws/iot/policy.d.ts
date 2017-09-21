---
layout: typescript-reference
repo: pulumi-aws
subpath: iot/policy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Policy extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly defaultVersionId: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly policy: fabric.Computed<string>;
    constructor(urnName: string, args: PolicyArgs);
}
export interface PolicyArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly policy: fabric.MaybeComputed<string>;
}
