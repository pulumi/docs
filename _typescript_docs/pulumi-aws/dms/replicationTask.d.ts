---
layout: typescript-reference
repo: pulumi-aws
subpath: dms/replicationTask.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ReplicationTask extends fabric.Resource {
    readonly cdcStartTime?: fabric.Computed<string>;
    readonly migrationType: fabric.Computed<string>;
    readonly replicationInstanceArn: fabric.Computed<string>;
    readonly replicationTaskArn: fabric.Computed<string>;
    readonly replicationTaskId: fabric.Computed<string>;
    readonly replicationTaskSettings?: fabric.Computed<string>;
    readonly sourceEndpointArn: fabric.Computed<string>;
    readonly tableMappings: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly targetEndpointArn: fabric.Computed<string>;
    constructor(urnName: string, args: ReplicationTaskArgs);
}
export interface ReplicationTaskArgs {
    readonly cdcStartTime?: fabric.MaybeComputed<string>;
    readonly migrationType: fabric.MaybeComputed<string>;
    readonly replicationInstanceArn: fabric.MaybeComputed<string>;
    readonly replicationTaskId: fabric.MaybeComputed<string>;
    readonly replicationTaskSettings?: fabric.MaybeComputed<string>;
    readonly sourceEndpointArn: fabric.MaybeComputed<string>;
    readonly tableMappings: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly targetEndpointArn: fabric.MaybeComputed<string>;
}
