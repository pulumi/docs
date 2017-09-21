---
layout: typescript-reference
repo: pulumi-aws
subpath: ecr/repository.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Repository extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly registryId: fabric.Computed<string>;
    readonly repositoryUrl: fabric.Computed<string>;
    constructor(urnName: string, args: RepositoryArgs);
}
export interface RepositoryArgs {
    readonly name?: fabric.MaybeComputed<string>;
}
