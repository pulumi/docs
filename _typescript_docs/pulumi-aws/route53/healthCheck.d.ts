---
layout: typescript-reference
repo: pulumi-aws
subpath: route53/healthCheck.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class HealthCheck extends fabric.Resource {
    readonly childHealthThreshold?: fabric.Computed<number>;
    readonly childHealthchecks?: fabric.Computed<string[]>;
    readonly cloudwatchAlarmName?: fabric.Computed<string>;
    readonly cloudwatchAlarmRegion?: fabric.Computed<string>;
    readonly enableSni: fabric.Computed<boolean>;
    readonly failureThreshold?: fabric.Computed<number>;
    readonly fqdn?: fabric.Computed<string>;
    readonly insufficientDataHealthStatus?: fabric.Computed<string>;
    readonly invertHealthcheck?: fabric.Computed<boolean>;
    readonly ipAddress?: fabric.Computed<string>;
    readonly measureLatency?: fabric.Computed<boolean>;
    readonly port?: fabric.Computed<number>;
    readonly referenceName?: fabric.Computed<string>;
    readonly regions?: fabric.Computed<string[]>;
    readonly requestInterval?: fabric.Computed<number>;
    readonly resourcePath?: fabric.Computed<string>;
    readonly searchString?: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly type: fabric.Computed<string>;
    constructor(urnName: string, args: HealthCheckArgs);
}
export interface HealthCheckArgs {
    readonly childHealthThreshold?: fabric.MaybeComputed<number>;
    readonly childHealthchecks?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly cloudwatchAlarmName?: fabric.MaybeComputed<string>;
    readonly cloudwatchAlarmRegion?: fabric.MaybeComputed<string>;
    readonly enableSni?: fabric.MaybeComputed<boolean>;
    readonly failureThreshold?: fabric.MaybeComputed<number>;
    readonly fqdn?: fabric.MaybeComputed<string>;
    readonly insufficientDataHealthStatus?: fabric.MaybeComputed<string>;
    readonly invertHealthcheck?: fabric.MaybeComputed<boolean>;
    readonly ipAddress?: fabric.MaybeComputed<string>;
    readonly measureLatency?: fabric.MaybeComputed<boolean>;
    readonly port?: fabric.MaybeComputed<number>;
    readonly referenceName?: fabric.MaybeComputed<string>;
    readonly regions?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly requestInterval?: fabric.MaybeComputed<number>;
    readonly resourcePath?: fabric.MaybeComputed<string>;
    readonly searchString?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly type: fabric.MaybeComputed<string>;
}
