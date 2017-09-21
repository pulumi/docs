---
layout: typescript-reference
repo: pulumi-aws
subpath: rds/eventSubscription.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class EventSubscription extends fabric.Resource {
    readonly customerAwsId: fabric.Computed<string>;
    readonly enabled?: fabric.Computed<boolean>;
    readonly eventCategories?: fabric.Computed<string[]>;
    readonly name: fabric.Computed<string>;
    readonly snsTopic: fabric.Computed<string>;
    readonly sourceIds?: fabric.Computed<string[]>;
    readonly sourceType?: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: EventSubscriptionArgs);
}
export interface EventSubscriptionArgs {
    readonly enabled?: fabric.MaybeComputed<boolean>;
    readonly eventCategories?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly snsTopic: fabric.MaybeComputed<string>;
    readonly sourceIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly sourceType?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
