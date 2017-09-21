---
layout: typescript-reference
repo: pulumi-aws
subpath: cloudformation/stack.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Stack extends fabric.Resource {
    readonly capabilities?: fabric.Computed<string[]>;
    readonly disableRollback?: fabric.Computed<boolean>;
    readonly iamRoleArn?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly notificationArns?: fabric.Computed<string[]>;
    readonly onFailure?: fabric.Computed<string>;
    readonly outputs: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly parameters: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly policyBody: fabric.Computed<string>;
    readonly policyUrl?: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly templateBody: fabric.Computed<string>;
    readonly templateUrl?: fabric.Computed<string>;
    readonly timeoutInMinutes?: fabric.Computed<number>;
    constructor(urnName: string, args: StackArgs);
}
export interface StackArgs {
    readonly capabilities?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly disableRollback?: fabric.MaybeComputed<boolean>;
    readonly iamRoleArn?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly notificationArns?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly onFailure?: fabric.MaybeComputed<string>;
    readonly parameters?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly policyBody?: fabric.MaybeComputed<string>;
    readonly policyUrl?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly templateBody?: fabric.MaybeComputed<string>;
    readonly templateUrl?: fabric.MaybeComputed<string>;
    readonly timeoutInMinutes?: fabric.MaybeComputed<number>;
}
