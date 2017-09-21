---
layout: typescript-reference
repo: pulumi-aws
subpath: ssm/maintenanceWindowTask.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class MaintenanceWindowTask extends fabric.Resource {
    readonly loggingInfo?: fabric.Computed<{
        s3BucketName: string;
        s3BucketPrefix?: string;
        s3Region: string;
    }[]>;
    readonly maxConcurrency: fabric.Computed<string>;
    readonly maxErrors: fabric.Computed<string>;
    readonly priority?: fabric.Computed<number>;
    readonly serviceRoleArn: fabric.Computed<string>;
    readonly targets: fabric.Computed<{
        key: string;
        values: string[];
    }[]>;
    readonly taskArn: fabric.Computed<string>;
    readonly taskParameters?: fabric.Computed<{
        name: string;
        values: string[];
    }[]>;
    readonly taskType: fabric.Computed<string>;
    readonly windowId: fabric.Computed<string>;
    constructor(urnName: string, args: MaintenanceWindowTaskArgs);
}
export interface MaintenanceWindowTaskArgs {
    readonly loggingInfo?: fabric.MaybeComputed<{
        s3BucketName: fabric.MaybeComputed<string>;
        s3BucketPrefix?: fabric.MaybeComputed<string>;
        s3Region: fabric.MaybeComputed<string>;
    }>[];
    readonly maxConcurrency: fabric.MaybeComputed<string>;
    readonly maxErrors: fabric.MaybeComputed<string>;
    readonly priority?: fabric.MaybeComputed<number>;
    readonly serviceRoleArn: fabric.MaybeComputed<string>;
    readonly targets: fabric.MaybeComputed<{
        key: fabric.MaybeComputed<string>;
        values: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    }>[];
    readonly taskArn: fabric.MaybeComputed<string>;
    readonly taskParameters?: fabric.MaybeComputed<{
        name: fabric.MaybeComputed<string>;
        values: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    }>[];
    readonly taskType: fabric.MaybeComputed<string>;
    readonly windowId: fabric.MaybeComputed<string>;
}
