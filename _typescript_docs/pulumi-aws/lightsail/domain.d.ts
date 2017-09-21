---
layout: typescript-reference
repo: pulumi-aws
subpath: lightsail/domain.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Domain extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly domainName: fabric.Computed<string>;
    constructor(urnName: string, args: DomainArgs);
}
export interface DomainArgs {
    readonly domainName: fabric.MaybeComputed<string>;
}
