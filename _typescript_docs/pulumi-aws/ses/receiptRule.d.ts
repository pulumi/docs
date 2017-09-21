---
layout: typescript-reference
repo: pulumi-aws
subpath: ses/receiptRule.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class ReceiptRule extends fabric.Resource {
    readonly addHeaderAction?: fabric.Computed<{
        headerName: string;
        headerValue: string;
        position: number;
    }[]>;
    readonly after?: fabric.Computed<string>;
    readonly bounceAction?: fabric.Computed<{
        message: string;
        position: number;
        sender: string;
        smtpReplyCode: string;
        statusCode?: string;
        topicArn?: string;
    }[]>;
    readonly enabled: fabric.Computed<boolean>;
    readonly lambdaAction?: fabric.Computed<{
        functionArn: string;
        invocationType: string;
        position: number;
        topicArn?: string;
    }[]>;
    readonly name: fabric.Computed<string>;
    readonly recipients?: fabric.Computed<string[]>;
    readonly ruleSetName: fabric.Computed<string>;
    readonly s3Action?: fabric.Computed<{
        bucketName: string;
        kmsKeyArn?: string;
        objectKeyPrefix?: string;
        position: number;
        topicArn?: string;
    }[]>;
    readonly scanEnabled: fabric.Computed<boolean>;
    readonly snsAction?: fabric.Computed<{
        position: number;
        topicArn: string;
    }[]>;
    readonly stopAction?: fabric.Computed<{
        position: number;
        scope: string;
        topicArn?: string;
    }[]>;
    readonly tlsPolicy: fabric.Computed<string>;
    readonly workmailAction?: fabric.Computed<{
        organizationArn: string;
        position: number;
        topicArn?: string;
    }[]>;
    constructor(urnName: string, args: ReceiptRuleArgs);
}
export interface ReceiptRuleArgs {
    readonly addHeaderAction?: fabric.MaybeComputed<{
        headerName: fabric.MaybeComputed<string>;
        headerValue: fabric.MaybeComputed<string>;
        position: fabric.MaybeComputed<number>;
    }>[];
    readonly after?: fabric.MaybeComputed<string>;
    readonly bounceAction?: fabric.MaybeComputed<{
        message: fabric.MaybeComputed<string>;
        position: fabric.MaybeComputed<number>;
        sender: fabric.MaybeComputed<string>;
        smtpReplyCode: fabric.MaybeComputed<string>;
        statusCode?: fabric.MaybeComputed<string>;
        topicArn?: fabric.MaybeComputed<string>;
    }>[];
    readonly enabled?: fabric.MaybeComputed<boolean>;
    readonly lambdaAction?: fabric.MaybeComputed<{
        functionArn: fabric.MaybeComputed<string>;
        invocationType?: fabric.MaybeComputed<string>;
        position: fabric.MaybeComputed<number>;
        topicArn?: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly recipients?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly ruleSetName: fabric.MaybeComputed<string>;
    readonly s3Action?: fabric.MaybeComputed<{
        bucketName: fabric.MaybeComputed<string>;
        kmsKeyArn?: fabric.MaybeComputed<string>;
        objectKeyPrefix?: fabric.MaybeComputed<string>;
        position: fabric.MaybeComputed<number>;
        topicArn?: fabric.MaybeComputed<string>;
    }>[];
    readonly scanEnabled?: fabric.MaybeComputed<boolean>;
    readonly snsAction?: fabric.MaybeComputed<{
        position: fabric.MaybeComputed<number>;
        topicArn: fabric.MaybeComputed<string>;
    }>[];
    readonly stopAction?: fabric.MaybeComputed<{
        position: fabric.MaybeComputed<number>;
        scope: fabric.MaybeComputed<string>;
        topicArn?: fabric.MaybeComputed<string>;
    }>[];
    readonly tlsPolicy?: fabric.MaybeComputed<string>;
    readonly workmailAction?: fabric.MaybeComputed<{
        organizationArn: fabric.MaybeComputed<string>;
        position: fabric.MaybeComputed<number>;
        topicArn?: fabric.MaybeComputed<string>;
    }>[];
}
