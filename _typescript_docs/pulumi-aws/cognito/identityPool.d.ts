---
layout: typescript-reference
repo: pulumi-aws
subpath: cognito/identityPool.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class IdentityPool extends fabric.Resource {
    readonly allowUnauthenticatedIdentities?: fabric.Computed<boolean>;
    readonly cognitoIdentityProviders?: fabric.Computed<{
        clientId?: string;
        providerName?: string;
        serverSideTokenCheck?: boolean;
    }[]>;
    readonly developerProviderName?: fabric.Computed<string>;
    readonly identityPoolName: fabric.Computed<string>;
    readonly openidConnectProviderArns?: fabric.Computed<string[]>;
    readonly samlProviderArns?: fabric.Computed<string[]>;
    readonly supportedLoginProviders?: fabric.Computed<{
        [key: string]: string;
    }>;
    constructor(urnName: string, args: IdentityPoolArgs);
}
export interface IdentityPoolArgs {
    readonly allowUnauthenticatedIdentities?: fabric.MaybeComputed<boolean>;
    readonly cognitoIdentityProviders?: fabric.MaybeComputed<{
        clientId?: fabric.MaybeComputed<string>;
        providerName?: fabric.MaybeComputed<string>;
        serverSideTokenCheck?: fabric.MaybeComputed<boolean>;
    }>[];
    readonly developerProviderName?: fabric.MaybeComputed<string>;
    readonly identityPoolName: fabric.MaybeComputed<string>;
    readonly openidConnectProviderArns?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly samlProviderArns?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly supportedLoginProviders?: fabric.MaybeComputed<{
        [key: string]: fabric.MaybeComputed<string>;
    }>;
}
