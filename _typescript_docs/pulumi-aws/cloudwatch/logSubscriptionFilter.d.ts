---
layout: typescript-reference
repo: pulumi-aws
subpath: cloudwatch/logSubscriptionFilter.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { LogGroup } from "./logGroup";
export declare class LogSubscriptionFilter extends fabric.Resource {
    readonly destinationArn: fabric.Computed<string>;
    readonly filterPattern: fabric.Computed<string>;
    readonly logGroup: fabric.Computed<LogGroup>;
    readonly name: fabric.Computed<string>;
    readonly roleArn: fabric.Computed<string>;
    constructor(urnName: string, args: LogSubscriptionFilterArgs);
}
export interface LogSubscriptionFilterArgs {
    readonly destinationArn: fabric.MaybeComputed<string>;
    readonly filterPattern: fabric.MaybeComputed<string>;
    readonly logGroup: fabric.MaybeComputed<LogGroup>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly roleArn?: fabric.MaybeComputed<string>;
}
