---
layout: typescript-reference
repo: pulumi-aws
subpath: emr/cluster.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Cluster extends fabric.Resource {
    readonly applications?: fabric.Computed<string[]>;
    readonly autoscalingRole?: fabric.Computed<string>;
    readonly bootstrapAction?: fabric.Computed<{
        args?: string[];
        name: string;
        path: string;
    }[]>;
    readonly clusterState: fabric.Computed<string>;
    readonly configurations?: fabric.Computed<string>;
    readonly coreInstanceCount?: fabric.Computed<number>;
    readonly coreInstanceType: fabric.Computed<string>;
    readonly ec2Attributes?: fabric.Computed<{
        additionalMasterSecurityGroups?: string;
        additionalSlaveSecurityGroups?: string;
        emrManagedMasterSecurityGroup?: string;
        emrManagedSlaveSecurityGroup?: string;
        instanceProfile: string;
        keyName?: string;
        serviceAccessSecurityGroup?: string;
        subnetId?: string;
    }[]>;
    readonly keepJobFlowAliveWhenNoSteps: fabric.Computed<boolean>;
    readonly logUri?: fabric.Computed<string>;
    readonly masterInstanceType: fabric.Computed<string>;
    readonly masterPublicDns: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly releaseLabel: fabric.Computed<string>;
    readonly securityConfiguration?: fabric.Computed<string>;
    readonly serviceRole: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly terminationProtection: fabric.Computed<boolean>;
    readonly visibleToAllUsers?: fabric.Computed<boolean>;
    constructor(urnName: string, args: ClusterArgs);
}
export interface ClusterArgs {
    readonly applications?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly autoscalingRole?: fabric.MaybeComputed<string>;
    readonly bootstrapAction?: fabric.MaybeComputed<{
        args?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        name: fabric.MaybeComputed<string>;
        path: fabric.MaybeComputed<string>;
    }>[];
    readonly configurations?: fabric.MaybeComputed<string>;
    readonly coreInstanceCount?: fabric.MaybeComputed<number>;
    readonly coreInstanceType?: fabric.MaybeComputed<string>;
    readonly ec2Attributes?: fabric.MaybeComputed<{
        additionalMasterSecurityGroups?: fabric.MaybeComputed<string>;
        additionalSlaveSecurityGroups?: fabric.MaybeComputed<string>;
        emrManagedMasterSecurityGroup?: fabric.MaybeComputed<string>;
        emrManagedSlaveSecurityGroup?: fabric.MaybeComputed<string>;
        instanceProfile: fabric.MaybeComputed<string>;
        keyName?: fabric.MaybeComputed<string>;
        serviceAccessSecurityGroup?: fabric.MaybeComputed<string>;
        subnetId?: fabric.MaybeComputed<string>;
    }>[];
    readonly keepJobFlowAliveWhenNoSteps?: fabric.MaybeComputed<boolean>;
    readonly logUri?: fabric.MaybeComputed<string>;
    readonly masterInstanceType: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly releaseLabel: fabric.MaybeComputed<string>;
    readonly securityConfiguration?: fabric.MaybeComputed<string>;
    readonly serviceRole: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly terminationProtection?: fabric.MaybeComputed<boolean>;
    readonly visibleToAllUsers?: fabric.MaybeComputed<boolean>;
}
