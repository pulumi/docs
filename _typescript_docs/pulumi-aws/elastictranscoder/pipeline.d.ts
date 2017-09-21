---
layout: typescript-reference
repo: pulumi-aws
subpath: elastictranscoder/pipeline.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Pipeline extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly awsKmsKeyArn?: fabric.Computed<string>;
    readonly contentConfig: fabric.Computed<{
        bucket: string;
        storageClass?: string;
    }[]>;
    readonly contentConfigPermissions?: fabric.Computed<{
        access?: string[];
        grantee?: string;
        granteeType?: string;
    }[]>;
    readonly inputBucket: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly notifications?: fabric.Computed<{
        completed?: string;
        error?: string;
        progressing?: string;
        warning?: string;
    }[]>;
    readonly outputBucket: fabric.Computed<string>;
    readonly role: fabric.Computed<string>;
    readonly thumbnailConfig: fabric.Computed<{
        bucket: string;
        storageClass?: string;
    }[]>;
    readonly thumbnailConfigPermissions?: fabric.Computed<{
        access?: string[];
        grantee?: string;
        granteeType?: string;
    }[]>;
    constructor(urnName: string, args: PipelineArgs);
}
export interface PipelineArgs {
    readonly awsKmsKeyArn?: fabric.MaybeComputed<string>;
    readonly contentConfig?: fabric.MaybeComputed<{
        bucket?: fabric.MaybeComputed<string>;
        storageClass?: fabric.MaybeComputed<string>;
    }>[];
    readonly contentConfigPermissions?: fabric.MaybeComputed<{
        access?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        grantee?: fabric.MaybeComputed<string>;
        granteeType?: fabric.MaybeComputed<string>;
    }>[];
    readonly inputBucket: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly notifications?: fabric.MaybeComputed<{
        completed?: fabric.MaybeComputed<string>;
        error?: fabric.MaybeComputed<string>;
        progressing?: fabric.MaybeComputed<string>;
        warning?: fabric.MaybeComputed<string>;
    }>[];
    readonly outputBucket?: fabric.MaybeComputed<string>;
    readonly role: fabric.MaybeComputed<string>;
    readonly thumbnailConfig?: fabric.MaybeComputed<{
        bucket?: fabric.MaybeComputed<string>;
        storageClass?: fabric.MaybeComputed<string>;
    }>[];
    readonly thumbnailConfigPermissions?: fabric.MaybeComputed<{
        access?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        grantee?: fabric.MaybeComputed<string>;
        granteeType?: fabric.MaybeComputed<string>;
    }>[];
}
