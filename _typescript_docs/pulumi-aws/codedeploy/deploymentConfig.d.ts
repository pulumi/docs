---
layout: typescript-reference
repo: pulumi-aws
subpath: codedeploy/deploymentConfig.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class DeploymentConfig extends fabric.Resource {
    readonly deploymentConfigId: fabric.Computed<string>;
    readonly deploymentConfigName: fabric.Computed<string>;
    readonly minimumHealthyHosts: fabric.Computed<{
        type: string;
        value?: number;
    }[]>;
    constructor(urnName: string, args: DeploymentConfigArgs);
}
export interface DeploymentConfigArgs {
    readonly deploymentConfigName: fabric.MaybeComputed<string>;
    readonly minimumHealthyHosts: fabric.MaybeComputed<{
        type: fabric.MaybeComputed<string>;
        value?: fabric.MaybeComputed<number>;
    }>[];
}
