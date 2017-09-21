---
layout: typescript-reference
repo: pulumi-aws
subpath: cfg/recorder.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Recorder extends fabric.Resource {
    readonly name: fabric.Computed<string>;
    readonly recordingGroup: fabric.Computed<{
        allSupported?: boolean;
        includeGlobalResourceTypes?: boolean;
        resourceTypes?: string[];
    }[]>;
    readonly roleArn: fabric.Computed<string>;
    constructor(urnName: string, args: RecorderArgs);
}
export interface RecorderArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly recordingGroup?: fabric.MaybeComputed<{
        allSupported?: fabric.MaybeComputed<boolean>;
        includeGlobalResourceTypes?: fabric.MaybeComputed<boolean>;
        resourceTypes?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    }>[];
    readonly roleArn: fabric.MaybeComputed<string>;
}
