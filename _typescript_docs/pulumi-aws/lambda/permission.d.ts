---
layout: typescript-reference
repo: pulumi-aws
subpath: lambda/permission.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { Function } from "./function";
export declare class Permission extends fabric.Resource {
    readonly action: fabric.Computed<string>;
    readonly function: fabric.Computed<Function>;
    readonly principal: fabric.Computed<string>;
    readonly qualifier?: fabric.Computed<string>;
    readonly sourceAccount?: fabric.Computed<string>;
    readonly sourceArn?: fabric.Computed<string>;
    readonly statementId: fabric.Computed<string>;
    constructor(urnName: string, args: PermissionArgs);
}
export interface PermissionArgs {
    readonly action: fabric.MaybeComputed<string>;
    readonly function: fabric.MaybeComputed<Function>;
    readonly principal: fabric.MaybeComputed<string>;
    readonly qualifier?: fabric.MaybeComputed<string>;
    readonly sourceAccount?: fabric.MaybeComputed<string>;
    readonly sourceArn?: fabric.MaybeComputed<string>;
    readonly statementId?: fabric.MaybeComputed<string>;
}
