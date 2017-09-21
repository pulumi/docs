---
layout: typescript-reference
repo: pulumi-aws
subpath: emr/securityConfiguration.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class SecurityConfiguration extends fabric.Resource {
    readonly configuration: fabric.Computed<string>;
    readonly creationDate: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly namePrefix?: fabric.Computed<string>;
    constructor(urnName: string, args: SecurityConfigurationArgs);
}
export interface SecurityConfigurationArgs {
    readonly configuration: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
}
