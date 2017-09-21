---
layout: typescript-reference
repo: pulumi-aws
subpath: inspector/resourceGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ResourceGroup extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly tags: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: ResourceGroupArgs);
}
export interface ResourceGroupArgs {
    readonly tags: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
