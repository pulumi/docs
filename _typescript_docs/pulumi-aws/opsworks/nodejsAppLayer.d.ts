---
layout: typescript-reference
repo: pulumi-aws
subpath: opsworks/nodejsAppLayer.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class NodejsAppLayer extends fabric.Resource {
    readonly autoAssignElasticIps?: fabric.Computed<boolean>;
    readonly autoAssignPublicIps?: fabric.Computed<boolean>;
    readonly autoHealing?: fabric.Computed<boolean>;
    readonly customConfigureRecipes?: fabric.Computed<string[]>;
    readonly customDeployRecipes?: fabric.Computed<string[]>;
    readonly customInstanceProfileArn?: fabric.Computed<string>;
    readonly customJson?: fabric.Computed<string>;
    readonly customSecurityGroupIds?: fabric.Computed<string[]>;
    readonly customSetupRecipes?: fabric.Computed<string[]>;
    readonly customShutdownRecipes?: fabric.Computed<string[]>;
    readonly customUndeployRecipes?: fabric.Computed<string[]>;
    readonly drainElbOnShutdown?: fabric.Computed<boolean>;
    readonly ebsVolume?: fabric.Computed<{
        iops?: number;
        mountPoint: string;
        numberOfDisks: number;
        raidLevel?: string;
        size: number;
        type?: string;
    }[]>;
    readonly elasticLoadBalancer?: fabric.Computed<string>;
    readonly layerId: fabric.Computed<string>;
    readonly installUpdatesOnBoot?: fabric.Computed<boolean>;
    readonly instanceShutdownTimeout?: fabric.Computed<number>;
    readonly name: fabric.Computed<string>;
    readonly nodejsVersion?: fabric.Computed<string>;
    readonly stackId: fabric.Computed<string>;
    readonly systemPackages?: fabric.Computed<string[]>;
    readonly useEbsOptimizedInstances?: fabric.Computed<boolean>;
    constructor(urnName: string, args: NodejsAppLayerArgs);
}
export interface NodejsAppLayerArgs {
    readonly autoAssignElasticIps?: fabric.MaybeComputed<boolean>;
    readonly autoAssignPublicIps?: fabric.MaybeComputed<boolean>;
    readonly autoHealing?: fabric.MaybeComputed<boolean>;
    readonly customConfigureRecipes?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly customDeployRecipes?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly customInstanceProfileArn?: fabric.MaybeComputed<string>;
    readonly customJson?: fabric.MaybeComputed<string>;
    readonly customSecurityGroupIds?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly customSetupRecipes?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly customShutdownRecipes?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly customUndeployRecipes?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly drainElbOnShutdown?: fabric.MaybeComputed<boolean>;
    readonly ebsVolume?: fabric.MaybeComputed<{
        iops?: fabric.MaybeComputed<number>;
        mountPoint: fabric.MaybeComputed<string>;
        numberOfDisks: fabric.MaybeComputed<number>;
        raidLevel?: fabric.MaybeComputed<string>;
        size: fabric.MaybeComputed<number>;
        type?: fabric.MaybeComputed<string>;
    }>[];
    readonly elasticLoadBalancer?: fabric.MaybeComputed<string>;
    readonly installUpdatesOnBoot?: fabric.MaybeComputed<boolean>;
    readonly instanceShutdownTimeout?: fabric.MaybeComputed<number>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly nodejsVersion?: fabric.MaybeComputed<string>;
    readonly stackId: fabric.MaybeComputed<string>;
    readonly systemPackages?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly useEbsOptimizedInstances?: fabric.MaybeComputed<boolean>;
}
