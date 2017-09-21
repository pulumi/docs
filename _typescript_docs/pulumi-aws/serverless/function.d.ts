---
layout: typescript-reference
repo: pulumi-aws
subpath: serverless/function.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { Role, RolePolicyAttachment } from "../iam";
import * as lambda from "../lambda";
import { ARN } from "../arn";
export interface Context {
    callbackWaitsForEmptyEventLoop: boolean;
    readonly functionName: string;
    readonly functionVersion: string;
    readonly invokedFunctionArn: string;
    readonly memoryLimitInMB: string;
    readonly awsRequestId: string;
    readonly logGroupName: string;
    readonly logStreamName: string;
    readonly identity: any;
    readonly clientContext: any;
    getRemainingTimeInMillis(): string;
}
export declare type Handler = (event: any, context: Context, callback: (error: any, result: any) => void) => any;
export interface FunctionOptions {
    policies: ARN[];
    timeout?: number;
    memorySize?: number;
    deadLetterConfig?: {
        targetArn: fabric.MaybeComputed<string>;
    };
}
export declare class Function {
    readonly lambda: lambda.Function;
    readonly role: Role;
    readonly policies: RolePolicyAttachment[];
    constructor(name: string, options: FunctionOptions, func: Handler);
}
