---
layout: typescript-reference
repo: pulumi-aws
subpath: ses/domainIdentity.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class DomainIdentity extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly domain: fabric.Computed<string>;
    readonly verificationToken: fabric.Computed<string>;
    constructor(urnName: string, args: DomainIdentityArgs);
}
export interface DomainIdentityArgs {
    readonly domain: fabric.MaybeComputed<string>;
}
