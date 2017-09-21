---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/userLoginProfile.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class UserLoginProfile extends fabric.Resource {
    readonly encryptedPassword: fabric.Computed<string>;
    readonly keyFingerprint: fabric.Computed<string>;
    readonly passwordLength?: fabric.Computed<number>;
    readonly passwordResetRequired?: fabric.Computed<boolean>;
    readonly pgpKey: fabric.Computed<string>;
    readonly user: fabric.Computed<string>;
    constructor(urnName: string, args: UserLoginProfileArgs);
}
export interface UserLoginProfileArgs {
    readonly passwordLength?: fabric.MaybeComputed<number>;
    readonly passwordResetRequired?: fabric.MaybeComputed<boolean>;
    readonly pgpKey: fabric.MaybeComputed<string>;
    readonly user: fabric.MaybeComputed<string>;
}
