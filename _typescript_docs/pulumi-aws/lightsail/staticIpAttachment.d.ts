---
layout: typescript-reference
repo: pulumi-aws
subpath: lightsail/staticIpAttachment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class StaticIpAttachment extends fabric.Resource {
    readonly instanceName: fabric.Computed<string>;
    readonly staticIpName: fabric.Computed<string>;
    constructor(urnName: string, args: StaticIpAttachmentArgs);
}
export interface StaticIpAttachmentArgs {
    readonly instanceName: fabric.MaybeComputed<string>;
    readonly staticIpName: fabric.MaybeComputed<string>;
}
