---
layout: typescript-reference
repo: pulumi-aws
subpath: ecr/repositoryPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class RepositoryPolicy extends fabric.Resource {
    readonly policy: fabric.Computed<string>;
    readonly registryId: fabric.Computed<string>;
    readonly repository: fabric.Computed<string>;
    constructor(urnName: string, args: RepositoryPolicyArgs);
}
export interface RepositoryPolicyArgs {
    readonly policy: fabric.MaybeComputed<string>;
    readonly repository: fabric.MaybeComputed<string>;
}
