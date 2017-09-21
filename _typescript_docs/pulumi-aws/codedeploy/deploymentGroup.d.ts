---
layout: typescript-reference
repo: pulumi-aws
subpath: codedeploy/deploymentGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class DeploymentGroup extends fabric.Resource {
    readonly alarmConfiguration?: fabric.Computed<{
        alarms?: string[];
        enabled?: boolean;
        ignorePollAlarmFailure?: boolean;
    }[]>;
    readonly appName: fabric.Computed<string>;
    readonly autoRollbackConfiguration?: fabric.Computed<{
        enabled?: boolean;
        events?: string[];
    }[]>;
    readonly autoscalingGroups?: fabric.Computed<string[]>;
    readonly deploymentConfigName?: fabric.Computed<string>;
    readonly deploymentGroupName: fabric.Computed<string>;
    readonly ec2TagFilter?: fabric.Computed<{
        key?: string;
        type?: string;
        value?: string;
    }[]>;
    readonly onPremisesInstanceTagFilter?: fabric.Computed<{
        key?: string;
        type?: string;
        value?: string;
    }[]>;
    readonly serviceRoleArn: fabric.Computed<string>;
    readonly triggerConfiguration?: fabric.Computed<{
        triggerEvents: string[];
        triggerName: string;
        triggerTargetArn: string;
    }[]>;
    constructor(urnName: string, args: DeploymentGroupArgs);
}
export interface DeploymentGroupArgs {
    readonly alarmConfiguration?: fabric.MaybeComputed<{
        alarms?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        enabled?: fabric.MaybeComputed<boolean>;
        ignorePollAlarmFailure?: fabric.MaybeComputed<boolean>;
    }>[];
    readonly appName: fabric.MaybeComputed<string>;
    readonly autoRollbackConfiguration?: fabric.MaybeComputed<{
        enabled?: fabric.MaybeComputed<boolean>;
        events?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    }>[];
    readonly autoscalingGroups?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly deploymentConfigName?: fabric.MaybeComputed<string>;
    readonly deploymentGroupName: fabric.MaybeComputed<string>;
    readonly ec2TagFilter?: fabric.MaybeComputed<{
        key?: fabric.MaybeComputed<string>;
        type?: fabric.MaybeComputed<string>;
        value?: fabric.MaybeComputed<string>;
    }>[];
    readonly onPremisesInstanceTagFilter?: fabric.MaybeComputed<{
        key?: fabric.MaybeComputed<string>;
        type?: fabric.MaybeComputed<string>;
        value?: fabric.MaybeComputed<string>;
    }>[];
    readonly serviceRoleArn: fabric.MaybeComputed<string>;
    readonly triggerConfiguration?: fabric.MaybeComputed<{
        triggerEvents: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        triggerName: fabric.MaybeComputed<string>;
        triggerTargetArn: fabric.MaybeComputed<string>;
    }>[];
}
