---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/vpcPeeringConnection.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class VpcPeeringConnection extends fabric.Resource {
    readonly acceptStatus: fabric.Computed<string>;
    readonly accepter: fabric.Computed<{
        allowClassicLinkToRemoteVpc?: boolean;
        allowRemoteVpcDnsResolution?: boolean;
        allowVpcToRemoteClassicLink?: boolean;
    }[]>;
    readonly autoAccept?: fabric.Computed<boolean>;
    readonly peerOwnerId: fabric.Computed<string>;
    readonly peerVpcId: fabric.Computed<string>;
    readonly requester: fabric.Computed<{
        allowClassicLinkToRemoteVpc?: boolean;
        allowRemoteVpcDnsResolution?: boolean;
        allowVpcToRemoteClassicLink?: boolean;
    }[]>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.Computed<string>;
    constructor(urnName: string, args: VpcPeeringConnectionArgs);
}
export interface VpcPeeringConnectionArgs {
    readonly accepter?: fabric.MaybeComputed<{
        allowClassicLinkToRemoteVpc?: fabric.MaybeComputed<boolean>;
        allowRemoteVpcDnsResolution?: fabric.MaybeComputed<boolean>;
        allowVpcToRemoteClassicLink?: fabric.MaybeComputed<boolean>;
    }>[];
    readonly autoAccept?: fabric.MaybeComputed<boolean>;
    readonly peerOwnerId?: fabric.MaybeComputed<string>;
    readonly peerVpcId: fabric.MaybeComputed<string>;
    readonly requester?: fabric.MaybeComputed<{
        allowClassicLinkToRemoteVpc?: fabric.MaybeComputed<boolean>;
        allowRemoteVpcDnsResolution?: fabric.MaybeComputed<boolean>;
        allowVpcToRemoteClassicLink?: fabric.MaybeComputed<boolean>;
    }>[];
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly vpcId: fabric.MaybeComputed<string>;
}
