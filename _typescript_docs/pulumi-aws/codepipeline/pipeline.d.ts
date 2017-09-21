---
layout: typescript-reference
repo: pulumi-aws
subpath: codepipeline/pipeline.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Pipeline extends fabric.Resource {
    readonly artifactStore: fabric.Computed<{
        encryptionKey?: {
            id: string;
            type: string;
        }[];
        location: string;
        type: string;
    }[]>;
    readonly name: fabric.Computed<string>;
    readonly roleArn: fabric.Computed<string>;
    readonly stage: fabric.Computed<{
        action: {
            category: string;
            configuration?: {
                [key: string]: any;
            };
            inputArtifacts?: string[];
            name: string;
            outputArtifacts?: string[];
            owner: string;
            provider: string;
            roleArn?: string;
            runOrder: number;
            version: string;
        }[];
        name: string;
    }[]>;
    constructor(urnName: string, args: PipelineArgs);
}
export interface PipelineArgs {
    readonly artifactStore: fabric.MaybeComputed<{
        encryptionKey?: fabric.MaybeComputed<{
            id: fabric.MaybeComputed<string>;
            type: fabric.MaybeComputed<string>;
        }>[];
        location: fabric.MaybeComputed<string>;
        type: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly roleArn: fabric.MaybeComputed<string>;
    readonly stage: fabric.MaybeComputed<{
        action: fabric.MaybeComputed<{
            category: fabric.MaybeComputed<string>;
            configuration?: fabric.MaybeComputed<{
                [key: string]: any;
            }>;
            inputArtifacts?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
            name: fabric.MaybeComputed<string>;
            outputArtifacts?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
            owner: fabric.MaybeComputed<string>;
            provider: fabric.MaybeComputed<string>;
            roleArn?: fabric.MaybeComputed<string>;
            runOrder?: fabric.MaybeComputed<number>;
            version: fabric.MaybeComputed<string>;
        }>[];
        name: fabric.MaybeComputed<string>;
    }>[];
}
