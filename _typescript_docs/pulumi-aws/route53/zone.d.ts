---
layout: typescript-reference
repo: pulumi-aws
subpath: route53/zone.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Zone extends fabric.Resource {
    readonly comment?: fabric.Computed<string>;
    readonly delegationSetId?: fabric.Computed<string>;
    readonly forceDestroy?: fabric.Computed<boolean>;
    readonly name: fabric.Computed<string>;
    readonly nameServers: fabric.Computed<string[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcId?: fabric.Computed<string>;
    readonly vpcRegion: fabric.Computed<string>;
    readonly zoneId: fabric.Computed<string>;
    constructor(urnName: string, args: ZoneArgs);
}
export interface ZoneArgs {
    readonly comment?: fabric.MaybeComputed<string>;
    readonly delegationSetId?: fabric.MaybeComputed<string>;
    readonly forceDestroy?: fabric.MaybeComputed<boolean>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly vpcId?: fabric.MaybeComputed<string>;
    readonly vpcRegion?: fabric.MaybeComputed<string>;
}
