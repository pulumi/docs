---
layout: typescript-reference
repo: pulumi-aws
subpath: codedeploy/application.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Application extends fabric.Resource {
    readonly name: fabric.Computed<string>;
    readonly uniqueId: fabric.Computed<string>;
    constructor(urnName: string, args: ApplicationArgs);
}
export interface ApplicationArgs {
    readonly name?: fabric.MaybeComputed<string>;
    readonly uniqueId?: fabric.MaybeComputed<string>;
}
