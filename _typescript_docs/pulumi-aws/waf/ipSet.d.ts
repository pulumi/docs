---
layout: typescript-reference
repo: pulumi-aws
subpath: waf/ipSet.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class IpSet extends fabric.Resource {
    readonly ipSetDescriptors?: fabric.Computed<{
        type: string;
        value: string;
    }[]>;
    readonly name: fabric.Computed<string>;
    constructor(urnName: string, args: IpSetArgs);
}
export interface IpSetArgs {
    readonly ipSetDescriptors?: fabric.MaybeComputed<{
        type: fabric.MaybeComputed<string>;
        value: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
}
