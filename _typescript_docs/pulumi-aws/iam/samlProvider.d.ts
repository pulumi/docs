---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/samlProvider.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SamlProvider extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly samlMetadataDocument: fabric.Computed<string>;
    readonly validUntil: fabric.Computed<string>;
    constructor(urnName: string, args: SamlProviderArgs);
}
export interface SamlProviderArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly samlMetadataDocument: fabric.MaybeComputed<string>;
}
