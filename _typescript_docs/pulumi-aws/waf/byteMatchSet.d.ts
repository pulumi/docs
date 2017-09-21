---
layout: typescript-reference
repo: pulumi-aws
subpath: waf/byteMatchSet.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ByteMatchSet extends fabric.Resource {
    readonly byteMatchTuples?: fabric.Computed<{
        fieldToMatch: {
            data?: string;
            type: string;
        }[];
        positionalConstraint: string;
        targetString?: string;
        textTransformation: string;
    }[]>;
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: ByteMatchSetArgs);
}
export interface ByteMatchSetArgs {
    readonly byteMatchTuples?: fabric.MaybeComputed<{
        fieldToMatch: fabric.MaybeComputed<{
            data?: fabric.MaybeComputed<string>;
            type: fabric.MaybeComputed<string>;
        }>[];
        positionalConstraint: fabric.MaybeComputed<string>;
        targetString?: fabric.MaybeComputed<string>;
        textTransformation: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
}
