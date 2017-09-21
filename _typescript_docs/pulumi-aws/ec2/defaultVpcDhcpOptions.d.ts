---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/defaultVpcDhcpOptions.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class DefaultVpcDhcpOptions extends fabric.Resource {
    readonly domainName: fabric.Computed<string>;
    readonly domainNameServers: fabric.Computed<string>;
    readonly netbiosNameServers?: fabric.Computed<string[]>;
    readonly netbiosNodeType?: fabric.Computed<string>;
    readonly ntpServers: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: DefaultVpcDhcpOptionsArgs);
}
export interface DefaultVpcDhcpOptionsArgs {
    readonly netbiosNameServers?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly netbiosNodeType?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
