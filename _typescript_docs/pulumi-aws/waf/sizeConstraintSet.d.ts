---
layout: typescript-reference
repo: pulumi-aws
subpath: waf/sizeConstraintSet.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SizeConstraintSet extends fabric.Resource {
    readonly name: fabric.Computed<string>;
    readonly sizeConstraints?: fabric.Computed<{
        comparisonOperator: string;
        fieldToMatch: {
            data?: string;
            type: string;
        }[];
        size: number;
        textTransformation: string;
    }[]>;
    constructor(urnName: string, args: SizeConstraintSetArgs);
}
export interface SizeConstraintSetArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly sizeConstraints?: fabric.MaybeComputed<{
        comparisonOperator: fabric.MaybeComputed<string>;
        fieldToMatch: fabric.MaybeComputed<{
            data?: fabric.MaybeComputed<string>;
            type: fabric.MaybeComputed<string>;
        }>[];
        size: fabric.MaybeComputed<number>;
        textTransformation: fabric.MaybeComputed<string>;
    }>[];
}
