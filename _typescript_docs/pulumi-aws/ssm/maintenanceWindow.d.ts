---
layout: typescript-reference
repo: pulumi-aws
subpath: ssm/maintenanceWindow.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class MaintenanceWindow extends fabric.Resource {
    readonly allowUnassociatedTargets?: fabric.Computed<boolean>;
    readonly cutoff: fabric.Computed<number>;
    readonly duration: fabric.Computed<number>;
    readonly enabled?: fabric.Computed<boolean>;
    readonly name: fabric.Computed<string>;
    readonly schedule: fabric.Computed<string>;
    constructor(urnName: string, args: MaintenanceWindowArgs);
}
export interface MaintenanceWindowArgs {
    readonly allowUnassociatedTargets?: fabric.MaybeComputed<boolean>;
    readonly cutoff: fabric.MaybeComputed<number>;
    readonly duration: fabric.MaybeComputed<number>;
    readonly enabled?: fabric.MaybeComputed<boolean>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly schedule: fabric.MaybeComputed<string>;
}
