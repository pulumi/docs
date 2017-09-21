---
layout: typescript-reference
repo: pulumi-aws
subpath: route53/record.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Record extends fabric.Resource {
    readonly alias?: fabric.Computed<{
        evaluateTargetHealth: boolean;
        name: string;
        zoneId: string;
    }[]>;
    readonly failoverRoutingPolicy?: fabric.Computed<{
        type: string;
    }[]>;
    readonly fqdn: fabric.Computed<string>;
    readonly geolocationRoutingPolicy?: fabric.Computed<{
        continent?: string;
        country?: string;
        subdivision?: string;
    }[]>;
    readonly healthCheckId?: fabric.Computed<string>;
    readonly latencyRoutingPolicy?: fabric.Computed<{
        region: string;
    }[]>;
    readonly name: fabric.Computed<string>;
    readonly records?: fabric.Computed<string[]>;
    readonly setIdentifier?: fabric.Computed<string>;
    readonly ttl?: fabric.Computed<number>;
    readonly type: fabric.Computed<string>;
    readonly weightedRoutingPolicy?: fabric.Computed<{
        weight: number;
    }[]>;
    readonly zoneId: fabric.Computed<string>;
    constructor(urnName: string, args: RecordArgs);
}
export interface RecordArgs {
    readonly alias?: fabric.MaybeComputed<{
        evaluateTargetHealth: fabric.MaybeComputed<boolean>;
        name: fabric.MaybeComputed<string>;
        zoneId: fabric.MaybeComputed<string>;
    }>[];
    readonly failoverRoutingPolicy?: fabric.MaybeComputed<{
        type: fabric.MaybeComputed<string>;
    }>[];
    readonly geolocationRoutingPolicy?: fabric.MaybeComputed<{
        continent?: fabric.MaybeComputed<string>;
        country?: fabric.MaybeComputed<string>;
        subdivision?: fabric.MaybeComputed<string>;
    }>[];
    readonly healthCheckId?: fabric.MaybeComputed<string>;
    readonly latencyRoutingPolicy?: fabric.MaybeComputed<{
        region: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly records?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly setIdentifier?: fabric.MaybeComputed<string>;
    readonly ttl?: fabric.MaybeComputed<number>;
    readonly type: fabric.MaybeComputed<string>;
    readonly weightedRoutingPolicy?: fabric.MaybeComputed<{
        weight: fabric.MaybeComputed<number>;
    }>[];
    readonly zoneId: fabric.MaybeComputed<string>;
}
