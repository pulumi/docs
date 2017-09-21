---
layout: typescript-reference
repo: pulumi-aws
subpath: ssm/patchBaseline.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class PatchBaseline extends fabric.Resource {
    readonly approvalRule?: fabric.Computed<{
        approveAfterDays: number;
        patchFilter: {
            key: string;
            values: string[];
        }[];
    }[]>;
    readonly approvedPatches?: fabric.Computed<string[]>;
    readonly description?: fabric.Computed<string>;
    readonly globalFilter?: fabric.Computed<{
        key: string;
        values: string[];
    }[]>;
    readonly name: fabric.Computed<string>;
    readonly rejectedPatches?: fabric.Computed<string[]>;
    constructor(urnName: string, args: PatchBaselineArgs);
}
export interface PatchBaselineArgs {
    readonly approvalRule?: fabric.MaybeComputed<{
        approveAfterDays: fabric.MaybeComputed<number>;
        patchFilter: fabric.MaybeComputed<{
            key: fabric.MaybeComputed<string>;
            values: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        }>[];
    }>[];
    readonly approvedPatches?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly description?: fabric.MaybeComputed<string>;
    readonly globalFilter?: fabric.MaybeComputed<{
        key: fabric.MaybeComputed<string>;
        values: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly rejectedPatches?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
}
