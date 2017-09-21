---
layout: typescript-reference
repo: pulumi-aws
subpath: ssm/patchGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class PatchGroup extends fabric.Resource {
    readonly baselineId: fabric.Computed<string>;
    readonly patchGroup: fabric.Computed<string>;
    constructor(urnName: string, args: PatchGroupArgs);
}
export interface PatchGroupArgs {
    readonly baselineId: fabric.MaybeComputed<string>;
    readonly patchGroup: fabric.MaybeComputed<string>;
}
