---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/vpnConnection.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class VpnConnection extends fabric.Resource {
    readonly customerGatewayConfiguration: fabric.Computed<string>;
    readonly customerGatewayId: fabric.Computed<string>;
    readonly routes: fabric.Computed<{
        destinationCidrBlock: string;
        source: string;
        state: string;
    }[]>;
    readonly staticRoutesOnly: fabric.Computed<boolean>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly tunnel1Address: fabric.Computed<string>;
    readonly tunnel1BgpAsn: fabric.Computed<string>;
    readonly tunnel1BgpHoldtime: fabric.Computed<number>;
    readonly tunnel1CgwInsideAddress: fabric.Computed<string>;
    readonly tunnel1PresharedKey: fabric.Computed<string>;
    readonly tunnel1VgwInsideAddress: fabric.Computed<string>;
    readonly tunnel2Address: fabric.Computed<string>;
    readonly tunnel2BgpAsn: fabric.Computed<string>;
    readonly tunnel2BgpHoldtime: fabric.Computed<number>;
    readonly tunnel2CgwInsideAddress: fabric.Computed<string>;
    readonly tunnel2PresharedKey: fabric.Computed<string>;
    readonly tunnel2VgwInsideAddress: fabric.Computed<string>;
    readonly type: fabric.Computed<string>;
    readonly vgwTelemetry: fabric.Computed<{
        acceptedRouteCount: number;
        lastStatusChange: string;
        outsideIpAddress: string;
        status: string;
        statusMessage: string;
    }[]>;
    readonly vpnGatewayId: fabric.Computed<string>;
    constructor(urnName: string, args: VpnConnectionArgs);
}
export interface VpnConnectionArgs {
    readonly customerGatewayConfiguration?: fabric.MaybeComputed<string>;
    readonly customerGatewayId: fabric.MaybeComputed<string>;
    readonly routes?: fabric.MaybeComputed<{
        destinationCidrBlock?: fabric.MaybeComputed<string>;
        source?: fabric.MaybeComputed<string>;
        state?: fabric.MaybeComputed<string>;
    }>[];
    readonly staticRoutesOnly?: fabric.MaybeComputed<boolean>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly type: fabric.MaybeComputed<string>;
    readonly vgwTelemetry?: fabric.MaybeComputed<{
        acceptedRouteCount?: fabric.MaybeComputed<number>;
        lastStatusChange?: fabric.MaybeComputed<string>;
        outsideIpAddress?: fabric.MaybeComputed<string>;
        status?: fabric.MaybeComputed<string>;
        statusMessage?: fabric.MaybeComputed<string>;
    }>[];
    readonly vpnGatewayId: fabric.MaybeComputed<string>;
}
