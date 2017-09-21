---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/rolePolicyAttachment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { ARN } from "../index";
import { Role } from "./role";
export declare class RolePolicyAttachment extends fabric.Resource {
    readonly policyArn: fabric.Computed<ARN>;
    readonly role: fabric.Computed<Role>;
    constructor(urnName: string, args: RolePolicyAttachmentArgs);
}
export interface RolePolicyAttachmentArgs {
    readonly policyArn: fabric.MaybeComputed<ARN>;
    readonly role: fabric.MaybeComputed<Role>;
}
