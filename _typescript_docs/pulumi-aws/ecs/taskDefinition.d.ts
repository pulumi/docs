---
layout: typescript-reference
repo: pulumi-aws
subpath: ecs/taskDefinition.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class TaskDefinition extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly containerDefinitions: fabric.Computed<string>;
    readonly family: fabric.Computed<string>;
    readonly networkMode: fabric.Computed<string>;
    readonly placementConstraints?: fabric.Computed<{
        expression?: string;
        type: string;
    }[]>;
    readonly revision: fabric.Computed<number>;
    readonly taskRoleArn?: fabric.Computed<string>;
    readonly volume?: fabric.Computed<{
        hostPath?: string;
        name: string;
    }[]>;
    constructor(urnName: string, args: TaskDefinitionArgs);
}
export interface TaskDefinitionArgs {
    readonly containerDefinitions: fabric.MaybeComputed<string>;
    readonly family: fabric.MaybeComputed<string>;
    readonly networkMode?: fabric.MaybeComputed<string>;
    readonly placementConstraints?: fabric.MaybeComputed<{
        expression?: fabric.MaybeComputed<string>;
        type: fabric.MaybeComputed<string>;
    }>[];
    readonly taskRoleArn?: fabric.MaybeComputed<string>;
    readonly volume?: fabric.MaybeComputed<{
        hostPath?: fabric.MaybeComputed<string>;
        name: fabric.MaybeComputed<string>;
    }>[];
}
