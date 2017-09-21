---
layout: typescript-reference
repo: pulumi-framework
subpath: unhandledError.d.ts
---
import * as aws from "@pulumi/aws";
export declare function getUnhandledErrorTopic(): aws.sns.Topic;
export declare type ErrorHandler = (message: string, payload: any) => void;
export declare function onError(name: string, handler: ErrorHandler): void;
