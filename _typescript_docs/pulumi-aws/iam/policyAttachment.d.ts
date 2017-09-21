---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/policyAttachment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { ARN } from "../index";
import { Group } from "./group";
import { Role } from "./role";
import { User } from "./user";
export declare class PolicyAttachment extends fabric.Resource {
    readonly groups?: fabric.Computed<Group[]>;
    readonly name: fabric.Computed<string>;
    readonly policyArn: fabric.Computed<ARN>;
    readonly roles?: fabric.Computed<Role[]>;
    readonly users?: fabric.Computed<User[]>;
    constructor(urnName: string, args: PolicyAttachmentArgs);
}
export interface PolicyAttachmentArgs {
    readonly groups?: fabric.MaybeComputed<fabric.MaybeComputed<Group>>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly policyArn: fabric.MaybeComputed<ARN>;
    readonly roles?: fabric.MaybeComputed<fabric.MaybeComputed<Role>>[];
    readonly users?: fabric.MaybeComputed<fabric.MaybeComputed<User>>[];
}
