---
layout: typescript-reference
repo: pulumi-aws
subpath: apigateway/restApi.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class RestApi extends fabric.Resource {
    readonly binaryMediaTypes?: fabric.Computed<string[]>;
    readonly body?: fabric.Computed<string>;
    readonly createdDate: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly rootResourceId: fabric.Computed<string>;
    constructor(urnName: string, args: RestApiArgs);
}
export interface RestApiArgs {
    readonly binaryMediaTypes?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly body?: fabric.MaybeComputed<string>;
    readonly description?: fabric.MaybeComputed<string>;
    readonly name?: fabric.MaybeComputed<string>;
}
