---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticsearch/domain.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Domain extends fabric.Resource {
    readonly accessPolicies: fabric.Computed<string>;
    readonly advancedOptions: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly arn: fabric.Computed<string>;
    readonly clusterConfig: fabric.Computed<{
        dedicatedMasterCount?: number;
        dedicatedMasterEnabled?: boolean;
        dedicatedMasterType?: string;
        instanceCount?: number;
        instanceType?: string;
        zoneAwarenessEnabled?: boolean;
    }[]>;
    readonly domainId: fabric.Computed<string>;
    readonly domainName: fabric.Computed<string>;
    readonly ebsOptions: fabric.Computed<{
        ebsEnabled: boolean;
        iops?: number;
        volumeSize?: number;
        volumeType: string;
    }[]>;
    readonly elasticsearchVersion?: fabric.Computed<string>;
    readonly endpoint: fabric.Computed<string>;
    readonly snapshotOptions?: fabric.Computed<{
        automatedSnapshotStartHour: number;
    }[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: DomainArgs);
}
export interface DomainArgs {
    readonly accessPolicies?: fabric.MaybeComputed<string>;
    readonly advancedOptions?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly clusterConfig?: fabric.MaybeComputed<{
        dedicatedMasterCount?: fabric.MaybeComputed<number>;
        dedicatedMasterEnabled?: fabric.MaybeComputed<boolean>;
        dedicatedMasterType?: fabric.MaybeComputed<string>;
        instanceCount?: fabric.MaybeComputed<number>;
        instanceType?: fabric.MaybeComputed<string>;
        zoneAwarenessEnabled?: fabric.MaybeComputed<boolean>;
    }>[];
    readonly domainName: fabric.MaybeComputed<string>;
    readonly ebsOptions?: fabric.MaybeComputed<{
        ebsEnabled: fabric.MaybeComputed<boolean>;
        iops?: fabric.MaybeComputed<number>;
        volumeSize?: fabric.MaybeComputed<number>;
        volumeType?: fabric.MaybeComputed<string>;
    }>[];
    readonly elasticsearchVersion?: fabric.MaybeComputed<string>;
    readonly snapshotOptions?: fabric.MaybeComputed<{
        automatedSnapshotStartHour: fabric.MaybeComputed<number>;
    }>[];
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
