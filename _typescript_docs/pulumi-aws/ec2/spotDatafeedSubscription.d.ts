---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/spotDatafeedSubscription.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SpotDatafeedSubscription extends fabric.Resource {
    readonly bucket: fabric.Computed<string>;
    readonly prefix?: fabric.Computed<string>;
    constructor(urnName: string, args: SpotDatafeedSubscriptionArgs);
}
export interface SpotDatafeedSubscriptionArgs {
    readonly bucket: fabric.MaybeComputed<string>;
    readonly prefix?: fabric.MaybeComputed<string>;
}
