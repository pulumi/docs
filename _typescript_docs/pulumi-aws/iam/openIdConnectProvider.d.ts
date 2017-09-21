---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/openIdConnectProvider.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class OpenIdConnectProvider extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly clientIdList: fabric.Computed<string[]>;
    readonly thumbprintList: fabric.Computed<string[]>;
    readonly url: fabric.Computed<string>;
    constructor(urnName: string, args: OpenIdConnectProviderArgs);
}
export interface OpenIdConnectProviderArgs {
    readonly clientIdList: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly thumbprintList: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly url: fabric.MaybeComputed<string>;
}
