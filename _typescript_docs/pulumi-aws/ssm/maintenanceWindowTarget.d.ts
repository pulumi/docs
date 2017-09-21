---
layout: typescript-reference
repo: pulumi-aws
subpath: ssm/maintenanceWindowTarget.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class MaintenanceWindowTarget extends fabric.Resource {
    readonly ownerInformation?: fabric.Computed<string>;
    readonly resourceType: fabric.Computed<string>;
    readonly targets: fabric.Computed<{
        key: string;
        values: string[];
    }[]>;
    readonly windowId: fabric.Computed<string>;
    constructor(urnName: string, args: MaintenanceWindowTargetArgs);
}
export interface MaintenanceWindowTargetArgs {
    readonly ownerInformation?: fabric.MaybeComputed<string>;
    readonly resourceType: fabric.MaybeComputed<string>;
    readonly targets: fabric.MaybeComputed<{
        key: fabric.MaybeComputed<string>;
        values: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    }>[];
    readonly windowId: fabric.MaybeComputed<string>;
}
