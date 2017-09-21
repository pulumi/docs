---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/usagePlanKey.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class UsagePlanKey extends fabric.Resource {
    readonly keyId: fabric.Computed<string>;
    readonly keyType: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly usagePlanId: fabric.Computed<string>;
    readonly value: fabric.Computed<string>;
    constructor(urnName: string, args: UsagePlanKeyArgs);
}
export interface UsagePlanKeyArgs {
    readonly keyId: fabric.MaybeComputed<string>;
    readonly keyType: fabric.MaybeComputed<string>;
    readonly usagePlanId: fabric.MaybeComputed<string>;
}
