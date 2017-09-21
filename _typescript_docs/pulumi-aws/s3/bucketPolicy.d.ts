---
layout: typescript-reference
repo: pulumi-aws
subpath: s3/bucketPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class BucketPolicy extends fabric.Resource {
    readonly bucket: fabric.Computed<string>;
    readonly policy: fabric.Computed<string>;
    constructor(urnName: string, args: BucketPolicyArgs);
}
export interface BucketPolicyArgs {
    readonly bucket: fabric.MaybeComputed<string>;
    readonly policy: fabric.MaybeComputed<string>;
}
