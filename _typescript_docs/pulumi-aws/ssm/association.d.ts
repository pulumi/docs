---
layout: typescript-reference
repo: pulumi-aws
subpath: ssm/association.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Association extends fabric.Resource {
    readonly associationId: fabric.Computed<string>;
    readonly instanceId?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly parameters: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly targets: fabric.Computed<{
        key: string;
        values: string[];
    }[]>;
    constructor(urnName: string, args: AssociationArgs);
}
export interface AssociationArgs {
    readonly instanceId?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly parameters?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly targets?: fabric.MaybeComputed<{
        key: fabric.MaybeComputed<string>;
        values: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    }>[];
}
