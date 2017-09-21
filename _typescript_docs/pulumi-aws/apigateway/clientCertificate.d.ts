---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/clientCertificate.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ClientCertificate extends fabric.Resource {
    readonly createdDate: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly expirationDate: fabric.Computed<string>;
    readonly pemEncodedCertificate: fabric.Computed<string>;
    constructor(urnName: string, args: ClientCertificateArgs);
}
export interface ClientCertificateArgs {
    readonly description?: fabric.MaybeComputed<string>;
}
