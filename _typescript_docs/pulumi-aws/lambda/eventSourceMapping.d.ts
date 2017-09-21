---
layout: typescript-reference
repo: pulumi-aws
subpath: lambda/eventSourceMapping.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class EventSourceMapping extends fabric.Resource {
    readonly batchSize?: fabric.Computed<number>;
    readonly enabled?: fabric.Computed<boolean>;
    readonly eventSourceArn: fabric.Computed<string>;
    readonly functionArn: fabric.Computed<string>;
    readonly functionName: fabric.Computed<string>;
    readonly lastModified: fabric.Computed<string>;
    readonly lastProcessingResult: fabric.Computed<string>;
    readonly startingPosition: fabric.Computed<string>;
    readonly state: fabric.Computed<string>;
    readonly stateTransitionReason: fabric.Computed<string>;
    readonly uuid: fabric.Computed<string>;
    constructor(urnName: string, args: EventSourceMappingArgs);
}
export interface EventSourceMappingArgs {
    readonly batchSize?: fabric.MaybeComputed<number>;
    readonly enabled?: fabric.MaybeComputed<boolean>;
    readonly eventSourceArn: fabric.MaybeComputed<string>;
    readonly functionName: fabric.MaybeComputed<string>;
    readonly startingPosition: fabric.MaybeComputed<string>;
}
