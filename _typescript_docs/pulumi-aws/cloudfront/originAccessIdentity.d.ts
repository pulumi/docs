---
layout: typescript-reference
repo: pulumi-aws
subpath: cloudfront/originAccessIdentity.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class OriginAccessIdentity extends fabric.Resource {
    readonly callerReference: fabric.Computed<string>;
    readonly cloudfrontAccessIdentityPath: fabric.Computed<string>;
    readonly comment?: fabric.Computed<string>;
    readonly etag: fabric.Computed<string>;
    readonly iamArn: fabric.Computed<string>;
    readonly s3CanonicalUserId: fabric.Computed<string>;
    constructor(urnName: string, args: OriginAccessIdentityArgs);
}
export interface OriginAccessIdentityArgs {
    readonly comment?: fabric.MaybeComputed<string>;
}
