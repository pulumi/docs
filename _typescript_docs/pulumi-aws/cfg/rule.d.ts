---
layout: typescript-reference
repo: pulumi-aws
subpath: cfg/rule.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Rule extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly inputParameters?: fabric.Computed<string>;
    readonly maximumExecutionFrequency?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly ruleId: fabric.Computed<string>;
    readonly scope?: fabric.Computed<{
        complianceResourceId?: string;
        complianceResourceTypes?: string[];
        tagKey?: string;
        tagValue?: string;
    }[]>;
    readonly source: fabric.Computed<{
        owner: string;
        sourceDetail?: {
            eventSource?: string;
            maximumExecutionFrequency?: string;
            messageType?: string;
        }[];
        sourceIdentifier: string;
    }[]>;
    constructor(urnName: string, args: RuleArgs);
}
export interface RuleArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly inputParameters?: fabric.MaybeComputed<string>;
    readonly maximumExecutionFrequency?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly scope?: fabric.MaybeComputed<{
        complianceResourceId?: fabric.MaybeComputed<string>;
        complianceResourceTypes?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        tagKey?: fabric.MaybeComputed<string>;
        tagValue?: fabric.MaybeComputed<string>;
    }>[];
    readonly source: fabric.MaybeComputed<{
        owner: fabric.MaybeComputed<string>;
        sourceDetail?: fabric.MaybeComputed<{
            eventSource?: fabric.MaybeComputed<string>;
            maximumExecutionFrequency?: fabric.MaybeComputed<string>;
            messageType?: fabric.MaybeComputed<string>;
        }>[];
        sourceIdentifier: fabric.MaybeComputed<string>;
    }>[];
}
