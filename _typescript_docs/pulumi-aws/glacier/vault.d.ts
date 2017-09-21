---
layout: typescript-reference
repo: pulumi-aws
subpath: glacier/vault.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Vault extends fabric.Resource {
    readonly accessPolicy?: fabric.Computed<string>;
    readonly arn: fabric.Computed<string>;
    readonly location: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly notification?: fabric.Computed<{
        events: string[];
        snsTopic: string;
    }[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: VaultArgs);
}
export interface VaultArgs {
    readonly accessPolicy?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly notification?: fabric.MaybeComputed<{
        events: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        snsTopic: fabric.MaybeComputed<string>;
    }>[];
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
