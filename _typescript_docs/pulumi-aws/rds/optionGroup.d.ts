---
layout: typescript-reference
repo: pulumi-aws
subpath: rds/optionGroup.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class OptionGroup extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly engineName: fabric.Computed<string>;
    readonly majorEngineVersion: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix: fabric.Computed<string>;
    readonly option?: fabric.Computed<{
        dbSecurityGroupMemberships?: string[];
        optionName: string;
        optionSettings?: {
            name: string;
            value: string;
        }[];
        port?: number;
        vpcSecurityGroupMemberships?: string[];
    }[]>;
    readonly optionGroupDescription?: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    constructor(urnName: string, args: OptionGroupArgs);
}
export interface OptionGroupArgs {
    readonly engineName: fabric.MaybeComputed<string>;
    readonly majorEngineVersion: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly option?: fabric.MaybeComputed<{
        dbSecurityGroupMemberships?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        optionName: fabric.MaybeComputed<string>;
        optionSettings?: fabric.MaybeComputed<{
            name: fabric.MaybeComputed<string>;
            value: fabric.MaybeComputed<string>;
        }>[];
        port?: fabric.MaybeComputed<number>;
        vpcSecurityGroupMemberships?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    }>[];
    readonly optionGroupDescription?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
