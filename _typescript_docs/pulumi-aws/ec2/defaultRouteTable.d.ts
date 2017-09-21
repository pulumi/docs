---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/defaultRouteTable.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class DefaultRouteTable extends fabric.Resource {
    readonly defaultRouteTableId: fabric.Computed<string>;
    readonly propagatingVgws?: fabric.Computed<string[]>;
    readonly route: fabric.Computed<{
        cidrBlock?: string;
        egressOnlyGatewayId?: string;
        gatewayId?: string;
        instanceId?: string;
        ipv6CidrBlock?: string;
        natGatewayId?: string;
        networkInterfaceId?: string;
        vpcPeeringConnectionId?: string;
    }[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: DefaultRouteTableArgs);
}
export interface DefaultRouteTableArgs {
    readonly defaultRouteTableId: fabric.MaybeComputed<string>;
    readonly propagatingVgws?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly route?: fabric.MaybeComputed<{
        cidrBlock?: fabric.MaybeComputed<string>;
        egressOnlyGatewayId?: fabric.MaybeComputed<string>;
        gatewayId?: fabric.MaybeComputed<string>;
        instanceId?: fabric.MaybeComputed<string>;
        ipv6CidrBlock?: fabric.MaybeComputed<string>;
        natGatewayId?: fabric.MaybeComputed<string>;
        networkInterfaceId?: fabric.MaybeComputed<string>;
        vpcPeeringConnectionId?: fabric.MaybeComputed<string>;
    }>[];
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
}
