---
layout: typescript-reference
repo: pulumi-aws
subpath: devicefarm/project.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Project extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: ProjectArgs);
}
export interface ProjectArgs {
    readonly name?: fabric.MaybeComputed<string>;
}
