---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticbeanstalk/applicationVersion.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { Bucket } from "../s3/bucket";
import { Application } from "./application";
export declare class ApplicationVersion extends fabric.Resource {
    readonly application: fabric.Computed<Application>;
    readonly bucket: fabric.Computed<Bucket>;
    readonly description?: fabric.Computed<string>;
    readonly forceDelete?: fabric.Computed<boolean>;
    readonly key: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: ApplicationVersionArgs);
}
export interface ApplicationVersionArgs {
    readonly application: fabric.MaybeComputed<Application>;
    readonly bucket: fabric.MaybeComputed<Bucket>;
    readonly description?: fabric.MaybeComputed<string>;
    readonly forceDelete?: fabric.MaybeComputed<boolean>;
    readonly key: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
}
