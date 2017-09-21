---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/policy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Policy extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly path?: fabric.Computed<string>;
    readonly policy: fabric.Computed<string>;
    constructor(urnName: string, args: PolicyArgs);
}
export interface PolicyArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly path?: fabric.MaybeComputed<string>;
    readonly policy: fabric.MaybeComputed<string>;
}
