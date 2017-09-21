---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/sshKey.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SshKey extends fabric.Resource {
    readonly encoding: fabric.Computed<string>;
    readonly fingerprint: fabric.Computed<string>;
    readonly publicKey: fabric.Computed<string>;
    readonly sshPublicKeyId: fabric.Computed<string>;
    readonly status: fabric.Computed<string>;
    readonly username: fabric.Computed<string>;
    constructor(urnName: string, args: SshKeyArgs);
}
export interface SshKeyArgs {
    readonly encoding: fabric.MaybeComputed<string>;
    readonly publicKey: fabric.MaybeComputed<string>;
    readonly status?: fabric.MaybeComputed<string>;
    readonly username: fabric.MaybeComputed<string>;
}
