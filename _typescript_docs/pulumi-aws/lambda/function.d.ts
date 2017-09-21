---
layout: typescript-reference
repo: pulumi-aws
subpath: lambda/function.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { ARN } from "../index";
export declare class Function extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly deadLetterConfig?: fabric.Computed<{
        targetArn: string;
    }[]>;
    readonly description?: fabric.Computed<string>;
    readonly environment?: fabric.Computed<{
        variables?: {
            [key: string]: string;
        };
    }[]>;
    readonly code?: fabric.Computed<fabric.asset.Archive>;
    readonly name: fabric.Computed<string>;
    readonly handler: fabric.Computed<string>;
    readonly invokeArn: fabric.Computed<string>;
    readonly kmsKeyArn?: fabric.Computed<string>;
    readonly lastModified: fabric.Computed<string>;
    readonly memorySize?: fabric.Computed<number>;
    readonly publish?: fabric.Computed<boolean>;
    readonly qualifiedArn: fabric.Computed<string>;
    readonly role: fabric.Computed<ARN>;
    readonly runtime: fabric.Computed<string>;
    readonly s3Bucket?: fabric.Computed<string>;
    readonly s3Key?: fabric.Computed<string>;
    readonly s3ObjectVersion?: fabric.Computed<string>;
    readonly sourceCodeHash: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly timeout?: fabric.Computed<number>;
    readonly tracingConfig: fabric.Computed<{
        mode: string;
    }[]>;
    readonly version: fabric.Computed<string>;
    readonly vpcConfig?: fabric.Computed<{
        securityGroupIds: string[];
        subnetIds: string[];
        vpcId: string;
    }[]>;
    constructor(urnName: string, args: FunctionArgs);
}
export interface FunctionArgs {
    readonly deadLetterConfig?: fabric.MaybeComputed<{
        targetArn: fabric.MaybeComputed<string>;
    }>[];
    readonly description?: fabric.MaybeComputed<string>;
    readonly environment?: fabric.MaybeComputed<{
        variables?: fabric.MaybeComputed<{
            [key: string]: fabric.MaybeComputed<string>;
        }>;
    }>[];
    readonly code?: fabric.asset.Archive;
    readonly name?: fabric.MaybeComputed<string>;
    readonly handler: fabric.MaybeComputed<string>;
    readonly kmsKeyArn?: fabric.MaybeComputed<string>;
    readonly memorySize?: fabric.MaybeComputed<number>;
    readonly publish?: fabric.MaybeComputed<boolean>;
    readonly role: fabric.MaybeComputed<ARN>;
    readonly runtime: fabric.MaybeComputed<string>;
    readonly s3Bucket?: fabric.MaybeComputed<string>;
    readonly s3Key?: fabric.MaybeComputed<string>;
    readonly s3ObjectVersion?: fabric.MaybeComputed<string>;
    readonly sourceCodeHash?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly timeout?: fabric.MaybeComputed<number>;
    readonly tracingConfig?: fabric.MaybeComputed<{
        mode: fabric.MaybeComputed<string>;
    }>[];
    readonly vpcConfig?: fabric.MaybeComputed<{
        securityGroupIds: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        subnetIds: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        vpcId?: fabric.MaybeComputed<string>;
    }>[];
}
