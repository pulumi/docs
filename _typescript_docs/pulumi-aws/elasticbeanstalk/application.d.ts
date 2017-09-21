---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticbeanstalk/application.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Application extends fabric.Resource {
    readonly description?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: ApplicationArgs);
}
export interface ApplicationArgs {
    readonly description?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
}
