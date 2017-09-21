---
layout: typescript-reference
repo: pulumi-aws
subpath: ssm/parameter.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Parameter extends fabric.Resource {
    readonly keyId?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly overwrite?: fabric.Computed<boolean>;
    readonly type: fabric.Computed<string>;
    readonly value: fabric.Computed<string>;
    constructor(urnName: string, args: ParameterArgs);
}
export interface ParameterArgs {
    readonly keyId?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly overwrite?: fabric.MaybeComputed<boolean>;
    readonly type: fabric.MaybeComputed<string>;
    readonly value: fabric.MaybeComputed<string>;
}
