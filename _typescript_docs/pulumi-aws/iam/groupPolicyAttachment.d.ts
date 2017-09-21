---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/groupPolicyAttachment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { ARN } from "../index";
import { Group } from "./group";
export declare class GroupPolicyAttachment extends fabric.Resource {
    readonly group: fabric.Computed<Group>;
    readonly policyArn: fabric.Computed<ARN>;
    constructor(urnName: string, args: GroupPolicyAttachmentArgs);
}
export interface GroupPolicyAttachmentArgs {
    readonly group: fabric.MaybeComputed<Group>;
    readonly policyArn: fabric.MaybeComputed<ARN>;
}
