---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/accessKey.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class AccessKey extends fabric.Resource {
    readonly encryptedSecret: fabric.Computed<string>;
    readonly keyFingerprint: fabric.Computed<string>;
    readonly pgpKey?: fabric.Computed<string>;
    readonly secret: fabric.Computed<string>;
    readonly sesSmtpPassword: fabric.Computed<string>;
    readonly status: fabric.Computed<string>;
    readonly user: fabric.Computed<string>;
    constructor(urnName: string, args: AccessKeyArgs);
}
export interface AccessKeyArgs {
    readonly pgpKey?: fabric.MaybeComputed<string>;
    readonly user: fabric.MaybeComputed<string>;
}
