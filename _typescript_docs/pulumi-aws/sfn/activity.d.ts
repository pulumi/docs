---
layout: typescript-reference
repo: pulumi-aws
subpath: sfn/activity.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Activity extends fabric.Resource {
    readonly creationDate: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: ActivityArgs);
}
export interface ActivityArgs {
    readonly name?: fabric.MaybeComputed<string>;
}
