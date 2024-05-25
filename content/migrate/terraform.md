---
title: Pulumi for Terraform Users
layout: terraform
url: /terraform
meta_desc: Learn more about the productivity and scalability benefits of Pulumi over Terraform.
benefits:
    scalability:
        classes:
            blurb: |
                Little blurb here about why this feature is interesting. This probably shouldn't be more than
                a sentence or two, such that it occupies two lines at desktop width. Here's how that'd look.
            ts: |
                import * as pulumi from "@pulumi/pulumi";
                import * as aws from "@pulumi/aws";

                /**
                * The StaticWebsite class provisions a cloud storage bucket
                * and a content-delivery network for it, exposing the name of
                * the storage bucket and the CDN URL for later use.
                */
                export class StaticWebsite {
                    private bucket: aws.s3.Bucket;
                    private cdn: aws.cloudfront.Distribution;

                    public bucketName: pulumi.Output<string>;
                    public originURL: pulumi.Output<string>;

                    constructor(domainName: string, defaultDocument: string = "index.html") {

                        // Create a storage bucket.
                        this.bucket = new aws.s3.Bucket("website-bucket", {
                            bucket: domainName,
                            website: {
                                indexDocument: defaultDocument
                            }
                        });

                        // Create a CloudFront CDN.
                        this.cdn = new aws.cloudfront.Distribution("website-cdn", {
                            enabled: true,
                            origins: [
                                {
                                    originId: this.bucket.arn,
                                    domainName: this.bucket.bucketRegionalDomainName
                                }
                            ],
                            defaultRootObject: defaultDocument,
                            defaultCacheBehavior: {
                                targetOriginId: this.bucket.arn,
                                allowedMethods: ["HEAD", "GET"],
                                cachedMethods: ["HEAD", "GET"],
                                viewerProtocolPolicy: "redirect-to-https",
                                forwardedValues: {
                                    cookies: { forward: "none" },
                                    queryString: false
                                }
                            },
                            restrictions: {
                                geoRestriction: {
                                    restrictionType: "none"
                                }
                            },
                            viewerCertificate: {
                                cloudfrontDefaultCertificate: true
                            }
                        });

                        // Expose the bucket name and origin URL so consumers can use them.
                        this.bucketName = this.bucket.bucket;
                        this.originURL = pulumi.interpolate`https://${this.cdn.domainName}`;
                    }
                }

                // Consumers of your API can provide and use only the properties they care about.
                const { bucketName, originURL } = new StaticWebsite("www.my-domain.com");

            hcl: |
                // Some code here.
        components:
            blurb: |
                Little blurb here about why this feature is interesting.
            ts: |
                import * as pulumi from "@pulumi/pulumi";
                import * as aws from "@pulumi/aws";


                interface StaticWebsiteArgs {
                    domainName: string;
                    defaultDocument?: string;
                }

                /**
                * The StaticWebsite component provisions a cloud storage bucket
                * and a content-delivery network for it. Exposes the name of
                * the storage bucket and the CDN origin URL.
                */
                export class StaticWebsite extends pulumi.ComponentResource {
                    private bucket: aws.s3.Bucket;
                    private cdn: aws.cloudfront.Distribution;

                    public bucketName: pulumi.Output<string>;
                    public originURL: pulumi.Output<string>;

                    constructor(name: string, args: StaticWebsiteArgs, opts?: pulumi.ComponentResourceOptions) {
                        super("acmecorp:index:StaticWebsite", name, args, opts);

                        if (!args.defaultDocument) {
                            args.defaultDocument = "index.html";
                        }

                        // Create a storage bucket.
                        this.bucket = new aws.s3.Bucket("website-bucket", {
                            bucket: args.domainName,
                            website: {
                                indexDocument: args.defaultDocument
                            }
                        }, { parent: this });

                        // Create a CloudFront CDN.
                        this.cdn = new aws.cloudfront.Distribution("website-cdn", {
                            enabled: true,
                            origins: [
                                {
                                    originId: this.bucket.arn,
                                    domainName: this.bucket.bucketRegionalDomainName
                                }
                            ],
                            defaultRootObject: "index.html",
                            defaultCacheBehavior: {
                                targetOriginId: this.bucket.arn,
                                allowedMethods: ["HEAD", "GET"],
                                cachedMethods: ["HEAD", "GET"],
                                viewerProtocolPolicy: "redirect-to-https",
                                forwardedValues: {
                                    cookies: { forward: "none" },
                                    queryString: false
                                }
                            },
                            restrictions: {
                                geoRestriction: {
                                    restrictionType: "none"
                                }
                            },
                            viewerCertificate: {
                                cloudfrontDefaultCertificate: true
                            }
                        }, { parent: this });

                        // Expose the bucket name and origin URL so consumers can use them.
                        this.bucketName = this.bucket.bucket;
                        this.originURL = pulumi.interpolate`https://${this.cdn.domainName}`;

                        // Register public properties as Pulumi outputs.
                        this.registerOutputs({
                            bucketName: this.bucketName,
                            originURL: this.originURL
                        });
                    }
                }

                // Consumers of your API can provide and use only the properties they care about.
                export const { bucketName, originURL } = new StaticWebsite("my-website", {
                    domainName: "www.my-domain.com"
                });
            hcl: |
                // Some code here.
        testing:
            blurb: |
                Little blurb here about why this feature is interesting.
            ts: |
                // Some code here.
            hcl: |
                // Some code here.
    productivity:
        loops:
            blurb: |
                Little blurb here about why this feature is interesting.
            ts: |
                // Upload all files in a folder.
                for (let file of files) {
                    const myObject = new aws.s3.BucketObject(file, {
                        bucket: bucket,
                        source: new pulumi.FileAsset(pathjoin(folder, file),
                    });
                }
            hcl: |
                resource "aws_s3_bucket_object" "data_txt" {
                    key        = "data.txt"
                    bucket     = "${aws_s3_bucket.mybucket.id}"
                    source     = "./files/data.txt"
                }

                resource "aws_s3_bucket_object" "index_html" {
                    key        = "index.html"
                    bucket     = "${aws_s3_bucket.mybucket.id}"
                    source     = "./files/index.html"
                }

                resource "aws_s3_bucket_object" "index_js" {
                    key        = "index.js"
                    bucket     = "${aws_s3_bucket.mybucket.id}"
                    source     = "./files/index.js"
                }

                resource "aws_s3_bucket_object" "main.css" {
                    key        = "main.css"
                    bucket     = "${aws_s3_bucket.mybucket.id}"
                    source     = "./files/main.css"
                }

                resource "aws_s3_bucket_object" "favicon.ico" {
                    key        = "favicon.ico"
                    bucket     = "${aws_s3_bucket.mybucket.id}"
                    source     = "./files/favicon.ico"
                }
        conditionals:
            blurb: |
                Little blurb here about why this feature is interesting.
            ts: |
                // Some code here.
            hcl: |
                // Some code here.
        eventHandlers:
            blurb: |
                Little blurb here about why this feature is interesting.
            ts: |
                // Some code here.
            hcl: |
                // Some code here.
        statementCompletion:
            blurb: |
                Little blurb here about why this feature is interesting.
            ts: |
                // Some code here.
            hcl: |
                // Some code here.
---
