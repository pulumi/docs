---
layout: typescript-reference
repo: pulumi-aws
subpath: opsworks/userProfile.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class UserProfile extends fabric.Resource {
    readonly allowSelfManagement?: fabric.Computed<boolean>;
    readonly profileId: fabric.Computed<string>;
    readonly sshPublicKey?: fabric.Computed<string>;
    readonly sshUsername: fabric.Computed<string>;
    readonly userArn: fabric.Computed<string>;
    constructor(urnName: string, args: UserProfileArgs);
}
export interface UserProfileArgs {
    readonly allowSelfManagement?: fabric.MaybeComputed<boolean>;
    readonly sshPublicKey?: fabric.MaybeComputed<string>;
    readonly sshUsername: fabric.MaybeComputed<string>;
    readonly userArn: fabric.MaybeComputed<string>;
}
