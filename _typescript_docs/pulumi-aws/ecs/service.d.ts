---
layout: typescript-reference
repo: pulumi-aws
subpath: ecs/service.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Service extends fabric.Resource {
    readonly cluster: fabric.Computed<string>;
    readonly deploymentMaximumPercent?: fabric.Computed<number>;
    readonly deploymentMinimumHealthyPercent?: fabric.Computed<number>;
    readonly desiredCount?: fabric.Computed<number>;
    readonly iamRole?: fabric.Computed<string>;
    readonly loadBalancer?: fabric.Computed<{
        containerName: string;
        containerPort: number;
        elbName?: string;
        targetGroupArn?: string;
    }[]>;
    readonly name: fabric.Computed<string>;
    readonly placementConstraints?: fabric.Computed<{
        expression?: string;
        type: string;
    }[]>;
    readonly placementStrategy?: fabric.Computed<{
        field?: string;
        type: string;
    }[]>;
    readonly taskDefinition: fabric.Computed<string>;
    constructor(urnName: string, args: ServiceArgs);
}
export interface ServiceArgs {
    readonly cluster?: fabric.MaybeComputed<string>;
    readonly deploymentMaximumPercent?: fabric.MaybeComputed<number>;
    readonly deploymentMinimumHealthyPercent?: fabric.MaybeComputed<number>;
    readonly desiredCount?: fabric.MaybeComputed<number>;
    readonly iamRole?: fabric.MaybeComputed<string>;
    readonly loadBalancer?: fabric.MaybeComputed<{
        containerName: fabric.MaybeComputed<string>;
        containerPort: fabric.MaybeComputed<number>;
        elbName?: fabric.MaybeComputed<string>;
        targetGroupArn?: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly placementConstraints?: fabric.MaybeComputed<{
        expression?: fabric.MaybeComputed<string>;
        type: fabric.MaybeComputed<string>;
    }>[];
    readonly placementStrategy?: fabric.MaybeComputed<{
        field?: fabric.MaybeComputed<string>;
        type: fabric.MaybeComputed<string>;
    }>[];
    readonly taskDefinition: fabric.MaybeComputed<string>;
}
