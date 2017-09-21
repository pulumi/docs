---
layout: typescript-reference
repo: pulumi-aws
subpath: simpledb/domain.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Domain extends fabric.Resource {
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: DomainArgs);
}
export interface DomainArgs {
    readonly name?: fabric.MaybeComputed<string>;
}
