---
layout: typescript-reference
repo: pulumi-aws
subpath: inspector/assessmentTemplate.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class AssessmentTemplate extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly duration: fabric.Computed<number>;
    readonly name: fabric.Computed<string>;
    readonly rulesPackageArns: fabric.Computed<string[]>;
    readonly targetArn: fabric.Computed<string>;
    constructor(urnName: string, args: AssessmentTemplateArgs);
}
export interface AssessmentTemplateArgs {
    readonly duration: fabric.MaybeComputed<number>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly rulesPackageArns: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly targetArn: fabric.MaybeComputed<string>;
}
