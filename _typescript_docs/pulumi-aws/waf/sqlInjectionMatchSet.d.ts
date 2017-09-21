---
layout: typescript-reference
repo: pulumi-aws
subpath: waf/sqlInjectionMatchSet.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SqlInjectionMatchSet extends fabric.Resource {
    readonly name: fabric.Computed<string>;
    readonly sqlInjectionMatchTuples?: fabric.Computed<{
        fieldToMatch: {
            data?: string;
            type: string;
        }[];
        textTransformation: string;
    }[]>;
    constructor(urnName: string, args: SqlInjectionMatchSetArgs);
}
export interface SqlInjectionMatchSetArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly sqlInjectionMatchTuples?: fabric.MaybeComputed<{
        fieldToMatch: fabric.MaybeComputed<{
            data?: fabric.MaybeComputed<string>;
            type: fabric.MaybeComputed<string>;
        }>[];
        textTransformation: fabric.MaybeComputed<string>;
    }>[];
}
