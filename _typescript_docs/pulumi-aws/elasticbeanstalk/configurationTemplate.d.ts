---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticbeanstalk/configurationTemplate.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ConfigurationTemplate extends fabric.Resource {
    readonly application: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly environmentId?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly setting: fabric.Computed<{
        name: string;
        namespace: string;
        resource?: string;
        value: string;
    }[]>;
    readonly solutionStackName?: fabric.Computed<string>;
    constructor(urnName: string, args: ConfigurationTemplateArgs);
}
export interface ConfigurationTemplateArgs {
    readonly application: fabric.MaybeComputed<string>;
    readonly description?: fabric.MaybeComputed<string>;
    readonly environmentId?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly setting?: fabric.MaybeComputed<{
        name: fabric.MaybeComputed<string>;
        namespace: fabric.MaybeComputed<string>;
        resource?: fabric.MaybeComputed<string>;
        value: fabric.MaybeComputed<string>;
    }>[];
    readonly solutionStackName?: fabric.MaybeComputed<string>;
}
