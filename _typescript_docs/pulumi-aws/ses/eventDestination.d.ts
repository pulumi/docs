---
layout: typescript-reference
repo: pulumi-aws
subpath: ses/eventDestination.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class EventDestination extends fabric.Resource {
    readonly cloudwatchDestination?: fabric.Computed<{
        defaultValue: string;
        dimensionName: string;
        valueSource: string;
    }[]>;
    readonly configurationSetName: fabric.Computed<string>;
    readonly enabled?: fabric.Computed<boolean>;
    readonly kinesisDestination?: fabric.Computed<{
        roleArn: string;
        streamArn: string;
    }[]>;
    readonly matchingTypes: fabric.Computed<string[]>;
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: EventDestinationArgs);
}
export interface EventDestinationArgs {
    readonly cloudwatchDestination?: fabric.MaybeComputed<{
        defaultValue: fabric.MaybeComputed<string>;
        dimensionName: fabric.MaybeComputed<string>;
        valueSource: fabric.MaybeComputed<string>;
    }>[];
    readonly configurationSetName: fabric.MaybeComputed<string>;
    readonly enabled?: fabric.MaybeComputed<boolean>;
    readonly kinesisDestination?: fabric.MaybeComputed<{
        roleArn: fabric.MaybeComputed<string>;
        streamArn: fabric.MaybeComputed<string>;
    }>[];
    readonly matchingTypes: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly name?: fabric.MaybeComputed<string>;
}
