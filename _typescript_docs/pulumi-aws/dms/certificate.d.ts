---
layout: typescript-reference
repo: pulumi-aws
subpath: dms/certificate.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Certificate extends fabric.Resource {
    readonly certificateArn: fabric.Computed<string>;
    readonly certificateId: fabric.Computed<string>;
    readonly certificatePem?: fabric.Computed<string>;
    readonly certificateWallet?: fabric.Computed<string>;
    constructor(urnName: string, args: CertificateArgs);
}
export interface CertificateArgs {
    readonly certificateId: fabric.MaybeComputed<string>;
    readonly certificatePem?: fabric.MaybeComputed<string>;
    readonly certificateWallet?: fabric.MaybeComputed<string>;
}
