---
layout: typescript-reference
repo: pulumi-aws
subpath: cfg/recorderStatus.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class RecorderStatus extends fabric.Resource {
    readonly isEnabled: fabric.Computed<boolean>;
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: RecorderStatusArgs);
}
export interface RecorderStatusArgs {
    readonly isEnabled: fabric.MaybeComputed<boolean>;
    readonly name?: fabric.MaybeComputed<string>;
}
