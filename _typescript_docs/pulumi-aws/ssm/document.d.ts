---
layout: typescript-reference
repo: pulumi-aws
subpath: ssm/document.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Document extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly content: fabric.Computed<string>;
    readonly createdDate: fabric.Computed<string>;
    readonly defaultVersion: fabric.Computed<string>;
    readonly description: fabric.Computed<string>;
    readonly documentType: fabric.Computed<string>;
    readonly hash: fabric.Computed<string>;
    readonly hashType: fabric.Computed<string>;
    readonly latestVersion: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly owner: fabric.Computed<string>;
    readonly parameter: fabric.Computed<{
        defaultValue?: string;
        description?: string;
        name?: string;
        type?: string;
    }[]>;
    readonly permissions?: fabric.Computed<{
        [key: string]: {
            accountIds: string;
            type: string;
        };
    }>;
    readonly platformTypes: fabric.Computed<string[]>;
    readonly schemaVersion: fabric.Computed<string>;
    readonly status: fabric.Computed<string>;
    constructor(urnName: string, args: DocumentArgs);
}
export interface DocumentArgs {
    readonly content: fabric.MaybeComputed<string>;
    readonly documentType: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly permissions?: fabric.MaybeComputed<{
        [key: string]: {
            accountIds: fabric.MaybeComputed<string>;
            type: fabric.MaybeComputed<string>;
        };
    }>;
}
