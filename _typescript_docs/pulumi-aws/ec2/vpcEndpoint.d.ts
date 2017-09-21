---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/vpcEndpoint.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class VpcEndpoint extends fabric.Resource {
    readonly cidrBlocks: fabric.Computed<string[]>;
    readonly policy: fabric.Computed<string>;
    readonly prefixListId: fabric.Computed<string>;
    readonly routeTableIds: fabric.Computed<string[]>;
    readonly serviceName: fabric.Computed<string>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: VpcEndpointArgs);
}
export interface VpcEndpointArgs {
    readonly policy?: fabric.MaybeComputed<string>;
    readonly routeTableIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly serviceName: fabric.MaybeComputed<string>;
    readonly vpcId: fabric.MaybeComputed<string>;
}
