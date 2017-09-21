---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/vpcDhcpOptions.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class VpcDhcpOptions extends fabric.Resource {
    readonly domainName?: fabric.Computed<string>;
    readonly domainNameServers?: fabric.Computed<string[]>;
    readonly netbiosNameServers?: fabric.Computed<string[]>;
    readonly netbiosNodeType?: fabric.Computed<string>;
    readonly ntpServers?: fabric.Computed<string[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: VpcDhcpOptionsArgs);
}
export interface VpcDhcpOptionsArgs {
    readonly domainName?: fabric.MaybeComputed<string>;
    readonly domainNameServers?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly netbiosNameServers?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly netbiosNodeType?: fabric.MaybeComputed<string>;
    readonly ntpServers?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
