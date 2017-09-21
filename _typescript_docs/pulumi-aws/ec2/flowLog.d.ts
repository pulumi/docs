---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/flowLog.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class FlowLog extends fabric.Resource {
    readonly eniId?: fabric.Computed<string>;
    readonly iamRoleArn: fabric.Computed<string>;
    readonly logGroupName: fabric.Computed<string>;
    readonly subnetId?: fabric.Computed<string>;
    readonly trafficType: fabric.Computed<string>;
    readonly vpcId?: fabric.Computed<string>;
    constructor(urnName: string, args: FlowLogArgs);
}
export interface FlowLogArgs {
    readonly eniId?: fabric.MaybeComputed<string>;
    readonly iamRoleArn: fabric.MaybeComputed<string>;
    readonly logGroupName: fabric.MaybeComputed<string>;
    readonly subnetId?: fabric.MaybeComputed<string>;
    readonly trafficType: fabric.MaybeComputed<string>;
    readonly vpcId?: fabric.MaybeComputed<string>;
}
