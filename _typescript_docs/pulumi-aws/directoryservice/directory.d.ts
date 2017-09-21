---
layout: typescript-reference
repo: pulumi-aws
subpath: directoryservice/directory.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Directory extends fabric.Resource {
    readonly accessUrl: fabric.Computed<string>;
    readonly alias: fabric.Computed<string>;
    readonly connectSettings?: fabric.Computed<{
        customerDnsIps: string[];
        customerUsername: string;
        subnetIds: string[];
        vpcId: string;
    }[]>;
    readonly description?: fabric.Computed<string>;
    readonly dnsIpAddresses: fabric.Computed<string[]>;
    readonly enableSso?: fabric.Computed<boolean>;
    readonly name: fabric.Computed<string>;
    readonly password: fabric.Computed<string>;
    readonly shortName: fabric.Computed<string>;
    readonly size?: fabric.Computed<string>;
    readonly type?: fabric.Computed<string>;
    readonly vpcSettings?: fabric.Computed<{
        subnetIds: string[];
        vpcId: string;
    }[]>;
    constructor(urnName: string, args: DirectoryArgs);
}
export interface DirectoryArgs {
    readonly alias?: fabric.MaybeComputed<string>;
    readonly connectSettings?: fabric.MaybeComputed<{
        customerDnsIps: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        customerUsername: fabric.MaybeComputed<string>;
        subnetIds: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        vpcId: fabric.MaybeComputed<string>;
    }>[];
    readonly description?: fabric.MaybeComputed<string>;
    readonly enableSso?: fabric.MaybeComputed<boolean>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly password: fabric.MaybeComputed<string>;
    readonly shortName?: fabric.MaybeComputed<string>;
    readonly size?: fabric.MaybeComputed<string>;
    readonly type?: fabric.MaybeComputed<string>;
    readonly vpcSettings?: fabric.MaybeComputed<{
        subnetIds: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        vpcId: fabric.MaybeComputed<string>;
    }>[];
}
