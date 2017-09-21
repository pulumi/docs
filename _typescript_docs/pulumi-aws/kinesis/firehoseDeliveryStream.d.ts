---
layout: typescript-reference
repo: pulumi-aws
subpath: kinesis/firehoseDeliveryStream.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class FirehoseDeliveryStream extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly destination: fabric.Computed<string>;
    readonly destinationId: fabric.Computed<string>;
    readonly elasticsearchConfiguration?: fabric.Computed<{
        bufferingInterval?: number;
        bufferingSize?: number;
        cloudwatchLoggingOptions: {
            enabled?: boolean;
            logGroupName?: string;
            logStreamName?: string;
        }[];
        domainArn: string;
        indexName: string;
        indexRotationPeriod?: string;
        retryDuration?: number;
        roleArn: string;
        s3BackupMode?: string;
        typeName?: string;
    }[]>;
    readonly name: fabric.Computed<string>;
    readonly redshiftConfiguration?: fabric.Computed<{
        cloudwatchLoggingOptions: {
            enabled?: boolean;
            logGroupName?: string;
            logStreamName?: string;
        }[];
        clusterJdbcurl: string;
        copyOptions?: string;
        dataTableColumns?: string;
        dataTableName: string;
        password: string;
        retryDuration?: number;
        roleArn: string;
        username: string;
    }[]>;
    readonly s3Configuration: fabric.Computed<{
        bucketArn: string;
        bufferInterval?: number;
        bufferSize?: number;
        cloudwatchLoggingOptions: {
            enabled?: boolean;
            logGroupName?: string;
            logStreamName?: string;
        }[];
        compressionFormat?: string;
        kmsKeyArn?: string;
        prefix?: string;
        roleArn: string;
    }[]>;
    readonly versionId: fabric.Computed<string>;
    constructor(urnName: string, args: FirehoseDeliveryStreamArgs);
}
export interface FirehoseDeliveryStreamArgs {
    readonly arn?: fabric.MaybeComputed<string>;
    readonly destination: fabric.MaybeComputed<string>;
    readonly destinationId?: fabric.MaybeComputed<string>;
    readonly elasticsearchConfiguration?: fabric.MaybeComputed<{
        bufferingInterval?: fabric.MaybeComputed<number>;
        bufferingSize?: fabric.MaybeComputed<number>;
        cloudwatchLoggingOptions?: fabric.MaybeComputed<{
            enabled?: fabric.MaybeComputed<boolean>;
            logGroupName?: fabric.MaybeComputed<string>;
            logStreamName?: fabric.MaybeComputed<string>;
        }>[];
        domainArn: fabric.MaybeComputed<string>;
        indexName: fabric.MaybeComputed<string>;
        indexRotationPeriod?: fabric.MaybeComputed<string>;
        retryDuration?: fabric.MaybeComputed<number>;
        roleArn: fabric.MaybeComputed<string>;
        s3BackupMode?: fabric.MaybeComputed<string>;
        typeName?: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly redshiftConfiguration?: fabric.MaybeComputed<{
        cloudwatchLoggingOptions?: fabric.MaybeComputed<{
            enabled?: fabric.MaybeComputed<boolean>;
            logGroupName?: fabric.MaybeComputed<string>;
            logStreamName?: fabric.MaybeComputed<string>;
        }>[];
        clusterJdbcurl: fabric.MaybeComputed<string>;
        copyOptions?: fabric.MaybeComputed<string>;
        dataTableColumns?: fabric.MaybeComputed<string>;
        dataTableName: fabric.MaybeComputed<string>;
        password: fabric.MaybeComputed<string>;
        retryDuration?: fabric.MaybeComputed<number>;
        roleArn: fabric.MaybeComputed<string>;
        username: fabric.MaybeComputed<string>;
    }>[];
    readonly s3Configuration: fabric.MaybeComputed<{
        bucketArn: fabric.MaybeComputed<string>;
        bufferInterval?: fabric.MaybeComputed<number>;
        bufferSize?: fabric.MaybeComputed<number>;
        cloudwatchLoggingOptions?: fabric.MaybeComputed<{
            enabled?: fabric.MaybeComputed<boolean>;
            logGroupName?: fabric.MaybeComputed<string>;
            logStreamName?: fabric.MaybeComputed<string>;
        }>[];
        compressionFormat?: fabric.MaybeComputed<string>;
        kmsKeyArn?: fabric.MaybeComputed<string>;
        prefix?: fabric.MaybeComputed<string>;
        roleArn: fabric.MaybeComputed<string>;
    }>[];
    readonly versionId?: fabric.MaybeComputed<string>;
}
