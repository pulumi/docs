---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/account.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Account extends fabric.Resource {
    readonly cloudwatchRoleArn?: fabric.Computed<string>;
    readonly throttleSettings: fabric.Computed<{
        burstLimit: number;
        rateLimit: number;
    }[]>;
    constructor(urnName: string, args: AccountArgs);
}
export interface AccountArgs {
    readonly cloudwatchRoleArn?: fabric.MaybeComputed<string>;
}
