---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/userPolicyAttachment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { ARN } from "../index";
import { User } from "./user";
export declare class UserPolicyAttachment extends fabric.Resource {
    readonly policyArn: fabric.Computed<ARN>;
    readonly user: fabric.Computed<User>;
    constructor(urnName: string, args: UserPolicyAttachmentArgs);
}
export interface UserPolicyAttachmentArgs {
    readonly policyArn: fabric.MaybeComputed<ARN>;
    readonly user: fabric.MaybeComputed<User>;
}
