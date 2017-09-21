---
layout: typescript-reference
repo: pulumi-aws
subpath: s3/bucket.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Bucket extends fabric.Resource {
    readonly accelerationStatus: fabric.Computed<string>;
    readonly acl?: fabric.Computed<string>;
    readonly arn: fabric.Computed<string>;
    readonly bucket: fabric.Computed<string>;
    readonly bucketDomainName: fabric.Computed<string>;
    readonly bucketPrefix?: fabric.Computed<string>;
    readonly corsRule?: fabric.Computed<{
        allowedHeaders?: string[];
        allowedMethods: string[];
        allowedOrigins: string[];
        exposeHeaders?: string[];
        maxAgeSeconds?: number;
    }[]>;
    readonly forceDestroy?: fabric.Computed<boolean>;
    readonly hostedZoneId: fabric.Computed<string>;
    readonly lifecycleRule?: fabric.Computed<{
        abortIncompleteMultipartUploadDays?: number;
        enabled: boolean;
        expiration?: {
            date?: string;
            days?: number;
            expiredObjectDeleteMarker?: boolean;
        }[];
        id: string;
        noncurrentVersionExpiration?: {
            days?: number;
        }[];
        noncurrentVersionTransition?: {
            days?: number;
            storageClass: string;
        }[];
        prefix?: string;
        tags?: {
            [key: string]: any;
        };
        transition?: {
            date?: string;
            days?: number;
            storageClass: string;
        }[];
    }[]>;
    readonly logging?: fabric.Computed<{
        targetBucket: string;
        targetPrefix?: string;
    }[]>;
    readonly policy?: fabric.Computed<string>;
    readonly region: fabric.Computed<string>;
    readonly replicationConfiguration?: fabric.Computed<{
        role: string;
        rules: {
            destination: {
                bucket: string;
                storageClass?: string;
            }[];
            id?: string;
            prefix: string;
            status: string;
        }[];
    }[]>;
    readonly requestPayer: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly versioning: fabric.Computed<{
        enabled?: boolean;
        mfaDelete?: boolean;
    }[]>;
    readonly website?: fabric.Computed<{
        errorDocument?: string;
        indexDocument?: string;
        redirectAllRequestsTo?: string;
        routingRules?: string;
    }[]>;
    readonly websiteDomain: fabric.Computed<string>;
    readonly websiteEndpoint: fabric.Computed<string>;
    constructor(urnName: string, args: BucketArgs);
}
export interface BucketArgs {
    readonly accelerationStatus?: fabric.MaybeComputed<string>;
    readonly acl?: fabric.MaybeComputed<string>;
    readonly arn?: fabric.MaybeComputed<string>;
    readonly bucket?: fabric.MaybeComputed<string>;
    readonly bucketPrefix?: fabric.MaybeComputed<string>;
    readonly corsRule?: fabric.MaybeComputed<{
        allowedHeaders?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        allowedMethods: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        allowedOrigins: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        exposeHeaders?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        maxAgeSeconds?: fabric.MaybeComputed<number>;
    }>[];
    readonly forceDestroy?: fabric.MaybeComputed<boolean>;
    readonly hostedZoneId?: fabric.MaybeComputed<string>;
    readonly lifecycleRule?: fabric.MaybeComputed<{
        abortIncompleteMultipartUploadDays?: fabric.MaybeComputed<number>;
        enabled: fabric.MaybeComputed<boolean>;
        expiration?: fabric.MaybeComputed<{
            date?: fabric.MaybeComputed<string>;
            days?: fabric.MaybeComputed<number>;
            expiredObjectDeleteMarker?: fabric.MaybeComputed<boolean>;
        }>[];
        id?: fabric.MaybeComputed<string>;
        noncurrentVersionExpiration?: fabric.MaybeComputed<{
            days?: fabric.MaybeComputed<number>;
        }>[];
        noncurrentVersionTransition?: fabric.MaybeComputed<{
            days?: fabric.MaybeComputed<number>;
            storageClass: fabric.MaybeComputed<string>;
        }>[];
        prefix?: fabric.MaybeComputed<string>;
        tags?: fabric.MaybeComputed<{
            [key: string]: any;
        }>;
        transition?: fabric.MaybeComputed<{
            date?: fabric.MaybeComputed<string>;
            days?: fabric.MaybeComputed<number>;
            storageClass: fabric.MaybeComputed<string>;
        }>[];
    }>[];
    readonly logging?: fabric.MaybeComputed<{
        targetBucket: fabric.MaybeComputed<string>;
        targetPrefix?: fabric.MaybeComputed<string>;
    }>[];
    readonly policy?: fabric.MaybeComputed<string>;
    readonly region?: fabric.MaybeComputed<string>;
    readonly replicationConfiguration?: fabric.MaybeComputed<{
        role: fabric.MaybeComputed<string>;
        rules: fabric.MaybeComputed<{
            destination: fabric.MaybeComputed<{
                bucket: fabric.MaybeComputed<string>;
                storageClass?: fabric.MaybeComputed<string>;
            }>[];
            id?: fabric.MaybeComputed<string>;
            prefix: fabric.MaybeComputed<string>;
            status: fabric.MaybeComputed<string>;
        }>[];
    }>[];
    readonly requestPayer?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly versioning?: fabric.MaybeComputed<{
        enabled?: fabric.MaybeComputed<boolean>;
        mfaDelete?: fabric.MaybeComputed<boolean>;
    }>[];
    readonly website?: fabric.MaybeComputed<{
        errorDocument?: fabric.MaybeComputed<string>;
        indexDocument?: fabric.MaybeComputed<string>;
        redirectAllRequestsTo?: fabric.MaybeComputed<string>;
        routingRules?: fabric.MaybeComputed<string>;
    }>[];
    readonly websiteDomain?: fabric.MaybeComputed<string>;
    readonly websiteEndpoint?: fabric.MaybeComputed<string>;
}
