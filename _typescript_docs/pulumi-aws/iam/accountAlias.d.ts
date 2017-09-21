---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/accountAlias.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class AccountAlias extends fabric.Resource {
    readonly accountAlias: fabric.Computed<string>;
    constructor(urnName: string, args: AccountAliasArgs);
}
export interface AccountAliasArgs {
    readonly accountAlias: fabric.MaybeComputed<string>;
}
