---
layout: typescript-reference
repo: pulumi-aws
subpath: autoscaling/group.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Group extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly availabilityZones: fabric.Computed<string[]>;
    readonly defaultCooldown: fabric.Computed<number>;
    readonly desiredCapacity: fabric.Computed<number>;
    readonly enabledMetrics?: fabric.Computed<string[]>;
    readonly forceDelete?: fabric.Computed<boolean>;
    readonly healthCheckGracePeriod?: fabric.Computed<number>;
    readonly healthCheckType: fabric.Computed<string>;
    readonly initialLifecycleHook?: fabric.Computed<{
        defaultResult: string;
        heartbeatTimeout?: number;
        lifecycleTransition: string;
        name: string;
        notificationMetadata?: string;
        notificationTargetArn?: string;
        roleArn?: string;
    }[]>;
    readonly launchConfiguration: fabric.Computed<string>;
    readonly loadBalancers: fabric.Computed<string[]>;
    readonly maxSize: fabric.Computed<number>;
    readonly metricsGranularity?: fabric.Computed<string>;
    readonly minElbCapacity?: fabric.Computed<number>;
    readonly minSize: fabric.Computed<number>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    readonly placementGroup?: fabric.Computed<string>;
    readonly protectFromScaleIn?: fabric.Computed<boolean>;
    readonly suspendedProcesses?: fabric.Computed<string[]>;
    readonly tag?: fabric.Computed<{
        key: string;
        propagateAtLaunch: boolean;
        value: string;
    }[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }[]>;
    readonly targetGroupArns: fabric.Computed<string[]>;
    readonly terminationPolicies?: fabric.Computed<string[]>;
    readonly vpcZoneIdentifier: fabric.Computed<string[]>;
    readonly waitForCapacityTimeout?: fabric.Computed<string>;
    readonly waitForElbCapacity?: fabric.Computed<number>;
    constructor(urnName: string, args: GroupArgs);
}
export interface GroupArgs {
    readonly availabilityZones?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly defaultCooldown?: fabric.MaybeComputed<number>;
    readonly desiredCapacity?: fabric.MaybeComputed<number>;
    readonly enabledMetrics?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly forceDelete?: fabric.MaybeComputed<boolean>;
    readonly healthCheckGracePeriod?: fabric.MaybeComputed<number>;
    readonly healthCheckType?: fabric.MaybeComputed<string>;
    readonly initialLifecycleHook?: fabric.MaybeComputed<{
        defaultResult?: fabric.MaybeComputed<string>;
        heartbeatTimeout?: fabric.MaybeComputed<number>;
        lifecycleTransition: fabric.MaybeComputed<string>;
        name: fabric.MaybeComputed<string>;
        notificationMetadata?: fabric.MaybeComputed<string>;
        notificationTargetArn?: fabric.MaybeComputed<string>;
        roleArn?: fabric.MaybeComputed<string>;
    }>[];
    readonly launchConfiguration: fabric.MaybeComputed<string>;
    readonly loadBalancers?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly maxSize: fabric.MaybeComputed<number>;
    readonly metricsGranularity?: fabric.MaybeComputed<string>;
    readonly minElbCapacity?: fabric.MaybeComputed<number>;
    readonly minSize: fabric.MaybeComputed<number>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly placementGroup?: fabric.MaybeComputed<string>;
    readonly protectFromScaleIn?: fabric.MaybeComputed<boolean>;
    readonly suspendedProcesses?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly tag?: fabric.MaybeComputed<{
        key: fabric.MaybeComputed<string>;
        propagateAtLaunch: fabric.MaybeComputed<boolean>;
        value: fabric.MaybeComputed<string>;
    }>[];
    readonly tags?: fabric.MaybeComputed<fabric.MaybeComputed<{
        [key: string]: any;
    }>>[];
    readonly targetGroupArns?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly terminationPolicies?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly vpcZoneIdentifier?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly waitForCapacityTimeout?: fabric.MaybeComputed<string>;
    readonly waitForElbCapacity?: fabric.MaybeComputed<number>;
}
