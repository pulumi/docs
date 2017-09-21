---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/keyPair.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class KeyPair extends fabric.Resource {
    readonly fingerprint: fabric.Computed<string>;
    readonly keyName: fabric.Computed<string>;
    readonly keyNamePrefix?: fabric.Computed<string>;
    readonly publicKey: fabric.Computed<string>;
    constructor(urnName: string, args: KeyPairArgs);
}
export interface KeyPairArgs {
    readonly keyName?: fabric.MaybeComputed<string>;
    readonly keyNamePrefix?: fabric.MaybeComputed<string>;
    readonly publicKey: fabric.MaybeComputed<string>;
}
