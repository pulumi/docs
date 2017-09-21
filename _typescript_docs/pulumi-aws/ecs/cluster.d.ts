---
layout: typescript-reference
repo: pulumi-aws
subpath: ecs/cluster.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Cluster extends fabric.Resource {
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: ClusterArgs);
}
export interface ClusterArgs {
    readonly name?: fabric.MaybeComputed<string>;
}
