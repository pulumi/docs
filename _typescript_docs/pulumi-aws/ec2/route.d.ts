---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/route.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Route extends fabric.Resource {
    readonly destinationCidrBlock?: fabric.Computed<string>;
    readonly destinationIpv6CidrBlock?: fabric.Computed<string>;
    readonly destinationPrefixListId: fabric.Computed<string>;
    readonly egressOnlyGatewayId: fabric.Computed<string>;
    readonly gatewayId: fabric.Computed<string>;
    readonly instanceId: fabric.Computed<string>;
    readonly instanceOwnerId: fabric.Computed<string>;
    readonly natGatewayId: fabric.Computed<string>;
    readonly networkInterfaceId: fabric.Computed<string>;
    readonly origin: fabric.Computed<string>;
    readonly routeTableId: fabric.Computed<string>;
    readonly state: fabric.Computed<string>;
    readonly vpcPeeringConnectionId?: fabric.Computed<string>;
    constructor(urnName: string, args: RouteArgs);
}
export interface RouteArgs {
    readonly destinationCidrBlock?: fabric.MaybeComputed<string>;
    readonly destinationIpv6CidrBlock?: fabric.MaybeComputed<string>;
    readonly egressOnlyGatewayId?: fabric.MaybeComputed<string>;
    readonly gatewayId?: fabric.MaybeComputed<string>;
    readonly instanceId?: fabric.MaybeComputed<string>;
    readonly natGatewayId?: fabric.MaybeComputed<string>;
    readonly networkInterfaceId?: fabric.MaybeComputed<string>;
    readonly routeTableId: fabric.MaybeComputed<string>;
    readonly vpcPeeringConnectionId?: fabric.MaybeComputed<string>;
}
