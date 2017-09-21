---
layout: typescript-reference
repo: pulumi-aws
subpath: codebuild/project.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Project extends fabric.Resource {
    readonly artifacts: fabric.Computed<{
        location?: string;
        name?: string;
        namespaceType?: string;
        packaging?: string;
        path?: string;
        type: string;
    }[]>;
    readonly buildTimeout?: fabric.Computed<number>;
    readonly description: fabric.Computed<string>;
    readonly encryptionKey: fabric.Computed<string>;
    readonly environment: fabric.Computed<{
        computeType: string;
        environmentVariable: {
            name: string;
            value: string;
        }[];
        image: string;
        privilegedMode?: boolean;
        type: string;
    }[]>;
    readonly name: fabric.Computed<string>;
    readonly serviceRole: fabric.Computed<string>;
    readonly source: fabric.Computed<{
        auth?: {
            resource?: string;
            type: string;
        }[];
        buildspec?: string;
        location?: string;
        type: string;
    }[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: ProjectArgs);
}
export interface ProjectArgs {
    readonly artifacts: fabric.MaybeComputed<{
        location?: fabric.MaybeComputed<string>;
        name?: fabric.MaybeComputed<string>;
        namespaceType?: fabric.MaybeComputed<string>;
        packaging?: fabric.MaybeComputed<string>;
        path?: fabric.MaybeComputed<string>;
        type: fabric.MaybeComputed<string>;
    }>[];
    readonly buildTimeout?: fabric.MaybeComputed<number>;
    readonly description?: fabric.MaybeComputed<string>;
    readonly encryptionKey?: fabric.MaybeComputed<string>;
    readonly environment: fabric.MaybeComputed<{
        computeType: fabric.MaybeComputed<string>;
        environmentVariable?: fabric.MaybeComputed<{
            name: fabric.MaybeComputed<string>;
            value: fabric.MaybeComputed<string>;
        }>[];
        image: fabric.MaybeComputed<string>;
        privilegedMode?: fabric.MaybeComputed<boolean>;
        type: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly serviceRole?: fabric.MaybeComputed<string>;
    readonly source: fabric.MaybeComputed<{
        auth?: fabric.MaybeComputed<{
            resource?: fabric.MaybeComputed<string>;
            type: fabric.MaybeComputed<string>;
        }>[];
        buildspec?: fabric.MaybeComputed<string>;
        location?: fabric.MaybeComputed<string>;
        type: fabric.MaybeComputed<string>;
    }>[];
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
