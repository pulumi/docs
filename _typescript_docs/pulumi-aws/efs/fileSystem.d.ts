---
layout: typescript-reference
repo: pulumi-aws
subpath: efs/fileSystem.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class FileSystem extends fabric.Resource {
    readonly creationToken: fabric.Computed<string>;
    readonly performanceMode: fabric.Computed<string>;
    readonly referenceName: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: FileSystemArgs);
}
export interface FileSystemArgs {
    readonly creationToken?: fabric.MaybeComputed<string>;
    readonly performanceMode?: fabric.MaybeComputed<string>;
    readonly referenceName?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
