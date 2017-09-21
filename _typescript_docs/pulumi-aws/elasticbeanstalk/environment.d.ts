---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticbeanstalk/environment.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { Application } from "./application";
import { ApplicationVersion } from "./applicationVersion";
export declare class Environment extends fabric.Resource {
    readonly allSettings: fabric.Computed<{
        name: string;
        namespace: string;
        resource?: string;
        value: string;
    }[]>;
    readonly application: fabric.Computed<Application>;
    readonly autoscalingGroups: fabric.Computed<string[]>;
    readonly cname: fabric.Computed<string>;
    readonly cnamePrefix: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly instances: fabric.Computed<string[]>;
    readonly launchConfigurations: fabric.Computed<string[]>;
    readonly loadBalancers: fabric.Computed<string[]>;
    readonly name: fabric.Computed<string>;
    readonly pollInterval?: fabric.Computed<string>;
    readonly queues: fabric.Computed<string[]>;
    readonly setting?: fabric.Computed<{
        name: string;
        namespace: string;
        resource?: string;
        value: string;
    }[]>;
    readonly solutionStackName: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly templateName?: fabric.Computed<string>;
    readonly tier?: fabric.Computed<string>;
    readonly triggers: fabric.Computed<string[]>;
    readonly version: fabric.Computed<ApplicationVersion>;
    readonly waitForReadyTimeout?: fabric.Computed<string>;
    constructor(urnName: string, args: EnvironmentArgs);
}
export interface EnvironmentArgs {
    readonly application: fabric.MaybeComputed<Application>;
    readonly cnamePrefix?: fabric.MaybeComputed<string>;
    readonly description?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly pollInterval?: fabric.MaybeComputed<string>;
    readonly setting?: fabric.MaybeComputed<{
        name: fabric.MaybeComputed<string>;
        namespace: fabric.MaybeComputed<string>;
        resource?: fabric.MaybeComputed<string>;
        value: fabric.MaybeComputed<string>;
    }>[];
    readonly solutionStackName?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly templateName?: fabric.MaybeComputed<string>;
    readonly tier?: fabric.MaybeComputed<string>;
    readonly version?: fabric.MaybeComputed<ApplicationVersion>;
    readonly waitForReadyTimeout?: fabric.MaybeComputed<string>;
}
