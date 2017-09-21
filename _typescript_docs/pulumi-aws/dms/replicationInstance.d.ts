---
layout: typescript-reference
repo: pulumi-aws
subpath: dms/replicationInstance.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ReplicationInstance extends fabric.Resource {
    readonly allocatedStorage: fabric.Computed<number>;
    readonly applyImmediately?: fabric.Computed<boolean>;
    readonly autoMinorVersionUpgrade: fabric.Computed<boolean>;
    readonly availabilityZone: fabric.Computed<string>;
    readonly engineVersion: fabric.Computed<string>;
    readonly kmsKeyArn: fabric.Computed<string>;
    readonly multiAz: fabric.Computed<boolean>;
    readonly preferredMaintenanceWindow: fabric.Computed<string>;
    readonly publiclyAccessible: fabric.Computed<boolean>;
    readonly replicationInstanceArn: fabric.Computed<string>;
    readonly replicationInstanceClass: fabric.Computed<string>;
    readonly replicationInstanceId: fabric.Computed<string>;
    readonly replicationInstancePrivateIps: fabric.Computed<string[]>;
    readonly replicationInstancePublicIps: fabric.Computed<string[]>;
    readonly replicationSubnetGroupId: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcSecurityGroupIds: fabric.Computed<string[]>;
    constructor(urnName: string, args: ReplicationInstanceArgs);
}
export interface ReplicationInstanceArgs {
    readonly allocatedStorage?: fabric.MaybeComputed<number>;
    readonly applyImmediately?: fabric.MaybeComputed<boolean>;
    readonly autoMinorVersionUpgrade?: fabric.MaybeComputed<boolean>;
    readonly availabilityZone?: fabric.MaybeComputed<string>;
    readonly engineVersion?: fabric.MaybeComputed<string>;
    readonly kmsKeyArn?: fabric.MaybeComputed<string>;
    readonly multiAz?: fabric.MaybeComputed<boolean>;
    readonly preferredMaintenanceWindow?: fabric.MaybeComputed<string>;
    readonly publiclyAccessible?: fabric.MaybeComputed<boolean>;
    readonly replicationInstanceClass: fabric.MaybeComputed<string>;
    readonly replicationInstanceId: fabric.MaybeComputed<string>;
    readonly replicationSubnetGroupId?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly vpcSecurityGroupIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
}
