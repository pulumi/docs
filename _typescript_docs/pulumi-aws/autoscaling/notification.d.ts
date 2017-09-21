---
layout: typescript-reference
repo: pulumi-aws
subpath: autoscaling/notification.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Notification extends fabric.Resource {
    readonly groupNames: fabric.Computed<string[]>;
    readonly notifications: fabric.Computed<string[]>;
    readonly topicArn: fabric.Computed<string>;
    constructor(urnName: string, args: NotificationArgs);
}
export interface NotificationArgs {
    readonly groupNames: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly notifications: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly topicArn: fabric.MaybeComputed<string>;
}
