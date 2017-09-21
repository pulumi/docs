---
layout: typescript-reference
repo: pulumi-aws
subpath: inspector/assessmentTarget.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class AssessmentTarget extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly resourceGroupArn: fabric.Computed<string>;
    constructor(urnName: string, args: AssessmentTargetArgs);
}
export interface AssessmentTargetArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly resourceGroupArn: fabric.MaybeComputed<string>;
}
