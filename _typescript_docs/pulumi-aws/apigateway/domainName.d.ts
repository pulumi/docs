---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/domainName.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class DomainName extends fabric.Resource {
    readonly certificateArn?: fabric.Computed<string>;
    readonly certificateBody?: fabric.Computed<string>;
    readonly certificateChain?: fabric.Computed<string>;
    readonly certificateName?: fabric.Computed<string>;
    readonly certificatePrivateKey?: fabric.Computed<string>;
    readonly certificateUploadDate: fabric.Computed<string>;
    readonly cloudfrontDomainName: fabric.Computed<string>;
    readonly cloudfrontZoneId: fabric.Computed<string>;
    readonly domainName: fabric.Computed<string>;
    constructor(urnName: string, args: DomainNameArgs);
}
export interface DomainNameArgs {
    readonly certificateArn?: fabric.MaybeComputed<string>;
    readonly certificateBody?: fabric.MaybeComputed<string>;
    readonly certificateChain?: fabric.MaybeComputed<string>;
    readonly certificateName?: fabric.MaybeComputed<string>;
    readonly certificatePrivateKey?: fabric.MaybeComputed<string>;
    readonly domainName: fabric.MaybeComputed<string>;
}
