---
layout: typescript-reference
repo: pulumi-framework
subpath: sns.d.ts
---
import * as aws from "@pulumi/aws";
export interface SNSItem {
    SignatureVersion: string;
    Timestamp: string;
    Signature: string;
    SigningCertUrl: string;
    MessageId: string;
    Message: string;
    MessageAttributes: {
        [key: string]: SNSMessageAttribute;
    };
    Type: string;
    UnsubscribeUrl: string;
    TopicArn: string;
    Subject: string;
}
export interface SNSMessageAttribute {
    Type: string;
    Value: string;
}
export declare function createSubscription(resName: string, topic: aws.sns.Topic, handler: (item: SNSItem) => Promise<void>): aws.sns.TopicSubscription;
