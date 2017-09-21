---
layout: typescript-reference
repo: pulumi-aws
subpath: kms/key.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Key extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly deletionWindowInDays?: fabric.Computed<number>;
    readonly description: fabric.Computed<string>;
    readonly enableKeyRotation?: fabric.Computed<boolean>;
    readonly isEnabled?: fabric.Computed<boolean>;
    readonly keyId: fabric.Computed<string>;
    readonly keyUsage: fabric.Computed<string>;
    readonly policy: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: KeyArgs);
}
export interface KeyArgs {
    readonly deletionWindowInDays?: fabric.MaybeComputed<number>;
    readonly description?: fabric.MaybeComputed<string>;
    readonly enableKeyRotation?: fabric.MaybeComputed<boolean>;
    readonly isEnabled?: fabric.MaybeComputed<boolean>;
    readonly keyUsage?: fabric.MaybeComputed<string>;
    readonly policy?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
