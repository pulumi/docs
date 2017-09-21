---
layout: typescript-reference
repo: pulumi-aws
subpath: opsworks/rdsDbInstance.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class RdsDbInstance extends fabric.Resource {
    readonly dbPassword: fabric.Computed<string>;
    readonly dbUser: fabric.Computed<string>;
    readonly instanceId: fabric.Computed<string>;
    readonly rdsDbInstanceArn: fabric.Computed<string>;
    readonly stackId: fabric.Computed<string>;
    constructor(urnName: string, args: RdsDbInstanceArgs);
}
export interface RdsDbInstanceArgs {
    readonly dbPassword: fabric.MaybeComputed<string>;
    readonly dbUser: fabric.MaybeComputed<string>;
    readonly rdsDbInstanceArn: fabric.MaybeComputed<string>;
    readonly stackId: fabric.MaybeComputed<string>;
}
