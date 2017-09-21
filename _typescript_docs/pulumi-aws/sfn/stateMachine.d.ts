---
layout: typescript-reference
repo: pulumi-aws
subpath: sfn/stateMachine.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class StateMachine extends fabric.Resource {
    readonly creationDate: fabric.Computed<string>;
    readonly definition: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly roleArn: fabric.Computed<string>;
    readonly status: fabric.Computed<string>;
    constructor(urnName: string, args: StateMachineArgs);
}
export interface StateMachineArgs {
    readonly definition: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly roleArn: fabric.MaybeComputed<string>;
}
