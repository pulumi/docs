---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/authorizer.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { RestApi } from "./restApi";
export declare class Authorizer extends fabric.Resource {
    readonly authorizerCredentials?: fabric.Computed<string>;
    readonly authorizerResultTtlInSeconds?: fabric.Computed<number>;
    readonly authorizerUri: fabric.Computed<string>;
    readonly identitySource?: fabric.Computed<string>;
    readonly identityValidationExpression?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly restApi: fabric.Computed<RestApi>;
    readonly type?: fabric.Computed<string>;
    constructor(urnName: string, args: AuthorizerArgs);
}
export interface AuthorizerArgs {
    readonly authorizerCredentials?: fabric.MaybeComputed<string>;
    readonly authorizerResultTtlInSeconds?: fabric.MaybeComputed<number>;
    readonly authorizerUri: fabric.MaybeComputed<string>;
    readonly identitySource?: fabric.MaybeComputed<string>;
    readonly identityValidationExpression?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
    readonly restApi: fabric.MaybeComputed<RestApi>;
    readonly type?: fabric.MaybeComputed<string>;
}
