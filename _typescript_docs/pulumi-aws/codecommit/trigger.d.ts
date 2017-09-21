---
layout: typescript-reference
repo: pulumi-aws
subpath: codecommit/trigger.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Trigger extends fabric.Resource {
    readonly configurationId: fabric.Computed<string>;
    readonly repositoryName: fabric.Computed<string>;
    readonly trigger: fabric.Computed<{
        branches?: string[];
        customData?: string;
        destinationArn: string;
        events: string[];
        name: string;
    }[]>;
    constructor(urnName: string, args: TriggerArgs);
}
export interface TriggerArgs {
    readonly repositoryName: fabric.MaybeComputed<string>;
    readonly trigger: fabric.MaybeComputed<{
        branches?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        customData?: fabric.MaybeComputed<string>;
        destinationArn: fabric.MaybeComputed<string>;
        events: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        name: fabric.MaybeComputed<string>;
    }>[];
}
