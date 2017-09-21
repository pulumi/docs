---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/accountPasswordPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class AccountPasswordPolicy extends fabric.Resource {
    readonly allowUsersToChangePassword?: fabric.Computed<boolean>;
    readonly expirePasswords: fabric.Computed<boolean>;
    readonly hardExpiry: fabric.Computed<boolean>;
    readonly maxPasswordAge: fabric.Computed<number>;
    readonly minimumPasswordLength?: fabric.Computed<number>;
    readonly passwordReusePrevention: fabric.Computed<number>;
    readonly requireLowercaseCharacters: fabric.Computed<boolean>;
    readonly requireNumbers: fabric.Computed<boolean>;
    readonly requireSymbols: fabric.Computed<boolean>;
    readonly requireUppercaseCharacters: fabric.Computed<boolean>;
    constructor(urnName: string, args: AccountPasswordPolicyArgs);
}
export interface AccountPasswordPolicyArgs {
    readonly allowUsersToChangePassword?: fabric.MaybeComputed<boolean>;
    readonly hardExpiry?: fabric.MaybeComputed<boolean>;
    readonly maxPasswordAge?: fabric.MaybeComputed<number>;
    readonly minimumPasswordLength?: fabric.MaybeComputed<number>;
    readonly passwordReusePrevention?: fabric.MaybeComputed<number>;
    readonly requireLowercaseCharacters?: fabric.MaybeComputed<boolean>;
    readonly requireNumbers?: fabric.MaybeComputed<boolean>;
    readonly requireSymbols?: fabric.MaybeComputed<boolean>;
    readonly requireUppercaseCharacters?: fabric.MaybeComputed<boolean>;
}
