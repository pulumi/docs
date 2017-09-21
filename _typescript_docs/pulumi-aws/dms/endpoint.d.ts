---
layout: typescript-reference
repo: pulumi-aws
subpath: dms/endpoint.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Endpoint extends fabric.Resource {
    readonly certificateArn: fabric.Computed<string>;
    readonly databaseName?: fabric.Computed<string>;
    readonly endpointArn: fabric.Computed<string>;
    readonly endpointId: fabric.Computed<string>;
    readonly endpointType: fabric.Computed<string>;
    readonly engineName: fabric.Computed<string>;
    readonly extraConnectionAttributes: fabric.Computed<string>;
    readonly kmsKeyArn: fabric.Computed<string>;
    readonly password?: fabric.Computed<string>;
    readonly port?: fabric.Computed<number>;
    readonly serverName?: fabric.Computed<string>;
    readonly serviceAccessRole?: fabric.Computed<string>;
    readonly sslMode: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly username?: fabric.Computed<string>;
    constructor(urnName: string, args: EndpointArgs);
}
export interface EndpointArgs {
    readonly certificateArn?: fabric.MaybeComputed<string>;
    readonly databaseName?: fabric.MaybeComputed<string>;
    readonly endpointId: fabric.MaybeComputed<string>;
    readonly endpointType: fabric.MaybeComputed<string>;
    readonly engineName: fabric.MaybeComputed<string>;
    readonly extraConnectionAttributes?: fabric.MaybeComputed<string>;
    readonly kmsKeyArn?: fabric.MaybeComputed<string>;
    readonly password?: fabric.MaybeComputed<string>;
    readonly port?: fabric.MaybeComputed<number>;
    readonly serverName?: fabric.MaybeComputed<string>;
    readonly serviceAccessRole?: fabric.MaybeComputed<string>;
    readonly sslMode?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly username?: fabric.MaybeComputed<string>;
}
