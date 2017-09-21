---
layout: typescript-reference
repo: pulumi-aws
subpath: iam/serverCertificate.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ServerCertificate extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly certificateBody: fabric.Computed<string>;
    readonly certificateChain?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly path?: fabric.Computed<string>;
    readonly privateKey: fabric.Computed<string>;
    constructor(urnName: string, args: ServerCertificateArgs);
}
export interface ServerCertificateArgs {
    readonly arn?: fabric.MaybeComputed<string>;
    readonly certificateBody: fabric.MaybeComputed<string>;
    readonly certificateChain?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly path?: fabric.MaybeComputed<string>;
    readonly privateKey: fabric.MaybeComputed<string>;
}
