---
layout: typescript-reference
repo: pulumi-aws
subpath: elastictranscoder/preset.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Preset extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly audio?: fabric.Computed<{
        audioPackingMode?: string;
        bitRate?: string;
        channels?: string;
        codec?: string;
        sampleRate?: string;
    }[]>;
    readonly audioCodecOptions?: fabric.Computed<{
        bitDepth?: string;
        bitOrder?: string;
        profile?: string;
        signed?: string;
    }[]>;
    readonly container: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly thumbnails?: fabric.Computed<{
        aspectRatio?: string;
        format?: string;
        interval?: string;
        maxHeight?: string;
        maxWidth?: string;
        paddingPolicy?: string;
        resolution?: string;
        sizingPolicy?: string;
    }[]>;
    readonly type: fabric.Computed<string>;
    readonly video?: fabric.Computed<{
        aspectRatio?: string;
        bitRate?: string;
        codec?: string;
        displayAspectRatio?: string;
        fixedGop?: string;
        frameRate?: string;
        keyframesMaxDist?: string;
        maxFrameRate?: string;
        maxHeight?: string;
        maxWidth?: string;
        paddingPolicy?: string;
        resolution?: string;
        sizingPolicy?: string;
    }[]>;
    readonly videoCodecOptions?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly videoWatermarks?: fabric.Computed<{
        horizontalAlign?: string;
        horizontalOffset?: string;
        id?: string;
        maxHeight?: string;
        maxWidth?: string;
        opacity?: string;
        sizingPolicy?: string;
        target?: string;
        verticalAlign?: string;
        verticalOffset?: string;
    }[]>;
    constructor(urnName: string, args: PresetArgs);
}
export interface PresetArgs {
    readonly audio?: fabric.MaybeComputed<{
        audioPackingMode?: fabric.MaybeComputed<string>;
        bitRate?: fabric.MaybeComputed<string>;
        channels?: fabric.MaybeComputed<string>;
        codec?: fabric.MaybeComputed<string>;
        sampleRate?: fabric.MaybeComputed<string>;
    }>[];
    readonly audioCodecOptions?: fabric.MaybeComputed<{
        bitDepth?: fabric.MaybeComputed<string>;
        bitOrder?: fabric.MaybeComputed<string>;
        profile?: fabric.MaybeComputed<string>;
        signed?: fabric.MaybeComputed<string>;
    }>[];
    readonly container: fabric.MaybeComputed<string>;
    readonly description?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly thumbnails?: fabric.MaybeComputed<{
        aspectRatio?: fabric.MaybeComputed<string>;
        format?: fabric.MaybeComputed<string>;
        interval?: fabric.MaybeComputed<string>;
        maxHeight?: fabric.MaybeComputed<string>;
        maxWidth?: fabric.MaybeComputed<string>;
        paddingPolicy?: fabric.MaybeComputed<string>;
        resolution?: fabric.MaybeComputed<string>;
        sizingPolicy?: fabric.MaybeComputed<string>;
    }>[];
    readonly type?: fabric.MaybeComputed<string>;
    readonly video?: fabric.MaybeComputed<{
        aspectRatio?: fabric.MaybeComputed<string>;
        bitRate?: fabric.MaybeComputed<string>;
        codec?: fabric.MaybeComputed<string>;
        displayAspectRatio?: fabric.MaybeComputed<string>;
        fixedGop?: fabric.MaybeComputed<string>;
        frameRate?: fabric.MaybeComputed<string>;
        keyframesMaxDist?: fabric.MaybeComputed<string>;
        maxFrameRate?: fabric.MaybeComputed<string>;
        maxHeight?: fabric.MaybeComputed<string>;
        maxWidth?: fabric.MaybeComputed<string>;
        paddingPolicy?: fabric.MaybeComputed<string>;
        resolution?: fabric.MaybeComputed<string>;
        sizingPolicy?: fabric.MaybeComputed<string>;
    }>[];
    readonly videoCodecOptions?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly videoWatermarks?: fabric.MaybeComputed<{
        horizontalAlign?: fabric.MaybeComputed<string>;
        horizontalOffset?: fabric.MaybeComputed<string>;
        id?: fabric.MaybeComputed<string>;
        maxHeight?: fabric.MaybeComputed<string>;
        maxWidth?: fabric.MaybeComputed<string>;
        opacity?: fabric.MaybeComputed<string>;
        sizingPolicy?: fabric.MaybeComputed<string>;
        target?: fabric.MaybeComputed<string>;
        verticalAlign?: fabric.MaybeComputed<string>;
        verticalOffset?: fabric.MaybeComputed<string>;
    }>[];
}
