---
layout: typescript-reference
repo: pulumi-aws
subpath: lightsail/keyPair.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class KeyPair extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly encryptedFingerprint: fabric.Computed<string>;
    readonly encryptedPrivateKey: fabric.Computed<string>;
    readonly fingerprint: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly pgpKey?: fabric.Computed<string>;
    readonly privateKey: fabric.Computed<string>;
    readonly publicKey: fabric.Computed<string>;
    constructor(urnName: string, args: KeyPairArgs);
}
export interface KeyPairArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly pgpKey?: fabric.MaybeComputed<string>;
    readonly publicKey?: fabric.MaybeComputed<string>;
}
