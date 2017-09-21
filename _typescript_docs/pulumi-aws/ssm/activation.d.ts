---
layout: typescript-reference
repo: pulumi-aws
subpath: ssm/activation.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Activation extends fabric.Resource {
    readonly description?: fabric.Computed<string>;
    readonly expirationDate?: fabric.Computed<string>;
    readonly expired: fabric.Computed<string>;
    readonly iamRole: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly registrationCount: fabric.Computed<number>;
    readonly registrationLimit?: fabric.Computed<number>;
    constructor(urnName: string, args: ActivationArgs);
}
export interface ActivationArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly expirationDate?: fabric.MaybeComputed<string>;
    readonly iamRole: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly registrationLimit?: fabric.MaybeComputed<number>;
}
