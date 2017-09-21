---
layout: typescript-reference
repo: pulumi-aws
subpath: elasticloadbalancing/cookieStickinessPolicy.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class CookieStickinessPolicy extends fabric.Resource {
    readonly cookieExpirationPeriod?: fabric.Computed<number>;
    readonly lbPort: fabric.Computed<number>;
    readonly loadBalancer: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: CookieStickinessPolicyArgs);
}
export interface CookieStickinessPolicyArgs {
    readonly cookieExpirationPeriod?: fabric.MaybeComputed<number>;
    readonly lbPort: fabric.MaybeComputed<number>;
    readonly loadBalancer: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
}
