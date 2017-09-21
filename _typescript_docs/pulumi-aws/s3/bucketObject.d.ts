---
layout: typescript-reference
repo: pulumi-aws
subpath: s3/bucketObject.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
import { Bucket } from "./bucket";
export declare class BucketObject extends fabric.Resource {
    readonly acl?: fabric.Computed<string>;
    readonly bucket: fabric.Computed<Bucket>;
    readonly cacheControl?: fabric.Computed<string>;
    readonly content?: fabric.Computed<string>;
    readonly contentDisposition?: fabric.Computed<string>;
    readonly contentEncoding?: fabric.Computed<string>;
    readonly contentLanguage?: fabric.Computed<string>;
    readonly contentType: fabric.Computed<string>;
    readonly etag: fabric.Computed<string>;
    readonly key: fabric.Computed<string>;
    readonly kmsKeyId?: fabric.Computed<string>;
    readonly serverSideEncryption: fabric.Computed<string>;
    readonly source?: fabric.Computed<fabric.asset.Asset>;
    readonly storageClass: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly versionId: fabric.Computed<string>;
    readonly websiteRedirect?: fabric.Computed<string>;
    constructor(urnName: string, args: BucketObjectArgs);
}
export interface BucketObjectArgs {
    readonly acl?: fabric.MaybeComputed<string>;
    readonly bucket: fabric.MaybeComputed<Bucket>;
    readonly cacheControl?: fabric.MaybeComputed<string>;
    readonly content?: fabric.MaybeComputed<string>;
    readonly contentDisposition?: fabric.MaybeComputed<string>;
    readonly contentEncoding?: fabric.MaybeComputed<string>;
    readonly contentLanguage?: fabric.MaybeComputed<string>;
    readonly contentType?: fabric.MaybeComputed<string>;
    readonly etag?: fabric.MaybeComputed<string>;
    readonly key?: fabric.MaybeComputed<string>;
    readonly kmsKeyId?: fabric.MaybeComputed<string>;
    readonly serverSideEncryption?: fabric.MaybeComputed<string>;
    readonly source?: fabric.asset.Asset;
    readonly storageClass?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly websiteRedirect?: fabric.MaybeComputed<string>;
}
