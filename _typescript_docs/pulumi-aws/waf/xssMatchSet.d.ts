---
layout: typescript-reference
repo: pulumi-aws
subpath: waf/xssMatchSet.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class XssMatchSet extends fabric.Resource {
    readonly name: fabric.Computed<string>;
    readonly xssMatchTuples?: fabric.Computed<{
        fieldToMatch: {
            data?: string;
            type: string;
        }[];
        textTransformation: string;
    }[]>;
    constructor(urnName: string, args: XssMatchSetArgs);
}
export interface XssMatchSetArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly xssMatchTuples?: fabric.MaybeComputed<{
        fieldToMatch: fabric.MaybeComputed<{
            data?: fabric.MaybeComputed<string>;
            type: fabric.MaybeComputed<string>;
        }>[];
        textTransformation: fabric.MaybeComputed<string>;
    }>[];
}
