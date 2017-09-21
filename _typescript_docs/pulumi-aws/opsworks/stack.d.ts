---
layout: typescript-reference
repo: pulumi-aws
subpath: opsworks/stack.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Stack extends fabric.Resource {
    readonly agentVersion: fabric.Computed<string>;
    readonly berkshelfVersion?: fabric.Computed<string>;
    readonly color?: fabric.Computed<string>;
    readonly configurationManagerName?: fabric.Computed<string>;
    readonly configurationManagerVersion?: fabric.Computed<string>;
    readonly customCookbooksSource: fabric.Computed<{
        password?: string;
        revision?: string;
        sshKey?: string;
        type: string;
        url: string;
        username?: string;
    }[]>;
    readonly customJson?: fabric.Computed<string>;
    readonly defaultAvailabilityZone: fabric.Computed<string>;
    readonly defaultInstanceProfileArn: fabric.Computed<string>;
    readonly defaultOs?: fabric.Computed<string>;
    readonly defaultRootDeviceType?: fabric.Computed<string>;
    readonly defaultSshKeyName?: fabric.Computed<string>;
    readonly defaultSubnetId: fabric.Computed<string>;
    readonly hostnameTheme?: fabric.Computed<string>;
    readonly stackId: fabric.Computed<string>;
    readonly manageBerkshelf?: fabric.Computed<boolean>;
    readonly name: fabric.Computed<string>;
    readonly region: fabric.Computed<string>;
    readonly serviceRoleArn: fabric.Computed<string>;
    readonly stackEndpoint: fabric.Computed<string>;
    readonly useCustomCookbooks?: fabric.Computed<boolean>;
    readonly useOpsworksSecurityGroups?: fabric.Computed<boolean>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: StackArgs);
}
export interface StackArgs {
    readonly agentVersion?: fabric.MaybeComputed<string>;
    readonly berkshelfVersion?: fabric.MaybeComputed<string>;
    readonly color?: fabric.MaybeComputed<string>;
    readonly configurationManagerName?: fabric.MaybeComputed<string>;
    readonly configurationManagerVersion?: fabric.MaybeComputed<string>;
    readonly customCookbooksSource?: fabric.MaybeComputed<{
        password?: fabric.MaybeComputed<string>;
        revision?: fabric.MaybeComputed<string>;
        sshKey?: fabric.MaybeComputed<string>;
        type: fabric.MaybeComputed<string>;
        url: fabric.MaybeComputed<string>;
        username?: fabric.MaybeComputed<string>;
    }>[];
    readonly customJson?: fabric.MaybeComputed<string>;
    readonly defaultAvailabilityZone?: fabric.MaybeComputed<string>;
    readonly defaultInstanceProfileArn: fabric.MaybeComputed<string>;
    readonly defaultOs?: fabric.MaybeComputed<string>;
    readonly defaultRootDeviceType?: fabric.MaybeComputed<string>;
    readonly defaultSshKeyName?: fabric.MaybeComputed<string>;
    readonly defaultSubnetId?: fabric.MaybeComputed<string>;
    readonly hostnameTheme?: fabric.MaybeComputed<string>;
    readonly manageBerkshelf?: fabric.MaybeComputed<boolean>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly region: fabric.MaybeComputed<string>;
    readonly serviceRoleArn: fabric.MaybeComputed<string>;
    readonly useCustomCookbooks?: fabric.MaybeComputed<boolean>;
    readonly useOpsworksSecurityGroups?: fabric.MaybeComputed<boolean>;
    readonly vpcId?: fabric.MaybeComputed<string>;
}
