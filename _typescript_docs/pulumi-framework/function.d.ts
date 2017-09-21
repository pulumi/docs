---
layout: typescript-reference
repo: pulumi-framework
subpath: function.d.ts
---
import * as aws from "@pulumi/aws";
export { Context, Handler } from "@pulumi/aws/serverless";
export declare class LoggedFunction {
    lambda: aws.lambda.Function;
    role: aws.iam.Role;
    constructor(name: string, policies: aws.ARN[], func: aws.serverless.Handler);
}
