---
layout: typescript-reference
repo: pulumi-aws
subpath: dms/replicationSubnetGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ReplicationSubnetGroup extends fabric.Resource {
    readonly replicationSubnetGroupArn: fabric.Computed<string>;
    readonly replicationSubnetGroupDescription: fabric.Computed<string>;
    readonly replicationSubnetGroupId: fabric.Computed<string>;
    readonly subnetIds: fabric.Computed<string[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: ReplicationSubnetGroupArgs);
}
export interface ReplicationSubnetGroupArgs {
    readonly replicationSubnetGroupDescription: fabric.MaybeComputed<string>;
    readonly replicationSubnetGroupId: fabric.MaybeComputed<string>;
    readonly subnetIds: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
