---
layout: typescript-reference
repo: pulumi-aws
subpath: codecommit/repository.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Repository extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly cloneUrlHttp: fabric.Computed<string>;
    readonly cloneUrlSsh: fabric.Computed<string>;
    readonly defaultBranch?: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly repositoryId: fabric.Computed<string>;
    readonly repositoryName: fabric.Computed<string>;
    constructor(urnName: string, args: RepositoryArgs);
}
export interface RepositoryArgs {
    readonly defaultBranch?: fabric.MaybeComputed<string>;
    readonly description?: fabric.MaybeComputed<string>;
    readonly repositoryName: fabric.MaybeComputed<string>;
}
